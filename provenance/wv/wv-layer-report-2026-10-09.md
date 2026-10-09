# West Virginia (US-WV) layer: contributor report

Layer `west_virginia`, version 0.43.0, 2026-10-09. Built from the three files listed in `wv-sources-2026-10-09.md`. The audit (`prompts/audit-layer.md`) has NOT been run.

Result: 256 concepts attested by West Virginia, 86 of them new and 170 already in the list. `python -m spedlex.build --check` passes. `pytest -q`: 81 passed.

## 1. Documents read and gaps

- **Policy 2419** (126CSR16, eff. 3/13/2023): read in full, 155 pages. It is a scanned image with no text layer, so every quote below comes from my own OCR text. OCR can drop or garble characters, so the quotes need a check against the PDF. Chapter and section are given where the text gives one.
- **Procedural Safeguards Notice** (Aug. 2024): read in full, 51 pp. Mostly the federal model notice, so most of its entries only record that West Virginia uses an existing concept. Its records are `candidate`; the Policy 2419 records are `machine_validated`.
- **OSEP QA 23-01** (federal): read in full, used only to confirm the wording of general supervision, SPP and monitoring. It is not cited by any record.
- **Gaps:** no West Virginia parent guide or IEP manual. The Speech-Language Pathology guidance and the forms named in Policy 2419 (for example the EC Report, SLD Team Report and Reevaluation Determination forms) were not available, so the form names come from the rule text only. The WVDE site blocked automated download, so the files are the copies the contributor supplied; I could not confirm they are the latest versions on wvde.us.

## 2. New concepts

Quotes are 15 words or fewer, copied from the OCR/extracted text. The page shown is the PDF page where the quote was found. Policy 2419 pages are printed page + 1; PSN pages are printed page + 3.

