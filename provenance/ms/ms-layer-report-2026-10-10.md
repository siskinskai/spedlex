# Mississippi layer report (2026-10-10)

Layer `mississippi` (US-MS), version 0.49.0. Drafted with `claude-sonnet-5-5`. Retrieved 2026-10-10 (the day the files were downloaded). 364 concepts attested, 299 of them already in SPEDLex and 65 new. Records from the rule text are `machine_validated` (27 new); records from the other PDFs are `candidate` (38 new).

Page convention: PDF page numbers throughout (not printed numbers). Printed page equals PDF page in the rule, the Educator Guide and the Family Guide; the Procedural Safeguards notice has no printed numbers after the front matter; in the IEP guidance printed = PDF minus 4 from PDF p. 5; Vol. I uses section-based printed numbers, so only PDF pages are cited. Rule citations give section and paragraph where known; most automatically attested rule citations are at section level only.

## 1. Documents read and missing

Read (all in `.sources-cache/ms/`, git-ignored, listed in `sources/documents.tsv`):

| doc_id | Document | PDF pages | Read how |
|---|---|---|---|
| ms-rule-74-19-2013 | State Board Policy Chapter 74, Rule 74.19 (eff. 2013-09-15; MDE copy) | 340 | Definitions, eligibility, procedures read in full. Funding subparts G and H (pp. 265-292) scanned for named programs and offices only. |
| ms-procedural-safeguards-2025 | Procedural Safeguards notice, rev. 2025-10-21 | 41 | Read in full |
| ms-vol1-eval-elig-2016 | Procedures Vol. I: Child Find, Evaluation and Eligibility (rev. 7/8/16) | 130 | Read in full; local school and detention-center lists in Appendix CF.B not recorded |
| ms-iep-guidance-2020 | IEP Development Guidance (3.3.20) | 108 | Read in full |
| ms-educator-guide-2026 | Educator Guide to Special Education (V5) | 36 | Read in full |
| ms-family-guide-mdr-2025 | Family Guide, Vol. 15: Manifestation Determination Review (V3) | 8 | Read in full; every term it defines is already cited elsewhere, so no record cites it (listed in `UNCITED_DOCS`) |

Missing or not used:

