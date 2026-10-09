# Audit: Arizona layer (`sources/states/arizona.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-08 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section and paragraph, or the cited PDF page, of text extracted from the documents in this folder (ligatures, quotes, dashes and line-break hyphens normalized). For entries that attest an existing concept without adding strings, the check passes if any of the concept's existing strings appears at the citation. Entries without a literal hit were checked by hand.

Documents: 7 A.A.C. 2 (Supp. 25-4, 186 pp.), ADE Procedural Safeguards Notice (Rev. 08-28-25, 30 pp.), Traveling the Special Education Highway (2019, 17 pp.), ESS Glossary of Acronyms and Terms (Revised May 2026, 60 pp.).

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `cwd` — Ariz. Admin. Code R7-2-401(B)(4) | Child with a disability | confirmed |  |  | from a public education agency. 4. " Child with a disability ," has the same |
| 2 | `evaluation` — Ariz. Admin. Code R7-2-401(B)(8) | full and individual evaluation | confirmed |  |  | special education evaluation and placement. 8. " Full and individual evaluation " means procedures used |
| 3 | `iee` — Ariz. Admin. Code R7-2-401(B)(9) | Independent educational evaluation | confirmed |  |  | and needs of the child. 9. " Independent educational evaluation " means an evaluation conducted |
| 4 | `consent` — Ariz. Admin. Code R7-2-401(B)(10) | informed written consent | confirmed |  |  | of the child in question. 10. " Informed written consent " means a person has |
| 5 | `mdt` — Ariz. Admin. Code R7-2-401(B)(12) | Multidisciplinary Evaluation Team | confirmed |  |  | for the provision of FAPE. 12. " Multidisciplinary Evaluation Team " has the same meaning |
| 6 | `mdt` — Ariz. Admin. Code R7-2-401(E)(3) | MET | confirmed |  |  | date of the Multidisciplinary Evaluation Team ( MET ) determination of eligibility. 4. If the |
| 7 | `lea` — Ariz. Admin. Code R7-2-401(B)(16) | public education agency, PEA | confirmed |  |  | also serve students without disabilities. 16. " Public education agency " or "PEA" means a |
| 8 | `sdi` — Ariz. Admin. Code R7-2-401(B)(18) | Specially designed instruction | confirmed |  |  | including supplemental aids and services. 18. " Specially designed instruction " has the same meaning |
| 9 | `sped_teacher` — Ariz. Admin. Code R7-2-401(B)(19) | Special education teacher | confirmed |  |  | prescribed in A.R.S. § 15-761. 19. " Special education teacher " means a teacher holding |
| 10 | `psw` — Ariz. Admin. Code R7-2-401(E)(7) | (existing strings of `psw`) | confirmed (checked by hand) |  | Two-column layout separates the "7." marker from its text; found in (E)(7)(d) | of whether the child exhibits a pattern of strengths and weaknesses in performance, achievement, or |
| 11 | `discrepancy` — Ariz. Admin. Code R7-2-401(E)(7) | (existing strings of `discrepancy`) | confirmed (checked by hand) |  | (E)(7)(d)(i) says "A discrepancy between achievement and ability"; not "severe" |  |
| 12 | `ed` — Ariz. Admin. Code R7-2-401(E)(7) | emotional disability | confirmed (checked by hand) |  | Found in (E)(7)(a) | individual initial evaluation shall include: a. Emotional disability : verification of a disorder by a |
| 13 | `transition` — Ariz. Admin. Code R7-2-401(G)(4) | Transition services, transition plan | confirmed |  |  | of the specially designed instruction. a. Transition services . Beginning not later than the first |
| 14 | `postsecondary` — Ariz. Admin. Code R7-2-401(G)(4) | Measurable postsecondary goals, postsecondary goals, independent living skills | confirmed |  |  | the IEP must include: i. Appropriate measurable postsecondary goals based upon age-appropriate transition assessments related |
| 15 | `course_study` — Ariz. Admin. Code R7-2-401(G)(4) | Courses of study, course of study | confirmed |  |  | and ii. The transition services, including courses of study , needed to assist the child |
| 16 | `age_majority` — Ariz. Admin. Code R7-2-401(G)(4) | Transfer of rights at age of majority, age of majority, rights at age of majority | confirmed |  |  | implementing a change in placement. b. Transfer of rights at age of majority . Beginning |
| 17 | `alt_assess` — Ariz. Admin. Code R7-2-401(G)(5) | Alternate assessment | confirmed |  |  | will be assessed with the state's alternate assessment as determined by the IEP team. |
| 18 | `sig_cog` — Ariz. Admin. Code R7-2-401(G)(5) | significant cognitive disability | confirmed |  |  | who are determined to have a significant cognitive disability based on the established eligibility criteria |
| 19 | `lre` — Ariz. Admin. Code R7-2-401(H) | Least restrictive environment | confirmed |  |  | agreed upon date and time. H. Least Restrictive Environment . 1. Each public education agency |
| 20 | `pwn` — Ariz. Admin. Code R7-2-401(I)(2) | Prior written notice, written notice | confirmed |  |  | accordance with the requirements of IDEA, prior written notice shall be provided to the parents |
| 21 | `ferpa` — Ariz. Admin. Code R7-2-401(J)(1) | Family Educational Rights and Privacy Act, FERPA | confirmed |  |  | the IDEA and its regulations, the Family Educational Rights and Privacy Act (FERPA) and its |
| 22 | `delegation` — Ariz. Admin. Code R7-2-401(J)(3) | Delegation of Rights | confirmed |  |  | or the student has executed a delegation of rights to make educational decisions pursuant to |
| 23 | `part_c_transition` — Ariz. Admin. Code R7-2-401(K)(2) | (existing strings of `part_c_transition`) | confirmed (checked by hand) |  | Paraphrase: transition from AzEIP to a public school preschool program | informed of the child's rights under part B of the Act, if any that |
| 24 | `ppps` — Ariz. Admin. Code R7-2-401(L) | (existing strings of `ppps`) | confirmed (checked by hand) |  | Paraphrase: "students enrolled in private schools by their parents" |  |
| 25 | `child_find` — ADE Traveling the Special Education Highway (2019), PDF p. 3 | Child find | confirmed |  |  | ...................................................................... 15 1 Child Find A Continuous Search Public schools must |
| 26 | `safeguards_notice` — ADE Traveling the Special Education Highway (2019), PDF p. 4 | Procedural safeguards notice, procedural safeguards | confirmed |  |  | school proposed or refused the action. Procedural Safeguards Notice The Procedural Safeguards Notice (PSN) provides |
| 27 | `autism` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Autism | confirmed |  |  | • • • • • • Autism (A) Developmental Delay (DD) Emotional Disability |
| 28 | `dd` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Developmental delay, DD | confirmed |  |  | • • • • Autism (A) Developmental Delay (DD) Emotional Disability (ED) Hearing Impairment |
| 29 | `hi` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Hearing impairment, HI | confirmed |  |  | Developmental Delay (DD) Emotional Disability (ED) Hearing Impairment (HI) Mild Intellectual Disability (MIID) Moderate |
| 30 | `md` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Multiple disabilities, MD | confirmed |  |  | Disability (MIID) Moderate Intellectual Disability (MIOD) Multiple Disabilities (MD) Multiple Disabilities with Severe Sensory |
| 31 | `oi` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Orthopedic impairment, OI | confirmed |  |  | Disabilities with Severe Sensory Impairment (MDSSI) Orthopedic Impairment (OI) Other Health Impairments (OHI) Preschool |
| 32 | `ohi` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | OHI, other health impairments | confirmed |  |  | Orthopedic Impairment (OI) Other Health Impairments ( OHI ) Preschool Severe Delay (PSD) Severe Intellectual |
| 33 | `sld` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Specific learning disability, SLD, learning disability | confirmed |  |  | Delay (PSD) Severe Intellectual Disability (SID) Specific Learning Disability (SLD) Speech/Language Impairment (SLI) Traumatic Brain |
| 34 | `tbi` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Traumatic brain injury, TBI | confirmed |  |  | Learning Disability (SLD) Speech/Language Impairment (SLI) Traumatic Brain Injury (TBI) Visual Impairment (VI) Independent Educational |
| 35 | `vi` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | visual impairment, VI | confirmed |  |  | Impairment (SLI) Traumatic Brain Injury (TBI) Visual Impairment (VI) Independent Educational Evaluation If you |
| 36 | `sli` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Speech/Language Impairment | confirmed |  |  | Disability (SID) Specific Learning Disability (SLD) Speech/Language Impairment (SLI) Traumatic Brain Injury (TBI) Visual |
| 37 | `id` — ADE Traveling the Special Education Highway (2019), PDF p. 7 | mild intellectual disability, MIID, moderate intellectual disability, severe intellectual disability | confirmed |  |  | Emotional Disability (ED) Hearing Impairment (HI) Mild Intellectual Disability (MIID) Moderate Intellectual Disability (MIOD) Multiple |
| 38 | `id` — ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 34 | MOID | confirmed |  |  | a free appropriate public education (FAPE). MOID Moderate Intellectual A term used in |
| 39 | `reeval` — ADE Traveling the Special Education Highway (2019), PDF p. 11 | Reevaluation | confirmed |  |  | "Reevaluation" (contact list; nearby names and contact details left out) |
| 40 | `mdr` — ADE Traveling the Special Education Highway (2019), PDF p. 12 | Manifestation determination | confirmed |  |  | a change in placement o A manifestation determination will decide if the behavior was |
| 41 | `iaes` — ADE Traveling the Special Education Highway (2019), PDF p. 12 | Interim alternative educational setting | confirmed |  |  | may move your child to an interim alternative educational setting or suspend your child for |
| 42 | `s504` — ADE Traveling the Special Education Highway (2019), PDF p. 13 | Section 504, Section 504 of the Rehabilitation Act | confirmed |  |  | Evaluation Team (MET) regarding eligibility for Section 504 of the Rehabilitation Act of 1973. |
| 43 | `sop` — ADE Traveling the Special Education Highway (2019), PDF p. 13 | (existing strings of `sop`) | confirmed (checked by hand) |  | "summary of the student's academic achievement and functional performance" |  |
| 44 | `std_diploma` — ADE Traveling the Special Education Highway (2019), PDF p. 13 | regular high school diploma | confirmed |  |  | learning. 2. He/she graduated with a regular high school diploma . • You, or your |
| 45 | `oah` — ADE Traveling the Special Education Highway (2019), PDF p. 14 | Arizona Office of Administrative Hearings | confirmed |  |  | request will be forwarded to the Arizona Office of Administrative Hearings and assigned to an |
| 46 | `state_complaint` — ADE Traveling the Special Education Highway (2019), PDF p. 14 | State complaint | confirmed |  |  | 1. Mediation • • • 2. State Complaint • • • 3. is a |
| 47 | `pti` — ADE Traveling the Special Education Highway (2019), PDF p. 16 | Parent training and information center | confirmed |  |  | "Parent training and information center" (contact list; nearby names and contact details left out) |
| 48 | `msaa` — ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 35 | MSAA | confirmed |  |  | outcomes can be monitored and supported. MSAA Multi-State Alternate An alternate statewide assessment |
| 49 | `az_doe` (new concept) — ADE Traveling the Special Education Highway (2019), PDF p. 16 | Arizona Department of Education, ADE | confirmed |  |  | Individuals with Disabilities Education Act (IDEA). Arizona Department of Education , Exceptional Student Services 1535 |
| 50 | `az_ess` (new concept) — ADE Traveling the Special Education Highway (2019), PDF p. 16 | Exceptional Student Services, ESS | confirmed |  |  | Act (IDEA). Arizona Department of Education, Exceptional Student Services 1535 W. Jefferson, Bin 24 Phoenix, |
| 51 | `az_dru` (new concept) — ADE Traveling the Special Education Highway (2019), PDF p. 14 | Dispute Resolution Unit | confirmed |  |  | process initiated by contacting the ADE/ESS, Dispute Resolution Unit ; and, a procedure facilitated by |
| 52 | `az_encircle` (new concept) — ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 45 | Encircle Families, Raising Special Kids | confirmed |  |  | support their child's education and development. Encircle Families (formerly Raising Special Kids) is the |
| 53 | `az_dra` (new concept) — ADE IDEA Part B Procedural Safeguards Notice (Rev. 08-28-25), PDF p. 1 | Disability Rights Arizona | confirmed |  |  | "Disability Rights Arizona" (contact list; nearby names and contact details left out) |
| 54 | `az_azeip` (new concept) — ADE Traveling the Special Education Highway (2019), PDF p. 3 | Arizona Early Intervention Program, AzEIP | confirmed |  |  | process; • refer you to the Arizona Early Intervention Program (AzEIP) for infants and toddlers; |
| 55 | `az_ahcccs` (new concept) — ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 35 | Arizona Health Care Cost Containment System, AHCCCS | confirmed |  |  | students. Through Arizona's Medicaid agency, AHCCCS ( Arizona Health Care Cost Containment System ), MSBC |
| 56 | `az_accom_school` (new concept) — Ariz. Admin. Code R7-2-401(B)(16) | Accommodation school | confirmed |  |  | means a school district, charter school, accommodation school , state supported institution, or other political |
| 57 | `az_boundaries` (new concept) — Ariz. Admin. Code R7-2-401(B)(3) | Boundaries of responsibility | confirmed |  |  | of a public education agency. 3. " Boundaries of responsibility " means for: a. A |
| 58 | `az_private_sped_school` (new concept) — Ariz. Admin. Code R7-2-401(B)(15) | Private special education school | confirmed |  |  | or a public education agency. 15. " Private special education school " means a nonpublic |
| 59 | `az_mdssi` (new concept) — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Multiple disabilities with severe sensory impairment, MDSSI | confirmed |  |  | Intellectual Disability (MIOD) Multiple Disabilities (MD) Multiple Disabilities with Severe Sensory Impairment (MDSSI) Orthopedic Impairment |
| 60 | `az_psd` (new concept) — ADE Traveling the Special Education Highway (2019), PDF p. 7 | Preschool severe delay, PSD | confirmed |  |  | Impairment (OI) Other Health Impairments (OHI) Preschool Severe Delay (PSD) Severe Intellectual Disability (SID) Specific |
| 61 | `az_grad_date` (new concept) — Ariz. Admin. Code R7-2-401(G)(4) | Estimated date of graduation | confirmed |  |  | reaching those goals; and iii. The estimated date of graduation for the student, including the |
| 62 | `az_azsci` (new concept) — ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 10 | Arizona Science Test, AzSCI | confirmed |  |  | reliable communication for all callers. AzSCI Arizona Science Test Arizona's statewide achievement test for Science, |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Arizona Schools for the Deaf and the Blind (ASDB) | R7-2-404(A) (RULE PDF p. 40); GLOSS p. 8 | The docstring says the full name appears only broken across GLOSS columns, but R7-2-404(A) has it unbroken. Add with `broader: state_sp_sch` |
| Home school district (HSD) | R7-2-404 (RULE PDF pp. 40-41); GLOSS p. 27 | Arizona voucher term; candidate concept |
| State Placing Agency | R7-2-404 (RULE PDF p. 40); GLOSS p. 53 | Candidate concept |
| Special education institutional voucher | R7-2-404(A) (RULE PDF p. 40) | Candidate concept |
| Division of Developmental Disabilities (DDD) | GLOSS p. 48 (unbroken) | Candidate agency concept |
| Arizona State Hospital (ASH) | R7-2-404(A) | Low priority; "ASH" is a common word in capitals |