| # | Key | Preferred term | Category | Quote (OCR/extracted text) | Citation |
|---|---|---|---|---|---|
| 1 | `wv_wvde` | West Virginia Department of Education | legal_procedural | "West Virginia Department of Education WVDHHR West Virginia Department of Health and Human Resources WVEIS" | Policy 2419, Acronyms and Abbreviations, PDF p. 11 |
| 2 | `wv_wvbe` | West Virginia Board of Education | legal_procedural | "West Virginia Board of Education WVDE West Virginia Department of Education WVDHHR West Virginia Department" | Policy 2419, Acronyms and Abbreviations, PDF p. 11 |
| 3 | `wv_dhhr` | West Virginia Department of Health and Human Resources | legal_procedural | "West Virginia Department of Health and Human Resources (WVDHHR). Services under Part C are designed" | Policy 2419, Definitions, PDF p. 23 |
| 4 | `wv_birth_to_three` | WV Birth to Three | early_intervention | "WV Birth to Three is responsible for the Child Find system for infants and toddlers," | Policy 2419, Ch. 2, § 2.A, PDF p. 37 |
| 5 | `wv_osp` | West Virginia Office of Special Education | legal_procedural | "West Virginia Department of Education, Office of Special Education 1900 Kanawha Boulevard, East, Building 6," | Procedural Safeguards Notice (Aug. 2024), PDF p. 24 |
| 6 | `wv_dfps` | Division of Federal Programs & Support | legal_procedural | "Division of Federal Programs & Support Office of Special Education Bldg. 6, Suite 750 1900" | Procedural Safeguards Notice (Aug. 2024), PDF p. 50 |
| 7 | `wv_advisory_council` | West Virginia Advisory Council for the Education of Exceptional Children | legal_procedural | "West Virginia Advisory Council for the Education of Exceptional Children; and 2. Makes those findings" | Procedural Safeguards Notice (Aug. 2024), PDF p. 34 |
| 8 | `wv_pti` | West Virginia Parent Training and Information | legal_procedural | "West Virginia Parent Training and Information (WVPTI) at 304-472-5697 or email wvpti@aol.com. 2 " | Procedural Safeguards Notice (Aug. 2024), PDF p. 5 |
| 9 | `wv_perc` | Parent/Educator Resource Center | legal_procedural | "Parent/Educator Resource Center State complaints, mediations, facilitated Individualized Education Program (FIEP) meeting requests and due" | Procedural Safeguards Notice (Aug. 2024), PDF p. 50 |
| 10 | `wv_drs` | West Virginia Division of Rehabilitation Services | transition | "West Virginia Division of Rehabilitation Services that include: 1. job exploration; 2. work-based learning; 3." | Policy 2419, Definitions, PDF p. 24 |
| 11 | `wv_wvsdb` | West Virginia Schools for the Deaf and the Blind | placement_setting | "126CSR16 Schools for the Deaf and the Blind so the parent/adult student is aware of" | Policy 2419, Ch. 4, § 2, PDF p. 51 |
| 12 | `wv_sdt` | West Virginia Schools of Diversion and Transition | placement_setting | "West Virginia Schools of Diversion and Transition or the West Virginia Schools for the Deaf" | Policy 2419, Ch. 3, § 3.D, PDF p. 46 |
| 13 | `wv_registry` | West Virginia Registry of Interpreters | personnel_role | "West Virginia Registry of Interpreters is paid in full by the employer for any service" | Policy 2419, Ch. 9, § 3.A, PDF p. 126 |
| 14 | `wv_policy_2419` | Policy 2419 | legal_procedural | "Policy 2419: Regulations for the Education of Students with Exceptionalities provide procedural safeguards to ensure" | Procedural Safeguards Notice (Aug. 2024), PDF p. 8 |
| 15 | `wv_policy_4350` | Policy 4350 | legal_procedural | "Policy 4350: Regulations for the Collection, Maintenance and Disclosure of Student Data protects confidentiality of" | Procedural Safeguards Notice (Aug. 2024), PDF p. 8 |
| 16 | `wv_policy_4373` | Policy 4373 | discipline | "Policy 4373, Expected Behavior in Safe and Supportive Schools (Policy 4373), and W. Va. Code" | Policy 2419, Definitions, PDF p. 17 |
| 17 | `wv_wveis` | West Virginia Education Information System | legal_procedural | "West Virginia Education Information System WV-MAP W. Va. 126CSR14, Policy 2340, West Virginia Measures of" | Policy 2419, Acronyms and Abbreviations, PDF p. 11 |
| 18 | `wv_online_iep` | WVDE Online IEP | iep_component | "WVDE Online IEP in the development of a student’s IEP. The IEP requirements are listed" | Policy 2419, Ch. 5, § 2, PDF p. 77 |
| 19 | `wv_taaes` | Temporary Assessment Accommodations Entry System | accommodation_modification | "(TAAES) application. Once West Virginia eligibility for special education services has been determined, the LEA" | Policy 2419, Ch. 5, § 4.B, PDF p. 92 |
| 20 | `wv_rcsp` | West Virginia Results and Compliance System Procedures | legal_procedural | "West Virginia Results and Compliance System Procedures, IDEA, and the State Performance Plan (SPP). IDEA" | Policy 2419, Ch. 9, § 2, PDF p. 121 |
| 21 | `wv_wvtss` | West Virginia Tiered System of Support | evaluation_eligibility | "West Virginia Tiered System of Support (WVTSS) and receives targeted and/or intensive supports, the LEA" | Policy 2419, Ch. 4, § 3.L, MTSS, PDF p. 62 |
| 22 | `wv_wvmap` | West Virginia Measures of Academic Progress | iep_component | "West Virginia Measures of Academic Progress West Virginia Board of Education policies may be found" | Policy 2419, Acronyms and Abbreviations, PDF p. 11 |
| 23 | `wv_wvgsa` | West Virginia General Summative Assessment | iep_component | "West Virginia General Summative Assessment (WVGSA), SAT School Day, or the West Virginia Alternate Summative" | Policy 2419, Ch. 9, § 2.C, PDF p. 124 |
| 24 | `wv_alt_summative` | West Virginia Alternate Summative Assessment | iep_component | "West Virginia Alternate Summative Assessment; in addition, students who are English learners, participate in the" | Policy 2419, Ch. 9, § 2.C, PDF p. 124 |
| 25 | `wv_participation_guidelines` | Participation Guidelines for West Virginia State Assessments | iep_component | "Participation Guidelines for West Virginia State Assessments and the test administration manuals. Role of the" | Policy 2419, Ch. 5, § 2.I, PDF p. 84 |
| 26 | `wv_ccrs` | West Virginia College- and Career-Readiness Standards | iep_component | "mastery of the West Virginia College- and Career-Readiness Standards." | Policy 2419, Definitions, PDF p. 17 |
| 27 | `wv_aaas` | West Virginia Alternate Academic Achievement Standards | iep_component | "West Virginia Alternate Academic Achievement Standards, each goal must have at least two objectives. Objectives" | Policy 2419, Ch. 5, § 2.E, PDF p. 79 |
| 28 | `wv_prek` | West Virginia Pre-K | placement_setting | "utilizing approved participating partners in West Virginia Pre-K." | Policy 2419, Ch. 6, § 3, PDF p. 96 |
| 29 | `wv_b8_survey` | IDEA Indicator B-8 Parent Involvement Survey | legal_procedural | "IDEA Indicator B-8 Parent Involvement Survey The WVDE is required to report to the US" | Procedural Safeguards Notice (Aug. 2024), PDF p. 5 |
| 30 | `wv_ec_report` | Eligibility Committee Report | evaluation_eligibility | "EC Report and provide a copy of the report to the parent/adult student. The parent/adult" | Policy 2419, Ch. 4, § 2, PDF p. 50 |
| 31 | `wv_sld_team_report` | SLD Team Report | evaluation_eligibility | "SLD Team Report The SLD Team Report must contain a statement of: 1. whether the" | Policy 2419, Ch. 4, § 3.L, PDF p. 65 |
| 32 | `wv_reeval_determination` | Reevaluation Determination form | evaluation_eligibility | "Reevaluation Determination form. If the MDET determines that additional evaluations are needed, the MDET will" | Policy 2419, Ch. 3, § 2.B, PDF p. 43 |
| 33 | `wv_eval_request_notice` | Notice of Individual Evaluation/Reevaluation Request | evaluation_eligibility | "Notice of Individual Evaluation/Reevaluation Request form is provided. The date of receipt by the school/LEA" | Policy 2419, Ch. 3, § 3.A, PDF p. 44 |
| 34 | `wv_three_prong` | Three-prong test of eligibility | evaluation_eligibility | "a three-pronged test of eligibility must be met." | Policy 2419, Ch. 4, § 3, PDF p. 51 |
| 35 | `wv_primary_exceptionality` | Primary exceptionality | evaluation_eligibility | "primary exceptionality when the student meets the criteria for more than one exceptionality. The committee" | Policy 2419, Ch. 4, § 1, PDF p. 50 |
| 36 | `wv_psych_adjustment` | Psychological adjustment disorder | evaluation_eligibility | "Psychological Adjustment Disorder. Significant emotional or behavioral symptoms that adversely affect a student's educational performance" | Policy 2419, Definitions, PDF p. 25 |
| 37 | `wv_underachievement` | Underachievement | evaluation_eligibility | "Underachievement. Academic achievement and or classroom performance that is significantly discrepant with the student's intellectual" | Policy 2419, Definitions, PDF p. 31 |
| 38 | `wv_hurgp` | Historically under-represented gifted population | evaluation_eligibility | "Historically Under-represented Gifted Population. Those students whose giftedness may not be apparent due to low" | Policy 2419, Definitions, PDF p. 18 |
| 39 | `wv_fle` | Functional Listening Evaluation | evaluation_eligibility | "Functional Listening Evaluation (FLE). Assessment of how a student's listening abilities are affected by noise," | Policy 2419, Definitions, PDF p. 17 |
| 40 | `wv_severity_levels` | Severity Levels for Adaptive Functioning | evaluation_eligibility | "Severity Levels for Adaptive Functioning Taken from the Diagnostic and Statistical Manual of Mental Disorders" | Policy 2419, Appendix, DSM-5 table, PDF p. 153 |
| 41 | `wv_fcas` | Functional Communication Assessment Summary | instrument | "Functional Communication Assessment Summary (see Speech-Language Pathology Services in West Virginia Schools: Guidance for West" | Policy 2419, Ch. 4, § 3.M, PDF p. 67 |
| 42 | `wv_spas` | Speech Production Assessment Summary | instrument | "Speech Production Assessment Summary (see Speech-Language Pathology Services in West Virginia Schools: Guidance for West" | Policy 2419, Ch. 4, § 3.M, PDF p. 67 |
| 43 | `wv_vas` | Voice Assessment Summary | instrument | "Voice Assessment Summary (see Speech-Language Pathology Services in West Virginia Schools: Guidance for West Virginia" | Policy 2419, Ch. 4, § 3.M, PDF p. 71 |
| 44 | `social_comm_dis` | Social communication disorder | health_condition | "Social communication disorder encompasses language use in social situations, communication that occurs between at least" | Policy 2419, Ch. 4, § 3.M, PDF p. 70 |
| 45 | `cluttering` | Cluttering | health_condition | "Cluttering) Diagnostic Criteria: Fluency refers to continuity, smoothness, rate, and effort of speech production. There" | Policy 2419, Ch. 4, § 3.M, PDF p. 68 |
| 46 | `cognitive_referencing` | Cognitive referencing | evaluation_eligibility | "Cognitive referencing refers to the practice of finding students not eligible for services when their" | Policy 2419, Ch. 4, § 3.M, PDF p. 72 |
| 47 | `language_sample` | Language sample analysis | evaluation_eligibility | "language sample analysis results in a score of at least 1.5 standard deviations or more" | Policy 2419, Ch. 4, § 3.M, PDF p. 66 |
| 48 | `dynamic_assessment` | Dynamic assessment | evaluation_eligibility | "dynamic assessment (test-teach-retest) that demonstrates limited or very limited improvement (see Speech-Language Pathology Services in" | Policy 2419, Ch. 4, § 3.M, PDF p. 67 |
| 49 | `pcc` | Percentage of consonants correct | score_metric | "percentage of Consonants Correct is 84 percent or below. 2. The student’s disability adversely affects" | Policy 2419, Ch. 4, § 3.M, PDF p. 68 |
| 50 | `dsm5` | Diagnostic and Statistical Manual of Mental Disorders | instrument | "Diagnostic and Statistical Manual of Mental Disorders (DSM-5) criteria (1 through 5) are met. 1." | Policy 2419, Ch. 4, § 3.A, PDF p. 52 |
| 51 | `wv_geft` | General Education: Full-Time | placement_setting | "(GEFT). One school-age option of the LRE continuum of services. The student’s specially designed instruction" | Policy 2419, Definitions, PDF p. 18 |
| 52 | `wv_gept` | General Education: Part-Time | placement_setting | "(GEPT). One school-age option of the LRE continuum of services. The student's specially designed instruction" | Policy 2419, Definitions, PDF p. 18 |
| 53 | `wv_separate_class` | Special Education: Separate Class | placement_setting | "Special Education: Separate Class - The student's specially designed instruction and related services are delivered" | Policy 2419, Ch. 5, § 2.J, PDF p. 86 |
| 54 | `wv_out_of_school_env` | Special Education: Out-of-School Environment | placement_setting | "Special Education: Out-of-School Environment - The student's specially designed instruction and related services are temporarily" | Policy 2419, Ch. 5, § 2.J, PDF p. 87 |
| 55 | `wv_correctional` | Special Education: Correctional Facilities | placement_setting | "Special Education: Correctional Facilities - The student's specially designed instruction and related services are delivered" | Policy 2419, Ch. 5, § 2.J, PDF p. 87 |
| 56 | `service_provider_location` | Service provider location | placement_setting | "service provider location. Service Provider Location - The student receives all special education and related" | Policy 2419, Ch. 5, § 2.J, PDF p. 88 |
| 57 | `wv_see` | Special education environment | placement_setting | "special education environment (SEE) or general education environment (GEE). 2. list the anticipated extent/frequency. A" | Policy 2419, Ch. 5, § 2.G, PDF p. 83 |
| 58 | `wv_shared_models` | Shared instructional models | placement_setting | "Shared Instructional Models. Include an array of service delivery options provided by general education, Title" | Policy 2419, Definitions, PDF p. 28 |
| 59 | `wv_case_mgmt` | Case management | personnel_role | "Case Management. The additional duties a special education teacher can be assigned for a group" | Policy 2419, Definitions, PDF p. 14 |
| 60 | `wv_close_supervision` | Close adult supervision | related_service | "Close Adult Supervision. The provision of staff to address the behavioral, academic, medical, health, safety," | Policy 2419, Definitions, PDF p. 14 |
| 61 | `wv_pep` | Personalized Education Plan | transition | "Personalized Education Plan (PEP) A plan developed to guide students and parents to thoughtfully explore" | Policy 2419, Definitions, PDF p. 23 |
| 62 | `wv_targeted_iep` | Targeted IEP review | iep_component | "Targeted IEP Review. May be conducted when only a portion of an IEP requires review" | Policy 2419, Definitions, PDF p. 30 |
| 63 | `wv_in_lieu` | IEP Team Member In-Lieu-of Attendance Report | iep_component | "provide IEP Team Member In-Lieu-of Attendance Report forms to the identified team member(s)." | Policy 2419, Ch. 5, § 1.D, PDF p. 76 |
| 64 | `wv_darf` | Disciplinary Action Review Form | discipline | "Disciplinary Action Review Form EC Eligibility Committee ECCAT Early Childhood Classroom Assistant Teacher EDEN Education" | Policy 2419, Acronyms and Abbreviations, PDF p. 10 |
| 65 | `expulsion` | Expulsion | discipline | "Expulsion. An action taken by the LEA removing a student from the student’s regular school" | Policy 2419, Definitions, PDF p. 17 |
| 66 | `wv_early_resolution` | Early resolution | legal_procedural | "Early resolution of state complaints Either the parent or the LEA may request early resolution" | Procedural Safeguards Notice (Aug. 2024), PDF p. 26 |
| 67 | `wv_ver_early_resolution` | Verification of Early Resolution | legal_procedural | "Verification of Early Resolution form, and the complaint is considered resolved. Allegations not resolved will" | Procedural Safeguards Notice (Aug. 2024), PDF p. 26 |
| 68 | `meeting_encourage_mediation` | Meeting to encourage mediation | legal_procedural | "meeting to encourage mediation, which is described in Part C of this section. The WVDE" | Policy 2419, Ch. 11, § 3.C, PDF p. 140 |
| 69 | `agreement_review_period` | Agreement review period | legal_procedural | "Agreement Review Period If the parent and the LEA enter into an agreement as a" | Procedural Safeguards Notice (Aug. 2024), PDF p. 32 |
| 70 | `attorneys_fees` | Attorneys' fees | legal_procedural | "the court, in its discretion, may award reasonable attorneys’ fees as part of the costs" | Procedural Safeguards Notice (Aug. 2024), PDF p. 36 |
| 71 | `civil_action` | Civil action | legal_procedural | "Civil actions, including the time period to file A party (the parent or the LEA)" | Procedural Safeguards Notice (Aug. 2024), PDF p. 35 |
| 72 | `destruction_pii` | Destruction of information | legal_procedural | "Destruction of Information Parents (or adult students) must be informed when personally identifiable information collected," | Procedural Safeguards Notice (Aug. 2024), PDF p. 20 |
| 73 | `public_benefits_consent` | Parental consent to access public benefits or insurance | legal_procedural | "PARENTAL CONSENT TO ACCESS PUBLIC BENEFITS OR INSURANCE (E.G, MEDICAID) This notice informs parents of" | Procedural Safeguards Notice (Aug. 2024), PDF p. 47 |
| 74 | `general_supervision` | General supervision | legal_procedural | "GENERAL SUPERVISION AND ACCOUNTABILITY FOR PERFORMANCE AND COMPLIANCE Section 1. General Supervision A. Responsibilities of" | Policy 2419, Ch. 9, § 1, PDF p. 117 |
| 75 | `spp` | State Performance Plan | legal_procedural | "State Performance Plan (SPP) for special education is developed, reviewed and/or revised, including performance goals" | Policy 2419, Ch. 9, § 1.B, PDF p. 120 |
| 76 | `apr` | Annual Performance Report | legal_procedural | "Annual Performance Report (APR) and IDEA, Section 618 reports. LEAs are given reasonable notice and" | Policy 2419, Ch. 9, § 1.B, PDF p. 120 |
| 77 | `intervener` | Intervener | personnel_role | "Intervener. A specially trained person who works consistently one-to-one with a student who is deafblind." | Policy 2419, Definitions, PDF p. 19 |
| 78 | `wv_esli` | Educational Sign Language Interpreter | personnel_role | "Educational Sign Language Interpreter. A paraprofessional meeting the requirements of W. Va. 126CSR136, Policy 5202," | Policy 2419, Definitions, PDF p. 16 |
| 79 | `wv_sign_support` | Sign Support Specialist | personnel_role | "Sign Support Specialist. A person employed to provide sign supported speech assistance to students (W.Va." | Policy 2419, Definitions, PDF p. 28 |
| 80 | `wv_eccat` | Early Childhood Classroom Assistant Teacher | personnel_role | "Early Childhood Classroom Assistant Teacher EDEN Education Data Exchange Network ELA English language arts ESSA" | Policy 2419, Acronyms and Abbreviations, PDF p. 10 |
| 81 | `aprn` | Advanced practice registered nurse | personnel_role | "advanced practice registered nurse (APRN), or physician’s assistant (PA) to determine a student's medically related" | Policy 2419, Definitions, PDF p. 20 |
| 82 | `physician_assistant` | Physician assistant | personnel_role | "or physician’s assistant (PA) to determine a student's medically related disability" | Policy 2419, Definitions, PDF p. 20 |
| 83 | `pre_ets` | Pre-employment transition services | transition | "Pre-Employment Transition Services (Pre-ETS). May include services provided by schools and by the West Virginia" | Policy 2419, Definitions, PDF p. 24 |
| 84 | `supported_employment` | Supported employment | transition | "Supported Employment. Paid work in the regular community work environment where persons without disabilities are" | Policy 2419, Definitions, PDF p. 30 |
| 85 | `hats` | Hearing assistive technology system | accommodation_modification | "(HATS) systems, curriculum accommodations, services, and other supports that are provided in general education classes" | Policy 2419, Ch. 5, § 2.G, PDF p. 81 |
| 86 | `cic` | Clean intermittent catheterization | related_service | "clean intermittent catheterization (CIC), recreation, including therapeutic recreation, counseling services, including rehabilitation counseling, orientation and" | Policy 2419, Definitions, PDF p. 26 |

