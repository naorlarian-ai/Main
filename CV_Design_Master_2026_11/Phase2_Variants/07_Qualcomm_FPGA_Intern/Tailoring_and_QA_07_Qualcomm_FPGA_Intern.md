# 07 Qualcomm FPGA Intern: tailoring and QA

**Target:** FPGA / RTL Internship (Qualcomm)  ·  **Status:** DRAFT, awaiting approval
**Files:** `Naor_Larian_CV_07_Qualcomm_FPGA_Intern.pdf` (final) · `.yaml` (editable source) · `_preview.png` · `_build_QA.json` · `_verify.txt`

## Tailoring decisions

- **No job description was available** in the project, so the CV is tailored to the FPGA/RTL internship role family. Qualcomm isn't named in the CV.
- **Headline:** Electrical Engineering Student | FPGA / RTL Internship.
- **Section order:** FPGA / RTL Projects, then Experience. Education leads the sidebar, so it sits at the same height as the projects.
- **Summary** presents the full FPGA flow: FSM-based architecture, RTL simulation, synthesis, implementation and on-board debugging in Vivado, demonstrated on physical Artix-7 hardware.
- **Cyber Gladiators** is the strongest evidence, tagged "Implemented on hardware". **RGB Median Filter** gets three architecture- and verification-focused bullets (components, FSM/buffers/RAM-ROM datapath integration, testbench verification) and is tagged "Simulation-verified".
- **Differs from 04 (Junior FPGA)** in three ways: it has internship positioning, more RGB architecture depth, a lighter experience section (three bullets), and Verification and FPGA Flow skill groups.
- **Not claimed:** industrial RTL, Verilog, SystemVerilog, UVM, ASIC flow, and timing closure.

All claims trace to the verified fact list (phase 2 brief) and the approved System Integration V3. In particular:
Cyber Gladiators = physically implemented on Basys 3; RGB Median Filter = simulation-verified only; C, Python and MATLAB = academic; spectrum analyzer = professional; all VSAT, CPI and commissioning work = remote, with CPI and commissioning counted separately.

## QA results

| Check | Result |
|---|---|
| Pages / size | 1 page, A4 (595.0 × 841.9 pt) |
| Overflow | none (main column slack 106 pt, sidebar slack 41.6 pt) |
| Text extent | x 37.0–557.6 pt, y 51.6–766.9 pt |
| Fonts | NotoSerif-Regular, NotoSerif-Bold, NotoSerif-Italic, NotoSerif-SemiBold (embedded subsets) |
| Words | 387 |

Extended verification (`source/verify.py --content`):

```
[PASS] Exactly one page — 1 page(s)
[PASS] A4 size — 595.0 × 841.9 pt
[PASS] All fonts embedded — NotoSerif-Bold, NotoSerif-Italic, NotoSerif-Regular, NotoSerif-SemiBold
[PASS] Searchable text present — 387 words
[PASS] Links: email / phone / LinkedIn — mailto:naorlarian@gmail.com, tel:+972507878716, https://linkedin.com/in/naor-larian
[PASS] Metadata title/author/keywords — title='Naor Larian – Electrical Engineering Student | FPGA / RTL Internship', author='Naor Larian'
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
[PASS] Target keywords present (18)
```

Visually inspected at 200 dpi: no clipping, overlaps, broken number ranges or hyphenated compounds, and no single-word widows.
