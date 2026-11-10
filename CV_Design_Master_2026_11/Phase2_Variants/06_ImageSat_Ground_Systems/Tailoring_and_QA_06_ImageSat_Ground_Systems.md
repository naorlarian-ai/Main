# 06 ImageSat Ground Systems: tailoring and QA

**Target:** Ground Systems Integration Engineer (ImageSat)  ·  **Status:** DRAFT, awaiting approval
**Files:** `Naor_Larian_CV_06_ImageSat_Ground_Systems.pdf` (final) · `.yaml` (editable source) · `_preview.png` · `_build_QA.json` · `_verify.txt`

## Tailoring decisions

- **No job description was available** in the project, so the CV is tailored to the satellite ground-systems integration role family. ImageSat isn't named in the CV.
- **Headline:** Electrical Engineering Student | Ground Systems Integration.
- **Summary** covers operational satellite communication systems, remote commissioning support, link verification, system monitoring and RF troubleshooting, plus coordination with customers and engineering teams. FPGA integration follows as evidence of hands-on integration.
- **Experience:** operational-systems support with the incident volume comes first. Commissioning is listed **before** CPI in this variant because it is closer to integration work; both are remote and counted separately. VSAT support highlights system monitoring, then interference work and SOPs follow.
- **Projects:** Cyber Gladiators is framed as **integrating two subsystems** (ESP32 ↔ FPGA over UART).
- **Skills:** Satellite Communication Systems (remote), RF & Diagnostics, and Commissioning & Procedures.
- **Not claimed:** Linux, SQL, on-site installation, ground-station hardware work, and end-to-end integration ownership.

All claims trace to the verified fact list (phase 2 brief) and the approved System Integration V3. In particular:
Cyber Gladiators = physically implemented on Basys 3; RGB Median Filter = simulation-verified only; C, Python and MATLAB = academic; spectrum analyzer = professional; all VSAT, CPI and commissioning work = remote, with CPI and commissioning counted separately.

## QA results

| Check | Result |
|---|---|
| Pages / size | 1 page, A4 (595.0 × 841.9 pt) |
| Overflow | none (main column slack 109.4 pt, sidebar slack 29.6 pt) |
| Text extent | x 37.0–558.3 pt, y 51.6–778.1 pt |
| Fonts | NotoSerif-Regular, NotoSerif-Bold, NotoSerif-SemiBold, NotoSerif-Italic (embedded subsets) |
| Words | 388 |

Extended verification (`source/verify.py --content`):

```
[PASS] Exactly one page — 1 page(s)
[PASS] A4 size — 595.0 × 841.9 pt
[PASS] All fonts embedded — NotoSerif-Bold, NotoSerif-Italic, NotoSerif-Regular, NotoSerif-SemiBold
[PASS] Searchable text present — 388 words
[PASS] Links: email / phone / LinkedIn — mailto:naorlarian@gmail.com, tel:+972507878716, https://linkedin.com/in/naor-larian
[PASS] Metadata title/author/keywords — title='Naor Larian – Electrical Engineering Student | Ground Systems Integration', author='Naor Larian'
[PASS] No overlapping text lines — 0 overlap(s)
[PASS] No text outside margins (clipping)
[PASS] Reading order: PyMuPDF stream — full page
[PASS] Every bullet intact: PyMuPDF stream — 8 bullets
[PASS] Reading order: pdftotext -raw — full page
[PASS] Every bullet intact: pdftotext -raw — 8 bullets
[PASS] Reading order: pdfminer (geometric) — main column
[PASS] Every bullet intact: pdfminer (geometric) — 8 bullets
[INFO] Sidebar placement under geometric parsing: after main column
[PASS] No banned / unsupported terms
[PASS] Target keywords present (17)
```

Visually inspected at 200 dpi: no clipping, overlaps, broken number ranges or hyphenated compounds, and no single-word widows.