## 3. Uncertainties

- **OCR.** All Policy 2419 wording is OCR. I corrected obvious slips by eye but did not compare every string to the page image. Words with hyphens, "§" and apostrophes are the most likely to be off.
- **Page numbers.** A few definitions run across two pages (for example TAAES, PDF p. 91 to 92). The table shows the page where the quoted words appear.
- **Candidate records.** The 15 `candidate` records come from the PSN only, not the rule: `wv_osp`, `wv_dfps`, `wv_advisory_council`, `wv_pti`, `wv_perc`, `wv_policy_2419`, `wv_policy_4350`, `wv_b8_survey`, `wv_early_resolution`, `wv_ver_early_resolution`, `agreement_review_period`, `attorneys_fees`, `civil_action`, `destruction_pii`, `public_benefits_consent`.
- **Categories.** The list has no clean category for several state items. Judgement calls: `wv_taaes` and `hats` as accommodation_modification; `wv_wvtss` as evaluation_eligibility; the assessment names (`wv_wvgsa`, `wv_alt_summative`, `wv_wvmap`) as iep_component; `wv_pep` and `wv_drs` as transition; `wv_close_supervision` as related_service; `wv_wvsdb` and `wv_sdt` as placement_setting.
- **Duplicates between states.** `wv_geft`, `wv_gept`, `wv_see` and `wv_separate_class` may overlap existing placement concepts such as regular class and special class. I kept them separate because Policy 2419 defines them as its own IEP placement choices.
- **Broader links.** Several `broader` links (for example `wv_osp` to `wv_wvde`) are my reading of how the offices relate.
- **Regional strings on existing concepts.** WV strings were added to existing concepts: PLEP (plaafp), SB-IEP (sb_iep), SAT (sst), MDET (mdt), EC (eligibility), "blindness and low vision" (vi), "emotional disorder" (ed), "exceptional gifted" (gifted), "speech sound disorder" (artic), SLPA (slp_assistant), among others. Whether each is a true synonym is for the audit.