## 3. Summary

- **62 entries: 62 confirmed, 0 misplaced, 0 not found.** 6 needed a hand check.
- **Safety:** no single letters, and no person's name standing alone as a term. Place names are graded automatically. Notes on individual strings are in the table.
- **Typing:** every all-capitals string is typed as an acronym or abbreviation; state-only strings carry the state tag.
- **Build:** `build --check` passes and all 70 tests pass.

**Most important fixes**

1. **Docstring inaccuracy:** the Arizona Schools for the Deaf and the Blind were left out because their name "appears only broken across GLOSS columns", but R7-2-404(A) (RULE PDF p. 40) has "Arizona Schools for the Deaf and the Blind (ASDB)" unbroken. Add it from there, and fix the docstring.
2. `GLOSS_URL` points to a 2020 file path ("5.20.2020"), while the document and its citation say "Revised May 2026". I can't tell from here whether that URL serves the cited version; please check it.
3. Consider adding the R7-2-404 voucher terms (home school district, State Placing Agency, institutional voucher). The docstring says only R7-2-401 was read, so these are new ground.

**Docstring:** Accurate apart from the ASDB point above. Page counts (186, 30, 17, 60) match; the RULE header reads Supp. 25-4, December 31, 2025; GLOSS p. 1 reads "Revised May 2026". The (E)(7) checks needed a hand look because the two-column layout separates paragraph numbers from their text.

**Update (2026-10-08):** Fix 1 applied: the docstring is corrected, and `arizona_supplement` adds the Arizona Schools for the Deaf and the Blind, institutional voucher, home school district and State Placing Agency from R7-2-404. The Division of Developmental Disabilities was not added, because New Jersey's layer already uses that exact name. **Fix 2 resolved, no change needed:** the `GLOSS_URL` file is the "Revised May 2026" version (checked 2026-10-08). Released in 0.38.0.
