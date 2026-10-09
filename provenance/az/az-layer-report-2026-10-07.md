# Arizona layer (v0.33.0): contributor report

Drafted 2026-10-07 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` should be run on it in a fresh conversation, ideally with a different model.

## 1. Documents read
- **RULE**: Ariz. Admin. Code R7-2-401, from the Secretary of State's 7 A.A.C. 2 (Supp. 25-4, 186 pp.). Only R7-2-401 was read (in full); the rest of the chapter is general education rules. Its subsections are lettered B (definitions) through P.
- **PSN**: ADE IDEA Part B Procedural Safeguards Notice (Rev. 08-28-25, 30 pp.). P. 1 was read in full and the rest searched; it follows the federal model notice.
- **HWY**: Traveling the Special Education Highway (ADE/ESS, revised 2019, 17 pp.), the parent guide. Read in full.
- **GLOSS**: ESS Glossary of Acronyms and Terms (revised May 2026, 60 pp.). It was searched. It is a three-column table, and pdftotext breaks many multi-word names across columns, so it is cited only where a name appears unbroken.
- **Missing**: Arizona's disability categories are defined in statute (A.R.S. 15-761), which was not provided, so they are cited from HWY p. 7.
- **How the files were read**: the PSN was downloaded through the browser pane and the others were saved by the contributor; all were converted to text with pdftotext. Copies are in `.sources-cache/az/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `az_doe` | Arizona Department of Education | "Disabilities Education Act (IDEA). Arizona Department of Education, Exceptional Student Services 1535 W. Jefferson, Bin" | ADE Traveling the Special Education Highway (2019), PDF p. 16 |
| `az_ess` | Exceptional Student Services | "Arizona Department of Education, Exceptional Student Services 1535 W. Jefferson, Bin 24 Phoenix, AZ 85007" | ADE Traveling the Special Education Highway (2019), PDF p. 16 |
| `az_dru` | Dispute Resolution Unit | "by contacting the ADE/ESS, Dispute Resolution Unit; and, a procedure facilitated by a trained, objective," | ADE Traveling the Special Education Highway (2019), PDF p. 14 |
| `az_encircle` | Encircle Families | "child's education and development. Encircle Families (formerly Raising Special Kids) is the PTI center in" | ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 45 |
| `az_dra` | Disability Rights Arizona | "Protection and Advocacy Agency: Disability Rights Arizona 5025 E. Washington St, Suite 202 Phoenix, AZ" | ADE IDEA Part B Procedural Safeguards Notice (Rev. 08-28-25), PDF p. 1 |
| `az_azeip` | Arizona Early Intervention Program | "refer you to the Arizona Early Intervention Program (AzEIP) for infants and toddlers; or, •" | ADE Traveling the Special Education Highway (2019), PDF p. 3 |
| `az_ahcccs` | Arizona Health Care Cost Containment System | "Medicaid agency, AHCCCS ( Arizona Health Care Cost Containment System), MSBC helps fund services such" | ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 35 |
| `az_accom_school` | Accommodation school | "school district, charter school, accommodation school, state supported institution, or other political subdivision of the" | Ariz. Admin. Code R7-2-401(B)(16) |
| `az_boundaries` | Boundaries of responsibility | "education agency. 3. ' Boundaries of responsibility' means for: a. A school district, the geographical" | Ariz. Admin. Code R7-2-401(B)(3) |
| `az_private_sped_school` | Private special education school | "education agency. 15. ' Private special education school' means a nonpublic educational institution where instruction" | Ariz. Admin. Code R7-2-401(B)(15) |
| `az_mdssi` | Multiple disabilities with severe sensory impairment | "(MIOD) Multiple Disabilities (MD) Multiple Disabilities with Severe Sensory Impairment (MDSSI) Orthopedic Impairment (OI) Other" | ADE Traveling the Special Education Highway (2019), PDF p. 7 |
| `az_psd` | Preschool severe delay | "Other Health Impairments (OHI) Preschool Severe Delay (PSD) Severe Intellectual Disability (SID) Specific Learning Disability" | ADE Traveling the Special Education Highway (2019), PDF p. 7 |
| `az_grad_date` | Estimated date of graduation | "goals; and iii. The estimated date of graduation for the student, including the course of" | Ariz. Admin. Code R7-2-401(G)(4) |
| `az_azsci` | Arizona Science Test | "for all callers. AzSCI Arizona Science Test Arizona's statewide achievement test for Science, administered to" | ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. 10 |

All quotes come from text extracted with pdftotext (or, for COMAR, the saved page text), with line breaks collapsed. Every new string and every attested key was checked automatically against its cited section or page; the few without a literal hit were checked by hand.

## 3. Unsure
- **Intellectual disability categories**: Arizona has three (mild, moderate and severe). Nevada's layer files the same labels as strings under `id`, so these do too, rather than as new concepts.
- **The MOID acronym** comes from GLOSS p. 34. HWY p. 7 prints "MIOD", which looks like a misprint and was left out.
- **`delegation` is now a general concept.** Illinois's "Delegation of Rights" was Illinois-only, but R7-2-401(J)(3) uses the same idea, under A.R.S. 15-773.
- **"Screening" was not mapped.** Arizona's R7-2-401(D) screening is child find screening for possible disabilities. The existing `screening` concept is the federal screening for instructional purposes, which is a different thing.
- **`az_dru` and `az_ess`** are cited to HWY, so they are candidates.
- **GLOSS is dated May 2026** on its cover, although its file name says 2020.

## 4. Risky
- **Place names** (graded high automatically): Arizona Department of Education, Disability Rights Arizona, Arizona Early Intervention Program, Arizona Health Care Cost Containment System, Arizona Science Test and Arizona Office of Administrative Hearings.
- **"SID"** (severe intellectual disability) is also a given name. It was left out; a reviewer could add it later as a known acronym.
- **New all-caps acronyms**: MET, PEA, ADE, ESS, MIID, MOID, MDSSI, PSD, AHCCCS, plus the mixed-case AzEIP and AzSCI. None is in the name lists. "MET" and "PEA" are also ordinary words, but they are matched only in capitals.

## 5. Left out on purpose
- "SID", and HWY's misprint "MIOD".
- "ED-P", "SEAP", "AZ-TAS" and the Arizona State Schools for the Deaf and the Blind, whose full names appear only broken across GLOSS columns. They could be added from a cleaner source.
- The autism category acronym "A" (a single letter), and all addresses and phone numbers.
