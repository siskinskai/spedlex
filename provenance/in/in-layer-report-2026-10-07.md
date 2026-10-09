# Indiana layer (v0.32.0): contributor report

Drafted 2026-10-07 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` should be run on it in a fresh conversation, ideally with a different model.

## 1. Documents read
- **RULE**: Special Education Rules, Title 511 Article 7 (IDOE's English compilation, May 2024, 167 pp.). 511 IAC 7-32 (definitions) and 7-41 (eligibility categories) were read in full; the other rules were read by section heading and searched.
- **PSN**: IDOE Notice of Procedural Safeguards (Aug. 2025, 25 pp.). Pp. 1-3, 19 and 25 were read in full and the rest searched; it follows the federal model notice.
- **NAV**: Navigating the Course (IDOE, Aug. 2025, 63 pp.), the parent guide. It was searched, and its acronym index on p. 7 was read in full.
- **How the files were read**: all three were downloaded from IDOE's Special Education page (two through the browser pane, one saved by the contributor), and converted to text with pdftotext. Copies are in `.sources-cache/in/`.
- **Missing**: none of the three document types.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `in_doe` | Indiana Department of Education | "INDIANA DEPARTMENT OF EDUCATION NOTICE OF PROCEDURAL SAFEGUARDS As the parent of a child who" | IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 1 |
| `in_dse` | Division of special education | "The department of education, division of special education is the state educational agency responsible for" | 511 IAC 7-33-1 |
| `in_oalp` | Office of Administrative Law Proceedings | "of education's designee, the Office of Administrative Law Proceedings (OALP) at the following address: Office" | IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 19 |
| `in_insource` | IN*SOURCE | "46268 josephmaley.org/ Telephone: 317-432-6657 IN*SOURCE PO Box 6185 South Bend, IN 46660 insource.org Telephone: 574-234-7101" | IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 25 |
| `in_idr` | Indiana Disability Rights | "Fax: 317-977-2385 Toll-free: 1-800-382-9100 Indiana Disability Rights 4755 Kingsway Dr, Suite 110 Indianapolis, IN 46205" | IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 25 |
| `in_isbvi` | Indiana School for the Blind and Visually Impaired | "of health. (4) The Indiana School for the Blind and Visually Impaired. (5) The Indiana" | 511 IAC 7-32-77 |
| `in_isd` | Indiana School for the Deaf | "Visually Impaired. (5) The Indiana School for the Deaf. (6) Programs operated by the department" | 511 IAC 7-32-77 |
| `in_school_corp` | School corporation | "the following: (1) Public school corporations operating programs individually or cooperatively. (2) Charter schools that" | 511 IAC 7-32-77 |
| `in_scols` | School corporation of legal settlement | "Board of Education SCOLS School Corporation of Legal Settlement SI Speech Impairment SLD Specific Learning" | IDOE Navigating the Course (Aug. 2025), PDF p. 7 |
| `in_legal_settlement` | Legal settlement | "511 IAC 7-32-56 ' Legal settlement' defined Sec. 56. 'Legal settlement', of a student, means" | 511 IAC 7-32-56 |
| `in_sepd` | Special education planning district | "511 IAC 7-32-87 ' Special education planning district' defined Sec. 87. 'Special education planning district'" | 511 IAC 7-32-87 |
| `in_article7` | Article 7 | "available. Special Education Terms Article 7 means Indiana's special education regulations that are found in" | IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 1 |
| `in_student_legal_age` | Student of legal age | "511 IAC 7-32-91 ' Student of legal age' defined Sec. 91. 'Student of legal age'" | 511 IAC 7-32-91 |
| `in_transition_iep` | Transition IEP | "IAC 7-42-6. (b) A transition IEP is an IEP that is: (1) developed in accordance" | 511 IAC 7-32-48 |
| `in_teacher_record` | Teacher of record | "Traumatic Brain Injury TOR Teacher of Record TOS Teacher of Service" | IDOE Navigating the Course (Aug. 2025), PDF p. 7 |
| `in_teacher_service` | Teacher of service | "Teacher of Record TOS Teacher of Service" | IDOE Navigating the Course (Aug. 2025), PDF p. 7 |
| `in_consult_collab` | Consultation and collaboration | "511 IAC 7-32-19 ' Consultation and collaboration' defined Sec. 19. 'Consultation and collaboration' means services" | 511 IAC 7-32-19 |
| `job_coach` | Job coach | "511 IAC 7-32-55 ' Job coach' defined Sec. 55. 'Job coach' means an individual who" | 511 IAC 7-32-55 |
| `systematic_obs` | Systematic observation | "511 IAC 7-32-96 ' Systematic observation' defined Sec. 96. 'Systematic observation' means an observation that" | 511 IAC 7-32-96 |
| `in_first_steps` | First Steps | "public school. Transitioning from First Steps to Early Childhood Special Education (511 IAC 7-43-2) Children" | IDOE Navigating the Course (Aug. 2025), PDF p. 30 |
| `in_istar` | Indiana Standards Tool for Alternative Reporting | "Family Service Plan ISTAR Indiana Standards Tool for Alternative Reporting PII Personally Identifiable Information PT" | IDOE Navigating the Course (Aug. 2025), PDF p. 7 |
| `in_choice_scholarship` | Choice scholarship | "this rule: (1) ' Choice scholarship student' means a student who has been awarded a" | 511 IAC 7-49-2 |
| `in_csep` | Choice special education plan | "IAC 4. (3) ' Choice special education plan' or 'CSEP' means the written document developed" | 511 IAC 7-49-2 |

All quotes come from text extracted with pdftotext (or, for COMAR, the saved page text), with line breaks collapsed. Every new string and every attested key was checked automatically against its cited section or page; the few without a literal hit were checked by hand.

## 3. Unsure
- **The NAV acronym index (p. 7) is printed in two columns.** In the extracted text the columns interleave, so each acronym (BLV, M-Team, NOPS, TOR, TOS, SCOLS, ISTAR, PAR) was matched to its expansion by hand. Please check them against the page.
- **"Cognitive disability"** is entered as a legacy string on `id`. NAV still uses the older label "CD Cognitive Disability", while the rule now says "intellectual disability".
- **`consult`**: Indiana's "consultation" (511 IAC 7-32-18), services to teachers about a student, is filed under the existing "Collaborative or consulting services" concept.
- **`part_c_transition`**: Indiana defines "transition planning" (7-32-99) narrowly, as the Part C to Part B move, so it went there rather than under `transition`.
- **`dc_educ_rep` is now a general concept.** It was DC-only, but Indiana appoints educational representatives too (7-43-6). Its key keeps the dc_ prefix, since keys never change.
- **Dropped during drafting**: `cert_completion` (Indiana's "certificate of completion" is a locally developed certificate rather than a state credential) and `state_sp_sch` at 7-32-77 (the rule names the two state schools but not the category).

## 4. Risky
- **Place names** (graded high automatically): Indiana Department of Education, IN*SOURCE, Indiana Disability Rights, Indiana School for the Blind and Visually Impaired, Indiana School for the Deaf, and Indiana Standards Tool for Alternative Reporting.
- **New all-caps acronyms**: CCC, IDOE, OALP, CSEP, SCOLS, ISTAR, BLV, NOPS, TOR, TOS. None is in the name lists, and all are case-sensitive and tagged US-IN. "CCC" here means case conference committee.
- **Common words**: "First Steps" is flagged common_english_word. "Consultation" is a single common word (none/phrase_or_token); it is not a name risk.

## 5. Left out on purpose
- The Joseph Maley Foundation (named for a person), and every address and phone number on PSN p. 25 and NAV p. 60.
- "Office of Special Education": the list already has it as a New York concept.
- The mild, moderate and severe intellectual disability criteria in 7-41-3, the ESA and ECA acronyms (each collides with an existing meaning), and "PAR" as an acronym (a common word).
- NAV's expansion of CSEP as "Choice Scholarship Education Plan", which differs from the rule's "choice special education plan".