- Later amendments to Rule 74.19. The file is the 2013 text; whether the State Board has amended it since was not checked.
- The Secretary of State copy of the rule (https://www.sos.ms.gov/ACCode/00000427c.pdf, effective Sept. 15, 2013) was found but not downloaded or compared.
- Other volumes of the MDE Procedures for Policy 74.19 (only Vol. I was provided).
- Part C (First Steps, Mississippi State Department of Health, https://msdh.ms.gov/ei): found, not downloaded. First Steps terms come only from the rule.
- MDE alternate-assessment and diploma-pathway web pages: not located as documents. The MAAP-A and diploma terms come from the IEP guidance and rule.
- mdek12.org/OSE and /specialeducation/pp/ could not be fetched from the tools here, so those index pages were not checked for newer editions.

## 2. New concepts

Quotes are at most 15 words and were checked verbatim against the cited PDF page by code. Citation is the section (rule) and PDF page.

| Key | Preferred term | Quote | Citation |
|---|---|---|---|
| `ms_mde` | Mississippi Department of Education | "The Mississippi Department of Education (MDE)" | Rule 74.19, §300.2(b)(1)(i), p. 20 |
| `ms_ose` | Mississippi Department of Education, Office of Special Education | "Office of Special Education (OSE)" | Rule 74.19, Program Improvement Monitoring, Introduction, p. 330 |
| `ms_parent_outreach` | Parent Outreach Division | "Parent Outreach Division Mississippi Department of Education" | Procedural Safeguards (2025), p. 4 |
| `ms_sbe` | Mississippi State Board of Education | "State Board of Education (SBE)" | Rule 74.19, §300.18(b)(2)(i)(D), p. 35 |
| `ms_state_supt` | State Superintendent of Education | "appointed by the State Superintendent of Education" | Rule 74.19, §300.168(a), p. 119 |
| `ms_office_accred` | Office of Accreditation | "Request by the Office of Accreditation, Commission on School Accreditation" | Rule 74.19, Program Improvement Monitoring, p. 333 |
| `ms_csa` | Commission on School Accreditation | "Request by the Office of Accreditation, Commission on School Accreditation" | Rule 74.19, Program Improvement Monitoring, p. 333 |
| `ms_ecp` | Educable Child Program | "Educable Child Program Reviews" | Rule 74.19, Program Improvement Monitoring, p. 333 |
| `ms_msdh` | Mississippi State Department of Health | "Mississippi State Department of Health (MSDH)" | Procedures Vol. I, p. 8 |
| `ms_mdhs` | Mississippi Department of Human Services | "Mississippi Department of Human Services (MDHS)" | Procedures Vol. I, p. 10 |
| `ms_dmh` | Mississippi Department of Mental Health | "Mississippi Department of Mental Health and Regional Community Mental Health Centers" | Procedures Vol. I, p. 8 |
| `ms_mdoc` | Mississippi Department of Corrections | "Mississippi Department of Corrections (MDOC)" | Procedures Vol. I, p. 11 |
| `ms_mscdd` | Mississippi Council on Developmental Disabilities | "The Mississippi Council on Developmental Disabilities" | IEP Guidance (2020), p. 80 |
| `ms_school_blind` | Mississippi School for the Blind | "the Mississippi School for the Blind" | Rule 74.19, Notice of Non-Discrimination, p. 2 |
| `ms_school_deaf` | Mississippi School for the Deaf | "the Mississippi School for the Deaf" | Rule 74.19, Notice of Non-Discrimination, p. 2 |
| `ms_school_arts` | Mississippi School of the Arts | "the Mississippi School of the Arts" | Rule 74.19, Notice of Non-Discrimination, p. 2 |
| `ms_school_math` | Mississippi School for Mathematics and Science | "the Mississippi School for Mathematics and Science" | Rule 74.19, Notice of Non-Discrimination, p. 2 |
| `ms_mod` | Mississippi Occupational Diploma | "Mississippi Occupational Diploma (MOD)" | IEP Guidance (2020), p. 76 |
| `ms_alt_diploma` | Mississippi Alternate Diploma | "Mississippi Alternate Diploma" | IEP Guidance (2020), p. 76 |
| `ms_maap` | Mississippi Academic Assessment Program | "Mississippi Academic Assessment Program-Alternate (MAAP-A)" | IEP Guidance (2020), p. 55 |
| `ms_maap_a` | Mississippi Academic Assessment Program-Alternate | "Mississippi Academic Assessment Program-Alternate (MAAP-A)" | IEP Guidance (2020), p. 55 |
| `ms_aaas` | Mississippi Alternate Academic Achievement Standards | "Mississippi Alternate Academic Achievement Standards (MS AAAS)" | IEP Guidance (2020), p. 26 |
| `ms_ccrs` | Mississippi College and Career Ready Standards | "Mississippi College and Career Ready Standards (MS CCRS)" | IEP Guidance (2020), p. 26 |
| `ms_mtam` | Mississippi Testing Accommodations Manual | "Refer to the Mississippi Testing Accommodations Manual" | IEP Guidance (2020), p. 50 |
| `ms_mkas2` | Mississippi Pre K-3 Assessment Support System | "Mississippi Pre K-3 Assessment Support System (MKAS2)" | IEP Guidance (2020), p. 63 |
| `ms_kra` | Kindergarten Readiness Assessment | "including the Kindergarten Readiness Assessment and Third Grade MAAP ELA Assessment" | IEP Guidance (2020), p. 58 |
| `ms_cpas2` | Mississippi Career Planning and Assessment System | "Mississippi Career Planning and Assessment System, 2nd Edition (MS-CPAS2)" | IEP Guidance (2020), p. 63 |
| `ms_elpt` | English Language Proficiency Test | "English Language Proficiency Test (ELPT)" | IEP Guidance (2020), p. 56 |
| `ms_statewide_assess` | Mississippi Statewide Assessment System | "Mississippi Statewide Assessment System" | IEP Guidance (2020), p. 55 |
| `ms_accountability` | Mississippi Public School Accountability Standards | "Mississippi Public School Accountability Standards" | IEP Guidance (2020), p. 58 |
| `ms_icap` | Individual Career and Academic Plan | "THE INDIVIDUAL CAREER AND ACADEMIC PLAN (ICAP)" | Educator Guide (V5), p. 15 |
| `ms_irp` | Individual Reading Plan | "Individual Reading Plan (IRP)" | IEP Guidance (2020), p. 22 |
| `ms_clp` | Current level of performance | "Determine Current Level of Performance (CLP)" | IEP Guidance (2020), p. 39 |
| `ms_mom` | Method of measurement | "Method of Measurement (MOM)" | IEP Guidance (2020), p. 35 |
| `ms_pag` | Progress on annual goal | "Progress on Annual Goal (PAG)" | IEP Guidance (2020), p. 41 |
| `ms_roi` | Rate of improvement | "Rate of Improvement (ROI)" | IEP Guidance (2020), p. 39 |
| `ms_tst` | Teacher Support Team | "Teacher Support Team (TST)" | Procedures Vol. I, p. 9 |
| `ms_msis` | Mississippi Student Information System | "Mississippi Student Information System Identification (MSIS)" | IEP Guidance (2020), p. 7 |
| `ms_ropo` | Report of Physical Observation | "The Report of Physical Observation (Appendix EE.G)" | Procedures Vol. I, p. 44 |
| `ms_child_find_contact` | Local/School Child Find Contact | "The Local/School Child Find Contact should inform both the Agency/District Child Find Coordinator" | Procedures Vol. I, p. 9 |
| `ms_teacher_narrative` | Teacher narrative | "Teacher Narrative" | Rule 74.19, Eligibility Guidelines, p. 295 |
| `ms_rda` | Results-Driven Accountability | "Results-Driven Accountability (RDA)" | Rule 74.19, Program Improvement Monitoring, p. 331 |
| `det_meets_req` | Meets Requirements | "1. Meets Requirements" | Rule 74.19, Program Improvement Monitoring, p. 332 |
| `det_needs_assist` | Needs Assistance | "2. Needs Assistance" | Rule 74.19, Program Improvement Monitoring, p. 332 |
| `det_needs_interv` | Needs Intervention | "3. Needs Intervention" | Rule 74.19, Program Improvement Monitoring, p. 332 |
| `det_needs_sub_interv` | Needs Substantial Intervention | "4. Needs Substantial Intervention" | Rule 74.19, Program Improvement Monitoring, p. 332 |
| `ms_audio_rec` | Audio recording of IEP meeting | "Audio Recording of Individualized Education Program Meeting" | Procedural Safeguards (2025), p. 12 |
| `elig_report` | Eligibility determination report | "A separate eligibility determination report must be used" | Rule 74.19, Eligibility Guidelines, p. 295 |
| `push_in` | Push-in services | "Push-In Services" | Educator Guide (V5), p. 24 |
| `team_teaching` | Team teaching | "Team Teaching: Both teachers share responsibility for instruction" | Educator Guide (V5), p. 24 |
| `station_teaching` | Station teaching | "Station Teaching: The class is divided into small groups that rotate through stations" | Educator Guide (V5), p. 24 |
| `parallel_teaching` | Parallel teaching | "Parallel Teaching" | Educator Guide (V5), p. 24 |
| `alternative_teaching` | Alternative teaching | "Alternative Teaching: One teacher works with the larger group" | Educator Guide (V5), p. 24 |
| `cico` | Check-in/check-out | "Check-In/Check-Out; CICO" | Educator Guide (V5), p. 22 |
| `simple_view_reading` | Simple View of Reading | "The Simple View of Reading" | Educator Guide (V5), p. 17 |
| `scarborough_rope` | Scarborough’s Reading Rope | "Scarborough’s Rope Model" | Educator Guide (V5), p. 17 |
| `oae` | Otoacoustic emissions | "Otoacoustic Emissions (OAE)" | Rule 74.19, Eligibility Guidelines, p. 309 |
| `assr` | Auditory steady state response | "Auditory Steady State Response (ASSR)" | Rule 74.19, Eligibility Guidelines, p. 309 |
| `audiogram` | Audiogram | "An audiogram and/or measures of auditory evoked potential" | Rule 74.19, Eligibility Guidelines, p. 309 |
| `immittance` | Acoustic immittance | "Acoustic Immitance measures" | Rule 74.19, Eligibility Guidelines, p. 309 |
| `orofacial_exam` | Orofacial examination | "Results of an orofacial examination" | Rule 74.19, Eligibility Guidelines, p. 315 |
| `stimulability` | Stimulability | "including a measure of stimulability" | Rule 74.19, Eligibility Guidelines, p. 316 |
| `corrected_age` | Corrected age | "Calculate corrected age for children born prior to thirty-eight" | Rule 74.19, Eligibility Guidelines, p. 304 |
| `asha` | American Speech-Language-Hearing Association | "The American Speech Language and Hearing Association recognizes four" | Rule 74.19, Eligibility Guidelines, p. 313 |
| `icd` | International Classification of Diseases | "International Statistical Classification of Diseases and Related Health Problems" | Rule 74.19, Eligibility Guidelines, p. 296 |

## 3. Unsure

Existing versus new:
- Mississippi's rule mirrors 34 CFR 300, so most terms (the disability categories, IEP parts, evaluation and discipline terms) were attested on existing concepts. Matching was done on preferred terms and every string, ignoring case. 299 of the 364 concepts already existed.
- Mississippi-specific wording was added as strings on existing concepts with the US-MS tag: SCD/SCDs (`sig_cog`), STIO, STIO/B and "Short-term instructional objectives and benchmarks" (`sto`), DB (`deafblind`), LS (`sli`), EmD (`ed`), MAAP-EOC (`eoc`), EIP/EIPs (`in_first_steps`), "Itinerate Services" (`itinerant`). DSM is added on `dsm5` with no tag because other states use it.
- Three candidate attestations were dropped because the existing key is an illustrative placeholder that cannot be attested: standard score, executive function and preferential seating.
- Terms with no good existing key and no strong source (regression, math scribe, percentile rank) were left out.

Synonyms and wording:
- `ms_ose` (Office of Special Education, OSE) is new; New York has `nysed_ose`. It is tagged US-MS only and cites the rule's Program Improvement Monitoring section (p. 330) and its own name.
- The wording "Current Level of Performance" versus "Current Level of Progress" for CLP: the IEP guidance uses both. The preferred term is "Current Level of Performance"; the other is not recorded as a string.
- STIO/B is the rule's own form for short-term instructional objectives and benchmarks; it is attested as a string on `sto`.
- ASHA's full name appears only on rule p. 313 as "American Speech Language and Hearing Association" (no comma), and "Immitance" is spelled that way in the source; both are recorded as written.

Currency:
- The rule is the 2013 text. Mississippi may have amended Rule 74.19 since; this was not checked.
- Educator Guide V5: the URL path says 2026/05 but the PDF was created 2025-11-21. The edition date in `documents.tsv` says so.
- Vol. I was revised 7/8/16, so its forms and names may be out of date; the 2015 file name still appears in the URL.
- IEP guidance is dated 3.3.20.

## 4. Risky

Acronyms (all new all-caps strings; none tripped a test):
- MDE collides with Michigan (`mi_mde`). Both layers keep it; the build lists it as ambiguous across states (US-MI, US-MS).
- MS CCRS and CCRS-like names: Alabama and West Virginia already have `al_ccrs` and `wv_ccrs`; Mississippi's is `ms_ccrs` with the string "MS CCRS" only.
- OSE could also read as other offices (`nysed_ose`).
- Two-letter strings DB, LS and EmD, plus PAG, ROI, TST, MOM, CLP, IRP, ICD, OAE, ASSR and ASHA, are short and could match unrelated text. Review these first.
- CLP: two different expansions in the guide (see section 3).

Place names (all carry `flags: ["place_name"]`): the Mississippi Department of Education and Office of Special Education, MSDH, MDHS, Mississippi Department of Mental Health, Mississippi Department of Corrections, Mississippi Council on Developmental Disabilities, the four state schools (Blind, Deaf, Arts, Mathematics and Science), the Mississippi diplomas, assessments, standards, the Testing Accommodations Manual, MS-CPAS2, MKAS2, accountability standards and MSIS. MKAS2 and MS-CPAS2 also trip `contains_number` (automatic).

Eponym: "Scarborough's Reading Rope" (`scarborough_rope`) is kept only as the full phrase, flagged `eponym`; the bare surname is not a string.

Ambiguous or generic phrases: "Push-in", "Team teaching", "Station teaching", "Parallel teaching" and "Alternative teaching" are plain words in general use; they are recorded as service-delivery terms only.

## 5. Left out and why

- Corrective action plan (CAP): exists as `ky_cap` on the Kentucky branch; not duplicated here, to avoid a merge collision.
- Maine-only health-condition and other `me_` keys: not Mississippi's.
- TA: ambiguous with "technical assistance".
- "Mattie T." (the consent decree): a personal name.
- Local juvenile detention centers, local schools and school districts in Vol. I Appendix CF.B: local names, not recorded.
- USM-affiliated schools and school abbreviations (MSD, MSB and similar): omitted.
- AAA (audiology): collides with `al_aaa`.
- Names of people in Vol. I acknowledgements and elsewhere: excluded.
- 48 further candidate terms (district-level, vendor, and non-special-education terms such as ncec, nps, ccss, vwm) were excluded as not Mississippi special-education terminology or too generic.
- Funding subparts G and H (rule pp. 265-292) were scanned, not read line by line; terms found only there were not added.
- Family Guide to Manifestation Determination: read, but no record cites it.

## 6. Possibly disfavored

Nothing found. No document in the set marks a term as outdated or discouraged, and `sources/disfavored.tsv` was not touched.

