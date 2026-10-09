# Alabama layer (v0.36.0): contributor report

Drafted 2026-10-08 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` should be run on it in a fresh conversation, ideally with a different model.

## 1. Documents read
- **RULE**: Ala. Admin. Code ch. 290-8-9, Special Education Services (Supp. No. 13-3, effective 11-04-13; ALSDE copy, 94 pp.). Read in full. `.sources-cache/al/` holds two copies (`AAC-290-8-9-11-4-2013.pdf` and `SE-AAC-290-8-9-11-4-2013.pdf`); their extracted text is the same apart from line breaks in the table of contents, so one can be deleted. The newest history note is "adopted as regular rule effective 11-04-13". **Not checked:** whether any rule was amended after 2013 (the legislature's code site couldn't be read here).
- **PSN**: Alabama's Procedural Safeguards (Special Education Rights), English v1.0, "ALSDE Approved January 2025" (29 pp.). Read in full. Cited by PDF page; printed page = PDF page - 2.
- **MAZE**: Mastering the Maze, Process 1: Referral Through IEP Implementation (August 2019 edition, 190 pp.). Read in full except PDF pp. 26-38, an older reprint of the federal model rights notice, which was skimmed. Cited by PDF page; printed page = PDF page - 3. Two-column pages interleave in the extracted text.
- **Missing**: an alternate assessment page and any diploma guidance newer than the 2013 rule (see §3).
- Not part of this layer: `Procedural_Safeguards_Notice.pdf` in the repository root is Arkansas's notice; it belongs in `.sources-cache/ar/`.
- Every new string and preferred term was checked automatically against its cited rule or page. 12 attestations with no literal hit were checked by hand and are wording variants (for example, "services comparable to" for `comparable`).

## 2. New concepts
Quotes are from the extracted text, 15 words or fewer.

| Key | Preferred term | Where it appears | Citation |
|---|---|---|---|
| `al_alsde` | Alabama State Department of Education | "ALSDE Alabama State Department of Education" | MAZE p. 7 |
| `al_sboe` | Alabama State Board of Education | "Alabama State Board of Education" (heading above the member list) | PSN p. 2 |
| `al_adrs` | Alabama Department of Rehabilitation Services | "ADRS Alabama Department of Rehabilitation Services" | MAZE p. 7 |
| `al_aeis` | Alabama's Early Intervention System | "AEIS Alabama's Early Intervention System" | MAZE p. 7 |
| `al_crs` | Children's Rehabilitation Services | "assistance in providing glasses/hearing aids (Children's Rehabilitation Services, Lion's Club, etc.)" | MAZE p. 153 |
| `al_medicaid` | Alabama State Medicaid Agency | "information of this student to the Alabama State Medicaid Agency and its contractors" | MAZE p. 120 |
| `al_adap` | Alabama Disabilities Advocacy Program | "Alabama Disabilities Advocacy Program (ADAP)" | PSN p. 12 |
| `al_apec` | Alabama Parent Education Center | "Alabama Parent Education Center (APEC)" | PSN p. 12 |
| `al_ric` | Regional Inservice Center | "RIC Regional Inservice Center" | MAZE p. 8 |
| `al_sets` | Special Education Tracking System | "SETS Special Education Tracking System" | MAZE p. 8 |
| `al_invite` | Notice and Invitation to a Meeting/Consent for Agency Participation | form title | MAZE p. 40 |
| `al_nci` | Notice and Consent for Initial Evaluation | form title | MAZE p. 47 |
| `al_reeval_notice` | Notice of IEP Team's Decision Regarding Reevaluation | "a copy of the Notice of IEP Team's Decision Regarding Reevaluation" | MAZE p. 42 |
| `al_elig_notice` | Notice and Eligibility Decision Regarding Special Education Services | form title | MAZE p. 64 |
| `al_consent_svc` | Notice and Consent for the Provision of Special Education Services | form title | MAZE p. 72 |
| `al_sif` | Special Instructional Factors | "SPECIAL INSTRUCTIONAL FACTORS Items checked "YES" will be addressed in this IEP" | MAZE p. 77 |
| `al_acc_checklist` | IEP Accommodations Checklist | "accommodations that are listed on the "IEP Accommodations Checklist."" | MAZE p. 95 |
| `al_persons_resp` | Persons Responsible for IEP Implementation | form title | MAZE p. 102 |
| `al_ecec` | Environmental, Cultural, and/or Economic Concerns | "Environmental, Cultural, and/or Economic Concerns ... Guide for Completing the ECEC Page" (contents) | MAZE p. 4 |
| `al_ffi` | Family Focus Interview | "Codes: Family Focus Interview (FFI) Natural Environment Observation (NEO)" | MAZE p. 56 |
| `al_neo` | Natural Environment Observation | same line | MAZE p. 56 |
| `al_elpp` | Early Learning Progress Profile | "Early Learning Progress Profile (ELPP)" | MAZE p. 56 |
| `al_predicted` | Predicted achievement model | "Public agencies that choose to use the predicted achievement model must use" | r. 290-8-9-.03(10) |
| `al_aaa` | Alabama Alternate Assessment | "AAA Alabama Alternate Assessment" | MAZE p. 7 |
| `al_aaa_pdd` | Alabama Alternate Assessment Program Participation Decision Documentation | "must use the Alabama Alternate Assessment Program Participation Decision Documentation form" | MAZE p. 78 |
| `al_ext_std` | Alabama Extended Standards | "or Alabama Extended Standards for students with significant cognitive disabilities" | r. 290-8-9-.05(6) |
| `al_aas` | Alabama Alternate Achievement Standards | "students with significant cognitive disabilities are based on Alabama Alternate Achievement Standards" | MAZE p. 91 |
| `al_dev_std` | Alabama Developmental Standards for Preschool Children | "and the Alabama Developmental Standards for Preschool Children for both school years" | MAZE p. 75 |
| `al_trans_std` | Alabama Transition Standards | "based on standards listed in the Alabama Transition Standards document" | MAZE p. 83 |
| `al_cos` | Alabama Course of Study | "content standards listed in the Alabama Course of Study" | MAZE p. 75 |
| `al_ccrs` | College and Career Ready Standards | "CCRS College and Career Ready Standards" | MAZE p. 7 |
| `al_ahsd` | Alabama High School Diploma | "graduating from high school with the Alabama High School Diploma (AHSD)" | MAZE p. 45 |
| `al_gen_path` | General Education Pathway | "General Education Pathway (Intended to prepare student for college and career)" | MAZE p. 81 |
| `al_ess_path` | Essentials Pathway | "Essentials Pathway (Intended to prepare student for a career/competitive employment)" | MAZE p. 81 |
| `al_aas_path` | Alternate Achievement Standards Pathway | "Alternate Achievement Standards Pathway (AAS)" | MAZE p. 81 |
| `al_aod` | Alabama Occupational Diploma | "including those pursuing the Alabama Occupational Diploma (AOD)" | r. 290-8-9-.10(9) |
| `al_ahsge` | Alabama High School Graduation Exam | "passes all portions of the Alabama High School Graduation Exam (AHSGE)" | r. 290-8-9-.10(9) |
| `al_post_survey` | Alabama Post-School Outcomes Survey | "This survey is called the Alabama Post-School Outcomes Survey." | MAZE p. 108 |
| `al_grst` | Gifted Referrals Screening Team | "Gifted Referrals Screening Team (GRST). Each LEA must establish a team(s)" | r. 290-8-9-.12(2) |
| `al_edt` | Eligibility Determination Team | "Each LEA must establish an Eligibility Determination Team(s) (EDT)" | r. 290-8-9-.12(5) |
| `al_matrix` | Matrix of Multiple Criteria | "Matrix of Multiple Criteria. The matrix of multiple criteria developed by" | r. 290-8-9-.12(5) |
| `al_gep` | Gifted Education Plan | "Gifted Education Plan (GEP). Each gifted student receiving pull-out services" | r. 290-8-9-.12(7) |
| `psychometrist` | Psychometrist | "clinical psychologists, school psychologists, school psychometrists, clinical psychiatrists" | r. 290-8-9-.02(3) |
| `indiv_intel` | Individual intellectual evaluation | "Individual Intellectual Evaluations. Public agencies must conduct or have conducted" | r. 290-8-9-.02(3) |
| `ceis` | Coordinated early intervening services | "CEIS Coordinated Early Intervening Services" | MAZE p. 7 |
| `cceis` | Comprehensive coordinated early intervening services | "CCEIS Comprehensive Coordinated Early Intervening Services" | MAZE p. 7 |
| `osep` | Office of Special Education Programs | "OSEP Office of Special Education Programs" | MAZE p. 8 |
| `bcba` | Board-Certified Behavior Analyst | "BCBA Board-Certified Behavior Analyst" | MAZE p. 7 |
| `sbmh` | School based mental health | "SBMH School Based Mental Health" | MAZE p. 8 |
| `vr_services` | Vocational rehabilitation services | "VRS Vocational Rehabilitation Services" | MAZE p. 9 |
| `bus_susp` | Bus suspension | "Bus Suspension. Whether a bus suspension would count as a day of suspension" | r. 290-8-9-.09(7) |
| `iss` | In-school suspension | "In-School Suspension. A day of in-school suspension is not a removal" | r. 290-8-9-.09(8) |
| `carnegie` | Carnegie unit | "including the opportunity to earn Carnegie Units" | r. 290-8-9-.10(9) |
| `head_start` | Head Start | "supplemental organized learning opportunities, e.g., preschool, Head Start, after school programs" | MAZE p. 22 |
| `sb_iep` | Standards-based IEP | "identify concerns to be addressed when developing a standards-based IEP" | MAZE p. 167 |

The last 13 have no `jurisdiction` (national concepts). `vr_services` carries "VRS" tagged US-AL only.

New strings on existing concepts (tagged US-AL unless marked): "emotional disability" (`ed`), "Problem Solving Team", "Problem-Solving Team" and "PST" (`sst`), "Eligibility Committee" (`eligibility`), "eligibility report" (`eval_report`), "Special Education Rights" and "Alabama's Procedural Safeguards" (`safeguards_notice`), "Notice of Proposal or Refusal to Take Action" (`pwn`), "Notice of Revocation of Consent for Continued Provision of Special Education and Related Services" (`revoke`), "Annual Goal Progress Report" (`progress`), "SAAFP" (`sop`), "Special Education Advisory Panel" and "SEAP" (`state_panel`), "special education complaint" (`state_complaint`), "special transportation" (`transport`), "career/technical education" (`voc_ed`), "intellectually gifted" (`gifted`), "graduation certificate" (`cert_completion`), "articulation/phonological disorder" (`artic`), "Individual Family Service Plan" (`ifsp`), "Transition Planning Meeting" (`part_c_transition`), "AUT" (`autism`), "DPH" (`dp_hearing`); untagged: "due process hearing request" (`dp_complaint`).

## 3. Unsure
- **Currency of the rule and the diploma terms.** The rule is the 2013 supplement. It names the Alabama High School Graduation Exam and the Alabama Occupational Diploma, while the 2019 guide describes three pathways to the Alabama High School Diploma and never mentions either. Both are kept because they are rule text, with neutral notes. A reviewer may want to mark them legacy once a newer source is in hand.
- **Alabama Extended Standards vs. Alabama Alternate Achievement Standards.** The rule (2013) and the guide (2019) use different names for standards for students with significant cognitive disabilities. They're two concepts here; they may be the same thing renamed.
- **"Graduation certificate"** went on `cert_completion`. Alabama awards it for completing the IEP, or for missing either the credits or the exit exam (r. .10(9)(c)-(e)), so it's broader than a certificate of completion.
- **Problem Solving Team** went on `sst` (student support team), as Louisiana's School Building Level Committee did.
- **"Eligibility Committee"** went on `eligibility` as a synonym. It names the group that makes the decision, not the decision itself.
- **Early Learning Progress Profile** is categorized `evaluation_eligibility`; `iep_component` would also fit.
- **"School based mental health"** is written without the hyphen because that's how the guide spells it.

## 4. Risky
- **Place names (graded high automatically):** 18 records beginning "Alabama". "Alabama" and "Alabama's" are also on the first-name list, so these are protected only as full phrases.
- **Acronyms with other meanings, all case-sensitive and tagged US-AL:** "PST" (Pacific Standard Time), "DPH" (Department of Public Health), "AAA", "NEO" (also a given name in some lists, though not flagged here), "SETS" (Kansas uses it for Special Education and Title Services; the build lists this as an allowed cross-state ambiguity), "EDT" (Eastern Daylight Time), "AOD", "RIC", "GEP".
- **Eponym:** `carnegie` ("Carnegie unit"), flagged `eponym`, full phrase only.
- **Name-list hits on common words:** "Early" (several records), "Head" (Head Start), "General" (General Education Pathway), "High" (diploma and exam), "Post" (outcomes survey), "Parent" (Alabama Parent Education Center).

## 5. Left out
- All people named (State Board members, superintendents, rule authors), addresses, phone numbers and emails; the county board credited on MAZE pp. 139-141.
- "SES" (ALSDE's Special Education Services section), because it usually means socioeconomic status; "DB", "EL" and "PBS" as two- or three-letter acronyms with common other meanings.
- Test products named in the MAZE questions (Slosson, K-BIT-2, WRAT-4, PIAT-R, UNIT, the Torrance tests, DIBELS, WIDA ACCESS, ACT products) and "ACAP summative", which appears only as an acronym.
- General education initiatives in the acronym list (AMSI, AMSTI, ARFI, ARI), eGAP (grants), SPP/APR, SSR (monitoring), UCP (a national charity), Legal Services Alabama and the Alabama State Bar.
- The transition service area codes on MAZE p. 86 (VE, CE, PM, T, ED, M, PE, LA, LTA, AG, FM), which are short codes on a form; "tongue thrust"; "socially maladjusted"; "Procedures for Determining Inability to Provide Informed Consent"; "Alabama High School Diploma with Advanced Endorsement" (r. .10(9)(a)), which could be added as a synonym of `al_ahsd`.
