# 03 Application Engineering: tailoring and QA

**Target:** Junior Application / Field Application Engineer  ·  **Status:** DRAFT, awaiting approval
**Files:** `Naor_Larian_CV_03_Application_Engineering.pdf` (final) · `.yaml` (editable source) · `_preview.png` · `_build_QA.json` · `_verify.txt`

## Tailoring decisions

- **Headline:** Electrical Engineering Student | Application Engineering. "Field" is deliberately left out, because all verified customer work is remote. The PDF keywords still include "Field Application Engineer" for search.
- **Summary** leads with nearly four years of customer-facing technical experience: remote configuration, activation and troubleshooting, customer guidance, and coordination with engineering teams. FPGA integration is the supporting evidence.
- **Experience** puts customer interaction up front: incident handling, VSAT configuration and activation per service agreement, and CPI and commissioning with "guiding customers". A dedicated customers ↔ engineering-teams coordination bullet comes next, then SOPs as technical documentation.
- **Projects** emphasise integration (ESP32 ↔ FPGA over UART) and demonstrating on real hardware. RGB is framed as a team contribution.
- **Sidebar:** a Customer-Facing Support skills group comes first. Languages moves above Coursework, because English matters for customer-facing roles.
- **Not claimed:** product development, sales engineering, on-site or field work, and installation.

All claims trace to the verified fact list (phase 2 brief) and the approved System Integration V3. In particular:
Cyber Gladiators = physically implemented on Basys 3; RGB Median Filter = simulation-verified only; C, Python and MATLAB = academic; spectrum analyzer = professional; all VSAT, CPI and commissioning work = remote, with CPI and commissioning counted separately.

## QA results

| Check | Result |
|---|---|
| Pages / size | 1 page, A4 (595.0 × 841.9 pt) |
| Overflow | none (main column slack 89.2 pt, sidebar slack 45.4 pt) |
| Text extent | x 37.0–555.7 pt, y 51.6–762.4 pt |
| Fonts | NotoSerif-Regular, NotoSerif-Bold, NotoSerif-SemiBold, NotoSerif-Italic (embedded subsets) |
| Words | 403 |

Extended verification (`source/verify.py --content`):

```
[PASS] Exactly one page — 1 page(s)
[PASS] A4 size — 595.0 × 841.9 pt
[PASS] All fonts embedded — NotoSerif-Bold, NotoSerif-Italic, NotoSerif-Regular, NotoSerif-SemiBold
[PASS] Searchable text present — 403 words
[PASS] Links: email / phone / LinkedIn — mailto:naorlarian@gmail.com, tel:+972507878716, https://linkedin.com/in/naor-larian
[PASS] Metadata title/author/keywords — title='Naor Larian – Electrical Engineering Student | Application Engineering', author='Naor Larian'
[PASS] No overlapping text lines — 0 overlap(s)
[PASS] No text outside margins (clipping)
[PASS] Reading order: PyMuPDF stream — full page
[PASS] Every bullet intact: PyMuPDF stream — 10 bullets
[PASS] Reading order: pdftotext -raw — full page
[PASS] Every bullet intact: pdftotext -raw — 10 bullets
[PASS] Reading order: pdfminer (geometric) — main column
[PASS] Every bullet intact: pdfminer (geometric) — 10 bullets
[INFO] Sidebar placement under geometric parsing: after main column
[PASS] No banned / unsupported terms
[PASS] Target keywords present (17)
```

Visually inspected at 200 dpi: no clipping, overlaps, broken number ranges or hyphenated compounds, and no single-word widows.
