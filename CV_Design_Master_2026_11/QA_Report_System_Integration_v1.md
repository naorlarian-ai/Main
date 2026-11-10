# QA Report: Naor_Larian_CV_System_Integration_v1

**Target role:** Junior System Integration Engineer / System Integration & Validation Engineer
**Reference:** `reference/Naor_Larian_CV_reference.pdf` (approved design, Naor_Larian_CV(5).pdf)
**Status:** Phase 1 complete. Awaiting design and content approval before the six remaining variants.

## Deliverables

| File | Description |
|---|---|
| `Naor_Larian_CV_System_Integration_v1.pdf` | Final one-page A4 PDF: selectable text, embedded fonts, clickable contacts |
| `Naor_Larian_CV_System_Integration_v1_preview.png` | 200 dpi render |
| `Comparison_Reference_vs_System_Integration_v1.pdf/.png` | Side-by-side: reference vs. new |
| `source/` | Editable source (YAML content + HTML/CSS template + build/QA scripts); see `source/README.md` |

## Final automated checks (last build)

| Check | Result |
|---|---|
| Pages | 1 (A4, 595 × 842 pt) |
| Page / column overflow | None. Main column slack 62 pt, sidebar slack 5 pt |
| Text margins (L / R / T / B) | 37 / 38 / 40 / 39 pt (balanced; reference ≈ 37 / 39 / 40 / 53, with uneven inner edges) |
| Fonts | Noto Serif Regular / Italic / SemiBold / Bold, embedded (same family as the reference) |
| Text extraction order | Correct in PyMuPDF (raw stream), pdftotext and pdfminer |
| Non-ASCII characters | Only `–` (en dash), `·` (middle dot), `×` |
| Links | mailto:, tel:, https://linkedin.com/in/naor-larian |
| PDF metadata | Title, Author, Subject, Keywords set |

## 1. Visual improvements implemented

Analysis of the reference with PyMuPDF found these issues, and each was fixed:

