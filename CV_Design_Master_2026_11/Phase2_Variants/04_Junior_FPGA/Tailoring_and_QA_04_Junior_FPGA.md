# 04 Junior FPGA: tailoring and QA

**Target:** Junior FPGA / Digital Hardware Engineer  ·  **Status:** DRAFT, awaiting approval
**Files:** `Naor_Larian_CV_04_Junior_FPGA.pdf` (final) · `.yaml` (editable source) · `_preview.png` · `_build_QA.json` · `_verify.txt`

## Tailoring decisions

- **Headline:** Electrical Engineering Student | FPGA & Digital Hardware.
- **Section order:** FPGA Projects first, then Professional Experience (`main: [projects, experience]`).
- **Cyber Gladiators** gets four bullets covering the full flow: architecture with FSM control, ESP32/UART integration, simulation then Vivado synthesis and implementation, and the hardware demo with on-board debugging. The stack line is tagged **"Implemented on hardware"**.
- **RGB Median Filter** has its stack line tagged **"Simulation-verified"**, and the bullets describe simulation and testbench verification only. This makes the hardware-versus-simulation distinction explicit.
- **Experience** is condensed to four bullets that show transferable debugging: fault isolation, remote VSAT/CPI/commissioning, interference, and SOPs.
- **Skills:** HDL & Design, Verification & Debug, Tools & Hardware, Interfaces & Memory. Advanced Hardware Design leads the coursework.
- **Not claimed:** professional RTL experience, Verilog, SystemVerilog, UVM, timing closure, and high-speed interfaces.

All claims trace to the verified fact list (phase 2 brief) and the approved System Integration V3. In particular:
Cyber Gladiators = physically implemented on Basys 3; RGB Median Filter = simulation-verified only; C, Python and MATLAB = academic; spectrum analyzer = professional; all VSAT, CPI and commissioning work = remote, with CPI and commissioning counted separately.

## QA results

| Check | Result |
|---|---|
| Pages / size | 1 page, A4 (595.0 × 841.9 pt) |
| Overflow | none (main column slack 75.9 pt, sidebar slack 41.6 pt) |
| Text extent | x 37.0–551.3 pt, y 51.6–766.9 pt |
| Fonts | NotoSerif-Regular, NotoSerif-Bold, NotoSerif-Italic, NotoSerif-SemiBold (embedded subsets) |
| Words | 411 |

Extended verification (`source/verify.py --content`):

```
[PASS] Exactly one page — 1 page(s)
[PASS] A4 size — 595.0 × 841.9 pt
[PASS] All fonts embedded — NotoSerif-Bold, NotoSerif-Italic, NotoSerif-Regular, NotoSerif-SemiBold
[PASS] Searchable text present — 411 words
[PASS] Links: email / phone / LinkedIn — mailto:naorlarian@gmail.com, tel:+972507878716, https://linkedin.com/in/naor-larian
[PASS] Metadata title/author/keywords — title='Naor Larian – Electrical Engineering Student | FPGA & Digital Hardware', author='Naor Larian'
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
