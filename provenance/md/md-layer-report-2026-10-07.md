# Maryland layer (v0.34.0): contributor report

Drafted 2026-10-07 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` should be run on it in a fresh conversation, ideally with a different model.

## 1. Documents read
- **RULE**: COMAR 13A.05.01, Regulations .01-.16. There is no official PDF, so the text of each regulation page was copied from regs.maryland.gov through the browser pane into `.sources-cache/md/MD-COMAR-13A.05.01.txt`, and saved by the contributor. Regulation .03B was last amended effective Aug. 17, 2026. .02, .03 and .09 were read in full; the others were read by heading and searched.
- **PSN**: Parental Rights: Maryland Procedural Safeguards Notice (MSDE, July 2024, 51 pp.), which covers both Part C and Part B. Pp. 1-2, 14-17 and 36 were read and the rest searched.
- **IEPG**: Parent Information Series, The Individualized Education Program (MSDE, 2023, 20 pp.). Read in full.
- **Missing**: the Parent Information Series guide "The Special Education Process" could not be downloaded (its link led to a web page).
- Copies are in `.sources-cache/md/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `md_msde` | Maryland State Department of Education | "State Complaint with the Maryland State Department of Education (MSDE). In order for the State" | MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 36 |
| `md_deises` | Division of Early Intervention and Special Education Services | "the Assistant State Superintendent, Division of Early Intervention and Special Education Services, Maryland State Department" | MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 36 |
| `md_mitp` | Maryland Infants and Toddlers Program | "lead agency for the Maryland Infants and Toddlers Program, the statewide program of services and" | MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 19 |
| `md_extended_ifsp` | Extended IFSP | "or older through an Extended IFSP, an educational component must be included. If the parent" | MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 15 |
| `md_fss_coord` | Local Family Support Services Coordinator | "student's case manager or Local Family Support Services Coordinator can help! ❍ After the evaluation" | MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 16 |
| `md_seed` | SEED School | "local school systems, the SEED School, the Maryland Department of Health, the Department of Juvenile" | COMAR 13A.05.01.02A |
| `md_msb` | Maryland School for the Blind | "of Juvenile Services, the Maryland School for the Blind, the Maryland School for the Deaf," | COMAR 13A.05.01.02A |
| `md_msd` | Maryland School for the Deaf | "for the Blind, the Maryland School for the Deaf, and the Maryland Department of Labor." | COMAR 13A.05.01.02A |
| `md_mdh` | Maryland Department of Health | "the SEED School, the Maryland Department of Health, the Department of Juvenile Services, the Maryland" | COMAR 13A.05.01.02A |
| `md_djs` | Department of Juvenile Services | "Department of Health, the Department of Juvenile Services, the Maryland School for the Blind, the" | COMAR 13A.05.01.02A |
| `md_labor` | Maryland Department of Labor | "the Deaf, and the Maryland Department of Labor. B. Early intervention services to eligible infants" | COMAR 13A.05.01.02A |
| `md_mam` | Maryland Accommodations Manual | "in accordance with the Maryland Accommodations Manual, that provide students with disabilities equitable access during" | COMAR 13A.05.01.03B(1) |
| `md_moiep` | Maryland Online IEP | "Education Program (IEP) The Maryland online IEP (MOIEP) is a constantly evolving tool for Local" | MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 6 |
| `md_lcp` | Learning Continuity Plan | "are deaf-blind. (37-1) ' Learning Continuity Plan' means the sections of the IEP that address" | COMAR 13A.05.01.03B(37-1) |
| `md_emergency` | Emergency conditions | "(ii) Preschool programs. (22-1) Emergency Conditions. (a) 'Emergency Conditions' means a period of time of" | COMAR 13A.05.01.03B(22-1) |
| `md_hs_diploma` | Maryland High School Diploma | "provide credits towards a Maryland High School Diploma; • Identify the child for the alternative" | MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 14 |

All quotes come from text extracted with pdftotext (or, for COMAR, the saved page text), with line breaks collapsed. Every new string and every attested key was checked automatically against its cited section or page; the few without a literal hit were checked by hand.

## 3. Unsure
- **`cert_completion` is now a general concept.** Virginia's "Certificate of Program Completion" was Virginia-only; IEPG p. 7 says Maryland students may graduate with a certificate of program completion.
- **"Local school system (LSS)"** went on `lea` as a synonym.
- **"Critical life skill"** (.03B(15)) went on the existing `critical_skill` concept, which came from DC.
- **"AAAS"** went on `alt_assess`, because that concept already holds "alternate academic achievement standards".
- **The SEED School** is listed because COMAR names it among the public agencies (.02A). Its name is not a place.

## 4. Risky
- **Place names** (graded high automatically): Maryland State Department of Education, Maryland Infants and Toddlers Program, Maryland School for the Blind, Maryland School for the Deaf, Maryland Department of Health, Maryland Department of Labor, Maryland Accommodations Manual, Maryland Online IEP, Maryland High School Diploma and Maryland Procedural Safeguards Notice.
- **New all-caps acronyms**: MSDE, LSS, MOIEP and AAAS. None is in the name lists.

## 5. Left out on purpose
- The State Board members, superintendents and governor named on PSN p. 2 and IEPG p. 19.
- The 24 local school systems and their phone numbers on IEPG p. 18 (county names).
- The two-letter acronym "AA", and all addresses.
