# Audit: Indiana layer (`sources/states/indiana.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-08 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section and paragraph, or the cited PDF page, of text extracted from the documents in this folder (ligatures, quotes, dashes and line-break hyphens normalized). For entries that attest an existing concept without adding strings, the check passes if any of the concept's existing strings appears at the citation. Entries without a literal hit were checked by hand.

Documents: 511 IAC 7 (IDOE compilation, May 2024, 167 pp.), IDOE Notice of Procedural Safeguards (Aug. 2025, 25 pp.), Navigating the Course (Aug. 2025, 63 pp.).

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `autism` — 511 IAC 7-41-1 | Autism, autism spectrum disorder | confirmed |  |  | 41. ELIGIBILITY CRITERIA 511 IAC 7-41-1 Autism spectrum disorder Sec. 1. (a) Autism |
| 2 | `vi` — 511 IAC 7-41-2 | blind or low vision | confirmed |  |  | related services needs. 511 IAC 7-41-2 Blind or low vision Sec. 2. (a) "Blind or |
| 3 | `id` — 511 IAC 7-41-3 | Intellectual disability, mild intellectual disability, moderate intellectual disability, severe intellectual d | confirmed |  |  | related services needs. 511 IAC 7-41-3 Intellectual disability Sec. 3. (a) An intellectual disability: |
| 4 | `hi` — 511 IAC 7-41-4 | Hearing impairment, hard of hearing, deaf or hard of hearing, hearing loss | confirmed |  |  | may be referred to as a hearing impairment , means the following: (1) A disability |
| 5 | `deafness` — 511 IAC 7-41-4 | deaf | confirmed |  |  | related services needs. 511 IAC 7-41-4 Deaf or hard of hearing Sec. 4. |
| 6 | `deafblind` — 511 IAC 7-41-5 | dual sensory impaired | confirmed |  |  | which may be referred to as dual sensory impaired , means a disability that: (1) |
| 7 | `dd` — 511 IAC 7-41-6 | Developmental delay, student with a developmental delay | confirmed |  |  | related services needs. 511 IAC 7-41-6 Developmental delay Sec. 6. (a) Developmental delay is |
| 8 | `ed` — 511 IAC 7-41-7 | emotional disability | confirmed |  |  | related services needs. 511 IAC 7-41-7 Emotional disability Sec. 7. (a) "Emotional disability" means |
| 9 | `sli` — 511 IAC 7-41-8 | language or speech impairment | confirmed |  |  | related services needs. 511 IAC 7-41-8 Language or speech impairment Sec. 8. (a) A language |
| 10 | `md` — 511 IAC 7-41-9 | Multiple disabilities | confirmed |  |  | related services needs. 511 IAC 7-41-9 Multiple disabilities Sec. 9. (a) "Multiple disabilities" means |
| 11 | `ohi` — 511 IAC 7-41-10 | Other health impairment, health impairment, other health impaired | confirmed |  |  | related services needs. 511 IAC 7-41-10 Other health impairment Sec. 10. (a) "Other health impairment" |
| 12 | `oi` — 511 IAC 7-41-11 | Orthopedic impairment | confirmed |  |  | related services needs. 511 IAC 7-41-11 Orthopedic impairment Sec. 11. (a) An orthopedic impairment |
| 13 | `sld` — 511 IAC 7-41-12 | Specific learning disability, learning disability | confirmed |  |  | related services needs. 511 IAC 7-41-12 Specific learning disability Sec. 12. (a) "Specific learning disability" |
| 14 | `tbi` — 511 IAC 7-41-13 | Traumatic brain injury | confirmed |  |  | speed. (E) Attention. 511 IAC 7-41-13 Traumatic brain injury Sec. 13. (a) A traumatic brain |
| 15 | `adaptive` — 511 IAC 7-32-3 | Adaptive behavior | confirmed |  |  | other achievement measures. 511 IAC 7-32-3 " Adaptive behavior " defined Sec. 3. "Adaptive behavior" |
| 16 | `adverse` — 511 IAC 7-32-5 | Adversely affects educational performance, educational performance | confirmed |  |  | common understandable language. 511 IAC 7-32-5 " Adversely affects educational performance " defined Sec. 5. |
| 17 | `at_device` — 511 IAC 7-32-7 | Assistive technology device, assistive technology | confirmed |  |  | Interviews. (5) Observations. 511 IAC 7-32-7 " Assistive technology device " defined Sec. 7. "Assistive |
| 18 | `at_service` — 511 IAC 7-32-8 | Assistive technology service | confirmed |  |  | of such device. 511 IAC 7-32-8 " Assistive technology service " defined Sec. 8. "Assistive |
| 19 | `bip` — 511 IAC 7-32-10 | Behavioral intervention plan | confirmed |  |  | statute or rule. 511 IAC 7-32-10 " Behavioral intervention plan " defined Sec. 10. (a) |
| 20 | `sto` — 511 IAC 7-32-11 | benchmarks | confirmed |  |  | in this section. 511 IAC 7-32-11 " Benchmarks " defined Sec. 11. "Benchmarks" means major |
| 21 | `iep_team` — 511 IAC 7-32-12 | case conference committee, CCC | confirmed |  |  | a student's IEP. 511 IAC 7-32-12 " Case conference committee " or "CCC" defined Sec. |
| 22 | `cop` — 511 IAC 7-32-14 | Change of placement | confirmed |  |  | (3) is different from a disciplinary change of placement described in 511 IAC 7-44-2. 3 |
| 23 | `consent` — 511 IAC 7-32-17 | (existing strings of `consent`) | confirmed (checked by hand) |  | Defined as "Consent" |  |
| 24 | `consult` — 511 IAC 7-32-18 | consultation | confirmed |  |  | consent was revoked. 511 IAC 7-32-18 " Consultation " defined Sec. 18. "Consultation" means services |
| 25 | `controlled` — 511 IAC 7-32-20 | Controlled substance | confirmed |  |  | of the student. 511 IAC 7-32-20 " Controlled substance " defined Sec. 20. "Controlled substance" |
| 26 | `dp_hearing` — 511 IAC 7-32-27 | due process hearing, hearing officer, independent hearing officer | confirmed |  |  | or electronic means. 511 IAC 7-32-27 " Due process hearing " defined Sec. 27. "Due |
| 27 | `evaluation` — 511 IAC 7-32-30 | educational evaluation | confirmed |  |  | general education environment. 511 IAC 7-32-30 " Educational evaluation " defined Sec. 30. (a) "Educational |
| 28 | `ed_records` — 511 IAC 7-32-31 | educational records | confirmed |  |  | the student's CCC. 511 IAC 7-32-31 " Educational records " defined Sec. 31. (a) "Educational |
| 29 | `surrogate` — 511 IAC 7-32-32 | educational surrogate parent | confirmed |  |  | of the record. 511 IAC 7-32-32 " Educational surrogate parent " defined Sec. 32. "Educational |
| 30 | `exp_hearing` — 511 IAC 7-32-37 | Expedited due process hearing | confirmed |  |  | Reading comprehension strategies. 511 IAC 7-32-37 " Expedited due process hearing " defined Sec. 37. |
| 31 | `esy` — 511 IAC 7-32-39 | Extended school year services, extended school year | confirmed |  |  | 511 IAC 7-44-9. 511 IAC 7-32-39 " Extended school year services " defined Sec. 39. |
| 32 | `fape` — 511 IAC 7-32-40 | Free appropriate public education, FAPE | confirmed |  |  | department of education. 511 IAC 7-32-40 " Free appropriate public education " or "FAPE" defined |
| 33 | `fba` — 511 IAC 7-32-41 | Functional behavioral assessment | confirmed |  |  | students without disabilities. 511 IAC 7-32-41 " Functional behavioral assessment " defined Sec. 41. "Functional |
| 34 | `func_perf` — 511 IAC 7-32-42 | Functional performance | confirmed |  |  | 511 IAC 7-40-3(b)(3). 511 IAC 7-32-42 " Functional performance " defined Sec. 42. "Functional performance" |
| 35 | `homeless` — 511 IAC 7-32-46 | Homeless children | confirmed |  |  | has the meaning given the term " homeless children and youths" in the McKinney-Vento Homeless |
| 36 | `illegal_drug` — 511 IAC 7-32-47 | Illegal drug | confirmed |  |  | (1) through (3). 511 IAC 7-32-47 " Illegal drug " defined Sec. 47. "Illegal drug" |
| 37 | `ifsp` — 511 IAC 7-32-49 | Individualized family service plan, IFSP | confirmed |  |  | by the CCC. 511 IAC 7-32-49 " Individualized family service plan " or "IFSP" defined |
| 38 | `itd` — 511 IAC 7-32-50 | Infant or toddler with a disability | confirmed |  |  | with a disability. 511 IAC 7-32-50 " Infant or toddler with a disability " defined |
| 39 | `lep` — 511 IAC 7-32-59 | Limited English proficient | confirmed |  |  | (6) other administrators. 511 IAC 7-32-59 " Limited English proficient " defined Sec. 59. "Limited |
| 40 | `lea` — 511 IAC 7-32-60 | Local educational agency | confirmed |  |  | fully in society. 511 IAC 7-32-60 " Local educational agency " defined Sec. 60. "Local |
| 41 | `mdr` — 511 IAC 7-32-61 | Manifestation determination | confirmed |  |  | and state-operated schools. 511 IAC 7-32-61 " Manifestation determination " defined Sec. 61. "Manifestation determination" |
| 42 | `mediation` — 511 IAC 7-32-62 | Mediation | confirmed |  |  | the student's IEP. 511 IAC 7-32-62 " Mediation " defined Sec. 62. "Mediation" means a |
| 43 | `medical` — 511 IAC 7-32-63 | Medical services | confirmed |  |  | to the student. 511 IAC 7-32-63 " Medical services " defined Sec. 63. "Medical services" |
| 44 | `mdt` — 511 IAC 7-32-65 | Multidisciplinary team | confirmed |  |  | and alternative communication. 511 IAC 7-32-65 " Multidisciplinary team " defined Sec. 65. "Multidisciplinary team" |
| 45 | `native_language` — 511 IAC 7-32-66 | Native language | confirmed |  |  | the educational evaluation. 511 IAC 7-32-66 " Native language " defined Sec. 66. "Native language", |
| 46 | `om` — 511 IAC 7-32-68 | orientation and mobility | confirmed |  |  | teacher" defined (Repealed) 511 IAC 7-32-68 " Orientation and mobility " defined Sec. 68. "Orientation |
| 47 | `ppps` — 511 IAC 7-32-71 | parentally-placed nonpublic school students with disabilities | confirmed |  |  | of this article. 511 IAC 7-32-71 " Parentally-placed nonpublic school students with disabilities " defined |
| 48 | `pti` — 511 IAC 7-32-72 | Parent training and information center | confirmed |  |  | a public agency. 511 IAC 7-32-72 " Parent training and information center " defined Sec. |
| 49 | `pe` — 511 IAC 7-32-74 | Physical education, adapted physical education | confirmed |  |  | including disability designation. 511 IAC 7-32-74 " Physical education " defined Sec. 74. (a) "Physical |
| 50 | `progress` — 511 IAC 7-32-76 | progress monitoring | confirmed |  |  | in the classroom. 511 IAC 7-32-76 " Progress monitoring " defined Sec. 76. "Progress monitoring" |
| 51 | `public_agency` — 511 IAC 7-32-77 | Public agency | confirmed |  |  | instruction and intervention. 511 IAC 7-32-77 " Public agency " defined Sec. 77. "Public agency" |
| 52 | `resolution` — 511 IAC 7-32-80 | Resolution meeting | confirmed |  |  | of that device. 511 IAC 7-32-80 " Resolution meeting " defined Sec. 80. "Resolution meeting" |
| 53 | `sbi` — 511 IAC 7-32-83 | Serious bodily injury | confirmed |  |  | 11, or 12. 511 IAC 7-32-83 " Serious bodily injury " defined Sec. 83. "Serious |
| 54 | `services_plan` — 511 IAC 7-32-84 | service plan | confirmed |  |  | or mental faculty. 511 IAC 7-32-84 " Service plan " defined Sec. 84. "Service plan" |
| 55 | `special_ed` — 511 IAC 7-32-86 | Special education | confirmed |  |  | situations and environments. 511 IAC 7-32-86 " Special education " defined Sec. 86. "Special education" |
| 56 | `sdi` — 511 IAC 7-32-88 | Specially designed instruction | confirmed |  |  | a written agreement. 511 IAC 7-32-88 " Specially designed instruction " defined Sec. 88. "Specially |
| 57 | `sig_cog` — 511 IAC 7-32-93.5 | Most significant cognitive disability, significant cognitive disability | confirmed |  |  | 511 IAC 7-32-93.5 "Student with the most significant cognitive disability " defined Sec. 93.5. "Student |
| 58 | `sop` — 511 IAC 7-32-94 | summary of performance | confirmed |  |  | modifications of instruction. 511 IAC 7-32-94 " Summary of performance " defined Sec. 94. "Summary |
| 59 | `saas` — 511 IAC 7-32-95 | Supplementary aids and services, supplementary aids | confirmed |  |  | student's postsecondary goals. 511 IAC 7-32-95 " Supplementary aids and services " defined Sec. 95. |
| 60 | `part_c_transition` — 511 IAC 7-32-99 | transition planning | confirmed |  |  | with a disability. 511 IAC 7-32-99 " Transition planning " defined Sec. 99. "Transition planning" |
| 61 | `transition` — 511 IAC 7-32-100 | Transition services, coordinated set of activities | confirmed |  |  | disruptions in services. 511 IAC 7-32-100 " Transition services " defined Sec. 100. (a) "Transition |
| 62 | `universal_design` — 511 IAC 7-32-102 | Universal design | confirmed |  |  | In the community. 511 IAC 7-32-102 " Universal design " defined Sec. 102. "Universal design" |
| 63 | `voc_ed` — 511 IAC 7-32-104 | Vocational education | confirmed |  |  | in IC 20-43-1-34. 511 IAC 7-32-104 " Vocational education " defined Sec. 104. "Vocational education" |
| 64 | `ward` — 511 IAC 7-32-105 | Ward of the State | confirmed |  |  | or advanced degree. 511 IAC 7-32-105 " Ward of the state " defined Sec. 105. |
| 65 | `weapon` — 511 IAC 7-32-106 | Dangerous weapon | confirmed |  |  | defined Sec. 106. "Weapon" means: (1) " dangerous weapon " under 18 U.S.C. 930(g)(2), which |
| 66 | `alt_assess` — 511 IAC 7-36-10 | Alternate assessment, alternate academic achievement standards | confirmed |  |  | a student will participate in an alternate assessment in lieu of the general assessment, |
| 67 | `ecse` — 511 IAC 7-43-2 | Early childhood special education | confirmed |  |  | early intervention services (Part C) to early childhood special education (Part B) Sec. 2. (a) |
| 68 | `age_majority` — 511 IAC 7-43-5 | transfer of parental rights | confirmed |  |  | the parent were informed of the transfer of parental rights in accordance with 511 IAC |
| 69 | `alt_diploma` — 511 IAC 7-43-4 | alternate diploma | confirmed |  |  | in 511 IAC 6-7.1-1(e); (B) an alternate diploma under 511 IAC 6-7.1-10; or (C) |
| 70 | `dc_educ_rep` — 511 IAC 7-43-6 | Educational representative | confirmed |  |  | 511 IAC 7-43-6 Appointment of an educational representative Sec. 6. (a) Any student eligible |
| 71 | `dp_hearing` — 511 IAC 7-45-8 | independent hearing officer | confirmed |  |  | any litigation completed. 511 IAC 7-45-8 Independent hearing officer qualifications Sec. 8. (a) A person |
| 72 | `excess_costs` — 511 IAC 7-47-1 | Excess costs | confirmed |  |  | enter into contracts to fund the excess costs of educating students whose disabilities are |
| 73 | `safeguards_notice` — IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 1 | procedural safeguards, notice of procedural safeguards | confirmed |  |  | INDIANA DEPARTMENT OF EDUCATION NOTICE OF PROCEDURAL SAFEGUARDS As the parent of a child |
| 74 | `sea` — IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 2 | State educational agency, SEA | confirmed |  |  | state-operated schools. Public Agency includes the state educational agency (SEA), LEAs, ESAs, public charter schools |
| 75 | `vi` — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | BLV | confirmed |  |  | Behavior Intervention Plan LI Language Impairment BLV Blind or Low Vision MD Multiple |
| 76 | `mdt` — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | M-Team | confirmed |  |  | Multiple Disabilities CCC Case Conference Committee M-Team Multidisciplinary Team CSEP Choice Scholarship Education |
| 77 | `safeguards_notice` — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | NOPS | confirmed |  |  | Team CSEP Choice Scholarship Education Plan NOPS Notice of Procedural Safeguards CD Cognitive |
| 78 | `id` — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | cognitive disability | confirmed |  |  | NOPS Notice of Procedural Safeguards CD Cognitive Disability OHI Other Health Impairment DB Deaf-Blind |
| 79 | `lea_rep` — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | public agency representative | confirmed |  |  | Deaf or Hard of Hearing PAR Public Agency Representative ECA End of Course Assessment ED |
| 80 | `in_doe` (new concept) — IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 1 | Indiana Department of Education, IDOE | confirmed |  |  | INDIANA DEPARTMENT OF EDUCATION NOTICE OF PROCEDURAL SAFEGUARDS As the |
| 81 | `in_dse` (new concept) — 511 IAC 7-33-1 | Division of special education | confirmed |  |  | earlier. (b) The department of education, division of special education is the state educational agency |
| 82 | `in_oalp` (new concept) — IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 19 | Office of Administrative Law Proceedings, OALP | confirmed |  |  | the secretary of education's designee, the Office of Administrative Law Proceedings (OALP) at the following |
| 83 | `in_insource` (new concept) — IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 25 | IN*SOURCE | confirmed |  |  | "IN*SOURCE" (contact list; nearby names and contact details left out) |
| 84 | `in_idr` (new concept) — IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 25 | Indiana Disability Rights | confirmed |  |  | "Indiana Disability Rights" (contact list; nearby names and contact details left out) |
| 85 | `in_isbvi` (new concept) — 511 IAC 7-32-77 | Indiana School for the Blind and Visually Impaired | confirmed |  |  | state department of health. (4) The Indiana School for the Blind and Visually Impaired . |
| 86 | `in_isd` (new concept) — 511 IAC 7-32-77 | Indiana School for the Deaf | confirmed |  |  | Blind and Visually Impaired. (5) The Indiana School for the Deaf . (6) Programs operated |
| 87 | `in_school_corp` (new concept) — 511 IAC 7-32-77 | School corporation | confirmed |  |  | are not part of a public school corporation . (3) Programs operated by the state |
| 88 | `in_scols` (new concept) — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | School corporation of legal settlement, SCOLS | confirmed |  |  | SBOE State Board of Education SCOLS School Corporation of Legal Settlement SI Speech Impairment SLD |
| 89 | `in_legal_settlement` (new concept) — 511 IAC 7-32-56 | Legal settlement | confirmed |  |  | are being learned. 511 IAC 7-32-56 " Legal settlement " defined Sec. 56. "Legal settlement", |
| 90 | `in_sepd` (new concept) — 511 IAC 7-32-87 | Special education planning district | confirmed |  |  | Speech-language pathology services. 511 IAC 7-32-87 " Special education planning district " defined Sec. 87. |
| 91 | `in_article7` (new concept) — IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. 1 | Article 7 | confirmed |  |  | that option available. Special Education Terms Article 7 means Indiana's special education regulations that |
| 92 | `in_student_legal_age` (new concept) — 511 IAC 7-32-91 | Student of legal age | confirmed |  |  | under this article. 511 IAC 7-32-91 " Student of legal age " defined Sec. 91. |
| 93 | `in_transition_iep` (new concept) — 511 IAC 7-32-48 | Transition IEP | confirmed |  |  | in 511 IAC 7-42-6. (b) A transition IEP is an IEP that is: (1) |
| 94 | `in_teacher_record` (new concept) — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | Teacher of record, TOR | confirmed |  |  | Plan TBI Traumatic Brain Injury TOR Teacher of Record TOS Teacher of Service SECTION I: |
| 95 | `in_teacher_service` (new concept) — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | Teacher of service, TOS | confirmed |  |  | Injury TOR Teacher of Record TOS Teacher of Service SECTION I: INTRODUCTION The purpose of |
| 96 | `in_consult_collab` (new concept) — 511 IAC 7-32-19 | Consultation and collaboration | confirmed |  |  | counseling and training. 511 IAC 7-32-19 " Consultation and collaboration " defined Sec. 19. "Consultation |
| 97 | `job_coach` (new concept) — 511 IAC 7-32-55 | Job coach | confirmed |  |  | and emotional skills. 511 IAC 7-32-55 " Job coach " defined Sec. 55. "Job coach" |
| 98 | `systematic_obs` (new concept) — 511 IAC 7-32-96 | Systematic observation | confirmed |  |  | 511 IAC 7-42-10. 511 IAC 7-32-96 " Systematic observation " defined Sec. 96. "Systematic observation" |
| 99 | `in_first_steps` (new concept) — IDOE Navigating the Course (Aug. 2025), PDF p. 30 | First Steps | confirmed |  |  | by the public school. Transitioning from First Steps to Early Childhood Special Education (511 |
| 100 | `in_istar` (new concept) — IDOE Navigating the Course (Aug. 2025), PDF p. 7 | Indiana Standards Tool for Alternative Reporting, ISTAR | confirmed |  |  | IFSP Individual Family Service Plan ISTAR Indiana Standards Tool for Alternative Reporting PII Personally Identifiable |
| 101 | `in_choice_scholarship` (new concept) — 511 IAC 7-49-2 | Choice scholarship | confirmed |  |  | definitions apply throughout this rule: (1) " Choice scholarship student" means a student who has |
| 102 | `in_csep` (new concept) — 511 IAC 7-49-2 | Choice special education plan, CSEP | confirmed |  |  | 20-51-1-4.7 and 512 IAC 4. (3) " Choice special education plan " or "CSEP" means |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Education Scholarship Account (ESA) education service plan | 511 IAC 7-50; 7-34-3, 7-34-5, 7-49-11; NAV pp. 5-9, 56-57 (30 uses) | Indiana's ESA program for students with disabilities. Add the full name only; "ESA" already means educational service agency |
| Indiana Complaint, Hearing, and Mediation Process (I-CHAMP) | PSN pp. 16-19 | IDOE's dispute resolution portal; candidate concept |
| Expedited evaluation | 511 IAC 7-32-38 | Defined term not in the dataset |
| Student with a print disability | 511 IAC 7-32-93 | Defined term not in the dataset |
| Duration of services; length and frequency of services | 511 IAC 7-32-28, 7-32-57 | Defined terms not in the dataset |
| Virtual instruction | 511 IAC 7-32-103.5 | Defined term not in the dataset |
| Certificate of completion | 511 IAC 7-43-4, 7-40-3; NAV pp. 32-33 | Attest existing `cert_completion` |
| Interim alternative educational setting, prior written notice, reevaluation, IEE | 511 IAC 7-32-53 and elsewhere (94, 157, 133, 54 uses) | Federal concepts the rule defines or uses heavily but the layer does not attest. Low priority |

## 3. Summary

- **102 entries: 102 confirmed, 0 misplaced, 0 not found.** 1 needed a hand check.
- **Safety:** no single letters, and no person's name standing alone as a term. Place names are graded automatically. Notes on individual strings are in the table.
- **Typing:** every all-capitals string is typed as an acronym or abbreviation; state-only strings carry the state tag.
- **Build:** `build --check` passes and all 70 tests pass.

**Most important fixes**

1. Add **Education Scholarship Account** (511 IAC 7-50 and NAV, 30 uses), as a full name only, since "ESA" already means educational service agency.
2. Add **I-CHAMP** (PSN pp. 16-19).
3. Several 511 IAC 7-32 definitions aren't attested: some exist in the dataset already (IAES, homebound instruction, travel training, early intervening services) and some don't (expedited evaluation, student with a print disability, virtual instruction).

**Docstring:** Accurate. Page counts (167, 25, 63) match, and the acronym index is on NAV p. 7 as stated.

**Update (2026-10-08):** Fixes 1-3 applied in `indiana_supplement`: Indiana education scholarship account and its education service plan (511 IAC 7-50-2), I-CHAMP (PSN p. 16), expedited evaluation, student with a print disability and virtual instruction. Homebound instruction, IAES, travel training and certificate of completion are now attested in the Indiana layer; early intervening services is attested in the supplement, because that concept is defined by a later layer. Released in 0.38.0.
