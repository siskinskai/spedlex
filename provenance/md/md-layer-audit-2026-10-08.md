# Audit: Maryland layer (`sources/states/maryland.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-08 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section and paragraph, or the cited PDF page, of text extracted from the documents in this folder (ligatures, quotes, dashes and line-break hyphens normalized). For entries that attest an existing concept without adding strings, the check passes if any of the concept's existing strings appears at the citation. Entries without a literal hit were checked by hand.

Documents: COMAR 13A.05.01 (text saved from regs.maryland.gov), MSDE Maryland Procedural Safeguards Notice (July 2024, 51 pp.), MSDE Parent Information Series: The IEP (2023, 20 pp.).

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `alt_assess` — COMAR 13A.05.01.03B(2-1) | AAAS | confirmed |  |  | §§1401-1419. (2-1) "Alternate academic achievement standards ( AAAS )" means academic achievement standards that: (a) |
| 2 | `alt_assess` — COMAR 13A.05.01.03B(2-2) | AAAS | confirmed |  |  | significant cognitive disabilities aligned with the AAAS . (3) "Assessment" means the process of |
| 3 | `at_device` — COMAR 13A.05.01.03B(4) | Assistive technology device, assistive technology | confirmed |  |  | special education and related services. (4) Assistive Technology Device . (a) "Assistive technology device" means |
| 4 | `at_service` — COMAR 13A.05.01.03B(5) | Assistive technology service | confirmed |  |  | replacement of such a device. (5) Assistive Technology Service . (a) "Assistive technology service" means |
| 5 | `audiology` — COMAR 13A.05.01.03B(7) | Audiology | confirmed |  |  | consistent with 34 CFR §300.39(b)(1). (7) " Audiology " means services which include: (a) Identification |
| 6 | `autism` — COMAR 13A.05.01.03B(8) | Autism | confirmed |  |  | evaluating the effectiveness of amplification. (8) " Autism " means a developmental disability that: (a) |
| 7 | `voc_ed` — COMAR 13A.05.01.03B(10) | career and technology education | confirmed |  |  | be in attendance for instruction. (10) " Career and technology education " means organized educational |
| 8 | `charter_school` — COMAR 13A.05.01.03B(11) | Charter school | confirmed |  |  | a baccalaureate or advanced degree. (11) " Charter school " means a school that operates |
| 9 | `consent` — COMAR 13A.05.01.03B(12) | (existing strings of `consent`) | confirmed (checked by hand) |  | Defined as "Consent" |  |
| 10 | `consult` — COMAR 13A.05.01.03B(13) | consultation | confirmed |  |  | of the revocation of consent. (13) " Consultation " means services provided to a teacher, |
| 11 | `counseling` — COMAR 13A.05.01.03B(14) | Counseling services | confirmed |  |  | implementation of a student's IEP. (14) " Counseling services " means services provided by qualified |
| 12 | `critical_skill` — COMAR 13A.05.01.03B(15) | critical life skill | confirmed |  |  | counselors, or other qualified personnel. (15) " Critical life skill " means a skill determined |
| 13 | `deafblind` — COMAR 13A.05.01.03B(17) | Deaf-blindness | confirmed |  |  | school day or business day. (17) " Deaf-blindness " means concomitant hearing and visual impairments, |
| 14 | `deafness` — COMAR 13A.05.01.03B(18) | Deafness | confirmed |  |  | or a student with blindness. (18) " Deafness " means a hearing impairment which: (a) |
| 15 | `ed` — COMAR 13A.05.01.03B(23) | emotional disability | confirmed |  |  | as described under COMAR 13A.03.05. (23) Emotional Disability . (a) "Emotional disability" means a condition |
| 16 | `evaluation` — COMAR 13A.05.01.03B(25) | Evaluation | confirmed |  |  | and (v) Other related materials. (25) Evaluation . (a) "Evaluation" means the process of |
| 17 | `esy` — COMAR 13A.05.01.03B(26) | Extended school year services, extended school year | confirmed |  |  | and .06 of this chapter. (26) " Extended school year services " means the individualized |
| 18 | `fape` — COMAR 13A.05.01.03B(27) | Free appropriate public education, FAPE | confirmed |  |  | the standards of the Department. (27) " Free appropriate public education (FAPE)" means special education |
| 19 | `gen_curr` — COMAR 13A.05.01.03B(28) | general curriculum | confirmed |  |  | U.S.C. §1414, and this chapter. (28) " General curriculum " means the curricular content adopted |
| 20 | `hi` — COMAR 13A.05.01.03B(29) | Hearing impairment | confirmed |  |  | from preschool through secondary education. (29) " Hearing impairment " means an impairment in hearing, |
| 21 | `homeless` — COMAR 13A.05.01.03B(30) | (existing strings of `homeless`) | confirmed (checked by hand) |  | "Homeless students" |  |
| 22 | `dp_hearing` — COMAR 13A.05.01.03B(31) | due process hearing, hearing officer, impartial hearing officer, impartial hearing | confirmed |  |  | of Administrative Hearings to conduct a due process hearing in accordance with 34 CFR §300.511(c) |
| 23 | `iee` — COMAR 13A.05.01.03B(33) | Independent educational evaluation | confirmed |  |  | or unlike the ones named. (33) " Independent educational evaluation " means assessment procedures conducted |
| 24 | `iep` — COMAR 13A.05.01.03B(34) | Individualized education program, IEP | confirmed |  |  | the education of the student. (34) " Individualized education program (IEP)" means a written statement |
| 25 | `iep_team` — COMAR 13A.05.01.03B(35) | IEP Team | confirmed |  |  | and .09 of this chapter. (35) " IEP team " means a group of individuals |
| 26 | `id` — COMAR 13A.05.01.03B(36) | Intellectual disability | confirmed |  |  | Regulation .10 of this chapter. (36) " Intellectual disability " means general intellectual functioning, adversely |
| 27 | `interpreting` — COMAR 13A.05.01.03B(37) | Interpreting services, oral transliteration, cued language transliteration | confirmed |  |  | manifested during the developmental period. (37) Interpreting Services . (a) "Interpreting services" means services for |
| 28 | `cart` — COMAR 13A.05.01.03B(37) | CART, communication access real-time translation | confirmed |  |  | services, including Communication Access Real-Time Translation ( CART ), C-Print, and TypeWell; and (v) Special |
| 29 | `lep` — COMAR 13A.05.01.03B(38) | Limited English proficient, LEP | confirmed |  |  | public education during emergency conditions. (38) " Limited English proficient (LEP)" means an individual who |
| 30 | `lea` — COMAR 13A.05.01.03B(39) | local school system, LSS | confirmed |  |  | speak, write, or understand English. (39) " Local school system (LSS)" means any of the |
| 31 | `md` — COMAR 13A.05.01.03B(44) | Multiple disabilities | confirmed |  |  | with the Maryland Accommodations Manual. (44) Multiple Disabilities . (a) "Multiple disabilities" means concomitant impairments, |
| 32 | `native_language` — COMAR 13A.05.01.03B(45) | Native language | confirmed |  |  | not include students with deaf-blindness. (45) Native Language . (a) "Native language" means the language |
| 33 | `nonacademic` — COMAR 13A.05.01.03B(46) | (existing strings of `nonacademic`) | confirmed (checked by hand) |  | "Nonacademic and extracurricular activities and services" |  |
| 34 | `ot` — COMAR 13A.05.01.03B(48) | Occupational therapy | confirmed |  |  | in accordance with COMAR 13A.09.10. (48) " Occupational therapy " means services which include: (a) |
| 35 | `om` — COMAR 13A.05.01.03B(49) | Orientation and mobility services, orientation and mobility, long cane | confirmed |  |  | impairment or loss of function. (49) Orientation and Mobility Services . (a) "Orientation and mobility |
| 36 | `oi` — COMAR 13A.05.01.03B(50) | Orthopedic impairment | confirmed |  |  | and tools, as determined appropriate. (50) Orthopedic Impairment . (a) "Orthopedic impairment" means a severe |
| 37 | `ohi` — COMAR 13A.05.01.03B(51) | Other health impairment, health impairment | confirmed |  |  | or burns which cause contractures. (51) " Other health impairment " means having limited strength, |
| 38 | `adhd` — COMAR 13A.05.01.03B(51) | Attention deficit hyperactivity disorder, attention deficit disorder | confirmed |  |  | Asthma; (b) Attention deficit disorder or attention deficit hyperactivity disorder ; (c) Diabetes; (d) Epilepsy; |
| 39 | `epilepsy` — COMAR 13A.05.01.03B(51) | Epilepsy | confirmed |  |  | deficit hyperactivity disorder; (c) Diabetes; (d) Epilepsy ; (e) A heart condition; (f) Hemophilia; |
| 40 | `sickle` — COMAR 13A.05.01.03B(51) | Sickle cell anemia | confirmed |  |  | (i) Nephritis; (j) Rheumatic fever; (k) Sickle cell anemia ; or (l) Tourette syndrome. (52) |
| 41 | `tourette` — COMAR 13A.05.01.03B(51) | Tourette syndrome | confirmed |  |  | (k) Sickle cell anemia; or (l) Tourette syndrome . (52) Parent. (a) "Parent" means: (i) |
| 42 | `parent_training` — COMAR 13A.05.01.03B(53) | Parent counseling and training | confirmed |  |  | a ward of the State. (53) " Parent counseling and training " means: (a) Assisting |
| 43 | `part_agency` — COMAR 13A.05.01.03B(54) | Participating agency | confirmed |  |  | with information about child development. (54) " Participating agency " means a public agency, other |
| 44 | `pii` — COMAR 13A.05.01.03B(55) | Personally identifiable information, personally identifiable | confirmed |  |  | transition services to the student. (55) " Personally identifiable information " means information that includes: |
| 45 | `pe` — COMAR 13A.05.01.03B(56) | Physical education, adaptive physical education | confirmed |  |  | the student with reasonable certainty. (56) Physical Education . (a) "Physical education" means the development |
| 46 | `pt` — COMAR 13A.05.01.03B(57) | Physical therapy | confirmed |  |  | education; and (iv) Motor development. (57) " Physical therapy " means services provided by a |
| 47 | `psych` — COMAR 13A.05.01.03B(58) | Psychological services | confirmed |  |  | of Maryland, and COMAR 10.38.03.02. (58) " Psychological services " means services that include: (a) |
| 48 | `public_agency` — COMAR 13A.05.01.03B(59) | Public agency | confirmed |  |  | developing positive behavioral intervention strategies. (59) Public Agency . (a) "Public agency" means a State |
| 49 | `recreation` — COMAR 13A.05.01.03B(62) | Recreation, therapeutic recreation, leisure education, recreation services | confirmed |  |  | special education or related services. (62) " Recreation " means services which include assessment of |
| 50 | `reeval` — COMAR 13A.05.01.03B(63) | Reevaluation | confirmed |  |  | community agencies, and leisure education. (63) " Reevaluation " means an evaluation conducted after the |
| 51 | `rehab` — COMAR 13A.05.01.03B(64) | Rehabilitation counseling services, rehabilitation counseling | confirmed |  |  | Regulation .06D of this chapter. (64) " Rehabilitation counseling services " means services provided: (a) |
| 52 | `related` — COMAR 13A.05.01.03B(65) | Related services | confirmed |  |  | the Rehabilitation Act of 1973. (65) Related Services . (a) "Related services" means transportation and |
| 53 | `school_day` — COMAR 13A.05.01.03B(66) | School day | confirmed |  |  | (iv) Replacement of the device. (66) " School day " means a day, including a |
| 54 | `nursing` — COMAR 13A.05.01.03B(67) | school health services | confirmed |  |  | in accordance with COMAR 13A.08.02.01. (67) " School health services " means services: (a) Provided |
| 55 | `services_plan` — COMAR 13A.05.01.03B(69) | service plan | confirmed |  |  | include education beyond grade 12. (69) " Service plan " means a written statement developed |
| 56 | `social_work` — COMAR 13A.05.01.03B(70) | Social work services in schools, social or developmental history, developmental history | confirmed |  |  | services and any transportation necessary. (70) " Social work services in schools " means services |
| 57 | `special_ed` — COMAR 13A.05.01.03B(71) | Special education | confirmed |  |  | of positive behavioral intervention strategies. (71) Special Education . (a) "Special education" means specially designed |
| 58 | `sdi` — COMAR 13A.05.01.03B(72) | Specially designed instruction | confirmed |  |  | consists of specially designed instruction. (72) " Specially designed instruction " means the adaptation of |
| 59 | `sld` — COMAR 13A.05.01.03B(73) | Specific learning disability, SLD, learning disability | confirmed |  |  | jurisdiction of the public agency. (73) Specific Learning Disability (SLD). (a) "SLD" means a disorder |
| 60 | `perceptual` — COMAR 13A.05.01.03B(73) | Perceptual disabilities | confirmed |  |  | (b) "SLD" includes conditions such as perceptual disabilities , brain injury, minimal brain dysfunction, dyslexia, |
| 61 | `mbd` — COMAR 13A.05.01.03B(73) | Minimal brain dysfunction | confirmed |  |  | such as perceptual disabilities, brain injury, minimal brain dysfunction , dyslexia, and developmental aphasia. (c) |
| 62 | `dyslexia` — COMAR 13A.05.01.03B(73) | Dyslexia | confirmed |  |  | disabilities, brain injury, minimal brain dysfunction, dyslexia , and developmental aphasia. (c) "SLD" does |
| 63 | `aphasia` — COMAR 13A.05.01.03B(73) | Developmental aphasia | confirmed |  |  | injury, minimal brain dysfunction, dyslexia, and developmental aphasia . (c) "SLD" does not include students |
| 64 | `sli` — COMAR 13A.05.01.03B(74) | Speech or language impairment | confirmed |  |  | environmental, cultural, or economic disadvantage. (74) " Speech or language impairment " means a communication |
| 65 | `slp` — COMAR 13A.05.01.03B(75) | (existing strings of `slp`) | confirmed (checked by hand) |  | "Speech-language pathology" means services | other settings. (b) "Special education" includes speech-language pathology services , travel training, career and technology |
| 66 | `dd` — COMAR 13A.05.01.03B(77) | student with a developmental delay | confirmed |  |  | consistent with 20 U.S.C. §1412(a)(16). (77) " Student with a developmental delay " means a |
| 67 | `cwd` — COMAR 13A.05.01.03B(78) | student with a disability | confirmed |  |  | as defined in COMAR 13A.13.01.03B(12)(c). (78) " Student with a disability " means a student, |
| 68 | `saas` — COMAR 13A.05.01.03B(79) | Supplementary aids and services, supplementary aids | confirmed |  |  | special education and related services. (79) " Supplementary aids and services " means aids and |
| 69 | `transition` — COMAR 13A.05.01.03B(80) | Transition services, coordinated set of activities | confirmed |  |  | Regulation .10 of this chapter. (80) Transition Services . (a) "Transition services" means a coordinated |
| 70 | `transport` — COMAR 13A.05.01.03B(81) | Transportation, special transportation | confirmed |  |  | Functional vocational evaluation, if appropriate. (81) " Transportation " means services which include: (a) Travel |
| 71 | `tbi` — COMAR 13A.05.01.03B(82) | Traumatic brain injury | confirmed |  |  | a student with a disability. (82) Traumatic Brain Injury . (a) "Traumatic brain injury" means |
| 72 | `travel_training` — COMAR 13A.05.01.03B(83) | Travel training | confirmed |  |  | (ii) Induced by birth trauma. (83) " Travel training " means providing instruction to students |
| 73 | `vi` — COMAR 13A.05.01.03B(84) | visual impairment | confirmed |  |  | to place within that environment. (84) Visual Impairment . (a) "Visual impairment" means impairment in |
| 74 | `ward` — COMAR 13A.05.01.03B(85) | Ward of the State | confirmed |  |  | includes partial sight and blindness. (85) Ward of the State . (a) "Ward of the |
| 75 | `referral` — COMAR 13A.05.01.04A | Referral | confirmed |  |  | 04 === https://regs.maryland.gov/us/md/exec/comar/13A.05.01.04 .04 Referral. A. Referral to a Public Agency. (1) A |
| 76 | `std_diploma` — COMAR 13A.05.01.06E(10) | regular high school diploma | confirmed |  |  | Graduation from secondary school with a regular high school diploma ; or (ii) Exceeding the |
| 77 | `state_panel` — COMAR 13A.05.01.15C(23) | State advisory committee | confirmed |  |  | the findings and decisions to the State Advisory Committee as described in COMAR 13A.05.02.05; and |
| 78 | `ppps` — COMAR 13A.05.01.16 | (existing strings of `ppps`) | confirmed (checked by hand) |  | "parentally placed nonpublic school students with disabilities" |  |
| 79 | `safeguards_notice` — MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 1 | Maryland Procedural Safeguards Notice | confirmed |  |  | Parental Rights: Maryland Procedural Safeguards Notice Infants and Toddlers Early Intervention Preschool |
| 80 | `oah` — MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 17 | Office of Administrative Hearings, OAH | confirmed |  |  | Administrative Law Judge (ALJ) with the Office of Administrative Hearings (OAH) requests an independent educational |
| 81 | `cert_completion` — MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 7 | Certificate of Program Completion | confirmed |  |  | a high school diploma or a certificate of program completion . Graduation requirements must be |
| 82 | `plaafp` — MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 8 | Present levels of academic achievement and functional performance, PLAAFP, present levels, PLAAFPs | confirmed |  |  | Services: The Individualized Education Program 7 Present Levels of Academic Achievement and Functional Performance (PLAAFP): |
| 83 | `acc_feat` — MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 10 | Accessibility features | confirmed |  |  | Education Program 9 Instructional and Assessment Accessibility Features This section of the IEP has |
| 84 | `esy` — MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 12 | Extended school year services, extended school year, ESY, ESY services | confirmed |  |  | on their current skills. Eligibility for Extended School Year services is a data driven decision |
| 85 | `md_msde` (new concept) — MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 36 | Maryland State Department of Education, MSDE | confirmed |  |  | file a State Complaint with the Maryland State Department of Education (MSDE). In order for |
| 86 | `md_deises` (new concept) — MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 36 | Division of Early Intervention and Special Education Services | confirmed |  |  | address to the Assistant State Superintendent, Division of Early Intervention and Special Education Services , |
| 87 | `md_mitp` (new concept) — MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 19 | Maryland Infants and Toddlers Program | confirmed |  |  | Services is lead agency for the Maryland Infants and Toddlers Program , the statewide program |
| 88 | `md_extended_ifsp` (new concept) — MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 15 | Extended IFSP | confirmed |  |  | child three or older through an Extended IFSP , an educational component must be included. |
| 89 | `md_fss_coord` (new concept) — MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 16 | Local Family Support Services Coordinator | confirmed |  |  | below, your student's case manager or Local Family Support Services Coordinator can help! ❍ After |
| 90 | `md_seed` (new concept) — COMAR 13A.05.01.02A | SEED School | confirmed |  |  | of Education, local school systems, the SEED School , the Maryland Department of Health, the |
| 91 | `md_msb` (new concept) — COMAR 13A.05.01.02A | Maryland School for the Blind | confirmed |  |  | the Department of Juvenile Services, the Maryland School for the Blind , the Maryland School |
| 92 | `md_msd` (new concept) — COMAR 13A.05.01.02A | Maryland School for the Deaf | confirmed |  |  | Maryland School for the Blind, the Maryland School for the Deaf , and the Maryland |
| 93 | `md_mdh` (new concept) — COMAR 13A.05.01.02A | Maryland Department of Health | confirmed |  |  | school systems, the SEED School, the Maryland Department of Health , the Department of Juvenile |
| 94 | `md_djs` (new concept) — COMAR 13A.05.01.02A | Department of Juvenile Services | confirmed |  |  | the Maryland Department of Health, the Department of Juvenile Services , the Maryland School for |
| 95 | `md_labor` (new concept) — COMAR 13A.05.01.02A | Maryland Department of Labor | confirmed |  |  | School for the Deaf, and the Maryland Department of Labor . B. Early intervention services |
| 96 | `md_mam` (new concept) — COMAR 13A.05.01.03B(1) | Maryland Accommodations Manual | confirmed |  |  | and procedures, in accordance with the Maryland Accommodations Manual , that provide students with disabilities |
| 97 | `md_moiep` (new concept) — MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. 6 | Maryland Online IEP, MOIEP | confirmed |  |  | The Individualized Education Program (IEP) The Maryland online IEP (MOIEP) is a constantly evolving tool |
| 98 | `md_lcp` (new concept) — COMAR 13A.05.01.03B(37-1) | Learning Continuity Plan | confirmed |  |  | for students who are deaf-blind. (37-1) " Learning Continuity Plan " means the sections of |
| 99 | `md_emergency` (new concept) — COMAR 13A.05.01.03B(22-1) | Emergency conditions | confirmed |  |  | schools; and (ii) Preschool programs. (22-1) Emergency Conditions . (a) "Emergency Conditions" means a period |
| 100 | `md_hs_diploma` (new concept) — MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. 14 | Maryland High School Diploma | confirmed |  |  | issue or provide credits towards a Maryland High School Diploma ; • Identify the child |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Nonpublic school | COMAR 13A.05.01.03B(47) (23 uses) | Attest existing `nps` (now California only) |
| Certified Orientation and Mobility Specialist (COMS) | COMAR 13A.05.01.08 | Candidate concept; no orientation-and-mobility specialist concept exists yet |
| Statewide assessment | COMAR 13A.05.01.03B(76) | Defined term not in the dataset |
| Early identification | COMAR 13A.05.01.03B(20) | Defined term not in the dataset |
| Mediator | COMAR 13A.05.01.03B(40) | Low priority |

