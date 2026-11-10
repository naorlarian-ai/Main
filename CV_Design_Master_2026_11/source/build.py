#!/usr/bin/env python3
"""Build a CV variant: YAML content -> HTML -> PDF (+ PNG preview + QA checks).

Usage:
    python3 build.py content/system_integration.yaml [--out ..] [--compare ref.pdf]

Requires: PyYAML, Jinja2, PyMuPDF, Node + Playwright (Chromium).
"""
import argparse, html, json, re, subprocess, sys
from pathlib import Path

import yaml, jinja2, pymupdf

HERE = Path(__file__).resolve().parent
A4 = (595.3, 841.9)


def md(text: str) -> str:
    """Minimal markup: escape HTML, **bold** -> <strong>, {text} -> no line break."""
    t = html.escape(" ".join(str(text).split()), quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\{(.+?)\}", r'<span class="nw">\1</span>', t)      # {no-wrap}
    # Widow control: keep the final two words of a paragraph on one line.
    # Only applied when the tail contains no markup, so tags are never split.
    m = re.search(r"(\S+ \S+)$", t)
    if m and "<" not in m.group(1) and ">" not in m.group(1) and len(t.split()) > 4:
        t = t[:m.start()] + f'<span class="nw">{m.group(1)}</span>'
    return t


def contact_href(c: str):
    if "@" in c: return "mailto:" + c
    if c.startswith(("linkedin.com", "github.com", "www.")): return "https://" + c
    if c.startswith("+"): return "tel:" + c.replace("-", "")
    return None


def render_html(data: dict) -> Path:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(HERE), autoescape=True)
    env.filters["md"] = lambda s: jinja2.utils.markupsafe.Markup(md(s))
    env.filters["href"] = contact_href
    out = HERE / f"{data['output_name']}.html"
    out.write_text(env.get_template("template.html.j2").render(**data), encoding="utf-8")
    return out


def qa_pdf(pdf: Path, data: dict, metrics: dict) -> dict:
    doc = pymupdf.open(pdf)
    doc.set_metadata({
        "title": data["meta"]["title"], "author": data["name"],
        "subject": "Curriculum Vitae", "keywords": data["meta"]["keywords"],
        "creator": "CV_Design_Master_2026_11 build.py", "producer": "Chromium / PyMuPDF",
    })
    doc.saveIncr()
    page = doc[0]
    words = page.get_text("words")
    x0 = min(w[0] for w in words); x1 = max(w[2] for w in words)
    y0 = min(w[1] for w in words); y1 = max(w[3] for w in words)
    fonts = sorted({f[3] for f in page.get_fonts()})
    sizes = sorted({round(s["size"], 1) for b in page.get_text("dict")["blocks"]
                    for l in b.get("lines", []) for s in l["spans"]})
    text = page.get_text()
    # ATS reading-order check on the raw content stream: section headings, and the
    # first bullet of each entry, must appear in document order.
    flat = " ".join(text.split())
    def first_words(s, n=6): return " ".join(re.sub(r"[*{}]", "", " ".join(s.split())).split()[:n])
    anchors = ["SUMMARY", data["experience_title"].upper(), first_words(data["experience"][0]["bullets"][0]),
               data["projects_title"].upper(), first_words(data["projects"][-1]["bullets"][-1])]
    anchors += [s["title"].upper() for s in data["sidebar"]]
    pos = [flat.find(a) for a in anchors]
    reading_order_ok = all(p >= 0 for p in pos) and pos == sorted(pos)
    report = {
        "pages": len(doc),
        "page_size_pt": [round(page.rect.width, 1), round(page.rect.height, 1)],
        "text_bbox_pt": [round(v, 1) for v in (x0, y0, x1, y1)],
        "right_margin_pt": round(page.rect.width - x1, 1),
        "bottom_margin_pt": round(page.rect.height - y1, 1),
        "fonts_embedded": fonts, "font_sizes_pt": sizes,
        "word_count": len(words),
        "non_ascii_glyphs": sorted({c for c in text if ord(c) > 127}),
        "reading_order_ok": reading_order_ok,
        **metrics,
    }
    doc.close()
    return report


def png(pdf: Path, out: Path, dpi=200):
    doc = pymupdf.open(pdf); doc[0].get_pixmap(dpi=dpi).save(out); doc.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("--out", default=str(HERE.parent))
    args = ap.parse_args()

    data = yaml.safe_load(Path(args.content).read_text(encoding="utf-8"))
    html_path = render_html(data)
    out_dir = Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)
    pdf = out_dir / f"{data['output_name']}.pdf"
    res = subprocess.run(["node", str(HERE / "render.js"), str(html_path), str(pdf)],
                         capture_output=True, text=True, check=True, cwd=HERE)
    metrics = json.loads(res.stdout.strip().splitlines()[-1])
    report = qa_pdf(pdf, data, metrics)
    png(pdf, out_dir / f"{data['output_name']}_preview.png")
    print(json.dumps(report, indent=2, ensure_ascii=False))

    problems = []
    if report["pages"] != 1: problems.append("not one page")
    if report["page_overflow"]: problems.append("content overflows page")
    if min(report["main_slack_pt"], report["side_slack_pt"]) < 0: problems.append("column overflow")
    if not report["reading_order_ok"]: problems.append("PDF text reading order broken (ATS risk)")
    if problems:
        sys.exit("QA FAILED: " + ", ".join(problems))
    print("QA OK")


if __name__ == "__main__":
    main()
