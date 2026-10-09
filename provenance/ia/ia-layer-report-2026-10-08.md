# Iowa layer (v0.41.0): contributor report

Drafted 2026-10-08 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` should be run on it in a fresh conversation, ideally with a different model. Build: `python -m spedlex.build --check` passes and `pytest -q` passes (78 tests). The layer attests 271 concepts and adds 58 (31 machine_validated, 27 candidate). There are no string conflicts. Two new cross-state ambiguities are allowed: ECI (TX/IA) and IDOE (IN/IA).

## 1. Documents read
- **RULE**: 281 IAC chapter 41, Special Education, saved from the Iowa Legislature's site as `.sources-cache/ia/IA-281-IAC-41-Dec-2025.pdf` (108 pp.; IAC printed 12/10/25; includes ARC 9811C and 9812C, effective 1/14/26). Read in full. pdfinfo reports minor syntax errors in the PDF, but the text extracted cleanly. Its printed page "Ch 41, p.N" equals PDF page N. Citations are by rule or subrule.
- **PSN**: Iowa DE, *Procedural Safeguards Manual: Rights of Parents of Students with Disabilities Ages 3-21* (August 2023, 50 pp.). Read in full. Cited by PDF page, which is the printed page number + 6.
- **GUIDE**: *Special Education Terms and Acronyms, Ages 3-21* (7 pp.), hosted on educate.iowa.gov. **No publisher or date is printed**; the PDF was created Feb. 18, 2021. The two-column table extracts out of order, so each term was paired with its acronym by reading the row order on the page.
- **Missing**: there is no main parent guide or IEP manual, so the terms sheet stands in for it. Iowa's IEP guidance, its eligibility standards, alternate assessment (DLM) pages and diploma guidance were not read.
- All text came from `pdftotext`. A script checked every new string against its cited subrule or page. The cases with no literal hit were checked by hand:
  - Attestations worded differently, e.g. "continuum of alternative services and placements" (`continuum`), "persons with print disabilities" (`print_disability`), "“final” versus “draft” IEPs" (`draft_iep`), "teacher with an endorsement to teach individuals who are blind or visually impaired" (`tvi`).
  - The cross-reference rule 41.123 ("281—41.611 to 41.626") prints the 41.611 definitions without the heading pattern the script looked for. Those definitions were read directly.
  - Strings verbatim elsewhere in the rule but not in the cited subrule: "area education agencies (AEAs)" at 41.2(1); "eligible individuals" throughout; "special education instructional/support services" at 41.412. The `ia_aea`, `ia_eligible_individual`, `ia_instr_svc` and `ia_support_svc` records cite the defining rule.
  - Descriptive preferred terms not printed in the documents, which are used to keep terms unique: "Iowa Department of Human Services" (the guide says "Department of Human Services") and "Iowa Early ACCESS".

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer) | Citation |
|---|---|---|---|
| `ia_doe` | Iowa Department of Education | "Iowa Department of Education IDOE/IDE/DE The education agency in the state of Iowa." | GUIDE p. 5 |
| `ia_dlr` | Division of Learning and Results | "Iowa Department of Education (Department) Division of Learning and Results" | PSN p. 8 |
| `ia_blss` | Bureau of Learner Strategies and Supports | "Division of Learning and Results Bureau of Learner Strategies and Supports" | PSN p. 8 |
| `ia_aea` | Area education agency | "“Area education agency” or “AEA” is a political subdivision of the state" | 41.4 |
| `ia_boee` | Board of Educational Examiners | "shall meet the board of educational examiners’ licensure (certification) and endorsement" | 41.401 |
| `ia_iac` | Iowa Administrative Code | "Iowa Administrative Code IAC" | GUIDE p. 5 |
| `ia_rules` | Iowa Administrative Rules of Special Education | "the Individuals with Disabilities Education Act (IDEA) and the Iowa Administrative Rules of Special Education" | PSN p. 7 |
| `ia_ask` | ASK Resource Center | "Iowa Parent Training and Information Center, ASK Resource Center" | PSN p. 7 |
| `ia_dri` | Disability Rights Iowa | "In Iowa, that is Disability Rights Iowa (DRI)." | PSN p. 8 |
| `ia_fep` | Family & Educator Partnership | "The AEA’s Family & Educator Partnership (FEP) program" | PSN p. 7 |
| `ia_i3` | Iowa IDEA Information | "Iowa IDEA Information … i3 An online and accessible platform for procedures" | GUIDE p. 5 |
| `ia_ivrs` | Iowa Vocational Rehabilitation Services | "IVRS Iowa’s state vocational rehabilitation program" | GUIDE p. 5 |
| `ia_tap` | Transition Alliance Program | "Transition Alliance Program TAP A partnership between the LEA and IVRS" | GUIDE p. 7 |
| `ia_dhs` | Iowa Department of Human Services | "Iowa’s agency that provides public assistance programs … Department of Human Services DHS" | GUIDE p. 2 |
| `ia_hhs` | Iowa Department of Health and Human Services | "the early hearing detection and intervention program in the Iowa department of health and human services" | 41.329(1) |
| `ia_idph` | Iowa Department of Public Health | "IDPH … Iowa Department of Public Health" | GUIDE p. 5 |
| `ia_chsc` | Child Health Specialty Clinics | "Child Health Specialty Clinics A community-based public health agency" | GUIDE p. 2 |
| `ia_dcch` | Division of Child and Community Health | "DCCH A division of the Carver College of Medicine" | GUIDE p. 3 |
| `ia_isd` | Iowa School for the Deaf | "The department, in consultation with the Iowa school for the deaf" | 41.329 |
| `ia_early_access` | Iowa Early ACCESS | "Early ACCESS EA Iowa’s system for providing early intervention services" | GUIDE p. 3 |
| `ia_eci` | Early Childhood Iowa | "Early Childhood Iowa ECI Programs across the state" | GUIDE p. 3 |
| `ia_swvpp` | Statewide Voluntary Preschool Program | "Statewide Voluntary Preschool Programs … SWVPP A preschool program available to Iowa residents" | GUIDE p. 7 |
| `ia_fsmp` | Family support mentoring program | "guidelines for a comprehensive family support mentoring program" | 41.329 |
| `ia_eligible_individual` | Eligible individual | "this term is synonymous with “child requiring special education” and “eligible individual.”" | 41.8 |
| `ia_dioe` | Disability in obtaining an education | "“Disability in obtaining an education” refers to a condition" | 41.8 |
| `ia_spm` | Systematic progress monitoring | "“Systematic progress monitoring” means a systematic procedure for collecting and displaying" | 41.51(15) |
| `ia_trial_placement` | Trial placement | "an eligible individual may be provided a trial placement in the general education setting" | 41.116(7) |
| `ia_classroom_clearance` | Classroom clearance | "Clearing classrooms. An IEP or a behavioral intervention plan shall not include" | 41.320(7) |
| `ia_accredited_np` | Accredited nonpublic school | "Additional rules relating to accredited nonpublic schools." | 41.413 |
| `ia_instr_svc` | Special education instructional services | "Instructional services are the specially designed instruction and accommodations" | 41.408(1) |
| `ia_delivery_system` | Delivery system for instructional services | "for creating a delivery system for instructional services" | 41.408(1) |
| `ia_support_svc` | Special education support services | "Support services are the specially designed instruction and activities that augment" | 41.409 |
| `multicat` | Multicategorical | "“Multicategorical” means special education in which the individuals … have different types of disabilities" | 41.51(11) |
| `ia_asst_director` | Assistant director of special education | "“Assistant director of special education” provides specific areawide administrative" | 41.402(3) |
| `ia_sped_consultant` | Special education consultant | "These services include special education consultant services, educational strategist services" | 41.409 |
| `ia_ed_strategist` | Educational strategist | "“Educational strategist” provides assistance to general education classroom teachers" | 41.402(3) |
| `ia_media_specialist` | Special education media specialist | "“Special education media specialist” is a media specialist" | 41.402(3) |
| `ia_sped_nurse` | Special education nurse | "“Special education nurse” is a professional registered nurse" | 41.402(3) |
| `ia_wec` | Work experience coordinator | "“Work experience coordinator” plans and implements sequential secondary programs" | 41.402(3) |
| `ia_psych_asst` | Psychology assistant | "“Psychology assistant” collects screening data through records review" | 41.403(2) |
| `ia_vision_asst` | Vision assistant | "“Vision assistant” provides materials in the appropriate medium" | 41.403(2) |
| `audiologist` | Audiologist | "“Audiologist” applies principles, methods and procedures for analysis of hearing functioning" | 41.402(3) |
| `occ_therapist` | Occupational therapist | "“Occupational therapist” is a licensed health professional" | 41.402(3) |
| `phys_therapist` | Physical therapist | "“Physical therapist” is a licensed health professional" | 41.402(3) |
| `speech_path` | Speech-language pathologist | "Speech Language Pathologist … SLP An expert in communication" | GUIDE p. 7 |
| `audiometrist` | Audiometrist | "“Audiometrist” provides hearing screening and other specific hearing-related activities" | 41.403(2) |
| `ot_assistant` | Occupational therapy assistant | "“Occupational therapy assistant” is licensed to perform occupational therapy procedures" | 41.403(2) |
| `pt_assistant` | Physical therapist assistant | "“Physical therapist assistant” is licensed to perform physical therapy procedures" | 41.403(2) |
| `slp_assistant` | Speech-language pathology assistant | "“Speech-language pathology assistant” provides certain language, articulation, voice and fluency activities" | 41.403(2) |
| `ehdi` | Early hearing detection and intervention program | "children identified through the early hearing detection and intervention program" | 41.329(1) |
| `cil` | Center for independent living | "Centers for Independent Living (CILs) Centers for Independent Living provide independent living supports" | PSN p. 9 |
| `aac` | Augmentative and alternative communication | "Augmentative and Alternative Communication AAC A means of communicating ideas" | GUIDE p. 1 |
| `cyshcn` | Children and youth with special health care needs | "Children and Youth with Special Health Care Needs … CYSHCN" | GUIDE p. 2 |
| `ihp` | Individual health plan | "IHP A document that outlines necessary services to address a student's health needs" | GUIDE p. 5 |
| `dyscalculia` | Dyscalculia | "Dyscalculia (math issues)" | GUIDE p. 5 |
| `ia_med_form` | Model Form: Request for Mediation | "Model Form: Request for Mediation" | PSN p. 45 |
| `ia_dp_form` | Model Form: Due Process Complaint (Request for Due Process Hearing) | same title | PSN p. 47 |
| `ia_sc_form` | Model Form: IDEA State Complaint | "Model Form: IDEA State Complaint" | PSN p. 49 |

The 15 national concepts (from `multicat` through `dyscalculia`) have no `jurisdiction`. Iowa's documents happen to be the first to attest them.

New strings on existing concepts, tagged US-IA unless noted:
- "behavior disorder" (41.50(2)), "BD", "emotional disorder" and "emotional disability" (GUIDE) on `ed`
- "head injury" on `tbi` (defined separately at 41.51(10) with the same wording as TBI)
- "special physical education" on `pe`
- "AEA director of special education" and "special education coordinator" on `sped_admin`
- "school district of the child's residence" and "district of residence of the child" on `resident_dist`
- "certificate of completion" on `cert_completion`
- "preappeal conference" (legacy, 41.506(5)) and "special education mediation conference" on `mediation`
- "request for due process hearing" on `dp_complaint`
- "Iowa Special Education Advisory Panel" on `state_panel`
- "Procedural Safeguards Manual" on `safeguards_notice`
- "AIM" and "AEM" on `nimas`
- "Child Outcome Summary Process", "COS" and "ECO" on `child_outcomes`
- "Disability Suspect" on `suspected`
- "Educational Evaluation Report" and "EER" on `eval_report`
- "ESYS" on `esy`
- "postsecondary expectations" and "PSE" on `postsecondary`
- "Postsecondary Summary", "PSS", "Student Accommodation Request" (legacy) and "SAR" on `sop`

Untagged: "general equivalency diploma" (`ged`), "accessible educational materials" (`nimas`), "para-educator" (`para`), "teacher of the visually impaired" (`tvi`), "Sp.Ed." (`special_ed`), "transfer of rights" (`age_majority`), and "speech language pathologist" and "SLP" (`speech_path`).

## 3. Unsure
- **`nc_sps` attested, not duplicated.** Iowa's 41.313 "Systematic problem-solving process" has the same name and purpose as North Carolina's concept, so Iowa attests it. That concept carries `jurisdiction: US-NC`. A reviewer may prefer a national parent concept.
- **Early ACCESS.** Colorado's untagged preferred term "Early Access" (gifted early entrance) blocks a normal string. "Early ACCESS" is therefore recorded as type `A` (case-sensitive), tagged US-IA, under the preferred term "Iowa Early ACCESS". It is not really an acronym; this is a judgment call.
- **DHS, HHS and IDPH are kept as three concepts.** The guide and the safeguards manual name the "Department of Human Services" and the "Iowa Department of Public Health". The 2025 rule names the "Iowa department of health and human services". These may now be one agency, but none of the documents says so, so they were not merged.
- **"head injury" on `tbi`.** The rule defines it separately (41.51(10)) with TBI's wording. It is recorded as a synonym, not a legacy term.
- **"special education coordinator" on `sped_admin`.** In Iowa this means an area-level role (41.402(3)). It merges with Delaware's tagged string.
- **Guide page pairing.** The table extracts out of order, so the acronym-to-term pairings were read from row order. Check DHS, IDPH, IHP, PSE and DS against the PDF.
- **Category choices**: `ihp` as `iep_component`; `ia_chsc` and `ia_dcch` as `health_condition` (agencies, but health-focused); `ia_fsmp` as `early_intervention`.

## 4. Risky
- **Ambiguous acronyms (tagged US-IA, allowed by the build):**
  - ECI (Texas: Early Childhood Intervention) and IDOE (Indiana: Department of Education).
  - EI = "eligible individual" in Iowa, but early intervention almost everywhere else.
  - DHS (also Homeland Security), TAP, SAR, PSS, PSE, BD, EA, AIM, AEM, i3, DRI.
  - DRI is not used by Disability Rights Idaho's record, but it is the same initials.
- **Place names:** the build auto-flags 12 records high-risk because they contain "Iowa" (`place_name`): agencies, the school for the deaf, Early Childhood Iowa and Iowa Early ACCESS. This is expected for state names.
- **No new all-caps or postal-code collisions:** `tests/test_match.py` passes unchanged. "DE" was deliberately not added (Delaware's postal code).
- **No eponyms added.** Grant Wood AEA (named for a person) was excluded along with the other AEA names.

## 5. Left out on purpose
- **Local agencies and places:** the nine individual AEAs (Keystone, Central Rivers, Prairie Lakes, Mississippi Bend, Grant Wood, Heartland, Green Hills, Great Prairie, Northwest) and the individual Centers for Independent Living, all named for places. All addresses, phone numbers, URLs and the one personal email address in the manual were also left out.
- **Two-letter acronyms with common other meanings:** EC, EL, DS and HS. "DE" is a postal code.
- **General programs defined in passing:** CDC, WIC and HIPAA.
- **The special education weighting plan, "weighted enrollment" and the levels of service (Level I-III, 41.907(9)):** these are funding formulas, which the procedure excludes. "Level I"/"Level II" are also Virginia strings.
- **"child requiring special education" (41.8):** already an untagged preferred term of Connecticut's `ct_child_req_sped`, so adding it would conflict.
- **"instructional services" alone:** it is Michigan's untagged preferred term.
- **"Iowa Parent Training and Information Center" as a string:** the manual uses it as a description of ASK, not a name.
- **Federal boilerplate with no Iowa-specific wording** (maintenance of effort, excess-cost and disproportionality calculations): not given strings.
- **Others:** "integrated school setting", "open enrollment", "severely disabled", "Agreement to Mediate", "Notice of Reevaluation", "Parental Safeguard Manual" (a one-off variant of the manual's title), "certificate of attendance", and the out-of-state placement provisions.

Remember to name the model (Claude Opus 5.5, `claude-opus-5-5`) in the pull request.
