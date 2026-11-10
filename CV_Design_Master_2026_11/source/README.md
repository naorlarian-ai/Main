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
├── verify.py                         ← extended checks (fonts, links, metadata, overlap,
│                                       3-extractor reading order, bullet integrity,
│                                       banned claims, per-variant keywords)
├── compare.py                        ← side-by-side of two PDFs
└── overview.py                       ← contact sheet of all 7 CVs

Phase 2 variants live in ../Phase2_Variants/<NN_Name>/ (YAML source + outputs per folder).
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
| `{text}` | keep on one line (e.g. `{Artix-7 / Basys 3}`) |

Automatically kept on one line: number ranges and dimensions (`15–25`, `640 × 480`) and
hyphenated compounds (`FSM-based`, `UART-to-VGA`).

### Layout options (per variant, all optional)

```yaml
main:                      # main-column order (default: experience, projects)
  - type: projects
  - type: experience
  - type: education        # also allowed in main/top, with title + items
top:                       # full-width sections between summary and columns
  - type: education
    title: Education
    items: [...]
qa_keywords: [...]         # keywords verify.py must find in the PDF text
```

Contact entries become clickable links automatically (email, `linkedin.com/...`, phone).
The last two words of every paragraph and bullet are automatically kept together (widow control).

## QA gate (build fails if any check fails)

- exactly one A4 page; no page or column overflow (reports remaining slack per column in pt)
- **PDF reading order**: section headings and bullets must appear in document order
  in the raw content stream, which is what many ATS parsers read. Avoid `position`,
  `opacity`, `transform` and `z-index` on text elements: Chromium paints those in a
  later layer, which moves their text to the end of the PDF stream.
- reports embedded fonts, font sizes, margins, non-ASCII glyphs and word count

## Variant build + verify

```bash
cd CV_Design_Master_2026_11/source
V=../Phase2_Variants/04_Junior_FPGA
NODE_PATH=$(npm root -g) python3 build.py $V/Naor_Larian_CV_04_Junior_FPGA.yaml --out $V --qa-json
python3 verify.py $V/Naor_Larian_CV_04_Junior_FPGA.pdf --content $V/Naor_Larian_CV_04_Junior_FPGA.yaml
python3 overview.py
```

## Making a new variant

1. Copy `content/system_integration.yaml` to `content/<role>.yaml`.
2. Change `output_name`, `meta`, `headline`, `summary`, bullet order/emphasis and skill groups.
3. Build, then check `main_slack_pt` / `side_slack_pt` (both ≥ 0) and look at the PNG.