## 4. Risky items

- **Acronyms that are ordinary words, names or brands:** SAT (a college-entrance test; here it is the Policy's abbreviation for the school team that refers students), EC, SEE, FLE, SPP, APR, DARF, PEP, CIC, HATS, CCRS (also used by Alabama; the build lists it as ambiguous across states), SLPA. The high-risk check passed for all of them, but each deserves a look.
- **Acronyms removed because tests flagged them:** GEE (a given name) and PA (Pennsylvania postal code). Neither is in the layer. The tests were not changed.
- **Place names:** 22 records carry the `place_name` risk flag because West Virginia is in the name (for example West Virginia Department of Education, Policy 2419, WV Birth to Three). The build marks these high risk by design. `wv_policy_2419` and `wv_aaas` also contain numbers.
- **Eponyms:** none added.
- **Names shared with other states:** "Office of Special Education" is used by New York, so the West Virginia record uses the full "West Virginia Office of Special Education". "General education environment" already belongs to Illinois, so West Virginia only attests it.
- **Policy numbers:** 2419, 4350 and 4373 are kept because the notice and rule use them as the names of the regulations. They look like numbers to a matcher.

## 5. Left out on purpose

Street address, phone numbers and web addresses of the Department; case-law names (Endrew F. v. Douglas County; Shaffer v. Weast); the test brand "SAT School Day" and the captioning brands C-Print and TypeWell; funding terms (high cost/high acuity); Board policy numbers other than 2419, 4350 and 4373 (2340, 2510, the 2520 series, 2525, 3300, 5202, 5500, 6200); the OHI conditions cancer, stroke, asthma, diabetes, heart condition, hemophilia, lead poisoning, leukemia, nephritis and rheumatic fever; medical specialists named in the eligibility criteria (ophthalmologist, optometrist, otologist, otolaryngologist, neurologist); the DSM-5 severity words (mild, moderate, severe, profound); the SLD cut-off numbers; staffing charts and class-size limits; the Level I, II and III service-need lists; the W. Va. Code sections on classroom video cameras; individual form names hosted by the Department; the acronyms GEE and PA (see section 4); and the placeholder key `exec_fn` (executive skills).

## Next

Run `prompts/audit-layer.md` in a fresh context, and name the model that did the research (`claude-sonnet-5-5`) in the PR.
