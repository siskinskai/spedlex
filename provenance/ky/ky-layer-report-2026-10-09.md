# Kentucky layer (v0.47.0): contributor report

Drafted 2026-10-09 with Claude Sonnet 5.5 (`claude-sonnet-5-5`) following `prompts/add-state.md` (the copy in the repository is v1.4). A person must review this before it is submitted, and `prompts/audit-layer.md` has **not** been run: it should be run in a fresh conversation, ideally with a different model. The layer attests 167 concepts and adds 24 (6 machine_validated, 18 candidate); 143 of the 167 already existed. The build reports no new ambiguous acronyms across states and no string conflicts.

## 1. Documents read
- **RULE**: 707 KAR 1:002, Definitions (9 pp.), read in full from the text layer with `pdftotext`. The heading says "(Amended at ARRS Committee)" and the history note ends "eff. 7-5-2023". **I could not check whether a later amendment is in effect.** Cited by the numbered definition in Section 1.
- **PSN**: KDE Part B Procedural Safeguards Notice (35 pp.), read in full. It is the OSEP model notice with Kentucky additions, so most entries only attest existing concepts. The cover says "Revised September 26, 2008" but the PDF metadata shows a modification on 2023-08-22, so the real edition date is uncertain. Cited by PDF page; printed page = PDF page minus 3.
- **GUIDE**: KDE IDEA Part B Special Education Process (6 pp., "Reviewed April 2025"), read in full. PDF page = printed page.
- **YOUTH**: KY-SPIN, A Youth Guide to the IEP (67 pp.), read in full from the text layer. It prints no page numbers, so citations are PDF pages. Pages 17, 19 and 21 are partly raster images with a garbled text layer; I cited only wording that was legible there (page titles). The guide is KY-SPIN's, hosted on the KDE site, so I typed its records `secondary_guidance`; a reviewer may prefer `state_guidance`. The guide's worked examples use first names; none were used.
- **Missing**: 707 KAR 1:300, 1:310, 1:320, 1:340, 1:350 and the other rules of Chapter 1 (only 1:002 was provided), the KDE IEP guidance document, the alternate-assessment pages, the diploma rule (704 KAR 3:305). The Kentucky layer therefore has no eligibility procedures, IEP-content rule or placement rule of its own.
- **Not done**: the Wayback Machine snapshot and a byte-for-byte check against the live URLs. The session that drafted this had no route to archive.org or education.ky.gov, so `wayback_url` is blank in all four manifest rows. SHA-256 hashes and sizes are of the files the contributor downloaded on 2026-10-09.
- A script checked that every string (and, for attestations without a new string, the concept's wording) appears in the cited rule item or page; the misses were fixed or checked by hand (section 3). A second script confirmed that each quote in section 2 appears on its cited page. Quotes are 15 words or fewer.

## 2. New concepts
| Key | Term | Quote (≤15 words) | Citation |
|---|---|---|---|
| `ky_kde` | Kentucky Department of Education | "The Kentucky Department of Education (KDE) must give notice" | PSN PDF p. 9 |
| `ky_oseel` | Office of Special Education and Early Learning | "KDE Office of Special Education and Early Learning (OSEEL)" | GUIDE p. 5 |
| `ky_idea_monitoring` | Division of IDEA Monitoring and Results | "Director, Division of IDEA Monitoring and Results" | PSN PDF p. 15 |
| `ky_ecab` | Exceptional Children Appeals Board | "KDE's Exceptional Children Appeals Board (ECAB)" | PSN PDF p. 25 |
| `ky_chfs` | Cabinet for Health and Family Services | "the Kentucky Cabinet for Health and Family Services act as a parent" | PSN PDF p. 6 |
| `ky_djj` | Department of Juvenile Justice | "the Department of Juvenile Justice through a legal process" | PSN PDF p. 6 |
| `ky_ksb` | Kentucky School for the Blind | "including the Kentucky School for the Blind (KSB)" | Rule § 1(36) |
| `ky_ksd` | Kentucky School for the Deaf | "the Kentucky School for the Deaf (KSD)" | Rule § 1(36) |
| `ky_ksis` | Kentucky Student Information System | "Kentucky Student Information System (KSIS), also known as Infinite Campus" | GUIDE p. 1 |
| `ky_spin` | Kentucky Special Parent Involvement Network | "Kentucky Special Parent Involvement Network (KY-SPIN)" | GUIDE p. 6 |
| `ky_kar` | Kentucky Administrative Regulations | "Kentucky Administrative Regulations (KARs)" | GUIDE p. 1 |
| `ky_sped_mentor` | Special education mentor | ""Special education mentor" means individuals with exceptional expertise, experience" | Rule § 1(57) |
| `ky_cap` | Corrective action plan | "Corrective action plan or "CAP" means a written improvement plan" | Rule § 1(18) |
| `ky_compliance_report` | Compliance monitoring report | ""Compliance monitoring report" means a written description of the findings" | Rule § 1(14) |
| `ky_program_of_studies` | Program of Studies | "the Program of Studies, 704 KAR 3:303" | Rule § 1(27)(b) |
| `ky_ksa` | Kentucky Summative Assessment | "the KSA (Kentucky Summative Assessment) test you take every year" | YOUTH p. 43 |
| `ky_aksa` | Alternative Kentucky Summative Assessment | "The AKSA or Alternative Kentucky Summative Assessment is an option" | YOUTH p. 46 |
| `func_hearing_assess` | Functional hearing, listening, and communication assessment | "Functional Hearing, Listening, and Communication Assessment" | YOUTH p. 16 (also p. 15; GUIDE p. 4) |
| `wioa` | Workforce Innovation and Opportunity Act | "Workforce Innovation and Opportunity Act (WIOA) Youth Programs" | YOUTH p. 47 |
| `smart_goals` | SMART goals | "you will probably hear them say, "S.M.A.R.T. Goals."" | YOUTH p. 25 |
| `meas_method` | Methods of measurement | "You will list these Methods of Measurement underneath the Annual Measurable Goal" | YOUTH p. 31 |
| `meas_direct` | Direct measure | "Direct Measure is when a teacher or" | YOUTH p. 32 |
| `meas_indirect` | Indirect measure | "Indirect Measures is a review of" | YOUTH p. 32 |
| `meas_authentic` | Authentic assessment | "Authentic Assessment is when your" | YOUTH p. 32 |

New strings on existing concepts (tagged US-KY unless noted): "Admissions and Release Committee", "ARC" and "ARC meeting" (`iep_team`); "Kentucky Multi-Tiered System of Supports" and "KyMTSS" (`mtss`); "emotional-behavioral disability" and "emotional-behavior disability" (`ed`); "mental disability" (legacy), "mild mental disability", "functional mental disability", "MMD", "FMD" (`id`); "exceptional children" (`exc_student`); "teacher of exceptional children" (`sped_teacher`); "DoSE" (`sped_admin`); "state special education advisory panel" (`state_panel`); "Kentucky Procedural Safeguards Notice" and "Procedural Safeguard Notice" (`safeguards_notice`); "high school diploma" (`std_diploma`); "home school" (`home_education`); "perceptual/motor disabilities" (`perceptual`); "impaired articulation" (`artic`); "resource classes" (`resource_room`); "private school children with disabilities" (`ppps`); "specially-designed instruction" (`sdi`); "functional vision/learning media assessment" and "functional vision and learning media assessment" (`fva`); "short-term instructional objectives" (`sto`); "supports for school personnel" (`program_mods`). Untagged (national) additions: "adverse effect" (`adverse`), "change of placement because of disciplinary removals" (`cop`), "state formal written complaint" and "formal written complaint" (`state_complaint`), "homeless child or youth" (`homeless`).

## 3. Unsure
- **Wording-only attestations** (the cited wording differs from the concept's name; I judged them the same idea): `consent` (Rule § 1(15) defines "Consent" for a parent; YOUTH p. 64 prints "Informed" and "consent" in separate columns); `slp` (§ 1(51)(a) "speech-language pathology and audiology services"); `social_work` (§ 1(51)(b) "social work services in school"); `postsecondary` (YOUTH p. 17 "Postsecondary Goal(s)"); `regular_class` (YOUTH p. 52 labels it "General Education" and says "regular classroom"); `hospital_instr` (YOUTH p. 52 "Hospital/Institution Instruction"); `self_det` (YOUTH p. 4 "self-advocacy").
- **Mental disability.** Kentucky's current rule still names the category "mental disability" with mild (MMD) and functional (FMD) subtypes; it does not use "intellectual disability". I put them under `id` (the existing "mental disability" string is typed legacy for Delaware, so I matched that type) and typed the two longer forms as synonyms. A reviewer may want MMD and FMD as their own concepts under `id`.
- **"emotional-behavior disability"** (§ 1(5) and (9)) is a one-word variant of the category name used in § 1(24); it may be a drafting slip, but it is in the text so it is recorded.
- **`std_diploma` + "high school diploma"** (§ 1(30)): the rule defines "high school diploma" against a certificate of completion or GED. Reviewer to confirm it is a synonym of "standard high school diploma". `cert_completion` and `ged` are attested from the same sentence, where they are named as things the diploma is not.
- **"home school"** (§ 1(31)) is defined "for purposes of 707 KAR Chapter 1 only" as a private school conducted in a residence; I recorded it as a synonym of `home_education`.
- **`state_complaint`**: I attested it from the PSN (heading and "state formal written complaint" wording, PDF pp. 12-13). I did **not** attest it from the rule's "Complaint" definition (§ 1(12)), which is a written allegation that an LEA violated IDEA and could be read either way.
- **Functional vision.** YOUTH p. 14 and GUIDE p. 4 print the combined heading "Functional Vision and Learning Media Assessment". I attached it to `fva` as two strings; `lma` (learning media assessment) exists and could take it instead.
- **KY-SPIN** is described only as a statewide non-profit that gives special-education information. Neither document says it is Kentucky's federally funded parent training and information center, so I did not set `broader: pti`.
- **Currency.** The PSN cover is dated 2008 and still names the "Cabinet for Health and Family Services"; the rule (2023) still uses "Cabinet for Families and Children", which is the older name (recorded as legacy). KDE's Office of Special Education and Early Learning (GUIDE) is the office name in 2025; older documents may call it by another name.
- **General ideas that carry a single-state tag** and were attested here: `co_special_factors` (Consideration of Special Factors; 34 CFR 300.324(a)(2), YOUTH p. 21) and `dc_educ_rep` (educational representative, YOUTH p. 19). The maintainers may want to drop their single-state tags.
- **Categories.** `ky_ksa` and `ky_aksa` are `iep_component`, following `wv_wvgsa`. `ky_program_of_studies` is `academic_skill`, following the Missouri learning-standards concept.
- **Page citations.** The PSN's cited pages are PDF pages (printed = PDF - 3). YOUTH has no printed pages. Rule citations are by definition number.
- **PSN edition** (2008 cover, 2023 metadata): `doc_id` is `ky-psn-2008`.

## 4. Risky
- **Auto-flagged high risk (place_name):** every new full phrase that begins with "Kentucky" (the Department of Education, both schools, the Student Information System, KY-SPIN, the Administrative Regulations, both summative assessments) and the manual `place_name` flag on the two schools. All are `never_bare`: only the full phrase is protected. `KY-SPIN` contains the postal code.
- **Acronyms.** New US-KY acronyms: KDE, OSEEL, ECAB, KSB, KSD, KSIS, KY-SPIN, KAR, KARs, KSA, AKSA, KyMTSS, ARC, CAP, DoSE, MMD, FMD. The build found no collision with another state's string. **`CAP` (Rule § 1(18)) collides with the first name "Cap" in the name dictionary (low risk, `phrase_only`). The contributor approved it and added "CAP" to the known all-caps collisions in `tests/test_match.py`; this is a change to a safety test's allowed list, so a reviewer should confirm it.** It matches case-sensitively, so the name "Cap" is not protected. `ARC` also looks like "The Arc" (existing `arc_il` and `co_arc` concepts are mixed-case phrases). `SMART goals` carries `common_english_word` (the name dictionary lists "Smart" as a surname; the phrase is phrase-only).
- **Phrases with name words:** "Department of Juvenile Justice" and "Office of Special Education and Early Learning" are low risk and `phrase_only` (the words Justice and Early are surnames or given names). Three new strings on existing concepts hit the name dictionaries at low risk: "high school diploma" (high), "short-term instructional objectives" (short) and the two "functional vision … learning media assessment" forms (media). They are phrase-only, so the bare words are not protected.
- No eponyms; no acronym that is a given name that I could find.

## 5. Left out
- Addresses, phone numbers, web addresses, the Frankfort street address and the complaint mailing address (the Division is named; the address is not).
- "First Steps" as a Kentucky concept: the string already exists as Indiana's `in_first_steps` and the build forbids the same string on two concepts. The existing string already protects the phrase; the PSN (p. 19) only says "First Steps". Attesting Indiana's concept for Kentucky would conflate two programs.
- Product and brand names: Infinite Campus (named beside KSIS), C-Print, Type Well.
- Case-law-style and person-named items: the OSEP policy letters to Nix and Zirkel, the OSEP Memo 11-07 title.
- Titles of documents I did not read: the Kentucky Guide to Special Education Due Process, KDE's Guidance Document for Individual Education Program (IEP) Development, KSIS Data Standards, KDE's guidance on alternate-assessment participation.
- Rule and statute citations as terms (707 KAR 1:320, 704 KAR 3:305, KRS 157.197, 34 CFR): the abbreviation "KRS" is never spelled out in the documents, so I did not invent an expansion.
- General-English or single-word definitions: collaboration, compliance, monitoring, enforcement, sanctions, withholding, functional, business day (already a synonym of `school_day`), caseload for special classes, class size for resource classes, qualified personnel, public expense, reasonable efforts to obtain voluntary compliance.
- OHI conditions with no SPEDLex concept (AIDS, asthma, diabetes, heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, tuberculosis); the ones that exist (ADHD, epilepsy, sickle cell, Tourette) are attested.
- Federal-model text in the PSN that names no Kentucky concept (attorneys' fees, civil action, time limits).
- Form-field vocabulary in the Youth Guide: Type of Service, Service Minutes, Service Frequency, Service Period, Service Provider, Start/End Date, rubric, time sampling, interval recording, and the supports list (visual prompts, chunking, scaffolding, manipulatives, preferential seating, listening guides, paraphrasing). Several are generic English; the common accommodations that already have a concept are attested.
- The "Center for Parent Information & Resources" and "Technical Assistance Network" in GUIDE p. 6 (a federal center and a generic program name).
- Present-levels domain headings that are plain English (Communication, Academic, Social and Emotional Status, General Intelligence, Health, Vision, Hearing, Motor Abilities).
- Student names: none appear in the documents except first names in the Youth Guide's worked examples, which were not used.
- A Kentucky state card and comparison-table column in `site/template.html` (optional step in CONTRIBUTING.md) were not added.

## 6. Possibly disfavored
None. None of the four documents says a term was replaced by rule or as offensive. (The rule keeps "mental disability" and the PSN names an agency, now the Cabinet for Health and Family Services, that the rule still calls the Cabinet for Families and Children; the second is a renamed agency, recorded as `legacy`, not disfavored.)
