#!/usr/bin/env python3
"""Extended verification of a built CV PDF (complements the gate in build.py).

Usage: python3 verify.py <cv.pdf> [--content cv.yaml] [--baseline previous.pdf]

With --content, the reading-order anchors follow that variant's section order and the
keyword check uses its `qa_keywords` list (default: the System Integration list below).

Checks: page size/count, embedded fonts, links, metadata, overlapping text lines,
extraction order in three independent extractors, banned/unsupported claims, and
(with --baseline) engineering keywords that disappeared since the previous version.
"""
import argparse, re, subprocess, sys
import pymupdf, yaml
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import normalize, reading_anchors
from pdfminer.high_level import extract_text as pdfminer_text

# Claims that must never appear (unsupported by source material or implying on-site work).
BANNED = [r"\blinux\b", r"\bsql\b", r"\bATP\b", r"\bSTP\b", r"test automation", r"automated test",
          r"on-site", r"onsite", r"\binstall(ed|ation)?\b", r"link budget", r"RF design",
          r"\bfield\b", r"\bowned\b", r"\bled\b", r"\bindustrial\b"]
KEYWORDS = ["System Integration", "Validation", "fault isolation", "RF spectrum", "VSAT",
            "modem configuration", "link verification", "service activation", "system monitoring",
            "CPI", "commissioning", "interference", "SOP", "FPGA", "VHDL", "Vivado", "Artix-7",
            "Basys 3", "ESP32", "UART", "VGA", "RTL simulation", "testbenches", "FSM", "Python",
            "MATLAB", "Spectrum analyzer", "satellite"]


def order_ok(text, anchors):
    # Case-sensitive: section headings are extracted in upper case, so "EXPERIENCE"
    # must not match the word "experience" inside the summary.
    flat = " ".join(text.split())
    pos = [flat.find(a) for a in anchors]
    return all(p >= 0 for p in pos) and pos == sorted(pos), pos


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("pdf"); ap.add_argument("--baseline")
    ap.add_argument("--content")
    a = ap.parse_args()
    data = normalize(yaml.safe_load(Path(a.content).read_text(encoding="utf-8"))) if a.content else None
    keywords = (data or {}).get("qa_keywords") or KEYWORDS
    doc = pymupdf.open(a.pdf); page = doc[0]; ok = True
    def check(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond)
        print(f"[{'PASS' if cond else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")

    check("Exactly one page", len(doc) == 1, f"{len(doc)} page(s)")
    check("A4 size", abs(page.rect.width - 595.3) < 1 and abs(page.rect.height - 841.9) < 1,
          f"{page.rect.width:.1f} × {page.rect.height:.1f} pt")
    fonts = page.get_fonts()
    check("All fonts embedded", all(f[1] != "n/a" and "+" in f[3] for f in fonts),
          ", ".join(sorted({f[3].split('+')[-1] for f in fonts})))
    text = page.get_text()
    check("Searchable text present", len(text.split()) > 300, f"{len(text.split())} words")
    uris = [l.get("uri") for l in page.get_links()]
    check("Links: email / phone / LinkedIn",
          any(u and u.startswith("mailto:") for u in uris) and any(u and u.startswith("tel:") for u in uris)
          and any(u and "linkedin.com/in/" in u for u in uris), ", ".join(map(str, uris)))
    md = doc.metadata
    check("Metadata title/author/keywords", md.get("title") and md.get("author") and md.get("keywords"),
          f"title='{md.get('title')}', author='{md.get('author')}'")

    # overlapping text lines (different lines whose boxes intersect noticeably)
    lines = [pymupdf.Rect(l["bbox"]) for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])]
    overlaps = 0
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            r = lines[i] & lines[j]
            if not r.is_empty and r.get_area() > 4 and r.height > 2.5:
                overlaps += 1
    check("No overlapping text lines", overlaps == 0, f"{overlaps} overlap(s)")
    words = page.get_text("words")
    inside = all(37 - 1 <= w[0] and w[2] <= page.rect.width - 36 and w[3] <= page.rect.height - 30 for w in words)
    check("No text outside margins (clipping)", inside)

    anchors = (["Naor Larian"] + reading_anchors(data)) if data else [
        "Naor Larian", "SUMMARY", "EXPERIENCE", "15–25 technical incidents", "ENGINEERING PROJECTS",
        "Cyber Gladiators", "RGB Median Filter", "EDUCATION", "TECHNICAL SKILLS", "LANGUAGES"]
    pdftotext = subprocess.run(["pdftotext", "-layout", a.pdf, "-"], capture_output=True, text=True).stdout
    raw = subprocess.run(["pdftotext", "-raw", a.pdf, "-"], capture_output=True, text=True).stdout
    side_titles = {s["title"].upper() for s in data["sidebar"]} if data else {
        "EDUCATION", "TECHNICAL SKILLS", "RELEVANT COURSEWORK", "LANGUAGES"}
    main_anchors = [x for x in anchors if x.upper() not in side_titles]
    bullets = []
    if data:
        for sec in data["main"]:
            for it in sec.get("items") or []:
                bullets += it.get("bullets") or []
    norm = lambda s: re.sub(r"-\s+", "-", " ".join(re.sub(r"[*{}]", "", str(s)).split())).lower()
    for name, t in [("PyMuPDF stream", text), ("pdftotext -raw", raw), ("pdfminer (geometric)", pdfminer_text(a.pdf))]:
        geometric = "geometric" in name
        good, pos = order_ok(t, main_anchors if geometric else anchors)
        bad = [an for an, p in zip(anchors, pos) if p < 0]
        check(f"Reading order: {name}" + (" — main column" if geometric else " — full page"), good,
              ("not found: " + "; ".join(bad)) if bad else "")
        flat = norm(t)
        broken = [b[:40] for b in bullets if norm(b) not in flat]
        check(f"Every bullet intact: {name}", not broken, ("split: " + " | ".join(broken)) if broken else f"{len(bullets)} bullets")
        if geometric:
            full_ok, _ = order_ok(t, anchors)
            print(f"[{'INFO' if full_ok else 'WARN'}] Sidebar placement under geometric parsing: "
                  + ("after main column" if full_ok else
                     "sidebar blocks interleave between main-column entries (whole blocks, no sentence splits; "
                     "inherent to the two-column master)"))
    del pdftotext

    hits = [p for p in BANNED if re.search(p, text, re.I)]
    check("No banned / unsupported terms", not hits, ", ".join(hits))
    missing = [k for k in map(str, keywords) if k.lower() not in " ".join(text.split()).lower()]
    check(f"Target keywords present ({len(keywords)})", not missing, ("missing: " + ", ".join(missing)) if missing else "")

    if a.baseline:
        tok = lambda s: set(re.findall(r"[A-Za-z][A-Za-z0-9\-/+]{2,}", s.lower()))
        base = tok(pymupdf.open(a.baseline)[0].get_text()); cur = tok(text)
        print("Words removed since baseline:", ", ".join(sorted(base - cur)) or "none")
        print("Words added since baseline:  ", ", ".join(sorted(cur - base)) or "none")
    print("\nOVERALL:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
