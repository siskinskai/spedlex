# Consistency audit across the state layers (2026-10-10)

Auditor: claude-opus-5-5. Scope: the 45 state layers on branch `integrate-ky-me-ms` (all of `main` plus Kentucky, Maine and Mississippi), checked against what the newer layers record. The lexicon's purpose did not change: protect special-education terms from redaction and name them consistently across states. Nothing here adds a new kind of term. The question was whether the layers built early record as much as the layers built later.

Method: counts were taken from `data/spedlex.jsonl` and `data/spedlex.csv`. For states whose documents are in `.sources-cache/`, the documents were searched again for acronyms, defined terms and capitalized names missing from SPEDLex. No term was added unless it was found on the cited page of a document in the manifest.

## 1. The early layers are thinner

The first 19 layers (Texas through Georgia, all read on Oct. 3) attest 36-196 concepts each. Most layers built since Oct. 8 attest 150-375. The later layers record things the early ones mostly skipped: the state agency's acronym and older names, its offices, the state's rule and statute names, other state agencies the documents name, state programs, forms and assessments, and the general terms the rules define.

| State | Concepts attested | Of the 156 federal-core concepts | Strings tagged to the state |
|---|---|---|---|
| Texas | 196 | 50 | 75 |
| California | 95 | 51 | 59 |
| New York | 117 | 58 | 52 |
| Florida | 75 | 46 | 42 |
| Pennsylvania | 71 | 26 | 69 |
| Illinois | 79 | 43 | 21 |
| Georgia | 44 | 29 | 14 |
| Ohio (before this audit) | 46 | 20 | 11 |
| North Carolina (before) | 39 | 22 | 9 |
| Michigan (before) | 93 | 52 | 14 |
| *Later layers, for comparison:* Alabama 237, Delaware 217, Iowa 278, West Virginia 277, New Mexico 245, Kentucky 170, Mississippi 376 | | | |

Attestation counts do not change protection, because a term any layer records is protected everywhere. They do matter for the Lexicon (`lookup`, `check`, `glossary`), which reports what each state calls a thing.

## 2. Added from documents already in hand (0.50.0)

Ohio, North Carolina and Michigan are among the ten largest states, their layers were thin, and their documents are in the manifest. Each got a supplement layer. Every new string was found on its cited page.

- **`ohio_supplement`** (17 new concepts, 3 strings): DEW and the older "Ohio Department of Education"; the Operating Standards; Ohio Administrative Code; Ohio Revised Code; ODJFS; Step Up to Quality (SUTQ); the non-chartered nonpublic school; four preschool settings (public school preschool special education, general education and integrated classes, and non-public school preschool programs); the regular early childhood setting; the re-evaluation team; reader services; the McKinney-Vento Homeless Assistance Act (eponym); the Rehabilitation Act of 1973; and two intellectual-disability criteria.
- **`north_carolina_supplement`** (8 new concepts, 2 strings, and 2 attestations of the new federal-law concepts): NCDPI; the North Carolina State Board of Education; the Department of Juvenile Justice and Delinquency Prevention; LEA Self-Assessment; Developmental Day Centers; Individual Residential Treatment (IRT); Extended Content Standards; the FutureReady Core Course of Study; GEPA.
- **`michigan_supplement`** (2 new, 2 strings): SOAHR (the older name of MOAHR); the MDE Office of Special Education (OSE); Special Education Mediation Services.

From the audits of the three new layers, these general terms were missing from SPEDLex entirely, in every state, and are now added: ESEA, SSI, SSDI, the Social Security Administration, PASS, the IPE, ASVAB, the ACT, English language arts, speech reception threshold, the Bureau of Indian Affairs, targeted case management, RESNA, special instruction (Part C), Unified English Braille, Nemeth Code and fetal alcohol syndrome.

## 3. Large states with no documents in hand

Texas, California, New York, Florida, Pennsylvania, Illinois and Georgia were built from web pages before the source manifest existed. None of their documents is in `.sources-cache/`, and this workspace cannot download from state websites. The terms below are **candidates to look for, not attested terms**. Each one is a common kind of record in the newer layers that SPEDLex lacks for that state. None was added.

