# New Hampshire layer (v0.27.0): contributor report

Drafted 2026-10-06 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` and CONTRIBUTING.md. A person must review this before it is submitted.

## 1. Documents read
- **RULE**: NH Special Education Reference Manual, Bureau of Special Education Support, 257 pp., "accurate as of October 20, 2023". It reprints the Ed 1100 rules with the matching RSA and 34 CFR text inserted after each rule. **This is the Department's compiled copy, not the official text** from the Office of Legislative Services. Records cited to it are typed `state_regulation`, so they are `machine_validated`; see Unsure below. Read in full: the Ed 1102 definitions, Ed 1103.01, Ed 1107.04 (Table 1100.1), Ed 1111.02-1111.04 (Tables 1100.2-1100.3), Ed 1113.12-13 and Ed 1122.02. The rest was read by heading and searched.
- **PSN**: Special Education Procedural Safeguards Handbook, updated December 20, 2024, 62 pp. Pages 1-4 and 33-35 were read in full and the rest searched.
- **PAGE**: Bureau of Special Education Support web page, read as page text.
- **Missing**: no separate parent guide was found. The PSN and the Bureau page cover the parent-facing material.
- **How the files were read**: same method as Michigan. pdf.js was blocked on education.nh.gov, so the text was extracted after download. Copies are in `.sources-cache/nh/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `nh_doe` | New Hampshire Department of Education | "(b) “Department” means the New Hampshire department of education . (c) “Destruction,” in reference to" | N.H. Code Admin. R. Ed 1102.02(b) (NH Special Education Reference Manual, Oct. 2023, p. 24) |
| `nh_bsess` | Bureau of Special Education Support | "Alphabetical List Contact Us Bureau of Special Education Support The Bureau of Special Education Support" | NHED Bureau of Special Education Support page |
| `nh_olh` | Office of Legislation and Hearings | "information, please call the Office of Legislation and Hearings at (603) 271-2299. Mediation - See" | NH Special Education Procedural Safeguards Handbook (Dec. 2024), PDF p. 34 |
| `nh_dcyf` | Division for Children, Youth and Families | "they mediate. (g) “ Division for children, youth and families ” (DCYF) means the division" | N.H. Code Admin. R. Ed 1102.02(g) (NH Special Education Reference Manual, Oct. 2023, p. 25) |
| `nh_ose_advocate` | Office of the Special Education Advocate | "Telephone: (603) 271-3741 www.education.nh.gov Office of the Special Education Advocate Governor Gallen Office Park Johnson" | NH Special Education Procedural Safeguards Handbook (Dec. 2024), PDF p. 4 |
| `nh_pic` | Parent Information Center | "or Low-Cost Assistance/ Resources Parent Information Center (PIC) 54 Old Suncook Road Concord, NH 03301" | NH Special Education Procedural Safeguards Handbook (Dec. 2024), PDF p. 4 |
| `nhseis` | New Hampshire Special Education Information System | "or youth. (d) “ New Hampshire Special Education Information System ” (NHSEIS) means a computer-based" | N.H. Code Admin. R. Ed 1102.04(d) (NH Special Education Reference Manual, Oct. 2023, p. 43) |
| `nh_sau` | School administrative unit | "that school districts or school administrative unit s, or both, are able to enter into" | N.H. Code Admin. R. Ed 1102.01(v) (NH Special Education Reference Manual, Oct. 2023, p. 23) |
| `nh_collab` | Collaborative program | "attending school. (v) “ Collaborative program ” means the cooperative agreements that school districts or" | N.H. Code Admin. R. Ed 1102.01(v) (NH Special Education Reference Manual, Oct. 2023, p. 23) |
| `nh_sending` | Sending district | "to serve. V. " Sending district " shall mean any school district or portion thereof" | N.H. Code Admin. R. Ed 1102.05(c) (NH Special Education Reference Manual, Oct. 2023, p. 49) |
| `nh_receiving` | Receiving district | "Qualified Examiners. (r) “ Receiving district ” means “receiving district” as defined in RSA 193:27,V." | N.H. Code Admin. R. Ed 1102.04(r) (NH Special Education Reference Manual, Oct. 2023, p. 48) |
| `nh_chartered` | Chartered public school | "(p) “ Chartered public school ” means “chartered public school” as defined in RSA 194-B:1," | N.H. Code Admin. R. Ed 1102.01(p) (NH Special Education Reference Manual, Oct. 2023, p. 19) |
| `nh_public_academy` | Public academy | "public school or a public academy . (l) “Private school” means any school that meets" | N.H. Code Admin. R. Ed 1102.04(n) (NH Special Education Reference Manual, Oct. 2023, p. 47) |
| `nh_private_provider` | Private provider of special education | "public kindergarten. (k) “ Private provider of special education ” means a private or non-district" | N.H. Code Admin. R. Ed 1102.04(k) (NH Special Education Reference Manual, Oct. 2023, p. 47) |
| `home_education` | Home education | "IEP team. (c) “ Home education ” means “home education” as defined in RSA 193-A:4," | N.H. Code Admin. R. Ed 1102.03(c) (NH Special Education Reference Manual, Oct. 2023, p. 28) |
| `nh_abi` | Acquired brain injury | "1105. (r) “Child with acquired brain injury ” (ABI) means brain injury that occurs after" | N.H. Code Admin. R. Ed 1102.01(r) (NH Special Education Reference Manual, Oct. 2023, p. 19) |
| `nh_func_blind` | Functionally blind | "sensory areas. (v) “ Functionally blind ” means “functionally blind” as defined in RSA 186-C:2,VI." | N.H. Code Admin. R. Ed 1102.02(v) (NH Special Education Reference Manual, Oct. 2023, p. 27) |
| `nh_qual_examiner` | Qualified examiner | "being determined. (q) “ Qualified examiner ” means a person licensed or certified in the" | N.H. Code Admin. R. Ed 1102.04(q) (NH Special Education Reference Manual, Oct. 2023, p. 48) |
| `nh_saif` | Specialist in the assessment of intellectual functioning | "and services. (h) “ Specialist in the assessment of intellectual functioning ” (SAIF) means a" | N.H. Code Admin. R. Ed 1102.05(h) (NH Special Education Reference Manual, Oct. 2023, p. 53) |
| `school_psych` | School psychologist | "AUTISM Academic Performance Associate School Psychologist Certified Educator Guidance Counselor Psychologist S.A.I.F.** School Psychologist Adaptive" | N.H. Code Admin. R. Ed 1107.04 (NH Special Education Reference Manual, Oct. 2023, p. 75) |
| `nh_assoc_school_psych` | Associate school psychologist | "Examiners AUTISM Academic Performance Associate School Psychologist Certified Educator Guidance Counselor Psychologist S.A.I.F.** School Psychologist" | N.H. Code Admin. R. Ed 1107.04 (NH Special Education Reference Manual, Oct. 2023, p. 75) |
| `nh_fcess` | Family centered early supports and services | "employment available. (p) “ Family centered early supports and services ” means the array of" | N.H. Code Admin. R. Ed 1102.02(p) (NH Special Education Reference Manual, Oct. 2023, p. 26) |
| `nh_admin_case_mgmt` | Administrative case management | "as amended. (d) “ Administrative case management ” means the following activities that are not" | N.H. Code Admin. R. Ed 1102.01(d) (NH Special Education Reference Manual, Oct. 2023, p. 10) |
| `nh_neutral_conf` | Neutral conference | "of Education. (e) “ Neutral conference ” means “neutral conference” as defined in RSA 186-C:23-b." | N.H. Code Admin. R. Ed 1102.04(e) (NH Special Education Reference Manual, Oct. 2023, p. 43) |
| `nh_committed_juvenile` | Committed juvenile student | "with disabilities. (w) “ Committed juvenile student ” means an individual who is committed to" | N.H. Code Admin. R. Ed 1102.01(w) (NH Special Education Reference Manual, Oct. 2023, p. 23) |

