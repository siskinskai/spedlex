# Independent audit: sources/states/wyoming.py (2026-10-08)

Method: followed `prompts/audit-layer.md` in a fresh session that did not see the drafting. The auditor is `claude-opus-5-5`; the layer was drafted by `claude-sonnet-5-5`, so this is a different-model check. Text was re-extracted with `pdftotext -layout` from `WY-Chapter-7-Rules.pdf` (OCR layer) and `WY-Procedural-Safeguards-2025.pdf`. A script found each rule citation by walking the section markers (Section n., then (a), (i), (A), ...) and each PSN page; every miss was read by hand. Where the OCR is garbled, the page image was viewed: PDF pp. 1 and 20 of the Chapter 7 copy confirm "Wyoming Department of Education (WDE)", "Court-ordered placements" and "The Department of Family Services (DFS)". Quotes are 15 words or fewer.

## Summary counts

| Block | Entries | Confirmed | Weak (concept there, wording differs) | Mapping | Not found |
|---|---|---|---|---|---|
| STRINGS (2 extra strings) | 118 | 109 | 8 | 1 | 0 |
| CONCEPTS | 10 | 10 | 0 | 0 | 0 |

Nothing is invented. Both text documents were readable; the portal scan (`WY-7767.pdf`) was not compared with the OCR copy, as the docstring says. Page counts match (30, 31 and 36 pages).

Three most important points:
1. **Missed core attestations.** The rule and notice use "due process" 135 times, "public agency" 91 times and "IEP Team" 13 times, but the layer attests neither `dp_complaint`, `public_agency` nor `iep_team`. Worth adding before release.
2. **Mapping:** `disprop` at § 9(d)(iii) is "disproportionate representation" (the 34 CFR 300.600(d)(3) monitoring priority), not "significant disproportionality" (300.646). The key already bundles the two, so this is a loose fit rather than an error.
3. **Key decision before IDs are committed:** `wy_interdistrict` and `wy_court_placement` have no jurisdiction (they are national concepts) but carry `wy_` keys. Keys are permanent once released; either give them `WYJ` or rename the keys now.

## Non-confirmed entries

| Key | Term | Verdict | Problem | Evidence |
|---|---|---|---|---|
| preschool_swd | (key) at § 3(b)(vi) | weak | Plural "preschool children with disabilities" is not one of the key's strings; worth adding as a plural. | "\"Preschool children with disabilities\" means children three (3)" |
| ppps | (key) at § 4(a)(iii) | weak | Paraphrase. | "parentally enrolled in a private elementary or secondary school" |
| eligibility | (key) at § 4(c) | weak | Heading only. | "Eligibility under the IDEA." |
| artic | (key) at § 4(d)(xi)(A)(I) | weak | "Articulation" alone; key strings are "articulation disorder" etc. | "Articulation eligibility criteria. Articulation means speech sound" |
| lang_dis | (key) at § 4(d)(xi)(A)(III) | confirmed (corrected) | First draft of this audit called it weak; "language impairment" is a `lang_dis` string. | "Language Impairment eligibility criteria" |
| revoke | (key) at § 6(b) | weak | | "the revocation of parental consent procedures" |
| homeless | (key) at PSN p. 21 | weak | | "In the case of a homeless child or youth" |
| disprop | (key) at § 9(d)(iii) | mapping | See point 2. | "Disproportionate representation of racial and ethnic groups in special" |

Confirmed by hand where OCR or layout defeated the script: `adaptive` (§ 4(d)(ii)(A)(III), OCR "(Ill)"), `mbd` (OCR "minir,al brain dysfunction"), `speech_path`, `fluency_dis` ("Stuttering"), `voice` ("Voice Impairment"), and all of § 6: `safeguards_notice`, `consent`, `iee`, `pwn`, `surrogate`, `age_majority` ("Transfer of parental rights at age of majority"), `unilateral_pl`, `ed_records`, `ferpa`. `wy_dfs` and `wy_court_placement` confirmed on the page image.

## Safety and typing

- "UPLIFT" is the preferred term, so it matches case-insensitively: ordinary "uplift" is protected anywhere. Not a name; flagged `common_english_word`. Acceptable, but a case-sensitive form would be tighter.
- "WDE" and "DFS" are regional to WY. No new string is a first name or surname on its own.
- "Cognitive Disability" (under `id`) and "home based education" are correctly tagged WY.

## Missed terms (existing concepts used two or more times, not attested)

1. Due process complaint (135 uses of "due process"). 2. Public agency (91). 3. School day (16). 4. Adversely affects educational performance (15). 5. IEP Team (13). 6. Suspected disability (12). 7. Code of student conduct (5). 8. Mode of communication (5). 9. Native language (5). 10. Charter school (3). 11. Scientific, research-based intervention (3). 12. General education curriculum (3). 13. Norm-referenced test (2). 14. School psychologist (2). 15. Americans with Disabilities Act (2). 16. Limited English proficiency (2).

## Docstring

Accurate, including the OCR warning. One addition: the `wy_interdistrict` and `wy_court_placement` records are national despite their keys.


## Resolution (applied 2026-10-08)

- Keys: `wy_interdistrict` and `wy_court_placement` are renamed `interdistrict_placement` and `court_placement`, like other national concepts first attested by a state (`case_by_case`, `audiologist`). They keep SPED:001246 and SPED:001247; the IDs had not been released.
- Removed the `disprop` attestation at § 9(d)(iii).
- Added the plural "preschool children with disabilities" to `preschool_swd`.
- Added 16 missed terms, each checked at its citation (section markers read by eye where the OCR is poor): `charter_school` § 3(b)(ii), `public_agency` § 4(a), `adverse` § 4(c)(i), `suspected` § 4(d)(i)(A), `school_psych` § 4(d)(v)(A), `srbi` § 4(d)(x)(D)(II), `lep` § 4(d)(x)(G)(VI), `norm_ref` § 4(d)(xi)(A)(I), `iep_team` § 5(c)(i)(B), `dp_complaint` § 7(c), and from the notice `ada`, `native_language`, `comm_mode` (p. 2), `school_day`, `code_conduct` (p. 14), `gen_curr` (p. 15).
- Not changed: "UPLIFT" stays the preferred term; preferred terms always match case-insensitively, and it is not a name.