| State | Candidates SPEDLex lacks (check against the documents) |
|---|---|
| Texas | State Office of Administrative Hearings (SOAH); Texas School for the Blind and Visually Impaired (TSBVI); Texas School for the Deaf (TSD); Texas Project FIRST; Partners Resource Network; Health and Human Services Commission (HHSC); Texas Workforce Commission; Individual Graduation Committee; Foundation High School Program; STAAR EOC; SHARS |
| California | Student Study Team (SST), Individual Transition Plan (ITP), ERMHS and Behavior Emergency Report (the layer's own docstring defers these four); regional centers; Early Start; Community Advisory Committee; Transition Partnership Program; Procedural Safeguards and Referral Service; Smarter Balanced |
| New York | Subcommittee on Special Education; Board of Cooperative Educational Services (full form of BOCES); Related Services Authorization; SETSS; ACCES-VR; the State Schools for the Blind and for the Deaf; IESP; the 4410 preschool programs; Regional Partnership Centers; Office of Children and Family Services |
| Florida | BEESS; FDLRS; Early Steps; Florida School for the Deaf and the Blind; matrix of services; Family Network on Disabilities; Florida Inclusion Network; Agency for Persons with Disabilities |
| Pennsylvania | Reevaluation Report (RR); PaTTAN; OCDEL; Office of Vocational Rehabilitation (OVR); Chapter 15 service agreement; the Pennsylvania School for the Deaf; the Western Pennsylvania School for Blind Children; annotated IEP |
| Illinois | Illinois Assessment of Readiness (IAR); IDHS (acronym); Illinois School for the Deaf; Illinois School for the Visually Impaired; Equip for Equality; 23 Ill. Adm. Code 226; Regional Office of Education; special education joint agreements/cooperatives |
| Georgia | Babies Can't Wait; Georgia Academy for the Blind; Georgia School for the Deaf; Georgia Vocational Rehabilitation Agency (GVRA); Parent to Parent of Georgia; Office of State Administrative Hearings (OSAH); Georgia Special Needs Scholarship; Georgia Pre-K; DBHDD |

Documents to download into `.sources-cache/<xx>/` (one or two per state cover most of the list: the state's own procedural safeguards notice plus its rule or parent guide). These are the official copies I found; use a newer one if the agency has posted it.

- TX: TEA Notice of Procedural Safeguards (via https://spedtex.tea.texas.gov/notice-of-procedural-safeguards), and the TEA "Overview of Special Education for Parents".
- CA: CDE Notice of Procedural Safeguards, https://www.cde.ca.gov/SP/SE/qa/documents/pseng.pdf, and 5 CCR §3001 (definitions).
- NY: NYSED Procedural Safeguards Notice (July 2017), https://www.nysed.gov/sites/default/files/special-education/nysed-procedural-safeguards-notice-july-2017.pdf, and 8 NYCRR Part 200.
- FL: the FDOE/BEESS Notice of Procedural Safeguards for Parents of Students with Disabilities, and Rule 6A-6.03011 to 6A-6.0361, F.A.C.
- PA: the PDE/PaTTAN Procedural Safeguards Notice, and 22 Pa. Code Chapter 14.
- IL: ISBE Notice of Procedural Safeguards, https://www.isbe.net/SPEDReqNotConForms/nc_proc_sfgrds_34-57j.pdf, and 23 Ill. Adm. Code 226.
- GA: GaDOE Parents' Rights (procedural safeguards), and Ga. Comp. R. & Regs. 160-4-7, https://www.law.cornell.edu/regulations/georgia/Ga-Comp-R-Regs-R-160-4-7-.09.

## 4. Repo-wide issues for the maintainer

1. **Two-letter all-caps acronyms can shelter initials.** METHODOLOGY §4 bars single letters because they would shelter initials, but nothing covers two-letter forms. SPEDLex has 26, and 18 of them are graded `none` and protected as bare tokens: HI, ID, MD, OI, LD, OT, PT, IQ, DB, LS, EC, ER, IU, AU, EI, EF, SS, PR. Many IEPs refer to the student by initials ("LS will..."), and those initials would survive redaction. Mississippi adds DB and LS. One option is to grade every two-letter all-caps string at least `low` (`phrase_only`). That is a change to `spedlex/risk.py`, so it needs a METHODOLOGY update and a test. I did not make it.
2. **Pending all-caps collisions.** CAP (Kentucky; "Cap" is a first name) and ASHA (Mississippi; "Asha") were added to the known list in `tests/test_match.py` at the contributors' instruction. Both still need a reviewer. "ELA" (English language arts) matches "Ela", so it was not added.
3. **21 single-state concepts are now attested by other states.** On Oct. 8 the maintainer made 12 such concepts national. These 21 are candidates for the same decision: Extended educational programming, In-home and community-based training, Staff-to-child ratio, Futures planning, Daily schedules with minimal unstructured time (TX, also NM); State criterion-referenced test (NV, MS); Specialized services for low-incidence disabilities (CA, MS); Neurological impairment (MA, MS); Social maladjustment (NJ, MS); School administrative unit (NH, ME; the Maine branch dropped the tag on the string but the concept is still NH-only); Acquired brain injury (NH, MS); First Steps (IN, MS); Eligibility Determination Team (AL, NM); Integrated classroom (AR, WV); Schedule of Services (AR, NM); Abbreviated school day (CO, ME); Child find coordinator (CO, MS); Consideration of Special Factors (CO, KY, NM); Intermediate educational unit (WY, ME, MS); Underachievement (WV, MS); Determining the Existence of a Specific Learning Disability (NM, MS).
4. **The early layers are not in the manifest.** 19 early layers and 5 supplements cite URLs without a `doc_id`, so `sources/documents.tsv` has no row for any Texas, California, New York, Florida, Pennsylvania, Illinois or Georgia document. The 0.45.0 CHANGELOG entry says "every state layer's sources carry one", which is not accurate.
5. **Same-named agencies.** Mississippi and New Jersey both have a "Division of Vocational Rehabilitation Services (DVRS)". The build forbids one string on two concepts, so Mississippi's was not added. Deciding whether that name becomes national is the maintainer's call.
6. **Fixed here:** `docs/COVERAGE.md` was missing four supplements (Alabama, Arizona, Indiana and Maryland), and the Mississippi branch's coverage totals were one state short.