All quotes come from text extracted with pdftotext (or page text for web pages), with line breaks collapsed. Page-header text sometimes runs into a quote. Every new string and every attested key was checked automatically: the string had to appear in the cited section or page. All checks passed.

## 3. Unsure
- **Source status**: the rule text comes from the Department's compiled manual, not the official Ed 1100 publication, but it is typed `state_regulation`. If the project wants only official regulation text to become `machine_validated`, change the RULE source type to `state_guidance`, or check the 21 records against the official rules first.
- "Acquired brain injury" (`nh_abi`) was made its own disability_category concept. New Hampshire counts it as a disability alongside TBI; it was not put under `tbi`.
- "Functionally blind" was placed under `vi` as a narrower concept. It comes from an RSA definition (RSA 186-C:2, VI) and is not an IDEA category.
- `home_education` (with "homeschooling") and `school_psych` were made national concepts.
- "Other health impaired" was added to `ohi` as a spelling variant, untagged.
- "Speech-language specialist" (Table 1100.1) attests the existing New Jersey concept `nj_sls`. The key keeps its `nj_` prefix because keys never change.

## 4. Risky
- **DCYF** now has two meanings: Washington's Department of Children, Youth, and Families and New Hampshire's Division for Children, Youth and Families. The build reports this as an allowed ambiguity.
- **Place names** (high risk): New Hampshire Department of Education, New Hampshire Special Education Information System.
- **Acronyms**: ABI, SAIF, PIC, ESP, SAC and NHSEIS are tagged US-NH. "Abi" and "Saif" are given names elsewhere, but neither is in the test name list, so the collision test passes. A reviewer may still want to flag them.

## 5. Left out on purpose
- **SAU**: the sources use it without ever spelling it out as "school administrative unit (SAU)". The concept `nh_sau` was added without the acronym.
- **NHED**: the PSN uses it for the Department without defining it.
- **"Disabilities Right Center, Inc."** (PSN p. 4): the name appears to be printed in a form that isn't the organization's own.
- "Bureau of Special Education" (PSN p. 4) is already a Pennsylvania-only concept (`bse`).
- The PSN's addresses and phone numbers.
