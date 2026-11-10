# Changes: System Integration v1 → v2

**Source:** `source/content/system_integration_v2.yaml` (the v1 content file and PDF are unchanged)
**QA (final build):** 1 A4 page · no page or column overflow (main slack 49 pt, sidebar 5 pt) · PDF reading order correct (PyMuPDF raw stream + pdftotext) · fonts embedded · margins 37–40 pt

## Verified facts applied

| Topic | v1 | v2 |
|---|---|---|
| CPI / commissioning | "10–15 CPI tests per month … during commissioning-related activities" (treated as one category) | "Remotely perform or support approximately **10–15 CPI** and **10–15 commissioning activities per month**, including operator-side RF measurements and step-by-step customer guidance" (two separate categories) |
| VSAT | "Provide operational integration support for VSAT systems, coordinating between customers and engineering teams" | "Provide **remote VSAT technical support** covering modem configuration, link verification, service activation and system monitoring, as defined by each customer's service agreement" |

## Repetition removed

- CPI, commissioning and VSAT each appear in exactly one experience bullet.
- Troubleshooting and fault isolation live in the incidents bullet and the interference bullet. They are not repeated in the VSAT bullet.
- Coordination with customers and engineering teams appears once in experience (the interference bullet) and once in the summary.
- Skills sidebar: "fault isolation" and "technical SOPs" are no longer repeated across groups.

## Overstatement review (whole CV)

| Item | Change | Reason |
|---|---|---|
| Summary: "{hands-on} experience on live satellite systems" | "nearly four years supporting live satellite communication systems" | "hands-on" could imply physical or on-site work |
| Summary: CPI and commissioning | "performs or supports" | Matches the verified wording exactly |
| Interference bullet: "RF interference and link degradation" | "RF interference cases" | "Link degradation" was my wording, not a verified fact |
| Skills: generic "Hardware integration" (under Integration & Verification) | Removed. "On-board debugging" moved under FPGA & Digital | It came only from the FPGA projects and could read as industrial integration |
| Skills: CPI and commissioning | Placed under Satellite & RF, **not** under VSAT Support | They are separate categories and are not verified as VSAT-specific |
| VSAT skills group | Labelled "VSAT Support (remote)" | Makes the remote scope explicit |
| Every bullet | Checked for on-site, installation or project-ownership wording | None remains. The only "physical hardware" wording refers to the candidate's own FPGA project |

## Still unconfirmed (carried over or new)

1. **Operator-side RF measurements for commissioning.** Verified for CPI (from the original CV). The bullet says "including", so it doesn't claim both, but please confirm whether commissioning also involves RF measurements.
2. **"Satellite Operator"** descriptor after AMOS-Spacecom. Keep it?
3. **"Handessaim" vs "Handesaim"** spelling.
4. **"Nearly four years"** should become "four years" from Dec 2026.
5. The interference bullet's "coordinating resolution with customers and engineering teams" relies on the general coordination fact. Please confirm it applies to interference cases.
