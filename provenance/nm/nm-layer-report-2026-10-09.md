# New Mexico layer (v0.44.0): contributor report

Drafted 2026-10-09 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` v1.2. A person must review this before it is submitted. `prompts/audit-layer.md` has **not** been run; run it in a fresh conversation, ideally with a different model. Build: `python -m spedlex.build --check` passes and `pytest -q` passes (84 tests). The layer attests 245 concepts and adds 47 (13 machine_validated, 34 candidate; 45 New Mexico-specific). There are no string conflicts. It adds two new cross-state acronym ambiguities, **SED** (US-NY, US-NM) and **DVR** (US-DE, US-NM).

## 1. Documents read

See `nm-sources-2026-10-09.md`. Each PDF was saved from the agency's site through the browser and read in full as `pdftotext` output. No fetch tool summarized or converted any of them.

- **RULE**: 6.31.2 NMAC, Children with Disabilities (eff. 7/14/2020, amended 7/31/2023), State Records Center PDF, 40 pp. PDF page = printed page. Cited as section and paragraph plus page, e.g. `6.31.2.7(B)(18), p. 3`.
- **PSN**: NMPED Special Education Procedural Safeguards (rev. December 2020), 35 pp. This is mostly the federal model notice plus New Mexico additions (FIEP, CYFD, wards of the state, resources list). Cited by **PDF page**; the printed page number is one lower.
- **GUIDE**: *Developing Quality IEPs* (NMPED Special Education Bureau, rev. October 2011), 127 pp. Cited by **PDF page**; the printed "Page N" is five lower. PDF pages 2–3 and 72–83 have no text layer (blank or image-only form pages), so I did not read them. Pages 72–83 probably hold the SLD determination form and the state IEP form images. The manual is from 2011, so several terms are legacy (see §3).
- **GRAD** (optional diploma document): *High School Graduation Requirements Guidance* (NMPED, April 2025; file posted August 2026), 47 pp. Cited by PDF page. I read pages 1–26 in full. For the course-catalog appendices (PDF pp. 27–47) I only **searched** for special-education wording; I did not read them line by line.
- **Missing or not used**: The NM TEAM manual (2026 revision, 496 pp.) was downloaded to `.sources-cache/nm/` but not read. Its evaluation and eligibility terms are not in this layer and should go in a later `new_mexico_supplement`. I found no separate parent guide; the GUIDE is the IEP manual.
- **Check**: a script tested whether each record's wording appears on its cited page. 42 records had no literal hit, and I checked all of them by hand. Most were wording differences, such as `cop` ("disciplinary changes of placement"), `prefs` ("strengths, preferences, and interests"), `psych` ("psychological service") and `primary_disability` ("primary (and if applicable, secondary) disability"). Others were phrases broken across the PSN's two columns or across a page break, such as `cceis`, which starts on rule p. 8 and ends on p. 9. As a result of this check, two form citations were moved from GUIDE p. 20 to p. 21.

## 2. New concepts

| Key | Term | Quote (≤15 words) | Citation |
|---|---|---|---|
| `nm_ped` | New Mexico Public Education Department | "see the information on the Public Education Department (PED) website" | PSN p. 2 |
| `nm_sed` | PED Special Education Division | "mail or fax the written request to the PED Special Education Division" | PSN p. 20 |
| `nm_cyfd` | Children, Youth and Families Department | "the Children, Youth and Families Department (CYFD)" | PSN p. 7 |
| `nm_nmac` | New Mexico Administrative Code | "“NMAC” means the New Mexico administrative code, including future amendments." | Rule 6.31.2.7(B)(13), p. 3 |
| `nm_6312` | 6.31.2 NMAC | "[6.31.2.1 NMAC - Rp, 6.31.2.1 NMAC, 7/14/2020]" | Rule 6.31.2.1, p. 1 |
| `nm_dhh_bor` | NM Deaf/Hard of Hearing Education Bill of Rights | "the NM Deaf/Hard of Hearing Education Bill of Rights (28 -11C-3)" | GUIDE p. 93 |
| `nm_stars` | STARS | "a required STARS data field in the Special Ed Events Template" | GUIDE p. 93 |
| `nm_dvr` | New Mexico Division of Vocational Rehabilitation | "if the New Mexico Division of Vocational Rehabilitation is going to provide transition services" | PSN p. 31 |
| `nm_pro` | Parents Reaching Out | "Parents Reaching Out (PRO)" | PSN p. 35 |
| `nm_epics` | Education for Parents of Indian Children with Special Needs | "Education for Parents of Indian Children with Special Needs (EPICS)" | PSN p. 35 |
| `nm_families_asap` | Families ASAP | "Families ASAP: Phone 1-855-484-0144" | PSN p. 35 |
| `nm_drnm` | Disability Rights New Mexico | "Disability Rights New Mexico (DRNM)" | PSN p. 35 |
| `nm_nadlc` | Native American Disability Law Center | "Native American Disability Law Center (NADLC)" | PSN p. 35 |
| `educational_decision_maker` | Educational decision-maker | "the State District Court Judge is required to appoint an educational decision-maker" | PSN p. 7 |
| `nm_ed_jurisdiction` | Educational jurisdiction | "The “educational jurisdiction” of a public agency includes the geographic area, age range" | Rule 6.31.2.7(B)(6), p. 2 |
| `nm_ssep` | State-supported educational program | "A “state-supported educational program” means a publicly-funded program that:" | Rule 6.31.2.7(B)(21), p. 4 |
| `nm_nmsd` | New Mexico School for the Deaf | "Children at the New Mexico School for the Deaf (NMSD)." | Rule 6.31.2.11(K), p. 21 |
| `nm_nmsbvi` | New Mexico School for the Blind and Visually Impaired | "Children at the New Mexico school for the blind and visually impaired (NMSBVI)." | Rule 6.31.2.11(L), p. 22 |
| `dual_discrepancy` | Dual discrepancy | "“Dual discrepancy” means the child does not achieve adequately" | Rule 6.31.2.7(B)(4), p. 2 |
| `nm_team` | New Mexico Technical Evaluation and Assessment Manual | "the New Mexico technical evaluation and assessment manual (New Mexico T.E.A.M.)" | Rule 6.31.2.10(G)(1), p. 11 |
| `nm_sfe` | New Mexico Standards for Excellence | "grade-level standards established in New Mexico standards for excellence" | Rule 6.31.2.7(B)(4), p. 2 |
| `nm_eps` | Expanded performance standards | "the expanded performance standards for students with significant cognitive disabilities" | Rule 6.31.2.11(D)(2), p. 18 |
| `nm_student_profile` | Student profile | "The Student Profile is a summary of what the IEP team currently knows" | GUIDE p. 34 |
| `nm_level_service` | Level of service | "recording the level of service (hours the student is receiving special education service)" | GUIDE p. 58 |
| `nm_continuing_iep` | Continuing or transition IEP | "a conditional certificate of transition in the form of a continuing or transition IEP" | GUIDE p. 45 |
| `nm_comm_considerations` | Addendum for Students who are Deaf or Hard of Hearing | "Addendum for Students who are Deaf or Hard of Hearing / Communication Considerations" | GUIDE p. 93 |
| `nm_esy_addendum` | Addendum for Determining Eligibility for Extended School Year Services | "the Addendum for Determining Eligibility for Extended School Year Services" | GUIDE p. 53 |
| `nm_nmaa` | New Mexico Alternate Assessment | "the student must meet eligibility criteria for New Mexico Alternate Assessment" | GUIDE p. 54 |
| `nm_aa_addendum` | Addendum for Determining Eligibility for the New Mexico Alternate Assessment | "the Addendum for Determining Eligibility for the New Mexico Alternate Assessment" | GUIDE p. 54 |
| `nm_prq` | Parent Report Questionnaire | "their answers to a Parent Report Questionnaire (Appendix A-5)" | GUIDE p. 24 |
| `nm_consent_form` | Parent Consent Form for Educational Evaluation | "Appendix A, Form 1: Parent Consent Form for Educational Evaluation" | GUIDE p. 20 |
| `nm_pwn_meeting` | Prior Written Notice of IEP Meeting | "Appendix A, Form 4: Prior Written Notice of IEP Meeting" | GUIDE p. 23 |
| `nm_elig_form` | Determination of Eligibility for Special Education Services | "Appendix A, Form 2: Determination of Eligibility for Special Education Services" | GUIDE p. 21 |
| `nm_sld_form` | Determining the Existence of a Specific Learning Disability | "Appendix A, Form 3: Determining the Existence of a Specific Learning Disability" | GUIDE p. 21 |
| `nm_student_bor` | Student Bill of Rights | "Appendix C / Student Bill of Rights" | GUIDE p. 125 |
| `nm_lifespan` | Life Span Transition Planning | "Life Span Transition planning for students in preschool and elementary grades" | GUIDE p. 47 |
| `nm_nsp` | Next-Step Plan | "the requirement for high school students to create Next-Step Plans" | GRAD p. 14 |
| `nm_diploma` | New Mexico Diploma of Excellence | "SECTION 1: NEW MEXICO DIPLOMA OF EXCELLENCE" | GRAD p. 6 |
| `nm_std_pos` | Standard program of study | "the requirements to obtain a diploma through the standard program of study" | Rule 6.31.2.11(G)(1)(d), p. 19 |
| `nm_ability_pos` | Ability program of study | "Students with disabilities that obtain a diploma through the Ability Program of Study" | GRAD p. 19 |
| `nm_modified_pos` | Modified program of study | "diploma obtained through the modified and ability programs of study" | Rule 6.31.2.11(G)(1)(c), p. 19 |
| `nm_career_pos` | Career Readiness Alternative Graduation Option | "Career Readiness Alternative Graduation Option: A career readiness program" | GUIDE p. 45 |
| `nm_cct` | Conditional certificate of transition | "Prior to the student’s receipt of a conditional certificate of transition" | Rule 6.31.2.11(G)(1)(d), p. 19 |
| `nm_doc` | Demonstration of competency | "Removal of Graduation Demonstrations of Competency" | GRAD p. 6 |
| `nm_nmge` | New Mexico Graduation Exam | "performance on the New Mexico Graduation Exam" | GUIDE p. 45 |
| `nm_sba` | Standards-Based Assessment | "Standards-Based Assessment (SBA) Spanish Reading" | GRAD p. 17 |
| `nm_asr` | New Mexico Assessment of Science Readiness | "New Mexico Assessment of Science Readiness (NM-ASR), Grade 11" | GRAD p. 17 |

**New strings on existing concepts** (tag US-NM unless noted):
- "SAT" on `sst`, from rule p. 3 and PSN p. 11. It was already a West Virginia string; the build merged the tags.
- "multi-layered system of supports" and "MLSS" on `mtss`.
- "FIEP meeting" on `iep_facil`.
- "state-level complaint" on `state_complaint`.
- "individual family services plan" on `ifsp`.
- "staff-to-student ratio" on `staff_ratio`.
- "Common Core Standards", "New Mexico Common Core State Standards" and "NMCCSS" on `ccss`.
- "state IDEA advisory panel", "New Mexico IDEA Advisory Panel", "New Mexico Individuals with Disabilities Education Act Advisory Panel" and "IDEA Panel" on `state_panel`.
- "Parent and Child Rights in Special Education" on `safeguards_notice`.
- "Prior Written Notice of Proposed Actions" on `pwn`.
- "Student/Family Vision" on `vision_future`.
- "Section 504 coordinator" on `s504_coord` (untagged).
- "Tier I" and "Tier II" on `tier1` (untagged).

**Extra strings inside new concepts that come from a different document than the concept's citation** (the build only allows one source per new concept):
- "NMPED": GUIDE p. 7.
- "SED": rule 6.31.2.7(B)(19), p. 3.
- "Special Education Bureau": GUIDE p. 1.
- "DVR": GUIDE p. 46.
- "Standard Graduation Option" and "Ability Alternative Graduation Option": GUIDE p. 45.
- "Alternate Assessment Addendum" and "continuing or transitioning IEP": GRAD pp. 21 and 25.
- "NSP": GRAD p. 15.
- "New Mexico Standards of Excellence": GUIDE p. 45 and GRAD p. 19.

## 3. Unsure

- **Concepts tagged to other states that I attested.** All four are general ideas, so the maintainers may want to drop the single-state tag:
  - `al_edt` (Alabama "Eligibility Determination Team"): New Mexico uses the same name in the rule and PSN.
  - `co_special_factors` (Colorado "Consideration of Special Factors"): GUIDE p. 37.
  - `ar_sched_services` (Arkansas "Schedule of Services"): GUIDE p. 55.
  - `cba` (Nevada "Classroom-based assessment"): GUIDE p. 13.
- **The PED division's name.**
  - The rule and PSN say "Special Education Division". That string already belongs to California's `cde_sed`, so I used the PSN's fuller "PED Special Education Division" as the preferred term.
  - GRAD calls the current office the "Office of Special Education". That string belongs to New York's `nysed_ose`, so I left it out. Making both strings national, or adding a regional mechanism for preferred terms, would let New Mexico attest them.
- **Graduation paths.**
  - The 2011 GUIDE names three graduation options: Standard, Career Readiness and Ability.
  - The 2023 rule names "modified and ability programs of study".
  - The 2025 GRAD names only two: Standard and Ability.
  - The documents do not say whether "modified" replaced "career readiness", so I kept them as separate concepts.
  - "Modified program of study" is my singular form of the rule's plural phrase. No document prints it exactly, so `nm_modified_pos` has no extra strings. Please check this one.
- **Legacy items**, kept for coverage: Special Education Bureau, the three 2011 graduation options, the New Mexico Alternate Assessment (GRAD now names Dynamic Learning Maps), the New Mexico Graduation Exam, and demonstrations of competency (removed in 2024).
- **`nm_continuing_iep` vs `in_transition_iep`.** The latter is now national ("Transition IEP"). New Mexico's "continuing or transition IEP" is the IEP a student keeps after the conditional certificate of transition. I kept it separate because the meaning may differ.
- **Keys without the `nm_` prefix.** `dual_discrepancy` and `educational_decision_maker` have no jurisdiction because they are general ideas. `educational_decision_maker` is placed under `surrogate`, which is a judgement call.
- **Other parent concepts I chose.** `nm_ssep` is under `state_ops`, `nm_dvr` under `vr_services`, and `dual_discrepancy` under `sld`.
- **`nm_stars`**: no document expands STARS, so the preferred term is the acronym. It is flagged `common_english_word`.
- **`gifted`** is attested from the 2011 GUIDE. The rule's history shows the gifted provisions were moved out of 6.31.2 in 2023, so New Mexico's gifted rule (6.31.3 NMAC) was not provided.
- **Citations.** PSN and GUIDE citations are PDF pages, not printed page numbers, and each citation says "PDF p.". Rule paragraph numbers in 6.31.2.13(I) are given as the rule prints them, although the rule's own cross-references inside that subsection are off by one.

## 4. Risky

- **Acronyms that are also ordinary words or have other common meanings.** All are matched case-sensitively:
  - **PRO** and **EPICS** (parent groups).
  - **STARS** (data system).
  - **SAT**: Student Assistance Team, but GRAD also uses "SAT School Day" for the College Board test.
  - **SBA**: not defined elsewhere in SPEDLex, but widely used for other things.
  - **PED**.
- **Ambiguous across states** (the build allows these and reports them):
  - **SED**: New York State Education Department and New Mexico's Special Education Division.
  - **DVR**: Delaware and New Mexico vocational rehabilitation divisions.
- **The scrub adapter flags "Bill"** in "Student Bill of Rights" and "NM Deaf/Hard of Hearing Education Bill of Rights". Both are full phrases only.
- **Auto-flagged place names.** Every "New Mexico …" term, plus "NM TEAM" and "NM-ASR", is flagged because it contains the state name. All are full phrases.
- **Name-list hits on ordinary words.** "Parent" (surname list) appears in three form names, and "Law" in "Native American Disability Law Center". These are ordinary words inside full phrases.
- I found no eponyms, and no acronyms that are also given names.

## 5. Left out

- **Funding terms**: Puente para los ninos fund, qualified student, school-age person, program units, annual determinations, and needs intervention.
- **Legal aid providers**: New Mexico Legal Aid Society and Pegasus Legal Services for Children, as in other layers.
- **Courts**: the Children's Court and juvenile court.
- **Contact details**: addresses, phone numbers and web addresses.
- **Products**: College Board and ACT products (SAT School Day, PSAT, WorkKeys) and Level All.
- **Graduation details**: course names and codes, the graduate profile, and the interim and final Next-Step Plan variants.
- **"Consent override"**: a procedure, not a document term families would see.
- **"FVE/LMA"** (GUIDE p. 91): the documents do not expand it.
- **"IFSP-IEP"**: a combined document form.
- **Forms with no likely family exposure**: the teacher modification and assistance forms, contact log, Special Transportation Instructions, and Addendum for Braille Instruction.
- **GUIDE student-profile domain labels**.
- **"Office of Special Education" and "Special Education Division" alone**: see §3.
