# Independent audit: sources/states/colorado.py (2026-10-08)

Method: followed prompts/audit-layer.md. Checked every entry against the text extracted from the three PDFs (pdftotext output with page markers, made by the drafter; the auditor did not re-run the extraction, which the first draft of this line wrongly claimed). PSN cited by PDF page (printed + 4, confirmed: printed "1" footer sits on PDF p. 5), GUIDE by page, RULE by rule number. Each STRINGS entry is (key, extra strings, citation); I tested the key's existing strings in `data/spedlex.csv` plus any extras against the cited page or rule, then read every miss by hand. Quotes are 15 words or fewer.

## Summary counts

| Block | Entries | Confirmed | Misplaced | Not found | Other (mapping/type/safety only) |
|---|---|---|---|---|---|
| STRINGS (230 entries, 14 extra strings) | 230 | 223 | 1 | 0 | 6 |
| CONCEPTS | 61 | 48 | 4 | 1 | 8 |

Note: in CONCEPTS the 13 listed rows are 4 misplaced (co_cde acronym, co_boces acronym, co_csi acronym, co_approved_facility plural), 1 not_found (s504_coord preferred term), 8 with a type, safety or wording note. Nothing in the whole module was invented: no entry is wholly absent from the documents. All three documents were readable, so no entry went unchecked.

Three most important fixes:
1. `s504_coord`: preferred term "Section 504 coordinator" is not in any document; the PSN says "504 Coordinator". Make "504 Coordinator" the evidenced string and drop or re-source the longer preferred term.
2. Re-cite acronyms that sit on the wrong rule: `CDE` (not at Rule 2.49), `BOCES` (not at 2.06), `CSI` (not at 2.48). Also fix `co_board`, which is only literally "Colorado State Board of Education" in the page header.
3. Fix the mapping of `sped_teacher` at GUIDE p. 153 ("Case Manager" is an IEP-team role, not necessarily a teacher) and `special_school` at GUIDE p. 80; correct the `ohi` extra type ("Other Health Impaired" is V in the CSV, S in the module); re-type `TEE`/"Temporary Educator Eligibility" as legacy.

## Non-confirmed entries

STRINGS

| Key | Term | Verdict | Correct citation | Problem | Evidence |
|---|---|---|---|---|---|
| ohi | Other Health Impaired (extra) | confirmed, type mismatch | | Module types S; CSV row (lowercase) is `spelling_variant`. Pick one; it is the same words as the rule's term. | "Other Health Impaired (OHI) means having limited strength" (Rule 2.09(7)) |
| state_ops | State Operated Program (extra, V) | misplaced | Rule 3.02(2) | Rule 2.50 heading is hyphenated "State-Operated Program"; the unhyphenated form appears only in the plural at 3.02. | "3.02(2) State Operated Programs" |
| sped_teacher | (key) at GUIDE p. 153 | mapping | | Only link is the existing synonym "case manager". Glossary defines a team role, not a teacher. Cite `sped_teacher` elsewhere or drop this attestation. | "The designated IEP team member who has primary responsibility for the IEP process" |
| special_school | (key) at GUIDE p. 80 | mapping (weak) | | Page says "separate schools"; key's matched string is "separate day school". Probably the same concept, but not the literal string. | "public or private separate schools or residential facilities" |
| disprop | (key) at Rule 5.01(22) | weak | | Rule says "overidentification and disproportionality"; the word "Significant" is absent here. | "Requirements regarding overidentification and disproportionality as established in 34 CFR" |
| annual_review | (key) at Rule 4.03(3) | weak | GUIDE p. 51 / p. 153 for the term | Rule states the 365-day requirement but never says "annual review". | "initiated and conducted at least once every 365 days" |
| dp_hearing | (key) at Rule 6.02(7.5)(c) | weak | Rule 6.02(7.5)(i) or PSN p. 22 | (c) is only ALJ assignment; "due process hearing" not named there. | "Assignment of an Administrative Law Judge." |

CONCEPTS

