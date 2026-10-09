# Independent audit: sources/states/west_virginia.py (2026-10-09)

Method: followed `prompts/audit-layer.md` in a fresh session that did not see the drafting. The layer was drafted by `claude-sonnet-5-5` (its `ASSISTED_BY`); the auditor is `claude-opus-5-5`, so this is a different-model check. Policy 2419 is a scanned image, so the auditor did not rely on the drafter's OCR: it re-ran tesseract on all 155 pages at 300 dpi and checked against both text layers (they agree; the auditor's layer also reads "Serious Bodily Injury" and "Out-of-School Suspension" correctly where the drafter's has OCR slips). The notice was extracted with `pdftotext`. A script looked for every entry's strings (the key's strings in `data/spedlex.jsonl`, plus each extra string) at the cited PDF page; every miss was read by hand, and one page image (Policy 2419, PDF p. 126) was viewed to settle an OCR ambiguity. Quotes are 15 words or fewer. The federal OSEP guidance was not audited because no record cites it.

## Summary counts

| Block | Entries | Confirmed | Weak (concept there, no listed string) | Misplaced | Not found |
|---|---|---|---|---|---|
| STRINGS (entry level) | 204 | 196 | 5 | 3 | 0 |
| CONCEPTS (entry level) | 86 | 85 | 0 | 0 | 1 (`wv_osp` preferred term) |
| Extra strings inside confirmed entries | | | | 13 | 2 |

Nothing in the module is invented as a concept: every concept is in the documents. Two extra strings and one preferred term are worded in ways neither document uses. Both West Virginia documents were readable. Page counts (155 and 51) and page offsets (Policy 2419 PDF = printed + 1, notice PDF = printed + 3) are confirmed.

Three most important points:
1. **Safety, needs a human decision:** `apr` adds the bare acronym "APR" with no regional tag, `pii_level` none and `phrase_or_token`. "APR" is also the month abbreviation (April), and it is the only month abbreviation in the whole safelist. In a document reading "DOB: APR 14, 2015", the matcher would protect part of a child's date of birth. Remove "APR" (keep "Annual Performance Report"), or have a reviewer decide how it should be graded.
2. **Strings the documents don't use:** "West Virginia Birth to Three" (`wv_birth_to_three`; both documents say only "WV Birth to Three"), "Division of Federal Programs and Support" (`wv_dfps`; the notice prints only "&"), and the `wv_osp` preferred term "West Virginia Office of Special Education" (the notice says "West Virginia Department of Education, Office of Special Education"). Remove the two variants and use wording the documents print for `wv_osp`.
3. **Misplaced citations:** 3 entries and 13 extra strings are found, but on another page (listed below). The worst case is `wv_policy_2419`, whose "Procedures Manual" and "126CSR16" strings are cited to the notice but appear only in the rule.

## Non-confirmed entries

| Key | Term | Verdict | Correct citation | Problem | Evidence |
|---|---|---|---|---|---|
| continuum | (key) at Definitions p. 14 | weak | or Ch. 5, § 2.J, PDF p. 85 | WV wording "Continuum of Services/Placements" is not a key string; "continuum of placement options" is on pp. 85 to 86. Consider adding the WV wording. | "Continuum of Services/Placements. A range of settings" |
| edu_interpreter | (key) at Definitions p. 16 | weak | | The only wording is "Educational Sign Language Interpreter", which `wv_esli` already records with `broader: edu_interpreter`. Redundant; consider dropping. | "Educational Sign Language Interpreter. A paraprofessional meeting the requirements" |
| ppps | (key) at Ch. 5, § 2.J p. 87 | weak | | WV heading only; no key string. Consider adding "Special Education: Parentally-Placed in Private School" (WV), like the other placement headings. | "Special Education: Parentally-Placed in Private School" |
| exclusionary | (key) at Ch. 4, § 3.L p. 63 | weak | | WV says "Exclusion Factors"; key says "Exclusionary factors". | "Standard 3 - Exclusion Factors" |
| homeless | (key) at PSN p. 27 | weak | | "homeless child or youth" is not a key string. Already attested at Definitions p. 18. | "If the student is a homeless child or youth" |
| cortical_vi | (key) at Ch. 4, § 3.B p. 53 | misplaced | Definitions, PDF p. 17 | p. 53 says "cortical visual impairment", not the key string. Consider adding "cortical visual impairment" as a spelling variant (p. 17 uses both). | "characteristic behaviors associated with cortical visual impairment" |
| ferpa | (key) at PSN p. 15 | misplaced | PSN p. 16 | | "20 U.S.C. 1232g (FERPA) and Policy 4350" |
| age_majority | (key) at PSN p. 8 | misplaced | PSN p. 19 | | "the age of majority under state law, must be obtained" |
| wv_osp | West Virginia Office of Special Education | not_found (wording) | PSN p. 24 | Preferred term is a constructed form. Doc wording is "Office of Special Education", which is also `nysed_ose`'s preferred term; a reviewer should choose. | "West Virginia Department of Education, Office of Special Education" |

Hand-confirmed after the script missed them: `sbi` and `oss` (OCR slips in the drafter's text only), `critical_skill` ("Critical Skills"), `ar_integrated` ("Integrated classrooms"), `wv_wvsdb` (the name runs over the page break from PDF p. 50 to p. 51), `wv_taaes` (runs over from p. 91 to p. 92), `dsm5` (p. 52; the auditor's OCR reads "DSM-S5").

## Extra strings at the wrong page or not in the documents

| Key | String | Verdict | Correct citation |
|---|---|---|---|
| wv_birth_to_three | West Virginia Birth to Three | not_found | Remove. Only "WV Birth to Three" appears (e.g. Ch. 2, § 2.A, PDF p. 37). |
| wv_dfps | Division of Federal Programs and Support | not_found | Remove. The notice prints "Division of Federal Programs & Support" (PSN p. 50). |
| wv_policy_2419 | West Virginia Procedures Manual for the Education of Students with Exceptionalities | misplaced | RULE § 126-16-3.1, PDF p. 3 (not in the notice) |
| wv_policy_2419 | 126CSR16 | misplaced | RULE, PDF p. 2 (page header; not in the notice) |
| wv_policy_4350 | Procedures for the Collection, Maintenance and Disclosure of Student Information | misplaced | PSN p. 16 (p. 8 has only the "Regulations ... Student Data" title) |
| plaafp | PLEP | misplaced | Ch. 5, § 2.D, PDF p. 78 (Definitions p. 24 has only "PLEPs") |
| hi | deaf and hard of hearing | misplaced | Definitions, PDF p. 16 (§ 3.H on p. 58 is headed "Hard of Hearing") |
| wv_alt_summative | WV Alternate Assessment; West Virginia Alternate Assessment | misplaced | Ch. 5, § 2.I, PDF p. 84 |
| wv_ccrs | CCRS | misplaced | Ch. 4, PDF p. 50 (also p. 79) |
| wv_aaas | Policy 2520.16 | misplaced | PDF p. 36 |
| wv_prek | Universal Pre-K | misplaced | PDF p. 75 or p. 102 |
| wv_esli | educational sign language interpreter I; ... II | misplaced | Ch. 9, § 3.A, PDF p. 126 (page image checked: "interpreter I or II") |
| wv_rcsp | RCSP | misplaced (minor) | PDF p. 122 (p. 121 has only the full name) |
| wv_taaes | TAAES | misplaced (minor) | PDF p. 92 |

## Mapping

- `aac` + "Augmentative/Alternative Communication Evaluation": an evaluation is not the same concept as AAC itself. Drop the string, or make it a WV concept with `broader: aac`.
- `amendment` + "IEP Amendment Form": a form rather than the amendment; minor, acceptable as WV usage.
- `wv_primary_exceptionality` may duplicate the existing `primary_disability` (DC, DE). Policy 2419 uses both: "primary exceptionality" (p. 50) and "primary disability" (pp. 67 to 72). It is kept separate presumably because "exceptionality" includes giftedness; a reviewer should confirm, or add "primary exceptionality" (WV) as a string on `primary_disability`.
- No other new national concept duplicates an existing key (checked `expulsion`, `attorneys_fees`, `civil_action`, `destruction_pii`, `public_benefits_consent`, `intervener`, `pre_ets`, `supported_employment`, `cic`, `hats`, `dsm5`, `spp`, `apr`, `general_supervision`, and the speech-language concepts).

## Safety and typing

- "APR": see point 1.
- No new acronym matches a first name or surname in `reference/names/`. The docstring is right that "GEE" is a given name (it is in both name lists) and was correctly left out.
- Every string containing "West Virginia" or "WV" is graded `high` / `never_bare` by the build.
- "educational sign language interpreter I" ends in a standalone single letter. It matches only as a phrase, so the risk is low, but it should be noted.
- Ambiguous but harmless, all tagged US-WV: "SAT" (Student Assistance Team; also the college test), "EC" (Eligibility Committee), "SEE" (an all-caps common word; `phrase_only`).
- Unrelated to this layer but seen while auditing: the Virginia key `vdoe` ("Virginia Department of Education") matches inside "West Virginia Department of Education". That's harmless, since both are agencies.
- Typing is correct: acronyms are `A`, WV-only strings carry US-WV, and generic national forms ("SLPA", "DSM-5", "Pre-ETS") are rightly left untagged.

## Missed terms (existing concepts the documents use but the layer doesn't attest; checked at the citation)

1. `test_accom`: "assessment accommodations", Ch. 5, § 2.I, PDF p. 84 (also pp. 81, 91, 92).
2. `program_mods`: "program modifications or supports", Ch. 5, PDF p. 80.
3. `regular_class`: "general education classroom", PDF p. 81 (also pp. 15, 61, 85, 86).
4. `sped_teacher`: "special education teacher", Definitions (Case Management), PDF p. 14.
5. `disprop`: "significant disproportionality", Ch. 9, PDF p. 118 (also pp. 124, 125).
6. `gen_teacher`: "general education teacher", Ch. 5, § 1, PDF p. 74.
7. `public_agency`: "public agency", Definitions, PDF p. 23; PSN pp. 21, 24.
8. `func_perf`: "functional performance", Definitions (PLEPs), PDF p. 24.
9. `referral`: Ch. 3, § 3 "Referrals", PDF p. 38; PSN p. 43.
10. `foster`: "foster parent", Definitions (Parent), PDF p. 22; PSN p. 11.
11. `lep`: "limited English proficiency", Definitions (Native Language), PDF p. 21; PSN p. 9.
12. `pe`: "Adaptive Physical Education" (defined), Definitions, PDF p. 12.
13. `para`: "paraprofessional", Definitions, PDF p. 16.
14. `sea`: "state educational agency", Definitions, PDF p. 17.
15. `std_diploma`: "regular high school diploma", Definitions, PDF p. 12.
16. `indirect_svc`: "Indirect Services" (defined), Definitions, PDF p. 19.
17. `init_place`: "Consent for Initial Placement", Ch. 5, § 2.K, PDF p. 89.
18. `lea_rep`: "LEA representative", Ch. 5, § 1, PDF p. 74.
19. `nonacademic`: "Nonacademic Services", PDF p. 36.
20. `daily_living` and `trans_assess`: "acquisition of daily living skills" and "age-appropriate transition assessments", Ch. 5, § 2.F, PDF p. 80.

## Docstring

Accurate on sources, dates, page counts, page offsets and what was left out. Suggested additions: say that "APR" was kept (or removed) despite the month collision, and correct the implication that every "Procedures Manual"/"126CSR16" attestation comes from the notice. The statement that both documents were "read in full" can't be checked from here.


## Resolution (2026-10-09)

- "APR": kept. The maintainer asked for it to be protected except inside a date. The matcher now skips any month name or abbreviation that has a number directly before or after it ("APR 14, 2015", "14-APR-15", "APR 2015"), so it cannot shelter part of a date of birth. "APR" away from numbers is still protected. See CHANGELOG [Unreleased], METHODOLOGY.md §5, USING.md rule 7, and the two new tests in `tests/test_match.py`.
- Removed "West Virginia Birth to Three", "Division of Federal Programs and Support", "Augmentative/Alternative Communication Evaluation", the `edu_interpreter` attestation (covered by `wv_esli`) and the `homeless` attestation at PSN p. 27.
- `wv_osp` preferred term is now "West Virginia Department of Education, Office of Special Education", the notice's wording (PSN p. 24). Plain "Office of Special Education" was not used because it is already `nysed_ose`'s preferred term.
- Fixed citations: `ferpa` to PSN p. 16, `age_majority` to PSN p. 19, `cortical_vi` to Definitions p. 17 (p. 53 kept for the variant), "PLEP" to Ch. 5, § 2.D p. 78, "deaf and hard of hearing" to Definitions p. 16. `wv_policy_2419` now cites the rule (§ 126-16-1.5, p. 2, also § 126-16-3.1, p. 3). Concepts whose strings sit on a second page now cite both, e.g. "PDF p. 124 (also Ch. 5, § 2.I, p. 84)", because STRINGS can't refer to a concept defined in the same layer.
- Added WV wording as strings: "Continuum of Services/Placements" (`continuum`), "Special Education: Parentally-Placed in Private School" (`ppps`), "exclusion factors" (`exclusionary`), "augmentative/alternative communication" (`aac`, plus an AAC attestation at Definitions p. 14), "cortical visual impairment" (`cortical_vi`, untagged: it is the common national spelling).
- Added all 20 missed terms listed above, plus `primary_disability` (Ch. 4, § 3.M, p. 67) and notice attestations for `referral`, `foster`, `lep` and `public_agency`.
- Kept, with notes: `wv_primary_exceptionality` stays separate from `primary_disability` because a West Virginia exceptionality includes giftedness. "IEP Amendment Form" stays on `amendment`.
- Rechecked by script against both OCR layers: every entry and extra string is at its cited page. The remaining script misses are OCR slips, plurals, and one name split by a page break, all confirmed by hand.
