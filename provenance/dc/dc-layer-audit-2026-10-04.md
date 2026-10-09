# Audit: District of Columbia layer (`sources/states/district_of_columbia.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-04 · Auditor: claude-opus-5-5, in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met.

Documents checked: 5-A DCMR Ch. 30 (OSSE compilation, 7/1/2022), PSN (rev. Aug. 2018), HB (SY2026-27), BRO (2026), all from `.sources-cache/dc/`. The ALT web page could not be downloaded here; it was read through a web fetch that returns a summary with quotes, so the six ALT-cited entries rest on that summary (four of them also appear verbatim on HB p. 17).

Method: each entry's strings were searched in the cited section or printed page of the extracted text. The 21 entries without a literal hit were checked by hand. All cited sections exist, the HB page offset (PDF page − 2) and PSN/BRO page numbering are correct.

## 1. Entries

| # | entry key | term | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `autism` (RULE 3011.1) | Autism | confirmed |  |  | on the basis of autism, the following shall apply: (a) Autism shall mean a developmental |
| 2 | `deafblind` (RULE 3011.2) | Deaf-blindness | confirmed |  |  | on the basis of deaf-blindness, the following shall apply: (a) Deaf-blindness shall mean concomitant hearing |
| 3 | `deafness` (RULE 3011.3) | Deafness | confirmed |  |  | on the basis of deafness, the following shall apply: (a) Deafness shall mean a hearing |
| 4 | `dd` (RULE 3011.4) | Developmental delay, developmental delays | confirmed |  |  | on the basis of developmental delay, the following shall apply: (a) Developmental delay shall mean |
| 5 | `ed` (RULE 3011.5) | emotional disability | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | on the basis of emotional disability, the following shall apply: (a) Emotional disability shall mean |
| 6 | `hi` (RULE 3011.6) | Hearing impairment | confirmed |  |  | on the basis of hearing impairment, the following shall apply: (a) Hearing impairment shall mean |
| 7 | `id` (RULE 3011.7) | Intellectual disability | confirmed |  |  | on the basis of intellectual disability, the following shall apply: (a) Intellectual disability shall mean |
| 8 | `md` (RULE 3011.8) | Multiple disabilities | confirmed |  |  | on the basis of multiple disabilities, the following shall apply: (a) Multiple disabilities shall mean |
| 9 | `oi` (RULE 3011.9) | Orthopedic impairment | confirmed |  |  | on the basis of orthopedic impairment, the following shall apply: (a) Orthopedic impairment shall mean |
| 10 | `ohi` (RULE 3011.10) | Other health impairment, health impairment | confirmed |  |  | on the basis of other health impairment, the following shall apply: (a) Other health impairment |
| 11 | `adhd` (RULE 3011.10) | Attention deficit hyperactivity disorder, attention deficit disorder | confirmed |  |  | attention deficit disorder or attention deficit hyperactivity disorder, diabetes, epilepsy, a heart condition, hemophilia, lead |
| 12 | `epilepsy` (RULE 3011.10) | Epilepsy | confirmed |  |  | deficit hyperactivity disorder, diabetes, epilepsy, a heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, |
| 13 | `sickle` (RULE 3011.10) | Sickle cell anemia | confirmed |  |  | leukemia, nephritis, rheumatic fever, sickle cell anemia, or Tourette syndrome; 7/1/2022 TITLE 5-A DCMR CHAPTER |
| 14 | `tourette` (RULE 3011.10) | Tourette syndrome | confirmed |  |  | sickle cell anemia, or Tourette syndrome; 7/1/2022 TITLE 5-A DCMR CHAPTER 30: SPECIAL EDUCATION (c) |
| 15 | `sld` (RULE 3011.11) | Specific learning disability, learning disability | confirmed |  |  | on the basis of specific learning disability, the following shall apply: (a) Specific learning disability |
| 16 | `dyslexia` (RULE 3011.11) | Dyslexia | confirmed |  |  | injury, minimal brain dysfunction, dyslexia, and developmental aphasia. Specific learning disability shall not include learning |
| 17 | `perceptual` (RULE 3011.11) | Perceptual disabilities | confirmed |  |  | including conditions such as perceptual disabilities, brain injury, minimal brain dysfunction, dyslexia, and developmental aphasia. |
| 18 | `mbd` (RULE 3011.11) | Minimal brain dysfunction | confirmed |  |  | perceptual disabilities, brain injury, minimal brain dysfunction, dyslexia, and developmental aphasia. Specific learning disability shall |
| 19 | `aphasia` (RULE 3011.11) | Developmental aphasia | confirmed |  |  | brain dysfunction, dyslexia, and developmental aphasia. Specific learning disability shall not include learning problems that |
| 20 | `oral_expr` (RULE 3011.11) | Oral expression | confirmed |  |  | the following areas: (1) Oral expression; (2) Listening comprehension; (3) Written expression; (4) Basic reading |
| 21 | `listen_comp` (RULE 3011.11) | Listening comprehension | confirmed |  |  | (1) Oral expression; (2) Listening comprehension; (3) Written expression; (4) Basic reading skills; (5) Reading |
| 22 | `written_expr` (RULE 3011.11) | Written expression | confirmed |  |  | (2) Listening comprehension; (3) Written expression; (4) Basic reading skills; (5) Reading fluency skills; (6) |
| 23 | `basic_reading` (RULE 3011.11) | basic reading skills | confirmed |  |  | (3) Written expression; (4) Basic reading skills; (5) Reading fluency skills; (6) Reading comprehension; 7/1/2022 |
| 24 | `fluency` (RULE 3011.11) | Reading fluency skills, reading fluency | confirmed |  |  | Basic reading skills; (5) Reading fluency skills; (6) Reading comprehension; 7/1/2022 TITLE 5-A DCMR CHAPTER |
| 25 | `reading_comp` (RULE 3011.11) | Reading comprehension | confirmed |  |  | Reading fluency skills; (6) Reading comprehension; 7/1/2022 TITLE 5-A DCMR CHAPTER 30: SPECIAL EDUCATION (7) |
| 26 | `math_calc` (RULE 3011.11) | Mathematics calculation | confirmed |  |  | 30: SPECIAL EDUCATION (7) Mathematics calculation; or (8) Mathematics problem solving; (c) The IEP Team |
| 27 | `math_ps` (RULE 3011.11) | Mathematics problem solving | confirmed |  |  | Mathematics calculation; or (8) Mathematics problem solving; (c) The IEP Team shall determine that its |
| 28 | `rti` (RULE 3011.11) | Response-to-Intervention model | confirmed |  | "Response-to-Intervention model" adds a word; synonym (S) fits better than spelling_variant (V) | research-based intervention, or a Response-to-Intervention model; or (C) Whether the child exhibits a pattern of |
| 29 | `srbi` (RULE 3011.11) | Scientific, research-based intervention, research-based intervention | confirmed |  |  | methods: (1) Eligibility using scientific, research-based interventions. In determining eligibility on the basis of specific |
| 30 | `psw` (RULE 3011.11) | Pattern of strengths and weaknesses | confirmed |  |  | the child exhibits a pattern of strengths and weaknesses in performance, achievement, or both, relative |
| 31 | `discrepancy` (RULE 3011.11) | discrepancy model | confirmed |  |  | (2) Eligibility using the discrepancy model. In determining eligibility on the basis of specific learning |
| 32 | `sli` (RULE 3011.12) | Speech or language impairment | confirmed |  |  | on the basis of speech or language impairment, the following shall apply: (a) Speech or |
| 33 | `artic` (RULE 3011.12) | articulation impairment | confirmed |  |  | the child displays an articulation impairment, including atypical production of speech sounds characterized by substitutions, |
| 34 | `lang_dis` (RULE 3011.12) | language impairment | confirmed |  |  | basis of speech or language impairment, the following shall apply: (a) Speech or language impairment |
| 35 | `tbi` (RULE 3011.13) | Traumatic brain injury | confirmed |  |  | on the basis of traumatic brain injury, the following shall apply: (a) Traumatic brain injury |
| 36 | `vi` (RULE 3011.14) | visual impairment | confirmed |  |  | on the basis of visual impairment, the following shall apply: (a) Visual impairment, including blindness, |
| 37 | `adaptive` (RULE 3011.7) | Adaptive behavior | confirmed |  |  | concurrently with deficits in adaptive behavior and manifested during the developmental period, that adversely affects |
| 38 | `cwd` (RULE 3099.1) | Child with a disability, children with disabilities | confirmed |  |  | functional capabilities of a child with a disability. The term does not include a medical |
| 39 | `eligibility` (RULE 3010) | Eligibility determination, determination of eligibility | confirmed |  |  | 3010 ELIGIBILITY DETERMINATION 3010.1 As part of the initial evaluation procedures described in Sections 3005 |
| 40 | `exclusionary` (RULE 3010.2) | determinant factor | confirmed |  |  | a disability if the determinant factor for that eligibility determination is: (a) Lack of appropriate |
| 41 | `s504` (RULE 3010.7) | Section 504, Section 504 of the Rehabilitation Act | confirmed |  |  | services or protections under Section 504 of the Rehabilitation Act of 1973, 29 U.S.C. § |
| 42 | `child_find` (RULE 3003) | Child find | confirmed |  |  | 3003 CHILD FIND 3003.1 Each LEA and public agency shall publish and implement child find |
| 43 | `screening` (RULE 3006.13) | Screening for instructional purposes, universal screening | confirmed |  |  | The screening of the child by a teacher, or school-based specialist to determine |
| 44 | `evaluation` (RULE 3005) | Evaluation, initial evaluation, individual evaluation | confirmed |  |  | 3005 INITIAL EVALUATION PROCESS 3005.1 The LEA shall ensure that a full and individual evaluation |
| 45 | `eval_report` (RULE 3006.11) | Evaluation report | confirmed |  |  | written evaluation (or re evaluation) report that includes: (1) Information provided by the parent(s); (2) |
| 46 | `observation` (RULE 3006.10) | observation | confirmed |  |  | Use information from an observation in routine classroom instruction in monitoring of the child's performance |
| 47 | `reeval` (RULE 3007.5) | triennial evaluation | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | reevaluation prior to the triennial evaluation pursuant to Section 3007.1, the LEA shall complete a |
| 48 | `medical` (RULE 3012.7) | Medical services | confirmed |  |  | 3012.7 Medical services as a related service includes services provided by a licensed physician to |
| 49 | `iee` (RULE 3038) | Independent educational evaluation | confirmed |  |  | 3038 INDEPENDENT EDUCATIONAL EVALUATIONS 3038.1 The LEA shall provide to the parent, upon request for |
| 50 | `iep` (RULE 3099.1) | Individualized education program, IEP | confirmed |  |  | employee of the LEA. Individualized education program or IEP – A written statement that specifies |
| 51 | `iep_team` (RULE 3008) | IEP Team, individualized education program team, Team meeting | confirmed |  |  | individualized education program ( IEP) Team for each child with a disability shall include the |
| 52 | `gen_teacher` (RULE 3008.1) | general education teacher | confirmed |  |  | At least one (1) general education teacher of the child, if the child is or |
| 53 | `sped_teacher` (RULE 3008.1) | Special education teacher, special education provider | confirmed |  |  | At least one (1) special education teacher, or if appropriate, at least one (1) special |
| 54 | `lea_rep` (RULE 3008.1) | Representative of the public agency, LEA representative, district representative | confirmed |  |  | A representative of the LEA who is qualified to provide, or supervise |
| 55 | `eval_interp` (RULE 3008.1) | Individual who can interpret the instructional implications of evaluation result | confirmed |  |  | the LEA; (e) An individual who can interpret the instructional implications of evaluation results, who: |
| 56 | `plaafp` (RULE 3017.8) | Present levels of academic achievement and functional performance, present level | confirmed |  |  | statement of the child's present levels of academic achievement and functional performance, including: (1) How |
| 57 | `annual_goals` (RULE 3017.8) | Measurable annual goals, annual goals | confirmed |  |  | (b) A statement of measurable annual goals, including academic and functional goals designed to meet |
| 58 | `progress` (RULE 3017.8) | Periodic reports on progress, progress reports, progress monitoring, method for  | confirmed |  |  | When periodic reports on the child's progress toward meeting the annual goals will be provided |
| 59 | `sto` (RULE 3017.8) | Benchmarks or short-term objectives, short-term objectives, benchmarks | confirmed |  |  | (c) A description of benchmarks or short-term objectives for children with disabilities who take alternate |
| 60 | `saas` (RULE 3017.8) | Supplementary aids and services, supplementary aids | confirmed |  |  | and related services and supplementary aids and services, including assistive technology, to be provided to |
| 61 | `program_mods` (RULE 3017.8) | program modifications, modifications | confirmed |  |  | a statement of the program modifications or supports for LEA personnel that will be provided |
| 62 | `removal_expl` (RULE 3017.8) | Explanation of the extent of nonparticipation, LRE justification, justification  | confirmed |  |  | An explanation of the extent, if any, to which the child will not participate |
| 63 | `test_accom` (RULE 3017.8) | accommodations | confirmed |  |  | of any individual appropriate accommodations necessary to measure the academic achievement and functional performance of |
| 64 | `alt_assess` (RULE 3017.8) | Alternate assessment | confirmed |  |  | with disabilities who take alternate assessments aligned to alternate achievement standards; (d) A statement of |
| 65 | `fld` (RULE 3017.8) | Frequency, location, and duration | confirmed |  |  | designated, and the anticipated frequency, location, and duration of those services and modifications. |
| 66 | `comm_mode` (RULE 3017.9) | Language and communication mode, communication needs, communication mode | confirmed |  |  | personnel in the child's language and communication mode, academic 7/1/2022 TITLE 5-A DCMR CHAPTER 30: |
| 67 | `pbis` (RULE 3017.10) | Positive behavioral interventions and supports, positive behavioral intervention | confirmed |  |  | (a) The use of positive behavioral interventions and supports and other strategies to address that |
| 68 | `fba` (RULE 3017.10) | Functional behavioral assessment | confirmed |  |  | Whether to conduct a functional behavioral assessment and develop a behavioral intervention plan for the |
| 69 | `bip` (RULE 3017.10) | Behavioral intervention plan | confirmed |  |  | assessment and develop a behavioral intervention plan for the child. |
| 70 | `braille` (RULE 3017.12) | Instruction in Braille, Braille, use of Braille | confirmed |  |  | the student's need for instruction in Braille or the use of Braille; (b) The IEP |
| 71 | `lep` (RULE 3099.1) | Limited English proficient, limited English proficiency, English learner | confirmed |  | Rule 3099.1 defines "English learner", not "limited English proficient"; mapping OK | English learner – A student as defined in Section |
| 72 | `annual_review` (RULE 3018.1) | annual IEP | confirmed |  |  | making progress toward the annual IEP goals. |
| 73 | `amendment` (RULE 3019) | IEP amendment | confirmed |  |  | parent to execute the IEP amendment. 7/1/2022 TITLE 5-A DCMR CHAPTER 30: SPECIAL EDUCATION 3019.4 |
| 74 | `comparable` (RULE 3020.5) | Comparable services | confirmed |  | "comparable services plan" is the document, not the services; acceptable as a synonym but a reviewer may prefer a narrower concept | in the form of comparable services, as follows: (a) Comparable services shall be provided as |
| 75 | `gen_curr` (RULE 3099.1) | General education curriculum | confirmed |  |  | maintain the problem behavior. General education curriculum – The curricular content adopted by the LEA |
| 76 | `sdi` (RULE 3099.1) | Specially designed instruction | confirmed |  |  | no cost – A specially-designed instruction, as defined by 34 C.F.R. § 300.39(b)(3) provided without |
| 77 | `special_ed` (RULE 3099.1) | Special education | confirmed |  |  | needs and eligibility for special education and related services. Assistive technology device – Any item, |
| 78 | `travel_training` (RULE 3099.1) | Travel training | confirmed |  |  | (d) Travel training; and (e) Vocational education. Specially designed instruction – |
| 79 | `voc_ed` (RULE 3099.1) | Vocational education | confirmed |  |  | (d) Travel training; and (e) Vocational education. |
| 80 | `para` (RULE 3099.1) | Paraprofessional | confirmed |  |  | Paraprofessional - An aide or other individual who provides |
| 81 | `related` (RULE 3012) | Related services, related service | confirmed |  |  | 3012 RELATED SERVICES 3012.1 The IEP Team shall determine whether a child with a disability |
| 82 | `audiology` (RULE 3012.3) | Audiology | confirmed |  |  | 3012.3 Audiology as a related service includes: (a) Identification of children with hearing loss; (b) |
| 83 | `counseling` (RULE 3012.4) | Counseling services | confirmed |  |  | 3012.4 Counseling services as a related service includes services provided by qualified social workers, psychologists, |
| 84 | `early_id` (RULE 3012.5) | Early identification and assessment of disabilities in children | confirmed |  |  | 3012.5 Early identification and assessment of disabilities in children as a related service includes the |
| 85 | `interpreting` (RULE 3012.6) | Interpreting services, oral transliteration, cued language transliteration | confirmed |  |  | 3012.6 Interpreting services as a related service includes: (a) Oral transliteration services, cued language transliteration |
| 86 | `cart` (RULE 3012.6) | communication access real-time translation | confirmed |  |  | and transcription services, including communication access real-time translation (CART), C- Print, and TypeWell for children |
| 87 | `ot` (RULE 3012.8) | Occupational therapy | confirmed |  |  | 3012.8 Occupational therapy as a related service is a service provided by a qualified occupational |
| 88 | `om` (RULE 3012.9) | Orientation and mobility services, orientation and mobility, long cane | confirmed |  |  | 3012.9 Orientation and mobility services as a related service includes services provided to blind or |
| 89 | `parent_training` (RULE 3012.10) | Parent counseling and training | confirmed |  |  | 3012.10 Parent counseling and training as a related service includes: (a) Assisting parents in understanding |
| 90 | `pt` (RULE 3012.11) | Physical therapy | confirmed |  |  | 3012.11 Physical therapy as a related service includes services provided by a qualified physical therapist. |
| 91 | `psych` (RULE 3012.12) | Psychological services | confirmed |  |  | 3012.12 Psychological services as a related service includes: (a) Administering psychological and educational tests, and |
| 92 | `recreation` (RULE 3012.13) | Recreation, therapeutic recreation, leisure education, recreation services | confirmed |  |  | 3012.13 Recreation as a related service includes: 7/1/2022 TITLE 5-A DCMR CHAPTER 30: SPECIAL EDUCATION |
| 93 | `rehab` (RULE 3012.14) | Rehabilitation counseling services, rehabilitation counseling | confirmed |  |  | 3012.14 Rehabilitation counseling services as a related service means services provided to a child with |
| 94 | `nursing` (RULE 3012.15) | School health services and school nurse services, school health services, school | confirmed |  |  | 3012.15 School health services and school nurse services as related services include health services that |
| 95 | `social_work` (RULE 3012.16) | social or developmental history, developmental history | confirmed |  |  | includes: (a) Preparing a social or developmental history on a child with a disability; (b) |
| 96 | `slp` (RULE 3012.17) | Speech-language pathology services | confirmed |  |  | 3012.17 Speech-language pathology services as a related service includes: (a) Identification of children with speech |
| 97 | `transport` (RULE 3012.18) | Transportation, transportation services | confirmed |  |  | 3012.18 Transportation as a related service: (a) Includes travel to and from school and between |
| 98 | `at_device` (RULE 3099.1) | Assistive technology device, assistive technology | confirmed |  |  | education and related services. Assistive technology device – Any item, piece of equipment, or product |
| 99 | `at_service` (RULE 3099.1) | Assistive technology service | confirmed |  |  | replacement of such device. Assistive technology service – Any service that directly assists a child |
| 100 | `pe` (RULE 3014) | Physical education, adapted physical education | confirmed |  |  | 3014 PHYSICAL EDUCATION AND ADAPTED PHYSICAL EDUCATION 3014.1 Each LEA shall make physical education services, |
| 101 | `esy` (RULE 3015) | Extended school year services, extended school year | confirmed |  |  | 3015 EXTENDED SCHOOL YEAR SERVICES 3015.1 The IEP Team shall determine, whether the provision of |
| 102 | `regression` (RULE 3015.2) | recoupment | confirmed |  |  | The time required for recoupment of previously attained or emerging critical skills. |
| 103 | `continuum` (RULE 3002) | Continuum of alternative placements | confirmed |  |  | 3002 CONTINUUM OF ALTERNATIVE PLACEMENTS 3002.1 The LEA shall ensure that a continuum of alternative |
| 104 | `regular_class` (RULE 3002.3) | regular education classroom | confirmed |  |  | the following environments: (a) Regular education classroom; (b) Special education classroom; (c) Special education day |
| 105 | `special_class` (RULE 3002.3) | special education classroom | confirmed |  |  | Regular education classroom; (b) Special education classroom; (c) Special education day program, through the process |
| 106 | `special_school` (RULE 3002.3) | special education day program | confirmed |  |  | Special education classroom; (c) Special education day program, through the process described in Section 3025; |
| 107 | `residential` (RULE 3002.3) | special education residential program | confirmed |  |  | in Section 3025; (d) Special education residential program, through the process described in Section 3025; |
| 108 | `residential` (RULE 3025.13) | residential treatment facility | confirmed |  |  | a residential or psychiatric residential treatment facility, shall be submitted through the SEA's procedures for |
| 109 | `home_instr` (RULE 3024) | Home instruction, home or hospital instruction, home and hospital instruction | confirmed |  |  | (REQUIRED FOR FAPE) 3024.1 Home instruction and hospital instruction are placements provided to a child |
| 110 | `hospital_instr` (RULE 3024) | hospital instruction | confirmed |  |  | 3024 HOME AND HOSPITAL INSTRUCTION (REQUIRED FOR FAPE) 3024.1 Home instruction and hospital instruction are |
| 111 | `lre` (RULE 3021) | Least restrictive environment | confirmed |  |  | 3021 LEAST RESTRICTIVE ENVIRONMENT 3021.1 An LEA shall provide a child with a disability a |
| 112 | `nonacademic` (RULE 3021.3) | extracurricular services | confirmed |  |  | provision of nonacademic and extracurricular services and activities, including meals, recess periods, after-school activities and |
| 113 | `aversive` (RULE 3025.9) | Aversive intervention | confirmed |  |  | Allows the use of aversive intervention in its policy or practice; or (b) Has not |
| 114 | `transition` (RULE 3026) | Transition services, secondary transition | confirmed |  |  | living skills and the transition services needed to assist the child in reaching those goals; |
| 115 | `postsecondary` (RULE 3026.1) | Measurable postsecondary goals, postsecondary goals, independent living skills | confirmed |  |  | services, including: (a) Appropriate measurable postsecondary goals based upon age-appropriate transition assessments related to training, |
| 116 | `trans_assess` (RULE 3026.1) | Age-appropriate transition assessments, transition assessments | confirmed |  |  | postsecondary goals based upon age-appropriate transition assessments related to training, education, employment, and where appropriate, |
| 117 | `interagency` (RULE 3026.1) | Interagency responsibilities and linkages, interagency linkages | confirmed |  | Rule spells it "inter-agency"; consider adding that spelling variant | A statement of inter-agency responsibilities or any needed linkages |
| 118 | `course_study` (RULE 3026.5) | course of study | confirmed |  |  | grade year, the child's course of study shall include a graduation plan that is reviewed |
| 119 | `std_diploma` (RULE 3026.6) | regular high school diploma | confirmed |  |  | opportunity to earn a regular high school diploma. |
| 120 | `exit_sped` (RULE 3028) | exit from special education | confirmed |  |  | 3028 EXIT FROM SPECIAL EDUCATION 3028.1 The LEA is responsible for developing and implementing a |
| 121 | `sop` (RULE 3028.5) | summary of performance | confirmed |  |  | the child with a summary of performance at no cost, in accordance with this section, |
| 122 | `fve` (RULE 3099.1) | Functional vocational evaluation | confirmed |  |  | and (3) Provision of a functional vocational evaluation. |
| 123 | `age_majority` (RULE 3035) | Transfer of rights at age of majority, age of majority, transfer of parental rig | confirmed |  |  | Any student who has reached eighteen (18) years of age and to whom all rights |
| 124 | `sdm` (RULE 3035) | supported decision-making | confirmed |  |  | RIGHTS: GENERAL PROVISIONS AND SUPPORTED DECISION-MAKING 3035.1 In accordance with D.C. Official Code § 46–101 |
| 125 | `fape` (RULE 3001.1) | Free appropriate public education, FAPE | confirmed |  |  | (LEA) shall make a free appropriate public education (FAPE) available to each child with a |
| 126 | `lea` (RULE 3001.1) | LEA, local education agency | confirmed |  |  | local education agency ( LEA) shall make a free appropriate public education (FAPE) available to |
| 127 | `sea` (RULE 3099.1) | SEA, state education agency | confirmed |  |  | adult appointed by the SEA to represent the educational interests of a child with a |
| 128 | `homeless` (RULE 3001.1) | Homeless children | confirmed |  |  | such as migrant or homeless children, even if they are advancing from grade to grade. |
| 129 | `ward` (RULE 3001.1) | Ward of the State, adjudicated dependent or ward of the court | confirmed |  |  | who resides in, or is a ward of, the District of Columbia |
| 130 | `part_c_transition` (RULE 3001.11) | Part C, Part B, early intervention services | confirmed |  |  | intervention services under IDEA Part C to special education and related services under IDEA Part |
| 131 | `ifsp` (RULE 3099.1) | Individualized family service plan, IFSP | confirmed |  |  | 1414 and this chapter. Individualized Family Service Plan or IFSP – A written plan for |
| 132 | `itd` (RULE 3099.1) | Infant or toddler with a disability | confirmed |  |  | intervention services to an infant or toddler with a disability and the infant's or toddler's |
| 133 | `native_language` (RULE 3099.1) | Native language | confirmed |  |  | sought, in the parent's native language or other mode of communication; (b) The parent understands |
| 134 | `ed_records` (RULE 3030) | Education records | confirmed |  |  | 3030 CONFIDENTIALITY OF EDUCATION RECORDS 3030.1 In accordance with the confidentiality procedures of IDEA and |
| 135 | `ferpa` (RULE 3030.1) | Family Educational Rights and Privacy Act, FERPA | confirmed |  |  | of IDEA and the Family Educational Rights and Privacy Act (FERPA), (20 U.S.C. § 1232g), |
| 136 | `pii` (RULE 3031.1) | Personally identifiable information, personally identifiable | confirmed |  |  | (d) Disclosing the child's personally identifiable information unless the information is contained in educational records |
| 137 | `consent` (RULE 3031) | Parental consent | confirmed |  |  | 3031 PARENTAL CONSENT 3031.1 The LEA shall obtain parental consent before: (a) Conducting an initial |
| 138 | `revoke` (RULE 3016.6) | Revocation of consent | confirmed |  |  | services because of the revocation of consent. |
| 139 | `pwn` (RULE 3032) | Prior written notice, written notice | confirmed |  |  | 3032 PRIOR WRITTEN NOTICE 3032.1 The LEA shall provide written notice to the parent of |
| 140 | `safeguards_notice` (PSN 1) | IDEA Part B Notice of Procedural Safeguards, Rights of Parents of Students with  | confirmed |  |  | District of Columbia IDEA Part B Notice of Procedural Safeguards Rights of Parents of Students |
| 141 | `surrogate` (PSN 9) | educational surrogate | confirmed |  |  | welfare); or (e) an educational surrogate who has been appointed in accordance with the IDEA |
| 142 | `foster` (PSN 9) | Foster parent | confirmed |  |  | adoptive parent; (b) a foster parent (but only if the biological or adoptive parent's authority |
| 143 | `gal` (RULE 3034.5) | Guardian ad litem | confirmed |  |  | serving as the child's guardian ad litem in a court proceeding. 7/1/2022 TITLE 5-A DCMR |
| 144 | `uhy` (RULE 3034.1) | Unaccompanied homeless youth | confirmed |  |  | The child is an unaccompanied homeless youth as defined in Section 725(6) of the McKinney-Vento |
| 145 | `ppps` (RULE 3040) | Parentally-placed private school children with disabilities | confirmed |  |  | representatives of parents of parentally-placed private school children with disabilities on all of the following: |
| 146 | `equitable` (RULE 3040) | Equitable services | confirmed |  |  | determine continued eligibility for equitable services, or when: (1) DCPS determines that the child's educational |
| 147 | `services_plan` (RULE 3099.1) | Services plan | confirmed |  |  | Services plan – A written statement that describes the special |
| 148 | `hqt` (RULE 3040.10) | Highly qualified special education teacher, highly qualified | confirmed |  |  | not required to meet highly qualified special education teacher requirements. |
| 149 | `part_agency` (PSN 14) | Participating agency | confirmed |  |  | U.S.C. 1232g (FERPA)).  Participating agency means any school district, agency or institution that collects, |
| 150 | `pti` (PSN 7) | Parent training and information center | confirmed |  |  | information for the: a. Parent Training and Information Center established under IDEA; b. D.C. Office |
| 151 | `idea` (PSN 2) | Individuals with Disabilities Education Act, IDEA | confirmed |  |  | PART B OF THE INDIVIDUALS WITH DISABILITIES EDUCATION ACT (IDEA) Revised August 2018 “Disability is |
| 152 | `ada` (PSN 29) | Americans with Disabilities Act | confirmed |  |  | the U.S. Constitution, the Americans with Disabilities Act of 1990, Title V of the Rehabilitation |
| 153 | `mediation` (RULE 3047) | Mediation, mediation agreement | confirmed |  |  | 3047 MEDIATION 3047.1 The parent of a child with a disability or the public agency |
| 154 | `state_complaint` (RULE 3048) | State complaint, state complaint procedures | confirmed |  |  | 3048 STATE COMPLAINTS 3048.1 The SEA, through the State Complaint Office (SCO), shall maintain written |
| 155 | `dp_complaint` (RULE 3049) | due process | confirmed |  |  | 3049 IMPARTIAL DUE PROCESS 3049.1 A parent of a child with a disability or a |
| 156 | `dp_hearing` (RULE 3049) | Impartial due process hearing, due process hearing | confirmed |  |  | time. 3049.4 When an impartial due process hearing is requested, the SEA shall inform the |
| 157 | `stay_put` (RULE 3050) | Child's status during proceedings, pendency, current educational placement | confirmed |  |  | 3050 CHILD'S STATUS DURING PROCEEDINGS 3050.1 The child with a disability shall remain in the |
| 158 | `resolution` (RULE 3052) | Resolution meeting, resolution process, resolution period | confirmed |  |  | 3052 RESOLUTION MEETINGS 3052.1 No later than fifteen (15) calendar days after receiving notice of |
| 159 | `state_panel` (RULE 3053.8) | State Education Agency Advisory Panel | confirmed |  |  | and decisions to the State Education Agency Advisory Panel and make the findings and decisions |
| 160 | `exp_hearing` (PSN 36) | Expedited due process hearing | confirmed |  |  | must arrange for an expedited due process hearing, which must occur within twenty (20) school |
| 161 | `code_conduct` (RULE 3043.1) | Code of student conduct | confirmed |  |  | disciplined under the same code of student conduct as a child without a disability, subject |
| 162 | `iaes` (RULE 3043.2) | Interim alternative educational setting | confirmed |  |  | placement to an appropriate interim alternative educational setting, another setting, or suspension, provided that: (a) |
| 163 | `cop` (RULE 3043.3) | Change of placement, pattern of removals | confirmed |  |  | 3043.3 A change of placement occurs if the removal is for more than ten (10) |
| 164 | `special_circ` (RULE 3043.9) | Special circumstances | confirmed |  | The phrase "special circumstances" is not in 3043.9 (concept only); the phrase appears at PSN p. 33 | may remove a child to an interim alternative educational setting ... without regard to |
| 165 | `weapon` (RULE 3043.9) | Dangerous weapon | confirmed |  | Rule says "weapon", not "dangerous weapon"; concept match OK | Carries a weapon, as defined by 34 C.F.R. § 300.530(i)(4) |
| 166 | `illegal_drug` (RULE 3043.9) | Illegal drug | confirmed |  |  | Knowingly possesses or uses illegal drugs |
| 167 | `controlled` (RULE 3043.9) | Controlled substance | confirmed |  |  | the sale of a controlled substance, as defined by 34 C.F.R. § 300.530(i)(3), while at |
| 168 | `sbi` (RULE 3043.9) | Serious bodily injury | confirmed |  |  | or (c) Has inflicted serious bodily injury, as defined by 34 C.F.R. § 300.530(i)(3), upon |
| 169 | `mdr` (RULE 3043.11) | Manifestation determination, manifestation determination meeting | confirmed |  |  | Team shall hold a manifestation determination meeting to review all relevant information in the child's |
| 170 | `basis_know` (PSN 37) | Basis of knowledge | confirmed |  |  | described in this notice. Basis of Knowledge for Disciplinary Matters An LEA will be deemed |
| 171 | `restraint` (RULE 3044.4) | physical restraints | confirmed |  |  | use any form of physical restraints, as defined in this chapter, except when the intervention |
| 172 | `mech_restraint` (RULE 3044.1) | mechanical restraint | confirmed |  | Already exists with no regional tag; this entry adds nothing but is harmless. Rule uses the plural "mechanical restraints" | The LEA shall not use any form of mechanical restraints |
| 173 | `reed` (HB 5) | analysis of existing data | confirmed |  |  | of Columbia eligibility criteria. Analysis of Existing Data The IEP team and other qualified professionals, |
| 174 | `eval_report` (HB 10) | evaluation summary report | confirmed |  |  | who wrote the report. Evaluation Summary Report: Upon completion of appropriate evaluation procedures, the LEA |
| 175 | `two_prong` (HB 10) | two-pronged test | confirmed |  |  | student must meet a two-pronged test to be considered a student with a disability: (1) |
| 176 | `social_hist` (HB 7) | social history assessment | confirmed |  |  | Assessment Functional Behavior Assessment Social History Assessment Health/Physical Physical Therapy Evaluation Motor Skills/Physical Development Occupational |
| 177 | `audiological_assess` (HB 7) | audiological evaluation | confirmed |  |  | Hearing: Audiological Evaluation, Auditory Processing Evaluation (evaluation table) |
| 178 | `voc_eval` (HB 7) | Vocational evaluation | confirmed |  |  | Occupational Therapy Evaluation Vocational Vocational Evaluation OFFICE OF THE STATE SUPERINTENDENT OF EDUCATION 7 |
| 179 | `consult` (HB 24) | consultation services | confirmed |  |  | that a student needs consultation services as part of their related services. Consultation services may |
| 180 | `comparable` (HB 27) | comparable services plan | confirmed |  |  | LEA. In designing the comparable services plan using the Comparable Services process in Special Programs, |
| 181 | `coteach` (HB 26) | Co-teaching | confirmed |  |  | Placement INCLUSIVE SCHOOL ENVIRONMENT Co-Teaching and Co-Planning Differentiated Learning Student Support Team 26 SPECIAL EDUCATION |
| 182 | `dys_screen` (HB 4) | Dyslexia screening | confirmed |  |  | For more information on Dyslexia screening requirements, please see OSSE's Special Education Non-Regulatory Guidance: Intersections |
| 183 | `ext_time` (HB 17) | Extended time | confirmed |  |  | Timing and Scheduling • Extended Time • Flexibility in Scheduling The IEP team may also |
| 184 | `large_print` (HB 17) | Large print | confirmed |  |  | Amplification • Magnification • Large Print Materials • Paper Based Materials • Clarification/Repetition of Directions |
| 185 | `asl` (HB 17) | ASL | confirmed |  |  | • Directions Available in ASL • Student Reads Assessment Aloud to Themselves • Masking Tools |
| 186 | `word_pred` (HB 17) | Word prediction | confirmed |  |  | on ELS/Literacy Assessments • Word Prediction External Device • Answers Recorded in Test Book (Paper-Based |
| 187 | `small_group` (HB 17) | small group testing | confirmed |  |  | • Individual Testing • Small Group Testing • On Screen Guidance • Unique/Non-Standard Accommodation Other |
| 188 | `indiv_admin` (HB 17) | individual testing | confirmed |  |  | with Minimal Distractions • Individual Testing • Small Group Testing • On Screen Guidance • |
| 189 | `msaa` (ALT) | Multi-State Alternate Assessment, MSAA | confirmed |  |  | (ALT page) The MSAA is a comprehensive assessment system |
| 190 | `dlm` (ALT) | DLM Science Alternate Assessment | confirmed |  |  | (ALT page) The DLM Science Alternate Assessment is based on Essential Elements (EEs) |
| 191 | `ess_elements` (ALT) | EEs | confirmed |  | "EEs" is mixed-case; phrase_cs with no regional tag, OK | (ALT page) based on Essential Elements (EEs) that are alternate achievement standards |
| 192 | `sig_cog` (ALT) | Most significant cognitive disability, most significant cognitive disabilities,  | confirmed |  |  | (ALT page) students with the most significant cognitive disabilities |
| 193 | `dc_osse` (RULE 3099.1) | Office of the State Superintendent of Education / OSSE | confirmed |  |  | Office of the State Superintendent of Education (OSSE) – The State |
| 194 | `dc_sco` (RULE 3048.1) | State Complaint Office / SCO | confirmed |  |  | The SEA, through the State Complaint Office (SCO), shall maintain written procedures for the investigation |
| 195 | `dc_odr` (HB 35) | Office of Dispute Resolution / ODR | confirmed |  | Acronym ODR collides with existing `odr_pa` (Pennsylvania); both regional-tagged. Reviewer decision | be provided to the Office of Dispute Resolution (ODR) on the same day that it |
| 196 | `dc_osse_dot` (HB 19) | Division of Transportation / OSSE-DOT | confirmed |  | "OSSE-DOT" contains the first name Dot (graded low/phrase_only; OK) | must work directly with Division of Transportation (OSSE-DOT) and agencies to complete appropriate documentation facilitating |
| 197 | `dc_pcsb` (RULE 3001.9) | District of Columbia Public Charter School Board / PCSB | confirmed |  | Contains a place name (Columbia), also a first name; graded low/phrase_only (OK) | prior approval by the District of Columbia Public Charter School Board (PCSB), in accordance with |
| 198 | `dc_cfsa` (RULE 3001.7) | Child and Family Services Agency / CFSA | confirmed |  |  | the District of Columbia Child and Family Services Agency (CFSA), who is committed to DYRS, |
| 199 | `dc_dyrs` (RULE 3001.6) | Department of Youth Rehabilitation Services / DYRS | confirmed |  |  | the District of Columbia Department of Youth Rehabilitation Services (DYRS) shall make FAPE available for |
| 200 | `dc_dhcf` (RULE 3025.14) | Department of Health Care Finance / DHCF | confirmed |  |  | the District of Columbia Department of Health Care Finance (DHCF) requirements for a Psychiatric Residential |
| 201 | `dc_dbh` (RULE 3025.16) | Department of Behavioral Health / DBH | confirmed |  |  | The District of Columbia Department of Behavioral Health (DBH) to determine whether the child qualifies |
| 202 | `dc_dds` (HB 13) | Department on Disability Services / DDS | confirmed |  | "DDS" is also a common degree abbreviation; regional tag limits it to US-DC | services, such as the Department on Disability Services (DDS) or Rehabilitation Services Administration (RSA); • |
| 203 | `dc_rsa` (HB 13) | Rehabilitation Services Administration / RSA | confirmed |  | Same name and acronym as the federal Rehabilitation Services Administration (ED/OSERS). Note could say so | Disability Services (DDS) or Rehabilitation Services Administration (RSA); • The student, in the following situations: |
| 204 | `dc_ombuds` (RULE 3032.2) | Office of the Ombudsman for Public Education | confirmed |  |  | U.S.C. § 1471); (2) Office of the Ombudsman for Public Education (D.C. Official Code § |
| 205 | `dc_sped_hub` (HB 14) | DC Special Education Hub / Special Education Hub | confirmed |  | Preferred term contains the place name "DC" but is graded none/phrase_or_token; place names are not checked by the risk grader | (202) 741-0886; educationombudsman.dc.gov • DC Special Education Hub (Office of the Ombudsman for Public Education), |
| 206 | `dc_osa` (RULE 3032.2) | Office of the Student Advocate | confirmed |  |  | et seq.); and (3) Office of the Student Advocate (D.C. Official Code § 38-371 et |
| 207 | `dc_aje` (HB 14) | Advocates for Justice and Education / AJE | confirmed |  | Contains Justice (first name and surname); graded low/phrase_only (OK) | training and information center: Advocates for Justice and Education (AJE), (202) 678-8060; aje-dc.org • The |
| 208 | `dc_strong_start` (BRO 2) | Strong Start DC Early Intervention Program / Strong Start DC | confirmed |  | Contains the place name "DC" and the surname Strong (graded low/phrase_only; OK) | or toddler, contact OSSE's Strong Start DC Early Intervention Program at (202) 727-3665. |
| 209 | `dc_special_programs` (HB 4) | Special Programs | confirmed |  | Common English phrase (flagged common_english_word); low value as a safelist term but not a name risk | document the referral in Special Programs, the statelevel special education database, within three days of |
| 210 | `dc_ch30` (RULE) | 5-A DCMR Chapter 30 | confirmed |  |  | TITLE 5-A DCMR CHAPTER 30: SPECIAL EDUCATION 3000 GENERAL PROVISIONS 3001 PROVISION OF FREE APPROPRIATE |
| 211 | `dc_language_access` (RULE 3009.8) | D.C. Language Access Act of 2004 / Language Access Act | confirmed |  | Contains the place name "D.C." (graded low/phrase_only; OK) | to comply with the D.C. Language Access Act of 2004 (D.C. Law 15-167; D.C. Official |
| 212 | `dc_sfasa` (HB 32) | Student Fair Access to School Act of 2018 | confirmed |  | Contains Fair (surname); low/phrase_only (OK) | and expulsion in the Student Fair Access to School Act of 2018 (DC Code §38-235 |
| 213 | `dc_hhi_act` (HB 26) | Students' Right to Home and Hospital Instruction Act of 2020 | confirmed |  |  | need consistent with the Students' Right to Home and Hospital Instruction Act of 2020. |
| 214 | `dc_dyslexia_act` (HB 4) | Addressing Dyslexia and Other Reading Difficulties Amendment Act of 2020 | confirmed |  |  | Additionally, consistent with the Addressing dyslexia and Other Reading Difficulties Amendment Act of 2020, LEAs |
| 215 | `dc_pcs_lea` (RULE 3003.3) | Public charter school LEA / public charter school LEAs | confirmed |  |  | services and programs. District public charter school LEAs shall conduct similar awareness activities to inform |
| 216 | `dc_lea_right` (HB 3) | LEA-of-right / geographical LEA-of-right | confirmed |  |  | (DCPS), as the geographical LEA-of-right, is responsible for the availability of FAPE to students enrolled |
| 217 | `dc_stage5` (HB 27) | Stage 5 enrollment | confirmed |  |  | the first day of stage 5 enrollment (attendance in school) and each related service must |
| 218 | `primary_disability` (RULE 3010.4) | Primary disability | confirmed |  |  | designate one (1) primary disability and one (1) or more secondary disabilities |
| 219 | `secondary_disability` (RULE 3010.4) | Secondary disability / secondary disabilities | confirmed |  |  | designate one (1) primary disability and one (1) or more secondary disabilities |
| 220 | `cbm` (HB 8) | Curriculum-based measurement / CBM | confirmed |  |  | CurriculumBased Measurement (CBM) is the best-known method of progress monitoring |
| 221 | `fva` (HB 7) | Functional vision assessment | confirmed |  |  | EvaluationAuditory Processing Evaluation Vision Functional Vision Assessment Learning Media Assessment Communication Speech and Language EvaluationAssistive |
| 222 | `lma` (HB 7) | Learning media assessment | confirmed |  |  | Vision Functional Vision Assessment Learning Media Assessment Communication Speech and Language EvaluationAssistive Technology Evaluation Emotional, |
| 223 | `dc_dwa` (RULE 3019.1) | Documented written agreement | confirmed |  |  | LEA and parent through documented written agreement, except that the LEA and parent may not |
| 224 | `dc_speech_only` (HB 21) | Speech-only IEP / Speech Only IEPs | confirmed |  |  | as Special Education ( Speech Only IEPs)” for more information. Alternatively, a parent of a |
| 225 | `dedicated_aide` (HB 16) | Dedicated aide | confirmed |  |  | SPECIAL EDUCATION PROCESS HANDBOOK Dedicated Aides In some cases, students with disabilities may be eligible |
| 226 | `comp_services` (HB 24) | Compensatory services | confirmed |  |  | consider the need for compensatory services. LEAs are 24 SPECIAL EDUCATION PROCESS HANDBOOK encouraged to |
| 227 | `critical_skill` (RULE 3015.3) | Critical skill | confirmed |  |  | provision of FAPE, a critical skill is a skill that is essential to a student's |
| 228 | `dc_mfs` (HB 19) | Medically Fragile Students / MFS | confirmed |  |  | following eligibility categories: • Medically Fragile Students (MFS) applies to students who cannot travel safely |
| 229 | `dc_sts` (HB 19) | Structured Transportation Supports / STS | confirmed |  |  | documented medical condition. • Structured Transportation Supports (STS) refers to a non-medical accommodation and/or form |
| 230 | `dc_asp` (HB 19) | Accessing Special Programs / ASP | confirmed |  |  | the student's disability. • Accessing Special Programs (ASP) refers to a special education instructional setting, |
| 231 | `dc_service_location` (RULE 3099.1) | Service location | confirmed |  |  | Service location – The physical address at which instruction |
| 232 | `dc_outside_lea` (RULE 3025) | Placement outside of the LEA | confirmed |  |  | 3025 PLACEMENT OUTSIDE OF THE LEA 3025.1 If an LEA anticipates that it may be |
| 233 | `dc_nonpublic` (RULE 3099.1) | Nonpublic special education school or program / nonpublic special education scho | confirmed |  |  | Nonpublic special education school or program – A privately owned or operated |
| 234 | `dc_coa` (RULE 3025.8) | Certificate of approval | confirmed |  |  | not hold a current certificate of approval, issued by the SEA in accordance with D.C. |
| 235 | `prtf` (RULE 3025.14) | Psychiatric residential treatment facility / PRTF | confirmed |  |  | (DHCF) requirements for a Psychiatric Residential Treatment Facility (PRTF), consistent with 29 DCMR § 948; |
| 236 | `dc_iep_coc` (RULE 3027) | IEP Certificate of Completion | confirmed |  |  | 3027 IEP CERTIFICATE OF COMPLETION FOR SPECIAL EDUCATION 3027.1 The LEA shall develop, publish, and |
| 237 | `dc_diploma_notice` (HB 31) | Notice of Change in Diploma Type | confirmed |  |  | the form of a Notice of Change in Diploma Type. The notice includes the following |
| 238 | `graduation_plan` (RULE 3026.5) | Graduation plan | confirmed |  |  | study shall include a graduation plan that is reviewed annually and modified, when necessary, to |
| 239 | `dc_educ_rep` (RULE 3099.1) | Educational representative | confirmed |  |  | Official Code § 38-171). Educational Representative – An adult appointed by the SEA to represent |
| 240 | `dc_parent_obs` (RULE 3041) | Parent observation | confirmed |  |  | 3041 PARENT OBSERVATION 3041.1 Upon request, the LEA shall provide timely classroom access, either together |
| 241 | `dc_hod` (RULE 3053.5) | Hearing Officer Determination / HOD | confirmed |  |  | 3053.5 The Hearing Officer Determination (HOD) shall be in writing and include all of the |
| 242 | `seclusion` (RULE 3045) | Seclusion | confirmed |  |  | 3045 SECLUSION 3045.1 The LEA shall not use any form of seclusion except in emergency |
| 243 | `prone_restraint` (RULE 3099.1) | Prone restraint | confirmed |  |  | Prone restraint – The use of force, use of |
| 244 | `chem_restraint` (RULE 3044.3) | Chemical restraint | confirmed |  |  | use any form of chemical restraints. A drug ordered by a licensed physician as part |
| 245 | `fade_plan` (HB 32) | BIP fade plan / fade plan | confirmed |  |  | team should establish a BIP fade plan when appropriate. A fade plan identifies the criteria |
| 246 | `informal_removal` (HB 33) | Informal removal / informal removals | confirmed |  |  | progress on IEP goals. Informal Removals Informal removals, although not defined by or referenced in |
| 247 | `dc_cape` (ALT) | DC CAPE Next | confirmed |  | Contains the place name "DC", graded none/phrase_or_token; category iep_component is questionable for a statewide test. Only source is the ALT web page | (ALT page) take alternate statewide assessments in place of DC CAPE Next |
| 248 | `ccss` (HB 15) | Common Core State Standards / CCSS | confirmed |  |  | goal; • Alignment to Common Core State Standards (CCSS): The specific CCSS that the goal |
| 249 | `ngss` (HB 17) | Next Generation Science Standards / NGSS | confirmed |  |  | standards based on the Next Generation Science Standards (NGSS). This assessment will be administered to |
| 250 | `essa` (ALT) | Every Student Succeeds Act | confirmed |  |  | (ALT page) The Every Student Succeeds Act (ESSA) places a 1% cap |

## 2. Missed terms

| Term | Citation | Suggested handling |
|---|---|---|
| Reasonable efforts (to obtain consent / parent participation) | 5-A DCMR § 3005.4–3005.6; HB pp. 5–7, 12–13; PSN | New concept; used 48 times across the documents |
| Specialized instruction | HB pp. 20–22, 27 | DC's usual name for specially designed instruction; add as synonym on `sdi` |
| System of record | 5-A DCMR § 3029 (also 3020.2, 3028.6) | New DC concept (OSSE's student data system; relates to `dc_special_programs`) |
| Referral / Referral Acknowledgment | 5-A DCMR § 3004.1–3004.3; HB p. 4 | No `referral` string exists in the list; "Referral Acknowledgment" is a DC form |
| Restraint and seclusion incident report | 5-A DCMR § 3046.2–3046.4 | New concept under `restraint` / `seclusion` |
| Power of attorney (educational) | 5-A DCMR § 3036.1–3036.2 | Transfer-of-rights alternative alongside `sdm` and `dc_educ_rep` |
| Part C representative | 5-A DCMR § 3008.2(b); HB p. 13 | IEP team participant |
| Settlement agreement | 5-A DCMR § 3048.3, 3053.7; PSN | Dispute-resolution concept |
| Child count | 5-A DCMR § 3042 | Section heading |
| Missed services | HB p. 24 | Relates to `comp_services` |
| Highly mobile children | 5-A DCMR § 3001.1, 3003.1 | Child-find population |
| Inclusive school environment / Universal Design for Learning | HB p. 26 | LRE practice terms |
| Behavior support | HB pp. 32–33 | Synonym candidate near `pbis`/`bip` |

## 3. Summary

- **Confirmed: 250 · Misplaced: 0 · Not found: 0.** 21 of these needed hand-checking because the documents use different wording (for example, the rule says "a representative of the LEA", not "LEA representative"). Each is confirmed above with a quote.
- **Safety:** no single letters, no new eponyms, no person's name as a standalone term. Every string with a name hit (Dot, Columbia, Justice, Strong, Fair, Parent, LEA) is graded low/phrase_only. **"Endrew F." (HB p. 15) is correctly left out**, and so is DCPS.

**Three most important fixes**
1. **Place names aren't graded:** "DC Special Education Hub" and "DC CAPE Next" contain "DC" but are graded none/phrase_or_token. "District of Columbia Public Charter School Board" got low only because Columbia is also a first name. Either make `spedlex/risk.py` check place names, or confirm with a reviewer that "DC" inside a multi-word phrase is acceptable.
2. **ODR collides:** the new `dc_odr` acronym is the same as Pennsylvania's `odr_pa`. This is a reviewer decision under AGENTS.md; raise it in the PR. Also note that DC's RSA shares its name with the federal Rehabilitation Services Administration.
3. **Clean up redundant or loosely typed strings:** the duplicate strings on `reeval` and `mech_restraint` add nothing and can go (the one on `ed` adds the DC tag, so keep it). Retype "Response-to-Intervention model" as a synonym (S). Add "inter-agency responsibilities". Add the missed terms above, at least "specialized instruction" and "reasonable efforts".

**Docstring:** accurate on documents, dates, page offsets and the 5-E DCMR note. Two small points: the HB "posted Aug. 26, 2026" date isn't in the PDF itself, and ALT is a web page, not a file, so "five ... extracted from the official files" is loose.

**Correction (2026-10-06):** an earlier version of this report called some strings redundant because they already existed. They aren't: each adds this state's regional tag, without which a matcher filtered to the state drops the string. Keep them.