| Key | Term | Verdict | Correct citation | Problem | Evidence |
|---|---|---|---|---|---|
| co_cde | CDE (acronym) | misplaced | Rule 3.02(3)(b)(ii) or PSN PDF p. 5 | Full name is at 2.49; the abbreviation is not. Name also contains place name "Colorado" (CSV marks it high/never_bare, good). | "means the Colorado Department of Education." (2.49); "Colorado Department of Education (CDE)" (3.02) |
| co_board | Colorado State Board of Education | partly found | Rule 2.47 | The definition says "State Board of Education"; the full string appears only as the running page header. Add "State Board" as a synonym (note already says so). | "State Board means the State Board of Education, created" |
| co_cdec | Colorado Department of Early Childhood | partly found | Rule 2.14(1) | Text has only "Department of Early Childhood (CDEC)"; the "Colorado" form is the module's. | "Department of Early Childhood (CDEC) means the department" |
| co_au | AUs (plural) | misplaced | Rule 12.02 (used there) | Not in the 2.03 definition. AU itself is confirmed. | "Administrative Unit (AU) means a school district" |
| co_boces | BOCES (acronym) | misplaced | Rule 3.01(3)(a)(ii) | 2.06 never uses the acronym. | "Board of Cooperative Services means a regional educational services unit" |
| co_csi | CSI (acronym) | misplaced | Rule 3.01-series (text "CSI school"); GUIDE p. 157 | 2.48 spells out the name only. | "State Charter School Institute means the State Charter School Institute" |
| co_approved_facility | Approved Facility Schools (plural) | misplaced | Rule 3.02(1) | Plural not at 2.20(1). Singular confirmed. Safe as a generic term. | "Standards for Approved Facility Schools, State Operated Programs" |
| co_abbrev_sched | Abbreviated School Day Schedules (plural) | misplaced | | Plural not at 2.01(1); singular confirmed. | "Abbreviated School Day Schedule means a schedule designed" |
| s504_coord | Section 504 coordinator (preferred) | not_found | none | Phrase absent from all three documents. Only "504 Coordinator" (PSN PDF p. 3) is there. The key is also not CO-tagged, which is right for a federal role. | "contact the 504 Coordinator for your school district." |
| co_seta | TEE / Temporary Educator Eligibility | type | Rule 3.04(3) | The rule says TEE "shall be formally referred to as" SETA, so TEE is the outdated name still in use. Consider L for the full form; keep TEE as A or L. | "shall be formally referred to as Special Education Temporary Authorization (SETA)" |
| co_eeo | EEO / EEOs | safety (ambiguity), type | GUIDE p. 44 | EEO normally means Equal Employment Opportunity; protecting it is harmless but note collision. "EEOs" is a plural, typed A, should be P. | "Extended Evidence Outcomes" (GUIDE p. 44) |
| co_ppra | PPRA | safety (ambiguity) | PSN PDF p. 18 | Same acronym is the federal Protection of Pupil Rights Amendment (not in these documents). PSN uses two expansions in one passage; the module records both, which is right. | "Protection of Persons from Restraint Act (PPRA)" |
| co_sop_csdb | Colorado School for the Deaf and the Blind | safety | Rule 2.50(1) | A named school plus a place name; docstring says schools are left out on purpose. CSV marks it high, but the docstring is inconsistent with including it. | "The Colorado School for the Deaf and the Blind" |

Other safety observations, no change needed: `ocr`/OCR is generic (optical character recognition) but typed A and unscoped, acceptable. Organisation names (`co_thrive`, `co_arc`, `co_dlc`, `co_peak`, `co_show_tell`, `co_tjp`) contain place names or common words; CSV marks the place-name ones high/never_bare; `co_early_access` carries common_english_word. `ward` ("Ward of the State") has a surname-like word but is low risk. `tourette` and `braille` are eponyms; CSV already marks them high/never_bare. `certificate of completion` is a CSV synonym tagged US-CA only; Colorado uses it at GUIDE p. 68 but the module adds no CO attestation.

Confirmed: 223 of 230 STRINGS entries and 48 of 61 CONCEPTS entries are found at their citation, mapped to the right key, and safe and typed correctly.

## Missed terms (most important first)

