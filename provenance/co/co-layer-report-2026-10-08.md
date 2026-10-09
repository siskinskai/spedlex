# Colorado layer (v0.39.0): contributor report

Drafted 2026-10-08 with Claude Sonnet 5.5 (`claude-sonnet-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted. `prompts/audit-layer.md` was run in a fresh context by a subagent of the same model family, not a different model (`co-layer-audit-2026-10-08.md`); a human or different-model audit is still advisable.

## 1. Documents read
- **RULE**: 1 CCR 301-8, Rules for the Administration of the Exceptional Children's Educational Act (126 pp., Editor's Notes list amendments through May 15, 2025). Rules 2.00-2.54 (definitions), 4.02, 4.03 and 12.01 were read; the rest was searched. The funding, tuition-contract and AU-reorganization rules (3.01-3.03, 7.03, 9.03-9.07) were not read line by line.
- **PSN**: CDE, "A Guide to Parent Rights in Special Education: Special Education Procedural Safeguards Notice" (April 2024, 51 pp.; the Appendix D footers read April 2025). Cited by PDF page (printed page + 4).
- **GUIDE**: CDE ESSU, "IEP Procedural Guidance" (revised July 2017, 158 pp.). A practitioner manual for administrative units, not a parent guide. Pages 12-39 and the model forms (pp. 83-147) were searched, not read in full. It predates the 2024 abbreviated-school-day law and the 2025 rule amendments.
- **Missing**: Colorado has no parent guide to the IEP in PDF form; CDE's parent FAQ is a web page of links (saved as `CO-CDE-Parent-FAQ.html`, not cited).
- Copies are in `.sources-cache/co/`.

## 2. New concepts (61)
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `co_cde` | Colorado Department of Education | "303, means the Colorado Department of Education. 2.50 State-Operated Program State-Operated Program means an approved" | 1 CCR 301-8, Rule 2.49, 2.20(1) |
| `co_essu` | Exceptional Student Services Unit | "complaint with the Exceptional Student Services Unit (ESSU) at the Colorado Department of Education (CDE)," | CDE PSN (Apr. 2024), PDF p. 5 |
| `co_board` | Colorado State Board of Education | "DEPARTMENT OF EDUCATION Colorado State Board of Education RULES FOR THE ADMINISTRATION OF THE EXCEPTIONAL" | 1 CCR 301-8, Rule 2.47 |
| `co_ofs` | Office of Facility Schools | "authorized by CDE’s Office of Facility Schools to provide educational services to students placed in" | 1 CCR 301-8, Rule 2.20(1) |
| `co_ecea` | Exceptional Children's Educational Act | "ADMINISTRATION OF THE EXCEPTIONAL CHILDREN'S EDUCATIONAL ACT 1 CCR 301-8 [Editor’s Notes follow the text" | 1 CCR 301-8, Rule 1.00 |
| `co_cdec` | Department of Early Childhood | "of Education 2.14 Department of Early Childhood Programs 2.14(1) Department of Early Childhood (CDEC) means" | 1 CCR 301-8, Rule 2.14(1) |
| `co_lco` | Local Coordinating Organization | "26.5- 1.104, C.R.S. 2.14(2) Local Coordinating Organization (LCO) means an entity as defined in 26.5-2-102(5)," | 1 CCR 301-8, Rule 2.14(2) |
| `co_upk` | Universal Preschool Program | "in 26.5-4-203(14), C.R.S. 2.14(4) Universal Preschool Program or Preschool Program means the preschool program created" | 1 CCR 301-8, Rule 2.14(4) |
| `co_au` | Administrative unit | "(IDEA) as amended. 2.03 Administrative Unit Administrative Unit (AU) means a school district, board of" | 1 CCR 301-8, Rule 2.03 |
| `co_aur` | Administrative unit of residence | "of Education 2.03(1) Administrative unit of residence Pursuant to sections 22-1-102 and 22-20-107.5, C.R.S., an" | 1 CCR 301-8, Rule 2.03(1) |
| `co_aua` | Administrative unit of attendance | "of residency. 2.03(2) Administrative unit of attendance An administrative unit of attendance (AUA) shall mean" | 1 CCR 301-8, Rule 2.03(2) |
| `co_alt_au` | Alternative administrative unit | "that participates in an alternative administrative unit, the alternative administrative unit is deemed the administrative" | 1 CCR 301-8, Rule 2.03(3) |
| `co_multi_au` | Multi-district administrative unit | "board of cooperative services, multi-district administrative unit, a charter school network, a charter school collaborative," | 1 CCR 301-8, Rule 2.03(4) |
| `co_boces` | Board of Cooperative Services | "a school district, board of cooperative services, multi-district administrative unit, a charter school network, a" | 1 CCR 301-8, Rule 2.06, 3.01(3)(a)(ii) |
| `co_csi` | State Charter School Institute | "collaborative, or the State Charter School Institute, that is providing educational services to exceptional children" | 1 CCR 301-8, Rule 2.48 |
| `co_charter_network` | Charter school network | "multi-district administrative unit, a charter school network, a charter school collaborative, or the State Charter" | 1 CCR 301-8, Rule 2.07(5) |
| `co_charter_collab` | Charter school collaborative | "charter school network, a charter school collaborative, or the State Charter School Institute, that is" | 1 CCR 301-8, Rule 2.07(4) |
| `co_approved_facility` | Approved facility school | "the regional centers, an approved facility school, a group home or group center, a mental" | 1 CCR 301-8, Rule 2.20(1), 3.02(1) |
| `co_online_school` | Multidistrict online school | "not including enrollment in multidistrict online schools; 9.01(1)(a)(ii) The PPR of the accounting district, as" | 1 CCR 301-8, Rule 9.01(4) |
| `co_sop_csdb` | Colorado School for the Deaf and the Blind | "attends the Colorado School for the Deaf and the Blind, such child shall be deemed" | 1 CCR 301-8, Rule 2.50(1) |
| `co_sco` | State Complaints Officer | "a state complaint, the State Complaints Officer (SCO) will continue with their investigation. If you" | CDE PSN (Apr. 2024), PDF p. 17 |
| `co_oac` | Office of Administrative Courts | "assigned by the Office of Administrative Courts (OAC) to conduct a hearing to resolve the" | CDE PSN (Apr. 2024), PDF p. 22 |
| `co_dpar` | Dispute Prevention and Assisted Resolution Supervisor | "regarding Mediation? Contact: Dispute Prevention and Assisted Resolution Supervisor Email: rains_k@cde.state.co.us Ph: 720-990-1464 Questions regarding" | CDE PSN (Apr. 2024), PDF p. 51 |
| `co_ppra` | Protection of Persons from Restraint Act | "seclusion under the Protection of Persons from Restraint Act (PPRA). CDE may also investigate concerns" | CDE PSN (Apr. 2024), PDF p. 18 |
| `co_tjp` | Transformative Justice Project | "parent may contact the Transformative Justice Project (https://tjpcolorado.org/our-programs) to have an attorney appointed to represent" | CDE PSN (Apr. 2024), PDF p. 22 |
| `co_peak` | PEAK Parent Center | "Colorado, Parent Centers include: PEAK Parent Center: PEAK Parent Center is a nonprofit that works" | CDE PSN (Apr. 2024), PDF p. 15 |
| `co_show_tell` | Show and Tell Corporation | "them at 719-531-9400. Show and Tell Corporation: Show and Tell is a 501(c)(3) parent-driven organization" | CDE PSN (Apr. 2024), PDF p. 15 |
| `co_thrive` | THRIVE Center | "the sister organization of THRIVE Center, formerly known as the Denver Metro Community Parent Resource" | CDE PSN (Apr. 2024), PDF p. 15 |
| `co_dlc` | Disability Law Colorado | "the CDE’s website (https://www.cde.state.co.us/cdesped/spedparents). Disability Law Colorado: Disability Law Colorado is the state’s designated protection" | CDE PSN (Apr. 2024), PDF p. 15 |
| `co_arc` | The Arc of Colorado | "Agency Contact Information The ARC of Colorado There are 15 chapters of The Arc in" | CDE PSN (Apr. 2024), PDF p. 37 |
| `ocr` | Office for Civil Rights | "at 1-800- 531-2105. Office for Civil Rights (OCR) The OCR serves student populations facing discrimination" | CDE PSN (Apr. 2024), PDF p. 37 |
| `s504_coord` | 504 Coordinator | "504, please contact the 504 Coordinator for your school district. School District: Please add the" | CDE PSN (Apr. 2024), PDF p. 3 |
| `counsel_youth` | Counsel for Youth | "a Guardian Ad Litem, Counsel for Youth, foster parent, or other kin. What if I" | CDE PSN (Apr. 2024), PDF p. 9 |
| `co_comm_plan` | Communication Plan | "disability shall include a Communication Plan as developed by the IEP team. The Plan shall" | 1 CCR 301-8, Rule 4.03(6)(a) |
| `co_lmp` | Learning Media Plan | "disability shall include a Learning Media Plan as developed by the IEP team based on" | 1 CCR 301-8, Rule 4.03(6)(b) |
| `co_literacy_mode` | Literacy mode | "U.S.C. § 1401(18). 2.31 Literacy Mode Literacy Mode means one of the following four systems" | 1 CCR 301-8, Rule 2.31 |
| `co_abbrev_day` | Abbreviated school day | "IN THESE RULES 2.01 Abbreviated School Day Abbreviated School Day means any school day during" | 1 CCR 301-8, Rule 2.01 |
| `co_abbrev_sched` | Abbreviated school day schedule | "been made. 2.01(1) Abbreviated School Day Schedule Abbreviated School Day Schedule means a schedule designed" | 1 CCR 301-8, Rule 2.01(1) |
| `co_child_find_coord` | Child find coordinator | "person designated as the child find coordinator who shall be responsible for an ongoing child" | 1 CCR 301-8, Rule 4.02(2)(b) |
| `co_building_referral` | Building level referral | "a process for a building level referral. The purpose of the building level process is" | 1 CCR 301-8, Rule 4.02(3) |
| `co_nonsig_change` | Nonsignificant change in program/services | "in placement. 4.03(8)(b)(i) Nonsignificant change in program/services. When a child’s educational program is altered, such" | 1 CCR 301-8, Rule 4.03(8)(b)(i) |
| `co_sig_change` | Significant change in placement | "not required. 4.03(8)(b)(ii) Significant change in placement: 4.03(8)(b)(ii)(A) A significant change in placement for educational" | 1 CCR 301-8, Rule 4.03(8)(b)(ii) |
| `co_comp_plan` | Comprehensive Plan | "of compliant special education comprehensive plan as required by IDEA and approved by the Department." | 1 CCR 301-8, Rule 8.01(1)(a) |
| `co_seta` | Special Education Temporary Authorization | "(TEE) Authorization / Special Education Temporary Authorization (SETA) Authorization for Temporary Educator Eligibility (TEE) for" | 1 CCR 301-8, Rule 3.04(3) |
| `co_eipa` | Educational Interpreter Performance Assessment | "areas of the Educational Interpreter Performance Assessment (EIPA). 3.04(1)(f)(ii) Documented content knowledge in these areas:" | 1 CCR 301-8, Rule 3.04(1)(f) |
| `co_state_iep` | State Recommended IEP | "the development of the State Recommended IEP and this guidance. Original Contributors: Adena Miller Stephanie" | CDE IEP Procedural Guidance (rev. July 2017), p. 4 |
| `co_service_delivery` | Service Delivery Statement | "Service Delivery Statement is used to:  Identify areas of the curriculum and the student’s" | CDE IEP Procedural Guidance (rev. July 2017), p. 75 |
| `co_rec_placement` | Recommended Placement in the Least Restrictive Environment | "as well. Recommended Placement in the Least Restrictive Environment is used to:  Document each" | CDE IEP Procedural Guidance (rev. July 2017), p. 76 |
| `co_special_factors` | Consideration of Special Factors | "Consideration of Special Factors is used to:  Consider any special factors that may interfere" | CDE IEP Procedural Guidance (rev. July 2017), p. 65 |
| `co_ps_plan` | Postsecondary Transition Plan | "Postsecondary Transition Plan is used to:  Identify the coordinated set of transition activities for" | CDE IEP Procedural Guidance (rev. July 2017), p. 68 |
| `co_invite_agencies` | Consent to Invite Agencies Related to Transition | "year. The Consent to Invite Agencies Related to Transition (English Version Spanish Version) must be" | CDE IEP Procedural Guidance (rev. July 2017), p. 41 |
| `notice_meeting` | Notice of Meeting | "4.02(3)(c)] [IDEA 300.301(c)2] A notice of meeting should be sent to the parent in a" | CDE IEP Procedural Guidance (rev. July 2017), p. 11 |
| `co_eeo` | Extended Evidence Outcomes | "achievement standards called the Extended Evidence Outcomes (EEOs), and who take an alternate assessment, the" | CDE IEP Procedural Guidance (rev. July 2017), p. 44 |
| `co_cas` | Colorado Academic Standards | "levels of performance, the Colorado Academic Standards, identified need(s), and annual goals that allow the" | CDE IEP Procedural Guidance (rev. July 2017), p. 43 |
| `co_eic` | Early Intervention Colorado | "collaboration between the local Early Intervention Colorado program and the local AU. http://www.cde.state.co.us/early/cfpreresources TRANSFERS A" | CDE IEP Procedural Guidance (rev. July 2017), p. 52 |
| `co_eldg` | Early Learning and Development Guidelines | "daily routines. Colorado's Early Learning and Development Guidelines (ELDGs) describe the trajectory of children's learning" | CDE IEP Procedural Guidance (rev. July 2017), p. 150 |
| `co_insurance_model` | Insurance model | "service delivery models:  Insurance model: Under the insurance model, the charter school pays an" | CDE IEP Procedural Guidance (rev. July 2017), p. 56 |
| `co_contracted_model` | Contracted model | "the charter school.  Contracted model: Under the contracted model, the administrative unit passes through" | CDE IEP Procedural Guidance (rev. July 2017), p. 56 |
| `co_combo_model` | Combination/modified insurance model | "attending the school.  Combination/Modified Insurance model: Under the combination/modified insurance model, the charter school" | CDE IEP Procedural Guidance (rev. July 2017), p. 56 |
| `co_alp` | Advanced Learning Plan | "of these Rules). 12.01(2) “Advanced Learning Plan” or “ALP” means a written record of a" | 1 CCR 301-8, Rule 12.01(2) |
| `co_early_access` | Early Access | "appropriate instructional level.” 12.01(12) “Early Access” means early entrance to kindergarten at age 4 or" | 1 CCR 301-8, Rule 12.01(12) |

Quotes come from text extracted with pdftotext, with line breaks collapsed. For RULE rows the quote is the first place the term appears in the rules text, which is not always the cited rule; the cited rule number was checked by hand. Every string was checked automatically against its cited page (PSN, GUIDE) or against the rules text (RULE); the audit then checked each by hand.

## 3. Unsure
- **"504 Coordinator"** is the preferred term, as the PSN writes it (PDF p. 3); a draft had "Section 504 coordinator", which no document uses.
- **Acronyms in the rules**: "CDE", "BOCES" and "AUs" appear in the rules but not in the rule that defines the term, so two citations list both places.
- **TEE** (Temporary Educator Eligibility) is typed legacy: Rule 3.04(3) says the authorization "shall be formally referred to as" SETA.
- **PPRA**: the PSN uses two different expansions for it in one passage; both are recorded. It is not the federal Protection of Pupil Rights Amendment.
- **Rule 2.20**: the Editor's Notes say it was repealed effective 06/30/2022, but the rule text still carries it.
- **Colorado School for the Deaf and the Blind** is a named school, kept because Rule 2.50(1) names it as a State-Operated Program.
- Weak mappings the audit flagged and that were removed: `sped_teacher` (GUIDE p. 153) and `special_school` (GUIDE p. 80). Three more are kept but their key's term is not literally in the cited text: `disprop` (Rule 5.01(22)), `annual_review` (Rule 4.03(3)), `dp_hearing` (Rule 6.02(7.5)(c)).

## 4. Risky
- **Place names** (graded high automatically): Colorado Department of Education, Colorado State Board of Education, Department of Early Childhood, Colorado School for the Deaf and the Blind, THRIVE Center (formerly "Denver Metro Community Parent Resource Center"), Disability Law Colorado, The Arc of Colorado, Colorado Academic Standards and Early Intervention Colorado.
- **Acronyms that collide or are ordinary words**: "CDE" (California's CDE, now an allowed cross-state ambiguity), "SCO" (DC's State Complaints Officer, now allowed), "EEO" (usually Equal Employment Opportunity), "OCR", "AU", "ESSU", "PPRA". "Early Access" carries `common_english_word`. "SOP" was dropped from the State-Operated Program concept because Texas uses it for Summary of Performance.
- **Organization names**: Counsel for Youth, Transformative Justice Project, PEAK Parent Center, Show and Tell Corporation. None contains a personal name.

## 5. Left out on purpose
- Every person named in the documents (task-force members, CDE staff, contact details) and the districts, BOCES and schools they work for, except the Colorado School for the Deaf and the Blind.
- SASID, ICAP, UIP and per-pupil revenue; tuition, contract-element and funding-formula terms; the YODeL training library and Quality Tips worksheets; commercial reading screeners.
- "Show and Tell" and "PEAK" on their own; CDE staff job titles other than the dispute-resolution roles; the long eligibility-criteria wording of each disability category.
- Twenty terms the audit says are missed (compensatory services, seclusion and restraint, case manager, self-contained class, post-school goal and others) are listed in the audit file for a later patch.
