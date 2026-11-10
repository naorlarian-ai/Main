# Phase 2: CV family overview (7 versions)

**Master:** `Naor_Larian_CV_System_Integration_v3.pdf` (approved, unchanged).
**Variants 02–07:** DRAFTS, awaiting approval. Nothing has been uploaded, nothing in the manifest or automation has changed, and no applications have been submitted.
**Visual overview:** `Overview_All_7_CVs.pdf` / `.png`. **Bundle:** `Naor_Larian_CV_Phase2_Variants.zip` (the six variant folders).

## Comparison of all seven versions

| # | Version | Headline (after "Electrical Engineering Student \|") | Main column order | Leads with | Distinctive emphasis |
|---|---|---|---|---|---|
| 01 | System Integration v3 (approved) | System Integration & Validation | Experience → Projects | Troubleshooting live SATCOM systems | Balanced: fault isolation, remote VSAT, CPI and commissioning, FPGA integration |
| 02 | RF Test & Validation | RF Test & Validation | Experience → Projects | RF spectrum measurements and link diagnostics | Interference, CPI and commissioning, link verification; professional spectrum analyzer; communications and DSP coursework; verification framing of projects |
| 03 | Application Engineering | Application Engineering | Experience → Projects | Customer-facing technical support | Remote configuration and activation, customer guidance, customer ↔ engineering coordination, SOPs; Languages promoted |
| 04 | Junior FPGA | FPGA & Digital Hardware | **Projects → Experience** | Cyber Gladiators (4 bullets, full flow) | "Implemented on hardware" vs "Simulation-verified" tags; HDL, verification and tools skills; Advanced Hardware Design first |
| 05 | Google Hardware Intern | Hardware Engineering Internship | **Education (full width) → Projects → Experience** | Academic status + hands-on hardware | Education at the top; "Hands-On Hardware Projects"; digital design and debugging skills |
| 06 | ImageSat Ground Systems | Ground Systems Integration | Experience → Projects | Operational satellite systems support | Commissioning listed before CPI, system monitoring, link verification; "integrated two subsystems" |
| 07 | Qualcomm FPGA Intern | FPGA / RTL Internship | **Projects → Experience** (Education leads sidebar) | Full FPGA flow, architecture | RGB architecture depth (datapath, FSM, buffers, RAM/ROM), verification; internship positioning |

Every summary is unique. The shared facts (education, dates, quantities) are identical across all seven.

## Recommended version per job family

| Job family / posting keywords | Use |
|---|---|
| System Integration, Integration & Validation, System Test (non-RF), V&V | **01 System Integration v3** |
| RF Test, RF Validation, SATCOM test, RF/communications lab, interference | **02 RF Test & Validation** |
| Application Engineer, Field Application Engineer, Technical Support Engineer (product), Customer Engineer, Solutions Engineer (junior) | **03 Application Engineering** |
| Junior FPGA, Digital Design, Hardware Engineer (FPGA), Embedded/FPGA | **04 Junior FPGA** |
| Hardware or EE internships, student positions in general hardware | **05 Hardware Internship** (Google version) |
| Ground segment, ground station, satellite operations engineering, NOC-to-engineering integration roles | **06 Ground Systems Integration** |
| FPGA/RTL/ASIC-adjacent internships and student roles | **07 FPGA / RTL Internship** (Qualcomm version) |
| Unsure / mixed hardware and systems posting | 01 (most balanced) |

Notes:
- 05, 06 and 07 contain **no employer-specific claims**, because no job descriptions were available in the project. They are role-family versions. When a real posting is available, the YAML can be tuned to its wording in minutes.
- For **FAE** postings that require on-site customer visits, 03 is still the right base. Discuss travel in the cover letter or interview, not on the CV, since all verified work is remote.

## Remaining factual uncertainties

1. **Commissioning and RF measurements.** Operator-side RF measurements are verified for CPI. In 01, 02, 03 and 06, the wording "including operator-side RF measurements and customer guidance" covers CPI and commissioning together. Please confirm whether commissioning also involves RF measurements; if not, I'll attach the phrase to CPI only.
2. **Customer guidance in commissioning.** 03 says "guiding customers through each procedure" for both CPI and commissioning. Customer guidance is verified in general and for CPI. Please confirm it also applies to commissioning.
3. **Interference and coordination.** "Coordinating resolution with customers and engineering teams" for interference cases (all variants except 05 and 07). This is still unconfirmed from V3.
4. **"Nearly four years".** Accurate until Dec 2026; after that it should read "four years". The change applies to all seven files.
5. **"Handessaim Tel Aviv".** The spelling comes from the original CV; the common spelling is "Handesaim". It is kept unless corrected.
6. **03 "customer-facing technical experience"** and **06 "operational satellite communication systems"** are reasonable characterisations of the verified role. Please confirm you're comfortable with them.

## Master-template notes (issues found during phase 2)

These were applied as the smallest safe corrections. **Rebuilding the approved V3 gives identical extracted text and identical word positions**: this was checked after each change. The approved V3 PDF itself was never rebuilt or overwritten.

| Issue | Correction |
|---|---|
| Number ranges and dimensions could break across lines ("15– / 25", "640 / × 480"). V3 avoided it only by chance | `build.py` keeps `N–M` and `N × M` together automatically |
| Hyphenated compounds could break at the hyphen ("FSM- / based"; V3's "hands-on" had been fixed by hand) | `build.py` keeps hyphenated compounds together automatically |
| Main-column order was hard-coded (Experience → Projects) | Optional `main:` list per variant; the default is unchanged |
| Internship variants needed Education first without emptying the sidebar | Optional full-width `top:` sections, using the existing section and entry styles (05 only) |
| `verify.py` was System-Integration specific and matched case-insensitively (false "experience" hit) | Variant-aware (`--content`), case-sensitive, per-variant `qa_keywords`, bullet-integrity check |

**ATS limitation of the master design (documented, not changed):** stream-order extractors (PyMuPDF, `pdftotext -raw`) read every version in exact document order. pdfminer's *geometric* layout mode reads the main column in order and keeps every bullet intact. In 05 it slots sidebar blocks between main-column entries, and the same applies to V3. No sentence is ever split. This is inherent to any two-column layout; removing it would need a single-column redesign. None of the versions have been tested in a commercial ATS.
