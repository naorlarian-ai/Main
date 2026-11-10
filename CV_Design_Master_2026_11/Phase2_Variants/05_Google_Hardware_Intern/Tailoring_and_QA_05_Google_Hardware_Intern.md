# 05 Google Hardware Intern: tailoring and QA

**Target:** Hardware / Electrical Engineering Internship (Google)  ·  **Status:** DRAFT, awaiting approval
**Files:** `Naor_Larian_CV_05_Google_Hardware_Intern.pdf` (final) · `.yaml` (editable source) · `_preview.png` · `_build_QA.json` · `_verify.txt`

## Tailoring decisions

- **No job description was available** in the project, so the CV is tailored to the hardware-internship role family and claims no Google-specific requirements. The CV text doesn't name Google.
- **Headline:** Electrical Engineering Student | Hardware Engineering Internship.
- **Education is a full-width section directly under the summary**, the only layout addition in phase 2 (see the master notes). It puts academic status and the 2027 graduation date at the top without unbalancing the columns.
- **Main column order:** Hands-On Hardware Projects, then Experience. The section title stresses the practical, physical hardware work.
- **Summary** opens with student status and "seeking a hardware engineering internship". It describes building and debugging a digital system on physical FPGA hardware, plus simulation and testbench verification, with professional experience as a secondary strength.
- **Skills:** Digital Design, Hardware & Debugging, Tools, and Programming (academic). Systems Troubleshooting shows transferable experience. Relevant Coursework is in the sidebar.
- **Not claimed:** semiconductor or silicon design, silicon validation, PCB design, specialised EDA tools, and Verilog.

All claims trace to the verified fact list (phase 2 brief) and the approved System Integration V3. In particular:
Cyber Gladiators = physically implemented on Basys 3; RGB Median Filter = simulation-verified only; C, Python and MATLAB = academic; spectrum analyzer = professional; all VSAT, CPI and commissioning work = remote, with CPI and commissioning counted separately.

## QA results

| Check | Result |
|---|---|
| Pages / size | 1 page, A4 (595.0 × 841.9 pt) |
| Overflow | none (main column slack 41.6 pt, sidebar slack 109.2 pt) |
| Text extent | x 37.0–558.1 pt, y 51.6–765.5 pt |
| Fonts | NotoSerif-Regular, NotoSerif-Bold, NotoSerif-SemiBold, NotoSerif-Italic (embedded subsets) |
| Words | 377 |

Extended verification (`source/verify.py --content`):

```
[PASS] Exactly one page — 1 page(s)
[PASS] A4 size — 595.0 × 841.9 pt
[PASS] All fonts embedded — NotoSerif-Bold, NotoSerif-Italic, NotoSerif-Regular, NotoSerif-SemiBold
[PASS] Searchable text present — 377 words
[PASS] Links: email / phone / LinkedIn — mailto:naorlarian@gmail.com, tel:+972507878716, https://linkedin.com/in/naor-larian
[PASS] Metadata title/author/keywords — title='Naor Larian – Electrical Engineering Student | Hardware Engineering Internship', author='Naor Larian'
[PASS] No overlapping text lines — 0 overlap(s)
[PASS] No text outside margins (clipping)
[PASS] Reading order: PyMuPDF stream — full page
[PASS] Every bullet intact: PyMuPDF stream — 8 bullets
[PASS] Reading order: pdftotext -raw — full page
[PASS] Every bullet intact: pdftotext -raw — 8 bullets
[PASS] Reading order: pdfminer (geometric) — main column
[PASS] Every bullet intact: pdfminer (geometric) — 8 bullets
[WARN] Sidebar placement under geometric parsing: sidebar blocks interleave between main-column entries (whole blocks, no sentence splits; inherent to the two-column master)
[PASS] No banned / unsupported terms
[PASS] Target keywords present (18)
```

Visually inspected at 200 dpi: no clipping, overlaps, broken number ranges or hyphenated compounds, and no single-word widows.
