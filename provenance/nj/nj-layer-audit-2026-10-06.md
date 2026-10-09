# Audit: New Jersey layer (`sources/states/new_jersey.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-06 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section or page of text extracted from the PDFs in this folder. Entries without a literal hit were checked by hand. Web pages were read through a fetch that returns quotes from the page, not the page itself.

Documents: N.J.A.C. 6A:14 (NJDOE current code), Parental Rights in Special Education (PTM 1506.13, rev. June 2026), NJDOE Parental Rights and Engagement web page.

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `hi` — N.J.A.C. 6A:14-3.5(c)1 | auditory impairment, auditorily handicapped | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it. "auditorily handicapped" correctly typed L | specified below. 1. “ Auditory impairment” corresponds to "auditorily handicapped" and further corresponds to the |
| 2 | `deafness` — N.J.A.C. 6A:14-3.5(c)1 | Deafness, deaf, deafness including hard of hearing | confirmed |  |  | Federal eligibility categories of deafness or hearing impairment. “Auditory impairment” means an inability to hear |
| 3 | `autism` — N.J.A.C. 6A:14-3.5(c)2 | Autism, autism spectrum disorder, ASD, autism spectrum disorders | confirmed |  |  | educational performance. 2. “ Autism” means a pervasive developmental disability that significantly impacts verbal and |
| 4 | `id` — N.J.A.C. 6A:14-3.5(c)3 | Intellectual disability, mild intellectual disability, moderate intellectual disability, s | confirmed |  |  | are required. 3. “ Intellectual disability” means a disability that is characterized by significantly below |
| 5 | `sli` — N.J.A.C. 6A:14-3.5(c)4 | communication impairment | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | and needs. 4. “ Communication impairment” means a language disorder in the areas of morphology, |
| 6 | `ed` — N.J.A.C. 6A:14-3.5(c)5 | emotional regulation impairment | confirmed |  |  | is due to an emotional regulation impairment as defined in (c)5 below. A child who |
| 7 | `md` — N.J.A.C. 6A:14-3.5(c)6 | Multiple disabilities, MD, multiple impairments, multiple impairment, severely multiply im | confirmed |  |  | school problems. 6. “ Multiple disabilities” means the presence of two or more disabling conditions, |
| 8 | `deafblind` — N.J.A.C. 6A:14-3.5(c)7 | deaf/blindness | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | include deaf-blindness. 7. " Deaf/blindness" means concomitant hearing and visual impairments, the combination of which |
| 9 | `oi` — N.J.A.C. 6A:14-3.5(c)8 | Orthopedic impairment, physical impairment, OI, physically impaired | confirmed |  |  | disability-blindness and intellectual disability- orthopedic impairment. The existence of two disabling conditions alone shall not |
| 10 | `ohi` — N.J.A.C. 6A:14-3.5(c)9 | Other health impairment, health impairment, other health-impairment, OHI, health impairmen | confirmed |  |  | is required. 9. " Other health impairment" means a disability characterized by having limited strength, |
| 11 | `adhd` — N.J.A.C. 6A:14-3.5(c)9 | Attention deficit hyperactivity disorder, ADHD, attention deficit disorder, ADD, OHI/ADD/A | confirmed |  |  | health problems, such as attention deficit hyperactivity disorder, a heart condition, tuberculosis, rheumatic fever, nephritis, |
| 12 | `tourette` — N.J.A.C. 6A:14-3.5(c)9 | Tourette syndrome, Tourette's syndrome, Tourette's | confirmed |  |  | medical condition, such as Tourette Syndrome, that adversely affects a student's educational performance. A medical |
| 13 | `epilepsy` — N.J.A.C. 6A:14-3.5(c)9 | Epilepsy, seizure disorder | confirmed |  |  | sickle cell anemia, hemophilia, epilepsy, lead poisoning, leukemia, diabetes, or any other medical condition, such |
| 14 | `sickle` — N.J.A.C. 6A:14-3.5(c)9 | Sickle cell anemia | confirmed |  |  | rheumatic fever, nephritis, asthma, sickle cell anemia, hemophilia, epilepsy, lead poisoning, leukemia, diabetes, or any |
| 15 | `preschool_swd` — N.J.A.C. 6A:14-3.5(c)10 | preschool child with a disability | confirmed |  |  | required. 72 10. " Preschool child with a disability" means a child between the ages |
| 16 | `dd` — N.J.A.C. 6A:14-3.5(c)10 | Developmental delay, DD, developmental delays, developmentally delayed, young child with a | confirmed |  |  | either: i. Is experiencing developmental delay, as measured by appropriate diagnostic instruments and procedures, in |
| 17 | `sld` — N.J.A.C. 6A:14-3.5(c)12 | Specific learning disability, learning disability, SLD, LD, specific learning disabilities | confirmed |  |  | (c)5 above. 12. " Specific learning disability" means a disorder in one or more of |
| 18 | `perceptual` — N.J.A.C. 6A:14-3.5(c)12 | Perceptual disabilities, perceptual disability | confirmed |  |  | including conditions, such as perceptual disabilities, brain injury, minimal brain dysfunction, dyslexia, and developmental aphasia. |
| 19 | `mbd` — N.J.A.C. 6A:14-3.5(c)12 | Minimal brain dysfunction | confirmed |  |  | perceptual disabilities, brain injury, minimal brain dysfunction, dyslexia, and developmental aphasia. i. A specific learning |
| 20 | `aphasia` — N.J.A.C. 6A:14-3.5(c)12 | Developmental aphasia | confirmed |  |  | brain dysfunction, dyslexia, and developmental aphasia. i. A specific learning disability can be determined when |
| 21 | `discrepancy` — N.J.A.C. 6A:14-3.5(c)12 | Severe discrepancy, ability-achievement discrepancy, IQ-achievement discrepancy, discrepan | confirmed |  |  | be determined when a severe discrepancy is found between the student's current achievement and intellectual |
| 22 | `basic_reading` — N.J.A.C. 6A:14-3.5(c)12 | basic reading skills, Basic reading skill | confirmed |  |  | following areas: ii. (1) Basic reading skills; (2) Reading comprehension; (3) Oral expression; (4) Listening |
| 23 | `reading_comp` — N.J.A.C. 6A:14-3.5(c)12 | Reading comprehension | confirmed |  |  | Basic reading skills; (2) Reading comprehension; (3) Oral expression; (4) Listening comprehension; (5) Mathematical calculation; |
| 24 | `oral_expr` — N.J.A.C. 6A:14-3.5(c)12 | Oral expression | confirmed |  |  | (2) Reading comprehension; (3) Oral expression; (4) Listening comprehension; (5) Mathematical calculation; (6) Mathematical problem |
| 25 | `listen_comp` — N.J.A.C. 6A:14-3.5(c)12 | Listening comprehension | confirmed |  |  | (3) Oral expression; (4) Listening comprehension; (5) Mathematical calculation; (6) Mathematical problem solving; (7) Written |
| 26 | `written_expr` — N.J.A.C. 6A:14-3.5(c)12 | Written expression | confirmed |  |  | Mathematical problem solving; (7) Written expression; and (8) Reading fluency. A specific learning disability may |
| 27 | `fluency` — N.J.A.C. 6A:14-3.5(c)12 | reading fluency, Reading fluency skills, oral reading fluency, ORF | confirmed |  |  | Written expression; and (8) Reading fluency. A specific learning disability may also be determined by |
| 28 | `tbi` — N.J.A.C. 6A:14-3.5(c)13 | Traumatic brain injury, TBI | confirmed |  |  | intellectual ability. 13. " Traumatic brain injury" means an acquired injury to the brain caused |
| 29 | `vi` — N.J.A.C. 6A:14-3.5(c)14 | visual impairment, visually impaired, Visual impairment including blindness, VI, visual im | confirmed |  |  | means concomitant hearing and visual impairments, the combination of which causes such severe communication and |
| 30 | `exclusionary` — N.J.A.C. 6A:14-3.5(b) | environmental, cultural, or economic disadvantage, determinant factor, Exclusionary factor | confirmed |  |  | emotional regulation impairment, or environmental, cultural, or economic disadvantage. iv. If the district board of |
| 31 | `lep` — N.J.A.C. 6A:14-3.5(b) | multilingual learner | confirmed |  |  | the student is a multilingual learner (ML). (c) A student shall be determined eligible and |
| 32 | `eligibility` — N.J.A.C. 6A:14-3.5(a) | determination of eligibility, Eligibility determination, eligibility meeting, eligibility  | confirmed |  |  | 6A:14-3.5 Determination of eligibility for special education and related services 6A:14-3.5 Determination of eligibility for |
| 33 | `eval_report` — N.J.A.C. 6A:14-3.5(a) | Evaluation report, full and individual evaluation report, ER, eligibility report, evaluati | confirmed |  |  | A copy of the evaluation report(s) and documentation and information that will be used for |
| 34 | `adaptive` — N.J.A.C. 6A:14-1.3 | Adaptive behavior, adaptive functioning, adaptive skills, adaptive behavior deficits | confirmed |  |  | reference herein. 8 " Adaptive behavior" means the ability to demonstrate personal independence and social |
| 35 | `age_majority` — N.J.A.C. 6A:14-1.3 | adult student, Transfer of rights at age of majority, age of majority, transfer of parenta | confirmed |  |  | socio-cultural group expectations. " Adult student" means a person who has attained age 18, who |
| 36 | `alt_assess` — N.J.A.C. 6A:14-1.3 | Alternate assessment, alternate academic achievement standards, AA-AAAS | confirmed |  |  | law or regulation. “ Alternate assessment” means the same as “alternative assessment for students with |
| 37 | `approved_priv` — N.J.A.C. 6A:14-1.3 | approved private school for students with disabilities | confirmed |  |  | at N.J.A.C. 6A:8-1.3. " Approved private school for students with disabilities" means an incorporated entity |
| 38 | `at_device` — N.J.A.C. 6A:14-1.3 | Assistive technology device, assistive technology, AT | confirmed |  |  | providing their education. " Assistive technology device" is defined in accordance with the definition of |
| 39 | `at_service` — N.J.A.C. 6A:14-1.3 | Assistive technology service, assistive technology services | confirmed |  |  | 6A:14 Appendix F. " Assistive technology service" is defined in accordance with the definition of |
| 40 | `consent` — N.J.A.C. 6A:14-1.3 | Parental consent, informed consent, informed parental consent, consent to evaluate | confirmed (checked by hand) |  |  | "Consent" means agreement in writing that is required by this chapter. |
| 41 | `dyslexia` — N.J.A.C. 6A:14-1.3 | Dyslexia, Specific Learning Disability/Dyslexia | confirmed |  |  | students with disabilities. “ Dyslexia” means a specific learning disability that is neurobiological in origin. |
| 42 | `esy` — N.J.A.C. 6A:14-1.3 | Extended school year services, extended school year, ESY, ESY services, twelve-month speci | confirmed |  |  | Children and Families. " Extended school year services" means special education and related services that |
| 43 | `iep` — N.J.A.C. 6A:14-1.3 | Individualized education program, IEP, IEPs, individualized education plan, individual edu | confirmed |  |  | to the parent. " Individualized education program" (IEP) means a written plan that sets forth |
| 44 | `iep_team` — N.J.A.C. 6A:14-1.3 | IEP Team, individualized education program team, IEP committee, ARD committee, Admission,  | confirmed |  |  | in this chapter. " IEP team" means the group of individuals who are responsible for |
| 45 | `native_language` — N.J.A.C. 6A:14-1.3 | Native language | confirmed |  |  | in his or her native language or other mode of communication; 9 2. Understands and |
| 46 | `ward` — N.J.A.C. 6A:14-1.3 | Ward of the State, adjudicated dependent or ward of the court | confirmed |  |  | to N.J.A.C. 6A:32-2.1. “ Ward of the State” means a student who, pursuant to an |
| 47 | `foster` — N.J.A.C. 6A:14-1.3 | resource family parent | confirmed |  |  | parent, the legal guardian, resource family parent when willing to so serve, a surrogate parent |
| 48 | `transition` — N.J.A.C. 6A:14-1.3 | Transition services, transition plan, coordinated set of activities, coordinated activitie | confirmed |  |  | 6A:14-3.5 or 3.6. “ Transition services” for students age 16 or older is defined in |
| 49 | `saas` — N.J.A.C. 6A:14-4.3(a) | Supplementary aids and services, supplementary aids, supplemental aids and services | confirmed |  |  | general education class with supplementary aids and services including, but not limited to, the following: |
| 50 | `consult` — N.J.A.C. 6A:14-4.3(a) | consultation services, Collaborative or consulting services, consultative services, direct | confirmed |  |  | 5. Integrated therapies; 6. Consultation services; and 98 7. (b) In-class resource programs. If it |
| 51 | `para` — N.J.A.C. 6A:14-4.3(a) | teacher aide | confirmed (checked by hand) |  |  | 3. Teacher aides; 4. Related services; 5. Integrated therapies |
| 52 | `continuum` — N.J.A.C. 6A:14-4.3(b) | Continuum of alternative placements, continuum of placements, continuum of placement optio | confirmed |  |  | school day, a full continuum of alternative placements as set forth in this subsection shall |
| 53 | `regression` — N.J.A.C. 6A:14-4.3(c) | recoupment, Severe or substantial regression, substantial regression | confirmed |  |  | level of functioning and recoupment cannot be expected in a reasonable length of time. The |
| 54 | `resource_room` — N.J.A.C. 6A:14-4.6(e) | resource program, Resource room, regular class and special education class combination, re | confirmed |  |  | criteria: supplementary instruction and resource programs 6A:14-4.6 Program criteria: supplementary instruction and resource programs (a) |
| 55 | `special_class` — N.J.A.C. 6A:14-4.7(a) | special class program | confirmed |  |  | 6A:14-4.7 Program criteria: special class programs, secondary programs, and vocational rehabilitation 6A:14-4.7 Program criteria: special |
| 56 | `dedicated_aide` — N.J.A.C. 6A:14-4.7(e) | personal aide | confirmed |  |  | required, students with a personal aide shall not be included in the student count: I |
| 57 | `home_instr` — N.J.A.C. 6A:14-4.8(a) | Home instruction, homebound instruction, instruction in the home or hospital, home or hosp | confirmed |  |  | 6A:14-4.8 Program criteria: home instruction 6A:14-4.8 Program criteria: home instruction (a) A student with a |
| 58 | `std_diploma` — N.J.A.C. 6A:14-4.11(a) | State-endorsed diploma | confirmed |  |  | (b) Graduation with a State-endorsed diploma is a change of placement that requires written notice |
| 59 | `sop` — N.J.A.C. 6A:14-4.11(b) | Summary of academic achievement and functional performance, summary of performance, SOP | confirmed (checked by hand) |  | Code wording differs ("summary of his or her ..."); concept match OK | provided a written summary of his or her academic achievement and functional performance |
| 60 | `safeguards_notice` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 3 | Parental Rights in Special Education | confirmed |  |  | Jersey Department of Education Parental Rights in Special Education New Jersey Administrative code for special |
| 61 | `safeguards_notice` — NJDOE Parental Rights and Engagement page | PRISE | confirmed (web page) |  |  | (PAGE) The PRISE booklet is available in multiple languages |
| 62 | `dp_hearing` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 22 | Impartial due process hearing, due process hearing, administrative law judge, ALJ, hearing | confirmed |  |  | may ask for an impartial due process hearing if there is a disagreement over the |
| 63 | `fba` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 42 | Functional behavioral assessment, FBA, functional behavior assessment, assessment of funct | confirmed |  |  | according to an IEP. Functional Behavioral Assessment The process of coming to an understanding of |
| 64 | `lre` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 42 | Least restrictive environment, LRE, peers without disabilities | confirmed |  |  | education services are needed. Least Restrictive Environment (LRE) To the maximum extent appropriate, children with |
| 65 | `stay_put` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 42 | stay-put, stay put, Child's status during proceedings, pendency, current educational place | confirmed |  |  | are not afforded a stay put if mediation or a due process hearing has been |
| 66 | `pti` — NJDOE Parental Rights and Engagement page | Parent training and information center, PTI, parent center, PTIC, PTIs | confirmed (web page) |  |  | (PAGE) New Jersey's federally designated Parent Training and Information Center (PTI) |
| 67 | `nj_doe` — N.J.A.C. 6A:14-1.3 | New Jersey Department of Education | confirmed |  |  | of Education" means the New Jersey Department of Education. "District board of education" means, except |
| 68 | `nj_osepdr` — N.J.A.C. 6A:14-1.3 | Office of Special Education Policy and Dispute Resolution | confirmed |  |  | resides. “Office” means the Office of Special Education Policy and Dispute Resolution in the Department |
| 69 | `nj_county_office` — N.J.A.C. 6A:14-4.9(a) | County office of education | confirmed |  |  | of Education through the county office of education (county office); and 3. (b) For a |
| 70 | `nj_dboe` — N.J.A.C. 6A:14-1.3 | District board of education | confirmed |  |  | disabilities placed by the district board of education responsible for providing their education. "Assistive technology |
| 71 | `nj_csssd` — N.J.A.C. 6A:14-4.3(b)5 | County special services school district | confirmed |  |  | following settings: i. A county special services school district; ii. An educational services commission; iii. |
| 72 | `nj_esc` — N.J.A.C. 6A:14-4.3(b)5 | Educational services commission | confirmed |  |  | school district; ii. An educational services commission; iii. A jointure commission; and iv. A New |
| 73 | `nj_jointure` — N.J.A.C. 6A:14-4.3(b)5 | Jointure commission | confirmed |  |  | services commission; iii. A jointure commission; and iv. A New Jersey approved private school for |
| 74 | `nj_cbvi` — N.J.A.C. 6A:14-3.5(c)14 | New Jersey Commission for the Blind and Visually Impaired | confirmed |  |  | be reported to the New Jersey Commission for the Blind and Visually Impaired. |
| 75 | `nj_oal` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 22 | Office of Administrative Law, OAL | confirmed |  |  | judge (ALJ) from the Office of Administrative Law (OAL). Who may ask for a due |
| 76 | `nj_span` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 3 | Statewide Parent Advocacy Network, SPAN | confirmed |  |  | contact information for the Statewide Parent Advocacy Network (SPAN), Disability Rights New Jersey (DRNJ), the |
| 77 | `nj_drnj` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 3 | Disability Rights New Jersey, DRNJ | confirmed |  |  | Parent Advocacy Network (SPAN), Disability Rights New Jersey (DRNJ), the County Offices of the New |
| 78 | `nj_dvrs` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 44 | Division of Vocational Rehabilitation Services, DVRS | confirmed |  |  | Division of Vocational Rehabilitation Services (DVRS) in the New Jersey Department of Labor and Workforce |
| 79 | `nj_ddd` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 44 | Division of Developmental Disabilities, DDD | confirmed |  |  | 292-8347 TTY: (609) 292-2919 Division of Developmental Disabilities in the New Jersey Department of Human |
| 80 | `nj_csoc` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 45 | Children's System of Care, CSOC | confirmed |  |  | of Children and Families: Children's System of Care DCF's Children's System of Care, (CSOC), (formerly |
| 81 | `nj_ddhh` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 46 | Division of the Deaf and Hard of Hearing, DDHH | confirmed |  |  | Division of the Deaf and Hard of Hearing in the New Jersey Department of Human |
| 82 | `nj_dds` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 46 | Division of Disability Services, DDS | confirmed |  | DDS now names three concepts (DC, NJ, CT); all regional-tagged. Reviewer decision | 588-2648 FAX: (609)-588-2528 Website Division of Disability Services in the New Jersey Department of Human |
| 83 | `nj_sepag` — NJDOE Parental Rights and Engagement page | Special Education Parent Advisory Group, SEPAG | confirmed (web page) |  |  | (PAGE) a special education parent advisory group is in place in the district |
| 84 | `nj_ldtc` — N.J.A.C. 6A:14-3.1(b) | Learning disabilities teacher-consultant | confirmed |  |  | a school psychologist, a learning disabilities teacherconsultant, and a school social worker. All child study |
| 85 | `nj_sls` — N.J.A.C. 6A:14-1.3 | Speech-language specialist | confirmed |  | Created here as NJ-only, but the New Hampshire layer also attests it (see NH report) | Appendix C. 12 " Speech-language specialist" means speech-language specialist or speech-language specialist-equivalent. "Statewide assessment" means |
| 86 | `referral` — N.J.A.C. 6A:14-1.3 | Referral | confirmed |  |  | an adult student. " Referral" means the written request for an initial evaluation to determine |
| 87 | `nj_social_maladj` — N.J.A.C. 6A:14-3.5(c)11 | Social maladjustment | confirmed |  |  | related services. 11. " Social maladjustment" means a consistent inability to conform to the standards |
| 88 | `nj_eligible_sls` — N.J.A.C. 6A:14-3.6(a) | Eligible for speech-language services | confirmed |  |  | speech-language services (a) " Eligible for speech-language services" means a speech and/or language disorder as |
| 89 | `nj_icr` — N.J.A.C. 6A:14-4.6(i) | In-class resource program | confirmed |  |  | instruction is given. (d) In-class resource programs and pull-out replacement resource programs are programs of |
| 90 | `nj_pullout` — N.J.A.C. 6A:14-4.6(d) | Pull-out replacement resource program | confirmed |  |  | In-class resource programs and pull-out replacement resource programs are programs of specialized instruction organized around |
| 91 | `nj_supp_instr` — N.J.A.C. 6A:14-4.6(a) | Supplementary instruction | confirmed |  |  | 6A:14-4.6 Program criteria: supplementary instruction and resource programs 6A:14-4.6 Program criteria: supplementary instruction and resource |
| 92 | `nj_njsls` — N.J.A.C. 6A:14-4.7(a) | New Jersey Student Learning Standards | confirmed |  |  | offer instruction in the New Jersey Student Learning Standards 105 unless the IEP specifies a |
| 93 | `nj_emergent` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 25 | Emergent relief | confirmed |  |  | is available. APPLICATION FOR EMERGENT RELIEF What is emergent relief? Emergent relief is a request |
| 94 | `cbi` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 43 | Community-Based Instruction, CBI | confirmed |  | Created as a general (non-NJ) concept from a NJ source; fine, but only NJ attests it so far | school districts on the Community-Based Instruction, and Person-Centered Approaches through Boggs Center on Developmental Disabilities |
| 95 | `nj_sle` — NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 43 | Structured learning experience, SLE | confirmed |  |  | on Person Centered Approaches. Structured Learning Experience (SLE) Structured learning experience means experiential, supervised in-depth |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Receiving school | N.J.A.C. 6A:14-7 (22 uses) | New concept for out-of-district placements |
| In-class resource | N.J.A.C. 6A:14-4.6 (10 uses) | Short form on `nj_icr` |
| Out-of-district placement | CODE (2 uses) | New concept or synonym |
| Summary of his or her academic achievement and functional performance | N.J.A.C. 6A:14-4.11(b) | Wording variant on `sop` |

## 3. Summary

- **95 entries: 95 confirmed, 0 misplaced, 0 not found.** Of the confirmed entries, 3 needed a hand check because the wording differs, and 3 rest on a web page.
- **Safety:** no single letters, no eponyms, and no person's name standing alone as a term. Place names are graded automatically.
- **Build:** `build --check` passes and all 53 tests pass with this layer in place.

**Most important fixes**

1. DDS now names three different agencies (DC, NJ, CT). The build allows it because each is regional-tagged; a reviewer should accept it on purpose.
2. `nj_sls` was created as NJ-only, but New Hampshire also uses the term (see the NH audit). Decide whether it should be a general concept.

**Docstring:** Accurate. The 3.5(c) category numbering matches the code exactly. "Marie H. Katzenbach School for the Deaf" (a person's name) and the Boggs Center are correctly left out.

**Correction (2026-10-06):** an earlier version of this report called some strings redundant because they already existed. They aren't: each adds this state's regional tag, without which a matcher filtered to the state drops the string. Keep them.

**Update (2026-10-07):** Fix 2 applied: `nj_sls` is now a general concept, because New Hampshire uses the title too. Fix 1 is left for a reviewer.
