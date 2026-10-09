# New Jersey layer (v0.26.0): contributor report

Drafted 2026-10-06 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` and CONTRIBUTING.md. A person must review this before it is submitted.

## 1. Documents read
- **CODE**: N.J.A.C. 6A:14, Special Education. This is NJDOE's current-code PDF, 179 pp. Subchapters 1, 3 and 4 were read in full. Subchapters 2 and 5-10 were read by heading and searched.
- **PRISE**: Parental Rights in Special Education (PTM 1506.13), revised June 2026, 69 pp. This is New Jersey's safeguards notice and main parent guide. Pages 1-6 and 41-47 were read in full and the rest searched. Citations use PDF pages.
- **PAGE**: NJDOE "Parental Rights and Engagement" web page, read as page text.
- **How the files were read**: same method as Michigan. Copies are in `.sources-cache/nj/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `nj_doe` | New Jersey Department of Education | "of Education" means the New Jersey Department of Education . "District board of education" means," | N.J.A.C. 6A:14-1.3 |
| `nj_osepdr` | Office of Special Education Policy and Dispute Resolution | "resides. “Office” means the Office of Special Education Policy and Dispute Resolution in the Department" | N.J.A.C. 6A:14-1.3 |
| `nj_county_office` | County office of education | "of Education through the county office of education (county office); and 3. For a period" | N.J.A.C. 6A:14-4.9(a) |
| `nj_dboe` | District board of education | "disabilities placed by the district board of education responsible for providing their education. "Assistive technology" | N.J.A.C. 6A:14-1.3 |
| `nj_csssd` | County special services school district | "following settings: i. A county special services school district ; ii. An educational services commission;" | N.J.A.C. 6A:14-4.3(b)5 |
| `nj_esc` | Educational services commission | "school district; ii. An educational services commission ; iii. A jointure commission; and iv. A" | N.J.A.C. 6A:14-4.3(b)5 |
| `nj_jointure` | Jointure commission | "services commission; iii. A jointure commission ; and iv. A New Jersey approved private school" | N.J.A.C. 6A:14-4.3(b)5 |
| `nj_cbvi` | New Jersey Commission for the Blind and Visually Impaired | "be reported to the New Jersey Commission for the Blind and Visually Impaired ." | N.J.A.C. 6A:14-3.5(c)14 |
| `nj_oal` | Office of Administrative Law | "judge (ALJ) from the Office of Administrative Law (OAL). Who may ask for a due" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 22 |
| `nj_span` | Statewide Parent Advocacy Network | "contact information for the Statewide Parent Advocacy Network (SPAN), Disability Rights New Jersey (DRNJ), the" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 3 |
| `nj_drnj` | Disability Rights New Jersey | "Parent Advocacy Network (SPAN), Disability Rights New Jersey (DRNJ), the County Offices of the New" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 3 |
| `nj_dvrs` | Division of Vocational Rehabilitation Services | "Follow-Up Support Services Division of Vocational Rehabilitation Services (DVRS) in the New Jersey Department of" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 44 |
| `nj_ddd` | Division of Developmental Disabilities | "292-8347 TTY: (609) 292-2919 Division of Developmental Disabilities in the New Jersey Department of Human" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 44 |
| `nj_csoc` | Children's System of Care | "of Children and Families: Children's System of Care DCF's Children's System of Care, (CSOC), (formerly" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 45 |
| `nj_ddhh` | Division of the Deaf and Hard of Hearing | "Division of the Deaf and Hard of Hearing in the New Jersey Department of Human" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 46 |
| `nj_dds` | Division of Disability Services | "588-2648 FAX: (609)-588-2528 Website Division of Disability Services in the New Jersey Department of Human" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 46 |
| `nj_sepag` | Special Education Parent Advisory Group | "Support Specialist Community-Based Resources Special Education Parent Advisory Group (SEPAG) BRIDGE Initiative for Engaging Parents" | NJDOE Parental Rights and Engagement page |
| `nj_ldtc` | Learning disabilities teacher-consultant | "a school psychologist, a learning disabilities teacher-consultant , and a school social worker. All child" | N.J.A.C. 6A:14-3.1(b) |
| `nj_sls` | Speech-language specialist | "N.J.A.C. 6A:14 Appendix C." Speech-language specialist " means speech-language specialist or speech-language specialist-equivalent. "Statewide assessment"" | N.J.A.C. 6A:14-1.3 |
| `referral` | Referral | "an adult student. " Referral " means the written request for an initial evaluation to" | N.J.A.C. 6A:14-1.3 |
| `nj_social_maladj` | Social maladjustment | "related services. 11. " Social maladjustment " means a consistent inability to conform to the" | N.J.A.C. 6A:14-3.5(c)11 |
| `nj_eligible_sls` | Eligible for speech-language services | "speech-language services (a) " Eligible for speech-language services " means a speech and/or language disorder" | N.J.A.C. 6A:14-3.6(a) |
| `nj_icr` | In-class resource program | "instruction is given. (d) In-class resource program s and pull-out replacement resource programs are programs" | N.J.A.C. 6A:14-4.6(i) |
| `nj_pullout` | Pull-out replacement resource program | "In-class resource programs and pull-out replacement resource program s are programs of specialized instruction organized" | N.J.A.C. 6A:14-4.6(d) |
| `nj_supp_instr` | Supplementary instruction | "6A:14-4.6 Program criteria: supplementary instruction and resource programs (a) Supplementary instruction is provided to students" | N.J.A.C. 6A:14-4.6(a) |
| `nj_njsls` | New Jersey Student Learning Standards | "offer instruction in the New Jersey Student Learning Standards unless the IEP specifies a modified" | N.J.A.C. 6A:14-4.7(a) |
| `nj_emergent` | Emergent relief | "is available. APPLICATION FOR EMERGENT RELIEF What is emergent relief? Emergent relief is a request" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 25 |
| `cbi` | Community-Based Instruction | "the transition-related topics of Community-Based Instruction , and Person-Centered Approaches through a partnership with The" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 43 |
| `nj_sle` | Structured learning experience | "on Person Centered Approaches. Structured Learning Experience (SLE) Structured learning experience means experiential, supervised in-depth" | NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. 43 |

All quotes come from text extracted with pdftotext (or page text for web pages), with line breaks collapsed. Page-header text sometimes runs into a quote. Every new string and every attested key was checked automatically: the string had to appear in the cited section or page. All checks passed.

## 3. Unsure
- **Child study team**: in New Jersey this is the evaluation team (school psychologist, LDT-C and school social worker). The list already has "child study team" as a synonym on `sst` (student support team) and "case manager" on `sped_teacher`. Neither was changed. Both mappings look questionable for New Jersey, and a reviewer should decide.
- **Social maladjustment** (`nj_social_maladj`) was made a disability_category concept. Under the federal definition it is an exclusion, not an eligibility category, but N.J.A.C. 6A:14-3.5(c)11 defines it as its own eligibility category.
- "Emotional regulation impairment" was put on `ed` and "communication impairment" on `sli`. These are New Jersey's current labels for those categories.
- "Multilingual learner" was added to `lep` untagged, because the term is used nationally.
- `referral` and `cbi` (Community-Based Instruction) were made national concepts.

## 4. Risky
- **DDS** now has three meanings: DC Department on Disability Services, NJ Division of Disability Services and CT Department of Developmental Services. The build reports this as an allowed ambiguity.
- **Common English words**: SPAN (`nj_span`) and Referral (`referral`) are flagged `common_english_word`.
- **Place names**: New Jersey Department of Education, New Jersey Commission for the Blind and Visually Impaired, Disability Rights New Jersey and New Jersey Student Learning Standards are high risk.
- **Acronyms**: OAL, DRNJ, DVRS, DDD, CSOC, DDHH, SEPAG, CBI, SLE and PRISE are tagged US-NJ.

## 5. Left out on purpose
- The State Board members and NJDOE officials named on PRISE pp. 1-2 (personal names listed with their counties).
- The Boggs Center, which is named for a person. It could be added later as an eponym if wanted.
