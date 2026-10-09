# Michigan layer (v0.25.0): contributor report

Drafted 2026-10-06 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` and CONTRIBUTING.md. A person must review this before it is submitted.

## 1. Documents read
- **RULE**: Michigan Administrative Rules for Special Education (MARSE), R 340.1701 to R 340.1873, as promulgated June 27, 2024. This is MDE's "all rules" PDF, 62 pp. Parts 1-3, 8, 9 and 10 were read in full. Parts 4-7 (personnel, finance, ISD plans) were read by heading, plus R 340.1793, R 340.1799e-g, R 340.1832 and R 340.1838.
- **PSN**: MDE Procedural Safeguards Notice, last updated 10/16/18, 53 pp. Pages 1-11 were read in full and the rest searched. It follows the federal model notice.
- **PROG**: MDE, "IEP Development: Special Education Programs and Services", May 2022, 7 pp. Read in full.
- **ALT**: MDE MI-Access web page, read as page text.
- **Missing**: Michigan has no single statewide parent guide. PROG stands in as the IEP guidance.
- **How the files were read**: all PDFs were downloaded from michigan.gov through the browser and checked by SHA-256, then converted to text. Copies are in `.sources-cache/mi/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `mi_mde` | Michigan Department of Education | "Michigan Department of Education , Office of Special Education Page 3 The Individuals with Disabilities" | MDE Procedural Safeguards Notice (updated 10/16/18), p. 3 |
| `mi_isd` | Intermediate school district | "is based; d. An intermediate school district plan; e. An individualized education program team report," | MDE Procedural Safeguards Notice (updated 10/16/18), p. 28 |
| `mi_isd_plan` | Intermediate school district plan | "areas. Rule 132. An intermediate school district plan for special education, or any modification thereof," | Mich Admin Code, R 340.1832 |
| `mi_psa` | Public school academy | "district, local school district, public school academy , and any other agency shall comply with" | Mich Admin Code, R 340.1733 |
| `mi_pac` | Parent advisory committee | "R 340.1838 Parent advisory committee . Rule 138. (1) A parent advisory committee shall be" | Mich Admin Code, R 340.1838 |
| `mi_moahr` | Michigan Office of Administrative Hearings and Rules | "the complaint to the Michigan office of administrative hearings and rules , which shall appoint" | Mich Admin Code, R 340.1724f |
| `mi_offer_fape` | Notice of an offer of a free appropriate public education | "an evaluation to the notice of an offer of a free appropriate public education or" | Mich Admin Code, R 340.1721b |
| `mi_operating_district` | Operating district | "conduct, or authorize the operating district to conduct, each subsequent individualized education program team meeting" | Mich Admin Code, R 340.1721e |
| `mi_instr_services` | Instructional services | "these rules: (a) " Instructional services " means services provided by teaching personnel that are" | Mich Admin Code, R 340.1701b |
| `mi_juvenile` | Youth placed in a juvenile detention facility | "related services. (d) " Youth placed in a juvenile detention facility " means a student" | Mich Admin Code, R 340.1701c |
| `mi_tc` | Teacher consultant | "R 340.1749 Teacher consultant with a student caseload; responsibilities. Rule 49. (1) The teacher consultant" | Mich Admin Code, R 340.1749 |
| `mi_departmentalize` | Departmentalization of special education programs | "R 340.1749c Departmentalization of special education programs . Rule 49c. (1) A school with more" | Mich Admin Code, R 340.1749c |
| `mi_sci_program` | Severe cognitive impairment program | "R 340.1738 Severe cognitive impairment program . Rule 38. A severe cognitive impairment program shall" | Mich Admin Code, R 340.1738 |
| `mi_sxi_program` | Severe multiple impairments program | "R 340.1748 Severe multiple impairments program . Rule 48. (1) A severe multiple impairment program" | Mich Admin Code, R 340.1748 |
| `mi_slp_provider` | Authorized provider of speech and language services | "services provided by an authorized provider of speech and language services shall be based on" | Mich Admin Code, R 340.1745 |
| `mi_msd` | Michigan School for the Deaf | "team shall consider the Michigan school for the deaf as a part of the total" | Mich Admin Code, R 340.1721e |
| `school_social_worker` | School social worker | "R 340.1799f " School social worker " defined. Rule 1799f. "School social worker" means a" | Mich Admin Code, R 340.1799f |
| `transition_coord` | Transition coordinator | "R 340.1799g Transition coordinator ; requirements. Rule 99g. (1) Full approval as a transition coordinator" | Mich Admin Code, R 340.1799g |
| `worksite_learning` | Worksite-based learning | "transition services. (i) For worksite-based learning , there must be a written agreement signed by" | Mich Admin Code, R 340.1733 |
| `mi_access` | MI-Access | "MI-Access is Michigan's alternate assessment system and is designed for students" | MDE MI-Access page |
| `mi_fi` | Functional Independence | "Participation and Supported Independence Functional Independence Michigan's Alternate Content Expectations for English Language Arts (ELA)," | MDE MI-Access page |
| `mi_si` | Supported Independence | "Work Readiness Participation and Supported Independence Functional Independence Michigan's Alternate Content Expectations for English Language" | MDE MI-Access page |
| `mi_ace` | Alternate content expectations | "is based on Michigan's alternate content expectations for English language arts, mathematics, science and social" | MDE MI-Access page |
| `mi_mstep` | M-STEP | "Accommodations Guidance Document for M-STEP , MI-Access, WIDA, PSAT, SAT, and WIN Work Readiness Participation" | MDE MI-Access page |

All quotes come from text extracted with pdftotext (or page text for web pages), with line breaks collapsed. Page-header text sometimes runs into a quote. Every new string and every attested key was checked automatically: the string had to appear in the cited section or page. All checks passed.

## 3. Unsure
- "Severe multiple impairment" was added under the existing `md` (multiple disabilities) key as a Michigan synonym. Michigan's category is narrower: R 340.1714 requires development 2 to 3 standard deviations below the mean plus further severe conditions. A reviewer may prefer a separate concept.
- "Early childhood developmental delay" was added under `dd`. R 340.1711 covers "a child through 7 years of age", which differs from the federal age range.
- `mi_isd` cites PSN p. 28 rather than the rule. The rules use the term throughout but have no definitions entry for it.
- `school_social_worker`, `transition_coord` and `worksite_learning` were added as national concepts with no jurisdiction tag, because the roles exist everywhere. Only Michigan attests them so far.

## 4. Risky
- **Place names** (high risk, flagged automatically): Michigan Department of Education, Michigan Office of Administrative Hearings and Rules, Michigan School for the Deaf, MI-Access.
- **Acronyms**: MDE, ISD, PSA, PAC, MOAHR, MSD, M-STEP, FI and SI. "PSA" and "PAC" are common outside special education and are tagged US-MI only. None of these collides with a given name in the test list.

## 5. Left out on purpose
- "SOAHR", the PSN's older name for the hearings office. The PSN never spells it out next to the current name, so it couldn't be tied to `mi_moahr` from the text alone.
- "OSE" (MDE Office of Special Education), which would clash with New York's `nysed_ose` preferred term.
- The State Board of Education member names in the PSN (personal names).
- Local district names used as examples.
