# CV Design Master (2026-11): build system

One design system, many content variants. Each variant is a single YAML file; the
layout, typography and QA checks are shared.

```
source/
├── content/system_integration.yaml   ← all wording for one variant (edit this)
├── template.html.j2                  ← page structure (shared)
├── styles.css                        ← design tokens + layout (shared)
├── fonts/                            ← Noto Serif (SIL OFL), embedded in the PDF
├── build.py                          ← YAML → HTML → PDF → PNG + QA gate
├── render.js                         ← headless Chromium print + overflow metrics
└── compare.py                        ← side-by-side vs. the reference
```

## Build

```bash
cd CV_Design_Master_2026_11/source
NODE_PATH=$(npm root -g) python3 build.py content/system_integration.yaml
python3 compare.py ../reference/Naor_Larian_CV_reference.pdf \
        ../Naor_Larian_CV_System_Integration_v1.pdf \
        ../Comparison_Reference_vs_System_Integration_v1
```

Requirements: Python 3 with `pyyaml`, `jinja2` and `pymupdf`, plus Node with `playwright` (Chromium).

## Content markup (YAML)

| Markup | Effect |
|---|---|
| `**text**` | bold emphasis (use sparingly: 1 phrase per bullet) |
| `{text}` | keep on one line (e.g. `{UART-to-VGA}`, `{3 × 3}`) |

Contact entries become clickable links automatically (email, `linkedin.com/...`, phone).
The last two words of every paragraph and bullet are automatically kept together (widow control).

## QA gate (build fails if any check fails)

- exactly one A4 page; no page or column overflow (reports remaining slack per column in pt)
- **PDF reading order**: section headings and bullets must appear in document order
  in the raw content stream, which is what many ATS parsers read. Avoid `position`,
  `opacity`, `transform` and `z-index` on text elements: Chromium paints those in a
  later layer, which moves their text to the end of the PDF stream.
- reports embedded fonts, font sizes, margins, non-ASCII glyphs and word count

## Making a new variant

1. Copy `content/system_integration.yaml` to `content/<role>.yaml`.
2. Change `output_name`, `meta`, `headline`, `summary`, bullet order/emphasis and skill groups.
3. Build, then check `main_slack_pt` / `side_slack_pt` (both ≥ 0) and look at the PNG.
