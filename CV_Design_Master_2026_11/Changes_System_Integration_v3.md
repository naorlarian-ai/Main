# Changes: System Integration v2 → v3 (final refinement)

**Source:** `source/content/system_integration_v3.yaml`. V1 and V2 files are unchanged.
**Design:** no changes to layout, typography, colours, proportions or CSS. All improvements are in content and line breaks.

## Content changes

| Area | v2 | v3 | Why |
|---|---|---|---|
| Headline | System Integration & Validation \| Electrical Engineering Student | **Electrical Engineering Student \| System Integration & Validation** | Status first, target second. It no longer reads as a current job title. It still fits on one line at the same size. |
| Summary | 5 lines; repeated VSAT, CPI and commissioning details from Experience; "Adds FPGA hardware integration experience from…" | 4 lines in three parts: (1) final-year EEE student, expected 2027; (2) nearly four years troubleshooting live satellite communication systems, using RF spectrum measurements, link verification and structured fault isolation alongside customers and engineering teams; (3) "Complemented by **hands-on FPGA integration** experience, demonstrated on physical Artix-7 hardware." | More concise and natural. Leads with transferable capabilities instead of a duty list. The operational detail lives only in Experience. |
| VSAT bullet | "…covering modem configuration, link verification, service activation and system monitoring, as defined by each customer's service agreement" | "Provide **remote VSAT technical support**: modem configuration, link verification, service activation, system monitoring and troubleshooting, per customer service agreement." | Adds the verified "troubleshooting" scope. 3 lines instead of 4. |
| CPI / commissioning bullet | "**10–15 CPI** and **10–15 commissioning activities per month**" | "**10–15 CPI activities** and **10–15 commissioning activities** per month" | Two explicitly separate categories, each with its own noun. "step-by-step" dropped, so no line ends on a single short phrase. |
| Interference bullet | "Investigate RF interference cases…" | "Investigate **RF interference**…" | Tighter wording. |
| SOP bullet | "Wrote and refined technical SOPs that made troubleshooting more consistent…" (past tense) | "Develop and refine **technical SOPs** that improve troubleshooting consistency and make critical procedures easier to find." | Present tense, consistent with a current role. The wording is closer to the original CV. |
| PDF metadata title | "… System Integration & Validation Engineer (Junior)" | "Naor Larian – Electrical Engineering Student \| System Integration & Validation" | The previous title implied a job title the candidate doesn't hold. |

Sections that needed no change after review: Projects, Education, Skills, Relevant Coursework and Languages.

## Line-break and layout outcomes (no CSS changes)

- The headline fits on one line, with the same alignment and spacing as V2.
- No widows, and no words split by a hyphen at line end ("hands-on" is kept together).
- Sidebar headroom went from 5 pt to **18 pt**, because the summary is one line shorter. This gives the other six versions safer room.
- The column divider still ends at the standard bottom margin, so the page frame is identical to V2.

## Accuracy review (whole CV)

| Item | Status |
|---|---|
| Cyber Gladiators | "demonstrated the full system on a Basys 3 board" and "debugged … on physical FPGA hardware". Hardware implementation verified ✔ |
| RGB Median Filter | "Verified … through RTL simulation and testbenches". Simulation only, with no hardware claim ✔ |
| Python, C, MATLAB/Simulink | Marked "(academic)" ✔. Spectrum analyser marked "(professional)" ✔ |
| CPI vs commissioning | Two separate counts and nouns ✔. VSAT bullet says "remote" ✔, CPI/commissioning bullet says "Remotely" ✔ |
| No on-site, installation, integration-ownership or ATP/STP claims | Automated scan for banned terms: none found ✔ |
| Not added | Linux, SQL, RF design, industrial RTL, test automation, ATP/STP ✔ |
| "hands-on" | Used only for the FPGA project, where the hardware work is physical ✔ |
| Employer descriptor, education | Unchanged ("AMOS-Spacecom · Satellite Operator"; education as in the source) ✔ |

## QA results (final build)

Build gate (`build.py`): **QA OK**, 1 page, no page or column overflow (main slack 62 pt, sidebar slack 18 pt), reading order OK.
Extended checks (`verify.py`, new and reusable for future variants):

```
[PASS] Exactly one page
[PASS] A4 size: 595.0 × 841.9 pt
[PASS] All fonts embedded: Noto Serif Regular / Italic / SemiBold / Bold
[PASS] Searchable text present: 419 words
[PASS] Links: mailto:naorlarian@gmail.com, tel:+972507878716, https://linkedin.com/in/naor-larian
[PASS] Metadata: title, author, subject and keywords set
[PASS] No overlapping text lines
[PASS] No text outside margins (clipping)
[PASS] Reading order: PyMuPDF stream / pdftotext -raw / pdfminer
[PASS] No banned / unsupported terms
[PASS] Core engineering keywords present (28 checked)
```

The keyword diff against V2 found no engineering keywords lost. Only connective words were removed ("works", "covering", "faster" and similar).
ATS note: verified with three open-source text extractors only. It has not been tested in a commercial ATS.

## Remaining factual uncertainties

1. **Commissioning and RF measurements.** The bullet reads "including operator-side RF measurements and customer guidance". The measurements are verified for CPI. Please confirm whether they also apply to commissioning activities.
2. **Interference and coordination.** Please confirm that "coordinating resolution with customers and engineering teams" applies specifically to interference cases.
3. **"Nearly four years".** This should become "four years" from December 2026.
4. **"Handessaim Tel Aviv".** The spelling comes from the original CV, and the commonly used spelling is "Handesaim". It is kept unless you confirm otherwise.