1. **Header contact block.** In the reference it sat flush against the top edge of the navy band (email at y = 39.7 pt, the same as the band's top edge). It now has proper inner padding, is vertically centred, and is separated by a subtle rule.
2. **Removed emoji/colour icons** (✉ ☎ ⌖ ▣, including a red colour-emoji phone). They were inconsistent in style, added colour noise, and get parsed as junk characters by ATS.
3. **One consistent left edge.** The reference used three different left edges (37 pt body, 42.6 pt summary heading, 55.5 pt summary text). Everything now aligns to the band edge.
4. **Dates moved out of headings into a right-aligned column** ("Dec 2022 – Present", "2026"), so the timeline can be scanned at a glance. Role, organisation and project names lead each entry.
5. **Sidebar carries the skills.** In the reference the right column ended around 65% of the way down and the left column was crammed. Technical Skills moved to the sidebar, so the page is now balanced and the main column holds only experience and projects.
6. **Section headings:** kept the reference's teal uppercase serif and "+" marker. The "+" is now a drawn vector, not a text glyph, so ATS no longer reads a stray "+". A hairline rule after each heading improves separation.
7. **Entry markers:** kept the reference's teal ● on entry titles. Bullet dots are lighter and smaller, so they no longer compete with the text.
8. **Project tech-stack line** (italic, grey) under each project title gives a quick keyword scan without crowding the bullets.
9. **Typography:** kept the 9.5 pt body size; sidebar 8.9 pt; consistent spacing scale; en dashes in date ranges (the reference used "2022 - Present").
10. **Widow control:** no single-word last lines (the reference had "logic.", "procedures.", "Basys 3", "systems.", "with honors.", "proficiency" alone on lines). Unbreakable groups such as `UART-to-VGA`, `3 × 3`, `Artix-7 / Basys 3` and `hands-on` are kept together.
11. **Vertical balance:** top and bottom margins are equal (40 / 39 pt). The reference ended its text about 53 pt from the bottom, with a large empty area in the right column.
12. **Kept unchanged by design:** A4, navy band colour, teal palette, Noto Serif, the ~65/35 column split and the column divider.

## 2. Textual improvements implemented

1. **Headline retargeted:** "FPGA & RTL | Electrical Engineering Student" became "System Integration & Validation | Electrical Engineering Student". Both are exact-match recruiter search terms.
2. **Summary rewritten** to lead with the strongest asset for this role: nearly four years on live SATCOM systems (fault isolation, RF spectrum measurements, link diagnostics, interference investigation, CPI testing, coordination with customers and engineering teams). FPGA integration follows as supporting evidence. It reads as an engineering profile, not a support or NOC profile.
3. **Experience moved above Projects.** For integration roles, real-world troubleshooting of operational systems is the main differentiator.
4. **Experience expanded from 3 to 5 bullets** using only the verified facts in the brief: interference investigation and fault isolation, VSAT operational integration support, and coordination with customers and engineering teams were added. Each bullet starts with a strong verb and ends with its purpose ("to isolate faults", "coordinating resolution with…").
5. **Cyber Gladiators:** emphasis moved from "verified RTL through simulation" to **integration and hardware demonstration** (ESP32 over UART, UART-to-VGA debugging on hardware, full system demonstrated on a Basys 3). This is what an integration recruiter looks for. "VHDL game engine" became "modular VHDL system", and "game logic" is kept for honesty.
6. **RGB Median Filter:** wording kept strictly simulation-level ("Verified … through RTL simulation and testbenches"), with **no hardware-validation claim**.
7. **Skills regrouped for the role**, with Systems & RF first, then Integration & Verification, FPGA & Digital, Interfaces, and Programming & Tools. The honest qualifiers "(professional)" for the spectrum analyser and "(academic)" for C, Python and MATLAB/Simulink are kept.
8. "Relevant Studies" became **"Relevant Coursework"**, the standard term ATS and recruiters expect. Communication Systems is listed first for this role.
9. Consistent tense (present for the current role, except the completed SOP work), Oxford-comma-free house style, US spelling ("behavior").

**Not added (no source support):** Linux, SQL, ATP/STP authorship, link-budget analysis, automated testing, RF design, industrial RTL work, and any new numbers.

## 3. Remaining limitations

- **Sidebar is nearly full (5 pt slack).** Variants that need more sidebar content must trim skills or move Coursework. The build gate will fail rather than clip, so this cannot silently break.
- **Main column ends about 62 pt above the sidebar.** This is intentional: I didn't add filler or invent content to make the columns end level.
- The VSAT bullet is the weakest one, because the source facts give only "operational integration support". One concrete detail from you would strengthen it (see question 2 below).
- Contact text in the band is 8.4 pt. It is readable in print, but it is the smallest text on the page.

## 4. ATS considerations

**Mitigations in place:**
- All text is real, selectable text in embedded fonts. There are no images of text, icons, tables or text boxes.
- The HTML follows reading order (header, summary, experience, projects, sidebar), and the PDF content stream follows it too. This was verified with three extractors and is now enforced by the build (`reading_order_ok`).
- Standard section names: Summary, Experience, Engineering Projects, Education, Technical Skills, Relevant Coursework, Languages.
- The title and date sit on the same extracted line ("Technical Support Engineer Dec 2022 – Present"), followed by the employer line.
- Decorative elements (the "+" markers, bullets, dots, rules) are vector shapes, not characters.

**Limitations (not fully verified):**
- **Not tested in a commercial ATS** (Workday, Greenhouse, SuccessFactors, Comeet and others). Parsers that split pages geometrically into columns could still merge lines across columns. The three open-source extractors tested all read it correctly.
- Some ATS mis-map the `·` separators in the project stack lines. The risk is low, and they can be swapped for commas in one line of YAML if needed.
- PDF Keywords metadata is set for completeness, but most ATS ignore it. Ranking depends on the visible text, which already contains the role keywords naturally.
- For portals that strip formatting, a plain single-column export could be produced from the same YAML if wanted.

## 5. Facts requiring confirmation

1. **CPI + commissioning.** The bullet reads "Support approximately 10–15 CPI tests per month … during commissioning-related activities." Please confirm that "commissioning-related" is accurate for these CPI tests. If it is, we could spell out "cross-polarization isolation (CPI)" once for non-SATCOM recruiters.
2. **VSAT integration support.** What does it concretely involve (e.g. new terminal or service activation, verification after changes, link line-up)? I used the conservative wording "Provide operational integration support for VSAT systems, coordinating between customers and engineering teams."
3. **"Nearly four years".** Accurate as of Nov 2026 (Dec 2022 to present). From Dec 2026 it should read "four years".
4. **Interference work.** "coordinating resolution with customers and internal engineering teams". Please confirm that this matches how interference cases are handled.
5. **"Satellite Operator"** was added as a descriptor after AMOS-Spacecom, for recruiters unfamiliar with the company. Keep it or remove it?
6. **Spelling of "Handessaim Tel Aviv"** (kept from the reference; it is commonly written "Handesaim"). Please confirm the official English spelling.
7. **Project years:** both projects are listed as 2026, as in the reference.
8. Contact details are unchanged from the reference.

## 6. Recruiter evaluation (System Integration, junior)

**What works:**
- In a 10-second scan, the headline, the summary's first line and the first experience entry answer the key questions: final-year EE student, nearly four years on operational satellite systems, and real troubleshooting volume (15–25 incidents a week, 10–15 CPI tests a month).
- It reads as an **engineer on operational systems**, not a helpdesk profile. The bullets are about RF measurements, link diagnostics, interference and fault isolation, which are core integration and validation behaviours.
- The FPGA project gives credible evidence of **hands-on hardware integration** (two subsystems over UART, debugged on hardware, demonstrated). This covers the "can they integrate and debug real hardware?" question that support-only candidates can't answer.
- It is honest. The academic, professional and simulation-only qualifiers raise trust with technical interviewers.

**What an integration hiring manager may still probe:**
- No formal test-procedure (ATP/STP) authorship or lab integration of new systems. This is not claimed, correctly. Expect interview questions on how CPI test steps and SOPs map to structured verification.
- No scripting or automation in a professional setting (Python is academic). If any work task used scripts, even small ones, it would be worth adding, but only if true.
- The VSAT bullet is generic until question 2 above is answered.

**Overall:** credible, well-targeted and honest positioning for entry-level System Integration & Validation roles. I haven't given a numerical score because no agreed rubric exists.
