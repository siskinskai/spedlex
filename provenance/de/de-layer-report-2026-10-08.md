# Delaware layer (v0.40.0): contributor report

Drafted 2026-10-08 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` (v1.1). A person must review this before it is submitted. The layer has **not** been audited; run `prompts/audit-layer.md` in a fresh context, ideally with a different model.

Result of `tools/add_state.py delaware`: attests 200 concepts, adds 37 (16 machine_validated, 21 candidate), plus `delaware_supplement` (no new concepts). `python -m spedlex.build --check` passes and `pytest` passes (77 tests).

## 1. Documents read
- **RULE922**: 14 DE Admin. Code 922 (definitions), amendments through 28 DE Reg. 727 (04/01/25). Sections 1.0-3.0 read in full.
- **RULE925**: 14 DE Admin. Code 925 (evaluations, eligibility, IEPs), amendments through 28 DE Reg. 731 (04/01/25). Section 6.0 (eligibility, all 12 classifications) read in full; 1.0-5.0 and 7.0-15.0 searched for Delaware terms, not read line by line.
- **PSN**: DDOE, "Delaware Procedural Safeguards: Parent and Child Rights in Special Education" (July 2026, 46 pp.). Read in full. Cited by PDF page (printed page = PDF page − 4 from PDF p. 5).
- **GUIDE**: PIC of Delaware, "Parents Are the Key", 2d ed. (2013, 56 pp.). Read in full. Cited by PDF page (printed page = PDF page − 4 from PDF p. 5). DDOE links it as its parent guide, but PIC wrote it, so its records use `secondary_guidance`. It is 13 years old: its category list, state test (DCAS) and URLs are out of date.
- **How the text was obtained**: the rules as rendered on regulations.delaware.gov (browser page text), the PDFs as text extracted page by page with pdf.js in the browser pane. After the files were saved, every string and preferred term was checked automatically against pdftotext output of the cited PDF page (PSN, GUIDE) or the cited rule's PDF, and every cited rule subsection number was checked to exist. All passed.
- **Missing**: none of the three required documents. Delaware has no current DDOE-authored parent guide; the 2013 PIC manual is the one DDOE links. Rule subparts 923, 924 and 926-929 were not read (926's safeguards are covered by the PSN).

## 2. New concepts (37)
Quotes are 15 words or fewer, from the extracted text with line breaks collapsed; contact details are omitted.

| Key | Preferred term | Where it appears | Citation |
|---|---|---|---|
| `de_doe` | Delaware Department of Education | "“Department of Education” or “DOE” means the Delaware Department of Education." | 14 DE Admin. Code 922.2.2.1, 3.0 (Department of Education) |
| `de_regs` | 14 DE Admin. Code 922 to 929 | "Regulations 922 to 929 (14 DE Admin. Code 922 to 929) implement" | 14 DE Admin. Code 922.1.1-1.2 |
| `de_pic` | Parent Information Center of Delaware | "Education (DDOE) or the Parent Information Center of Delaware (PIC). Contact information can be found" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 3 |
| `de_dsd` | Delaware School for the Deaf | "with disabilities, including the Delaware School for the Deaf, the Delaware Autism Program, the Department" | 14 DE Admin. Code 922.2.2.3 |
| `de_dap` | Delaware Autism Program | "for the Deaf, the Delaware Autism Program, the Department of Services for Children, Youth and" | 14 DE Admin. Code 922.2.2.3 |
| `de_dscyf` | Department of Services for Children, Youth and Their Families | "Delaware Autism Program, the Department of Services for Children, Youth and Their Families, and its" | 14 DE Admin. Code 922.2.2.3, 3.0 (Ward of the State) |
| `de_dhss` | Department of Health and Social Services | "or schools, and the Department of Health and Social Services, and its divisions, units, or" | 14 DE Admin. Code 922.2.2.3 |
| `de_prison_ed` | Prison Education Program | "of Corrections (through "the Prison Education Program") and are binding on each public agency in" | 14 DE Admin. Code 922.2.2.4 |
| `de_relative_caregiver` | Relative Caregiver's School Authorization | "and for whom a Relative Caregiver's School Authorization executed in compliance with 14 Del.C. §202(f)(1)" | 14 DE Admin. Code 922.3.0 (Parent) |
| `de_secretary` | Secretary of Education | "§3110) "Secretary" means the Secretary of Education of the Delaware Department of Education unless otherwise" | 14 DE Admin. Code 922.3.0 (Secretary) |
| `de_ed_class` | Educational classification | "more of the following educational classifications: Autism, Developmental Delay, Deaf-Blind (also referred to as "Dual" | 14 DE Admin. Code 922.3.0 (Educational Classification) |
| `ansd` | Auditory Neuropathy Spectrum Disorder | "Auditory Neuropathy Spectrum Disorder (ANSD), which is defined as the presence" | 14 DE Admin. Code 925.6.10.1.1.3 |
| `abr` | Auditory Brainstem Response | "an absent or grossly abnormal ABR (Auditory Brainstem Response)." | 14 DE Admin. Code 925.6.10.1.1.3 |
| `cortical_vi` | Cortical vision impairment | "6.17.1.1.2 Cortical vision impairment, or" | 14 DE Admin. Code 925.6.17.1.1.2 |
| `de_emp_first` | Employment First Policy | "parents consistent with Delaware's Employment First Policy articulated by 19 Del.C. §743. 7.2.2.2 Progress made" | 14 DE Admin. Code 925.7.2.2.1 |
| `de_12month` | Twelve-month program | "14 Del.C. §3110) 7.6 Twelve-month program eligibility: The DOE shall include a parental notice and" | 14 DE Admin. Code 925.7.6 |
| `de_daas` | Diploma of Alternate Achievement Standards | "a diploma or a Diploma of Alternate Achievement Standards, the student shall not be discriminated" | 14 DE Admin. Code 925.15.0 |
| `de_ecr` | Exceptional Children Resources | "Exceptional Children Resources July 2026 Exceptional Children Resources Delaware Department of Education" | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 1 |
| `de_sparc` | Special Education Partnership for the Amicable Resolution of Conflict | "The Special Education Partnership for the Amicable Resolution of Conflict (SPARC)" | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 7 |
| `de_drd` | Disability Rights Delaware | "Disability Rights Delaware, Community Legal Aid Society, Inc." | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 7 |
| `draft_iep` | Draft IEP | "a copy of the draft IEP with a letter clearly stating the IEP is only" | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 9 |
| `de_hearing_panel` | Hearing panel | "due process complaint, a hearing panel (or single hearing officer in the case of expedited" | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 21 |
| `de_med_form` | Request for Special Education Mediation Form | "A copy of the Request for Special Education Mediation form is attached to the back" | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 19 |
| `de_dp_form` | Due Process Complaint Form and Request for Due Process Hearing | "A copy of the Due Process Complaint Form and Request for Due Process Hearing is" | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 20 |
| `de_sc_form` | Special Education State Complaint Form | "A copy of the Special Education State Complaint form is attached to the back of" | DDOE Delaware Procedural Safeguards (July 2026), PDF p. 28 |
| `de_cdw` | Child Development Watch | "Child Development Watch (CDW) Birth to Three Program" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 49 |
| `educ_diag` | Educational Diagnostician | "Coordinator or the school's Educational Diagnostician. When is my child re-evaluated? Reevaluation does not always" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 16 |
| `de_dcas` | Delaware Comprehensive Assessment System | "assessments such as the Delaware Comprehensive Assessment System (DCAS). Parents Are the Key – Page" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 16 |
| `de_dstp` | DE Student Testing Program | "program that replaced the DE Student Testing Program (DSTP) as of spring 2009. Disability Classification" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 52 |
| `de_dati` | Delaware Assistive Technology Initiative | "Delaware Assistive Technology Initiative (DATI) Information about assistive technology devices and" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 50 |
| `de_ssp` | Student Success Plan | "has completed on his Student Success Plan (SSP). The SSP is a web-based career exploration" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 29 |
| `de_dvr` | Division of Vocational Rehabilitation | "responsibility of inviting the Division of Vocational Rehabilitation (DVR), Developmental Disabilities Services (DDDS) and other" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 30 |
| `de_ddds` | Developmental Disabilities Services | "of Vocational Rehabilitation (DVR), Developmental Disabilities Services (DDDS) and other agencies, as appropriate. It is" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 30 |
| `case_by_case` | Case-by-case determination | "a Behavioral Intervention Plan. Case-by-Case Determination – School personnel may consider any unique circumstances on" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 41 |
| `oss` | Out-of-school suspension | "suspension from school? An out-of-school suspension means that your child has been removed or "suspended"" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 42 |
| `de_gacec` | Governor's Advisory Council for Exceptional Citizens | "Governor's Advisory Council for Exceptional Citizens (GACEC) Policy guidance with respect" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 50 |
| `cprc` | Community Parent Resource Center | "Information Centers (PTIs) and Community Parent Resource Centers (CPRCs) are funded by the U.S. Department" | PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. 54 |

## 3. Unsure
- **Former categories (GUIDE, 2013)**: the GUIDE lists Multiple Disabilities, Deafness and Emotional Disturbance as Delaware categories; the current rule (922.3.0, 925.6.5.1) has 12 classifications without Multiple Disabilities or a separate Deafness, and uses Emotional Disability. `md` and `deafness` are attested from the GUIDE only. "mental disability" (glossary, PDF p. 52) is recorded under `id` as legacy, and "Preschool Speech Delay" (a former classification for 3- and 4-year-olds, same page) under `sli` as legacy. Both are the nearest-key guesses the prompt asks for.
- **`dc_educ_rep`**: Delaware's educational representative for an adult student who lacks capacity (PSN PDF pp. 14, 17) was attested under the existing DC-prefixed key, as Indiana's layer did, instead of a new `de_` concept.
- **`in_transition_iep`**: attested from the GUIDE without adding a Delaware-tagged string, because tagging the existing untagged "Transition IEP" would have made it Delaware-only.
- **`de_doe`**: cited to the rule (922.2.2.1 and the 922.3.0 definition, which gives "DOE"), so it is `machine_validated`. "DDOE" appears only in the PSN and GUIDE, so it is attached in `delaware_supplement` (PSN PDF p. 6, GUIDE PDF p. 3).
- **`de_pic`**: cited to the GUIDE (PDF p. 3), where "PIC" appears; 922.3.0 names the center in the PTI definition (recorded under `pti`).
- **`de_ddds`**: the GUIDE writes "Developmental Disabilities Services (DDDS)"; the agency's full name likely begins "Division of", which the document doesn't say, so the preferred term follows the document.
- **`de_dstp`**: preferred term is "DE Student Testing Program" as written; the expansion of DE is not spelled out in the document.
- **`de_hearing_panel`**: "Hearing panel" is a short, fairly general phrase; it is tagged to Delaware through the concept's jurisdiction only.
- **`de_secretary`**: "Secretary of Education" also names the U.S. Secretary; recorded as a Delaware concept per 922.3.0.
- **`de_12month`** (category `placement_setting`) and **`de_emp_first`** (category `transition`): category choices are judgment calls.
- **`ansd`, `abr`, `cortical_vi`, `draft_iep`, `educ_diag`, `case_by_case`, `oss`, `cprc`** were added as national concepts (no jurisdiction) because nothing in KEYS matched; a reviewer may prefer to map some of them elsewhere.
- **Curly apostrophes**: the documents use ’ in "Relative Caregiver’s School Authorization" and "Governor’s Advisory Council"; the module uses straight apostrophes, as other layers do.

## 4. Risky
- **"DOE"**: 922.3.0 defines it as the Delaware Department of Education; "doe" is also in the census surname list. The reviewer judged it rare as a real surname and accepted it, so "DOE" is now in the known all-caps collisions in `tests/test_match.py`. It is matched case-sensitively, so "Doe" written as a name is still not protected.
- **"PIC"**: now an allowed cross-state ambiguity (New Hampshire and Delaware).
- **"ED"**: the GUIDE's acronym for Educational Diagnostician; left out because it already means emotional disturbance.
- **Short acronyms tagged US-DE**: ESR, IST, PBS (also a broadcaster), SSP, DVR, ABR (national, untagged), ESP (already NH-tagged, now NH and DE). None collided with the name lists or the scrubber adapter.
- **Place names**: nine new concepts are high risk because they contain "Delaware"/"DE" (auto-flagged by the build). The PSN's full title, added as a Delaware synonym of `safeguards_notice`, also contains "Parent" (a surname) and "Delaware", which raises that concept's risk to high in the collision report.
- **Low-risk word hits** in the collision report: "Case-by-case determination" (Case), "Governor's Advisory Council for Exceptional Citizens" (Governor's, Council) and "Community Parent Resource Center" (Parent). All are whole phrases.
- **No eponyms** were added. The John G. Townsend Building (DDOE's address) was left out.

## 5. Left out on purpose
- Every person named in the documents and all addresses, phone numbers and e-mail addresses.
- "ED" for Educational Diagnostician (ambiguous), as above.
- Autism Delaware and The Arc of Delaware (GUIDE acknowledgments only), Delaware Volunteer Legal Services and the Community Legal Aid Society (general legal aid), the former "Disabilities Law Program" name (GUIDE PDF p. 50; would need its own source on `de_drd`), NICHCY and the TA Alliance (closed national centers).
- The "Conflict Resolution Program" (a common phrase), "one tier state" (a description), the unit funding system (funding), the IEP-meeting questionnaire (the PSN calls it only "a questionnaire"), progress codes M/S/N (single letters), the Interagency Release of Information form, the DDOE due process and state complaint information guides (named only on the forms), "14 DE Admin. Code 508" (the MTSS rule; `mtss` is attested), and the long eligibility-criteria wording (IQ ranges, dB thresholds, ADHD symptom lists).
