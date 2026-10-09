# Arkansas layer (v0.37.0): contributor report

Drafted 2026-10-08 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` should be run on it in a fresh conversation, ideally with a different model.

Result: the layer attests 158 concepts and adds 46 (17 machine_validated, 29 candidate). `build --check` passes and all 70 tests pass.

## 1. Documents read
- **RULE**: 6 CAR pt. 130, Subpart 2, Definitions, §§ 130-201 to 130-276 (`ADE_Spec._Ed._-_Definitions_6CARpt.130-Subpart2_Legal.pdf`, 33 pp.). Read in full. The page footer "03/11/2026 12:37:56 AM" is the date the copy was printed; the text has no effective date or history notes. Cited by section.
- **PSN**: "Arkansas Department of Education Procedural Safeguards Notice, Special Education Unit", titled inside "Part B Procedural Safeguards Notice" (`Procedural_Safeguards_Notice.pdf`, 47 pp.). Read in full. No date is printed; the PDF was created in September 2006 from a Word file. Apart from the header it is the 2006 U.S. Department of Education model notice. **It predates the 2008 federal rule on revoking consent and has no revocation text, and it gives 90 days to file a civil action.** Please check whether DESE has a newer notice; the process guide calls the notice "Your Rights Under IDEA". Cited by PDF page; printed page = PDF page - 3.
- **GUIDE**: Special Education Process Guide, DESE Special Education Unit, March 14, 2023 (`sped-process-guide.pdf`, 126 pp.). Read in full. Cited by PDF page; printed page = PDF page - 4.
- **Missing**: the other subparts of 6 CAR pt. 130 (procedures, discipline, dispute resolution), and the Special Education Eligibility Criteria and Program Guidelines for Children with Disabilities Ages 3-21, which hold Arkansas's category criteria. Adding these would let more terms be `machine_validated`.
- Every new string and preferred term was checked automatically against its cited section or page. Five attestations with no literal hit were checked by hand and are wording variants: `consent` (§ 130-212 defines "Consent"), `screening` ("Screening, for instructional purposes"), `pti` (plural "parent training and information centers", PSN p. 18), `mtss` ("multi-tiered intervention system", GUIDE p. 7) and `amendment` ("IEP amendments", GUIDE p. 53).

## 2. New concepts
Quotes are from the extracted text, 15 words or fewer.

| Key | Preferred term | Where it appears | Citation |
|---|---|---|---|
| `ar_ade` | Arkansas Department of Education | "Arkansas Department of Education Procedural Safeguards Notice" (page header) | PSN p. 1 |
| `ar_dese` | Arkansas Division of Elementary and Secondary Education | "supplement the Arkansas Division of Elementary and Secondary Education (DESE)" | GUIDE p. 2 |
| `ar_seu` | Special Education Unit of the Division of Elementary and Secondary Education | "psychometric standard established by the Special Education Unit of the Division..." | § 130-217 |
| `ar_psych_board` | Arkansas Psychology Board | "psychological examiner, licensed by the Arkansas Psychology Board" | § 130-254 |
| `ar_counsel_board` | Arkansas Board of Examiners in Counseling | "licensed by the Arkansas Board of Examiners in Counseling" | § 130-254 |
| `ar_slp_board` | Board of Examiners in Speech-Language Pathology and Audiology | "licensed by the Board of Examiners in Speech-Language Pathology and Audiology" | § 130-254 |
| `ar_esvi` | Educational Services for the Visually Impaired | "accessed from Educational Services for the Visually Impaired (ESVI)" | GUIDE p. 58 |
| `ar_ideas` | ArkansasIDEAS | "additional supports available through ArkansasIDEAS (Log in, Find Learning..." | GUIDE p. 58 |
| `ar_ats` | Arkansas Transition Services | "Transition Resources: Arkansas Transition Services" | GUIDE p. 103 |
| `ar_ida_office` | IDEA Data and Research Office | "mail the paper surveys to the IDEA Data and Research Office" | GUIDE p. 75 |
| `ar_abc` | Arkansas Better Chance | "all licensed Head Start and Arkansas Better Chance (ABC) programs" | GUIDE p. 86 |
| `ar_combo_rs` | Combination resource services/special class services | section heading | § 130-210 |
| `ar_combo_sr` | Combination special class services/resource services | section heading | § 130-211 |
| `ar_integrated` | Integrated classroom | section heading | § 130-233 |
| `ar_day_treatment` | School-based day treatment services | section heading | § 130-259 |
| `ar_instr_day` | Instructional day | section heading | § 130-240 |
| `ar_edu_examiner` | Educational examiner | "The educational examiner, licensed by the SEA, who may administer" | § 130-254 |
| `ar_school_psych_spec` | School psychology specialist | "The school psychology specialist, licensed by the SEA" | § 130-254 |
| `ar_psych_examiner` | Psychological examiner | "The psychological examiner, licensed by the Arkansas Psychology Board" | § 130-254 |
| `ar_student_evaluator` | Student evaluator | "The student evaluator who is either practicing as an intern" | § 130-254 |
| `edu_interpreter` | Educational interpreter (national) | section heading | § 130-221 |
| `dbps` | Data-based problem solving (national) | section heading "Data-based problem solving - Functional assessment" | § 130-214 |
| `core_acad` | Core academic subjects (national) | section heading | § 130-213 |
| `sbr` | Scientifically based research (national) | section heading | § 130-260 |
| `record_access` | Record of access (national) | "RECORD OF ACCESS 34 CFR §300.614" | PSN p. 14 |
| `child_outcomes` | Early Childhood Outcomes (national) | "EC2. Early Childhood Outcomes" | GUIDE p. 88 |
| `act_aspire` | ACT Aspire (national) | "statewide assessment for grades three through ten is the ACT Aspire" | GUIDE p. 71 |
| `nsttac` | National Secondary Transition Technical Assistance Center (national) | "The National Secondary Transition Technical Assistance Center (NSTTAC) developed" | GUIDE p. 103 |
| `i13_checklist` | Indicator 13 Checklist (national) | "Indicator 13 Checklist - The National Secondary Transition Technical Assistance Center" | GUIDE p. 103 |
| `ar_notice_conf` | Notice of Conference | "The Notice of Conference is used by the LEA" | GUIDE p. 15 |
| `ar_referral_conf` | Referral conference | "the referral conference, which must be held within 21 calendar days" | GUIDE p. 12 |
| `ar_epc` | Evaluation/Programming Conference | "The Evaluation/Programming Conference Decision Form/Notice of Decision documents the conclusions" | GUIDE p. 11 |
| `ar_sld_form` | Specific Learning Disability Eligibility Determination form | "the Specific Learning Disability Eligibility Determination form will also be completed" | GUIDE p. 33 |
| `ar_temp_iep` | Temporary IEP | "A temporary IEP must include specific conditions and timelines" | GUIDE p. 52 |
| `ar_sched_services` | Schedule of Services | "The Schedule of Services is used to document the Special Education Services" | GUIDE p. 66 |
| `ar_seecp` | Special Education Early Childhood Program | "Special Education Early Childhood Program (<49% of children in program...)" | GUIDE p. 92 |
| `ar_ecse_k` | Early Childhood Special Education to Kindergarten Transition Process | section heading "EC5." | GUIDE p. 95 |
| `ar_pao` | Public Agency Official | "The Public Agency Official receiving the referral should be noted" | GUIDE p. 14 |
| `ar_aas` | Arkansas Academic Standards | "must be knowledgeable in the Arkansas Academic Standards" | GUIDE p. 61 |
| `ar_elp_std` | Arkansas English Language Proficiency standards | "knowledgeable in the Arkansas English Language Proficiency standards" | GUIDE p. 61 |
| `ar_cdels` | Arkansas Child Development and Early Learning Standards | "Arkansas Child Development and Early Learning Standards (AR CDELS), released in April" | GUIDE p. 86 |
| `ar_rti` | RTI Arkansas | "a multi-tiered intervention system (e.g., RTI Arkansas)" | GUIDE p. 7 |
| `ar_dys_guide` | Dyslexia Resource Guide | "The initial screening described in the Dyslexia Resource Guide" | GUIDE p. 7 |
| `ar_sld_tam` | Arkansas Technical Assistance Manual: Identification of Children with Specific Learning Disabilities | "The Arkansas Technical Assistance Manual: Identification of Children with..." | GUIDE p. 36 |
| `ar_aa_manual` | Arkansas Alternate Assessment Participation Manual | "IEP team should use the Arkansas Alternate Assessment Participation Manual" | GUIDE p. 72 |
| `ar_alt_pathway` | Alternate Pathway to Graduation | "The Alternate Pathway to Graduation is intended to positively affect" | GUIDE p. 73 |

New strings on existing concepts (tagged US-AR unless noted): "Notice of Action" (`pwn`), "Your Rights Under IDEA" and "Part B Procedural Safeguards Notice" (untagged) (`safeguards_notice`), "consulting teacher" (`consult_teacher`), "resource services" (`resource_room`), "special class services" (`special_class`), "special day school, public", "special day school, private" and "Special Day School" (`special_school`), "co-taught services" (`coteach`), "Residential School" (`residential`), "Hospital Program" (`hospital_instr`), "Existing Data Review" and "EDR" (`reed`), "LPAC" (`lpac`), "Special Education Supervisor" and "Special Education Director" (`sped_admin`), "early intervening services" (untagged, `ceis`).

## 3. Unsure
- **Other states' concepts attested from Arkansas.** `nh_qual_examiner` (New Hampshire) is attested from § 130-254 and is the broader concept of `ar_edu_examiner`; `nc_recp` (North Carolina) from GUIDE p. 92; `lpac` (Texas) gets "LPAC" tagged US-AR. Earlier layers have done the same (five cases). An alternative is a national "Qualified examiner" concept; that needs a key decision by a maintainer.
- **LPAC is not spelled out** in the guide (GUIDE pp. 22, 59). It's used for English learners, as in Texas, but the meaning is inferred.
- **`special_school`** now carries both "special day school, public" and "special day school, private". The private one could instead belong under `nps` (California's nonpublic school concept).
- **`consult_teacher`** gets "consulting teacher" from § 130-232, which names the person who gives indirect services. The concept was built from New York's "consultant teacher services".
- **National or Arkansas-only:** `ar_instr_day`, `ar_psych_examiner` and `ar_student_evaluator` are marked Arkansas-only because the definitions are Arkansas's, but the terms are used elsewhere. `dbps`, `edu_interpreter`, `core_acad` (from NCLB) and `sbr` (from NCLB) are national.
- **`ar_epc`** is a conference and its decision form ("Evaluation/Programming Conference Decision Form/Notice of Decision"). Category `evaluation_eligibility`.
- **`ar_ats`**: the guide uses "ATS" ("Check out the ATS calendar", p. 101) but never spells it out, so the acronym was not added.
- **`child_outcomes`**: the guide writes "Early Childhood Outcomes Process (COS)" (p. 85). COS normally stands for Child Outcomes Summary, so "COS" was not added.
- **Age of majority** is 18 in the guide; the rule subpart provided doesn't say.

## 4. Risky
- **Place names:** every term starting with "Arkansas", plus "RTI Arkansas", is auto-flagged `place_name` (12 high-risk records).
- **Name-list hits:** "Arkansas Better Chance" (Chance as a first name and surname); "Day" in `ar_day_treatment` and `ar_instr_day`; "Early" in four early childhood terms; "English" in `ar_elp_std`. All are full phrases.
- **Ambiguous acronyms:** "DESE" now means three agencies (Massachusetts, Missouri, Arkansas), each tagged; the build lists it as an allowed cross-state ambiguity. "ABC" (tagged US-AR) is a very common acronym. "EDR" and "LPAC" are tagged US-AR.
- **Brand name:** `act_aspire` is a commercial test from ACT. It's included because it is the state's general assessment, as `access_ell` and `msaa` are.

## 5. Left out
- Every person named in the guide (the task force list on GUIDE p. 2) and the districts, cooperatives and advocacy groups they're listed with.
- Two-letter placement codes (RG, RR, SC, HM, IO, A1 and the like). Several are postal codes or common words.
- Test products given as examples (GUIDE p. 88) and links to outside sites.
- "PBS" (§ 130-253), which has common other meanings; the full term is attested on `pbis`.
- "Administrative case management" (§ 130-202): the string already belongs to the New Hampshire concept `nh_admin_case_mgmt`, which means scheduling and coordination, while Arkansas's definition is about buying record-keeping technology. Needs a maintainer decision.
- "DESE-SEU", "ADE-SEU", "EPC" and the variant "Evaluation Programming Conference": the build only takes a concept's strings from one cited page, and these appear on other pages than the preferred term. They can be added as STRINGS entries in a later version.
- Easter Seals Outreach, ArKids, Agency Connections, Transition Consultant, Parent Survey and the Consent to Access Public Insurance form, which the guide mentions only in passing.
