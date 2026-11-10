# 02 RF Test Validation: tailoring and QA

**Target:** Junior RF Test / Validation Engineer  ·  **Status:** DRAFT, awaiting approval
**Files:** `Naor_Larian_CV_02_RF_Test_Validation.pdf` (final) · `.yaml` (editable source) · `_preview.png` · `_build_QA.json` · `_verify.txt`

## Tailoring decisions

- **Headline:** Electrical Engineering Student | RF Test & Validation.
- **Summary** leads with RF measurement and troubleshooting on live satellite systems. It mentions professional spectrum-analyzer use, interference, CPI and commissioning, and closes with communications and DSP coursework plus simulation-based verification.
- **Experience** opens with RF spectrum measurements and link diagnostics (incident volume kept). Interference investigation comes second. CPI and commissioning appear as separate counts. The VSAT bullet is reframed around link verification and monitoring.
- **Projects** are trimmed to two bullets each and framed around verification (simulation first, then hardware). They support "validation" without competing with the RF experience.
- **Skills** are regrouped: RF Measurement & Diagnostics, Test & Validation, and Satellite Systems (remote) come first. Coursework is reduced to Communication Systems, DSP, and Signals & Systems.
- **Not claimed:** RF circuit design, automated test development, lab instruments other than the spectrum analyzer, and formal test-procedure (ATP/STP) authorship.

All claims trace to the verified fact list (phase 2 brief) and the approved System Integration V3. In particular:
Cyber Gladiators = physically implemented on Basys 3; RGB Median Filter = simulation-verified only; C, Python and MATLAB = academic; spectrum analyzer = professional; all VSAT, CPI and commissioning work = remote, with CPI and commissioning counted separately.

## QA results

| Check | Result |
|---|---|
| Pages / size | 1 page, A4 (595.0 × 841.9 pt) |
| Overflow | none (main column slack 79.3 pt, sidebar slack 29.6 pt) |
| Text extent | x 37.0–556.4 pt, y 51.6–778.1 pt |
| Fonts | NotoSerif-Regular, NotoSerif-Bold, NotoSerif-SemiBold, NotoSerif-Italic (embedded subsets) |
| Words | 418 |

Extended verification (`source/verify.py --content`):

```
[PASS] Exactly one page — 1 page(s)
[PASS] A4 size — 595.0 × 841.9 pt
[PASS] All fonts embedded — NotoSerif-Bold, NotoSerif-Italic, NotoSerif-Regular, NotoSerif-SemiBold
[PASS] Searchable text present — 418 words
[PASS] Links: email / phone / LinkedIn — mailto:naorlarian@gmail.com, tel:+972507878716, https://linkedin.com/in/naor-larian
[PASS] Metadata title/author/keywords — title='Naor Larian – Electrical Engineering Student | RF Test & Validation', author='Naor Larian'
[PASS] No overlapping text lines — 0 overlap(s)
[PASS] No text outside margins (clipping)
[PASS] Reading order: PyMuPDF stream — full page
[PASS] Every bullet intact: PyMuPDF stream — 9 bullets
[PASS] Reading order: pdftotext -raw — full page
[PASS] Every bullet intact: pdftotext -raw — 9 bullets
[PASS] Reading order: pdfminer (geometric) — main column
[PASS] Every bullet intact: pdfminer (geometric) — 9 bullets
[INFO] Sidebar placement under geometric parsing: after main column
[PASS] No banned / unsupported terms
[PASS] Target keywords present (17)
```

Visually inspected at 200 dpi: no clipping, overlaps, broken number ranges or hyphenated compounds, and no single-word widows.