## 3. Summary

- **100 entries: 100 confirmed, 0 misplaced, 0 not found.** 5 needed a hand check.
- **Safety:** no single letters, and no person's name standing alone as a term. Place names are graded automatically. Notes on individual strings are in the table.
- **Typing:** every all-capitals string is typed as an acronym or abbreviation; state-only strings carry the state tag.
- **Build:** `build --check` passes and all 70 tests pass.

**Most important fixes**

1. The docstring says ".03B last amended effective Aug. 17, 2026", but the saved text in .sources-cache/md/ has no effective dates, so I couldn't verify it. Record where the date came from, or drop it.
2. Attest `nps` from COMAR .03B(47); "nonpublic school" appears 23 times.
3. Consider adding Certified Orientation and Mobility Specialist (COMS), COMAR .08.

**Docstring:** Accurate apart from the amendment date above. Page counts (51, 20) match, and PSN/IEPG dates (July 2024, 2023) match the documents.

**Update (2026-10-08):** **Fix 1 resolved:** the regs.maryland.gov chapter history confirms .03B was amended effective Aug. 17, 2026 (53:16 Md. R. 687), and the docstring now names that source. **Correction to this audit (fix 2 withdrawn):** Maryland's "nonpublic school" means any private school, not California's certified nonpublic, nonsectarian school, so `nps` was not attested. Fix 3 applied: `maryland_supplement` adds Certified Orientation and Mobility Specialist (COMAR .08A(6)(d)) and statewide assessment (.03B(76)), and "early identification" is added to `early_id` (.03B(20)). Released in 0.38.0.
