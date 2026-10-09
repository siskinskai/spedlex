# Ohio layer (v0.29.0): contributor report

Drafted 2026-10-07 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` and CONTRIBUTING.md. A person must review this before it is submitted.

## 1. Documents read
- **RULE**: Operating Standards for the Education of Children with Disabilities, DEW booklet dated June 2025, 185 pp. It contains Ohio Adm.Code 3301-51-01 to 3301-51-11 and 3301-51-21. Read in full: 3301-51-01 (definitions), 3301-51-05(K) (dispute resolution), 3301-51-09 (delivery of services) and 3301-51-11 (preschool). The other rules were read by paragraph heading and searched.
- **PR**: A Guide to Parent Rights in Special Education: Special Education Procedural Safeguards Notice, April 2025, 36 pp. This is both Ohio's safeguards notice and its main parent guide. Pages 1-5, 13-14 and 35-36 were read in full and the rest searched. Citations use PDF pages; the printed numbers are one lower.
- **How the files were read**: both PDFs were linked from DEW's "Operating Standards and Guidance" page. They were downloaded through the browser, checked by SHA-256 and converted to text, with ligatures (ff, fi) normalized. Copies are in `.sources-cache/oh/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `oh_dew` | Ohio Department of Education and Workforce | "resolve the problem. The Ohio Department of Education and Workforce ’s Office for Exceptional Children" | DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 13 |
| `oh_oec` | Office for Exceptional Children | "of Education and Workforce’s Office for Exceptional Children can get involved and assist you with" | DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 13 |
| `oh_sst` | State Support Team | "you: • Your local State Support Team (Region #____) at (phone #____________).The parent and family" | DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 13 |
| `oh_ocecd` | Ohio Coalition for the Education of Children with Disabilities | "more information, contact_______________________________________. • Ohio Coalition for the Education of Children with Disabilities (OCECD) o" | DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 14 |
| `oh_county_bdd` | County board of developmental disabilities | "district, a nonpublic school, county board of developmental disabilities (county board of DD), other educational" | Ohio Adm.Code 3301-51-01(B)(14) |
| `oh_odys` | Ohio Department of Youth Services | "enrollment school district, the Ohio department of youth services , or provider for the "Autism" | Ohio Adm.Code 3301-51-01(B)(18) |
| `oh_jvsd` | Joint vocational school district | "of youth services, and joint vocational school district s; (b) Juvenile justice facilities, educational service" | Ohio Adm.Code 3301-51-01(B)(44) |
| `oh_district_of_service` | School district of service | "of residence. (59) " School district of service " means a school district that is" | Ohio Adm.Code 3301-51-01(B)(59) |
| `charter_school` | Charter school | "or funding. (8) " Charter school " or "community school" has the meaning given the" | Ohio Adm.Code 3301-51-01(B)(8) |
| `oh_chartered_nonpublic` | Chartered nonpublic school | "same meaning as " chartered nonpublic school ." (9) "Chartered nonpublic school" means a school" | Ohio Adm.Code 3301-51-01(B)(9) |
| `oh_osd` | Ohio School for the Deaf | "of education, including the Ohio school for the deaf and the Ohio state school for" | Ohio Adm.Code 3301-51-01(B)(64) |
| `oh_ossb` | Ohio State School for the Blind | "the deaf and the Ohio state school for the blind . (65) "Supplementary aids and" | Ohio Adm.Code 3301-51-01(B)(64) |
| `oh_ohi_major` | Other health impairment - major | "with disabilities. (45) " Other health impairment - major " means a child whose condition" | Ohio Adm.Code 3301-51-01(B)(45) |
| `oh_ohi_minor` | Other health impairment - minor | "Revised Code. (46) " Other health impairment - minor " means a child whose condition" | Ohio Adm.Code 3301-51-01(B)(46) |
| `oh_intervention_specialist` | Intervention specialist | "teacher and one licensed intervention specialist . (i) Both teachers are assigned to the classroom" | Ohio Adm.Code 3301-51-11 |
| `oh_ttw` | Transition to Work endorsement | "either: (i) Obtain the Transition to Work endorsement as defined in rule 3301-24-05 of the" | Ohio Adm.Code 3301-51-09(H)(7) |
| `oh_admin_review` | Administrative review | "(K) Dispute resolution (1) Administrative review s (a) Administrative reviews are recommended, but cannot be" | Ohio Adm.Code 3301-51-05(K)(1) |
| `oh_early_complaint` | Early complaint resolution | "OCECD website at www.ocecd.org. Early Complaint Resolution Early complaint resolution is when you attempt to" | DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 14 |
| `oh_autism_scholarship` | Autism Scholarship Program | "tell you about the Autism Scholarship Program and the Jon Peterson Scholarship Program. AUTISM SCHOLARSHIP" | DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 36 |
| `oh_jon_peterson` | Jon Peterson Special Needs Scholarship Program | "box, or email autismscholarship@education.ohio.gov. JON PETERSON SPECIAL NEEDS SCHOLARSHIP PROGRAM If your child is receiving" | DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 36 |

All quotes come from text extracted with pdftotext, with line breaks collapsed. Page-header and contact-list text sometimes runs into a quote. Every new string and every attested key was checked automatically against the cited section or page, and all checks passed.

## 3. Unsure
- **`charter_school`** is a new national concept with "community school" as an Ohio synonym. New Hampshire's `nh_chartered` and DC's `dc_pcs_lea` now list it as `broader` (DC keeps `lea` too). `oh_chartered_nonpublic` is deliberately not linked: the rule says it is not a charter school.
- **"State residential school"** was first drafted as its own concept, then moved onto the existing `state_sp_sch` (State special schools) as an Ohio synonym. The draft ID SPED:000860 is marked retired in `data/concept_ids.tsv`, following the precedent of `ct_srbi`. The Ohio School for the Deaf and the Ohio State School for the Blind sit under `state_sp_sch`.
- **OHI major and minor** are funding categories rather than separate disabilities. They are placed under `ohi`.
- **`oh_intervention_specialist`** is placed under `sped_teacher`. Ohio licenses teachers under this title (for example, "Intervention Specialist for..." in 3301-51-11).
- **Existing concepts reused**: "evaluation team report" and "ETR" went on `eval_report`, "educational service center" on `esa` (Texas also uses ESC there), and "school district of residence" on `resident_dist`.

## 4. Risky
- **Eponym**: the Jon Peterson Special Needs Scholarship Program is flagged `eponym`.
- **Place names** (high risk, automatic): Ohio Department of Education and Workforce, Ohio Coalition for the Education of Children with Disabilities, Ohio Department of Youth Services, Ohio School for the Deaf, Ohio State School for the Blind.
- **`oh_sst`** (State Support Team): its acronym SST is deliberately not added, because SST is already the student support team acronym.

## 5. Left out on purpose
- "Educational agency" and "Other educational agency". Ohio defines both, but they are ordinary phrases.
- Funding definitions such as "average daily membership" and "excess costs".
- The PR guide's blank regional contact lines.
- **Possible additions (missed terms)**: "county board of DD" (the rule's short form for `oh_county_bdd`), "parent mentor" variants, and the Ohio caseload terms in 3301-51-09(I).