1. Compensatory services: PSN PDF p. 21 ("compensatory services, additional"); key `comp_services` exists, no CO attestation.
2. Seclusion and restraint: PSN PDF p. 18 (line 648 "restraints or seclusion"); key `seclusion` exists; the module has only the PPRA act.
3. Case manager as its own concept: GUIDE p. 153 glossary. Better home than `sped_teacher`.
4. Self-Contained Class: GUIDE p. 157 glossary; no key.
5. Post-school goal(s): GUIDE p. 156 glossary; no key.
6. Independent Living Skills (transition domain): GUIDE p. 154 glossary, also p. 40.
7. Indirect Services / Direct Services: GUIDE pp. 154 and 153; key `indirect_svc` exists.
8. Dispute resolution (the umbrella term): PSN PDF p. 4 onward; GUIDE p. 153; no key.
9. Division of Vocational Rehabilitation: GUIDE p. 124; no key (agency name, low risk if phrase-only).
10. Parentally placed private school children: GUIDE pp. 56-57, Rules; key `ppps` exists.
11. Preschool Provider: Rule 2.14(3), next to the included CDEC, LCO and UPK items.
12. English learner / EL: GUIDE p. 154 ("EL English Learner"); would add to `lep`.
13. Paraprofessional: Rule 2.45(5); GUIDE p. 45; key `para` exists.
14. Adaptive behavior: Rule 2.09(4)(a); key `adaptive` exists.
15. Universal screening: GUIDE p. 14; key `screening` exists.
16. Community centered board: GUIDE p. 57; no key (organisation type).
17. Mediator / impartial mediator: PSN PDF p. 16; GUIDE p. 155.
18. Service delivery: GUIDE pp. 6, 157 glossary; no key (co_service_delivery covers only the IEP section name).
19. Medicaid billing consent: GUIDE pp. 29, 76, 125; no key.
20. Day treatment program: GUIDE p. 57; Rule 2.20(1) text.

## Docstring notes

Accurate (checked): RULE PDF has 126 pages and Editor's Notes end with amendments "eff. 05/15/2025"; PSN has 51 pages, body footers read "April 2024" and appendix footers "April 2025" (D1-D4); GUIDE has 158 pages, footers "REVISED 07/2017", printed page equals PDF page; PSN printed + 4 equals PDF page; rules 2.00-2.54 and Rule 12.01 exist as described.

Needs fixing or caution:
- The docstring says the districts, BOCES and schools named in the documents are left out, but `co_sop_csdb` (a named school) and the named organisations are included. State that official state programs and advocacy organisations are the exception.
- It says "RULE records are 'machine_validated'; the others are 'candidate'", but STRINGS rows for existing keys keep their existing status, so only new records follow this rule.
- Rule 2.20 appears in the Editor's Notes as "repealed eff. 06/30/2022" while the text still carries "2.20 Facility" and "2.20(1)". Citations to 2.20(1) match the text; the docstring should mention the conflict, or the cited number may be unstable.
- "Rules 3.01-3.03, 7.03, 9.03-9.07 were not read line by line" is honest, yet `co_online_school` cites Rule 9.01(4) and `co_comp_plan` cites 8.01(1)(a); both check out.
- Could not check: the ruleVersionId and the two CDE resource-manager URLs (no network access used). The GUIDE pages 12-39 and 83-147 were only searched, as the docstring says.


## Resolution (added by the drafter)
Applied before release: `s504_coord` now uses "504 Coordinator"; CDE, BOCES and approved-facility citations list the rule where the acronym or plural appears; `co_cdec` preferred term is "Department of Early Childhood"; the "CSI", "AUs" and "Abbreviated School Day Schedules" strings, the unconfirmed BOCES, State Recommended IEP Forms and Permission to Invite Agencies variants were dropped; TEE strings are typed legacy; "EEOs" is typed plural; "Other Health Impaired" is typed spelling variant; the `sped_teacher` and `special_school` attestations were removed; the docstring was corrected. Not changed: `co_board` (full name only in the PDF running header), `co_ppra`, `co_sop_csdb`, and the `disprop`, `annual_review`, `dp_hearing` attestations; they are listed in the report. The 20 missed terms are left for a later patch.
