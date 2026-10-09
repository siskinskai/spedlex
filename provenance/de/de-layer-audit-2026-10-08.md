# Independent audit: sources/states/delaware.py and delaware_supplement.py (2026-10-08)

Method: followed `prompts/audit-layer.md` in a fresh session that did not see the drafting. The auditor is `claude-opus-5-5`, the same model that drafted this layer, so this is a fresh-context check, not a different-model check. Text was re-extracted by the auditor with `pdftotext -layout` from the four PDFs in `.sources-cache/de/`. A script looked for every entry's strings (the key's existing strings in `data/spedlex.jsonl`, plus each extra string) at the cited section or PDF page; every miss was then read by hand. Quotes are 15 words or fewer.

## Summary counts

| Block | Entries | Confirmed | Weak (concept there, no listed string) | Misplaced | Not found |
|---|---|---|---|---|---|
| delaware STRINGS (25 extra strings) | 219 | 213 | 6 | 0 | 0 |
| delaware CONCEPTS | 37 | 37 | 0 | 0 | 0 |
| delaware_supplement STRINGS | 2 | 2 | 0 | 0 | 0 |

Nothing in the module is invented: every term is in the documents. All four documents were readable. Page counts in the docstring match the PDFs (9, 28, 46 and 56 pages); PSN printed page = PDF page minus 4 is confirmed (printed "1" on PDF p. 5).

Three most important points:
1. **Safety, needs an explicit human decision:** `de_doe` adds the bare all-caps acronym "DOE". "Doe" is a census surname and the stock placeholder surname. The matcher now protects it in all-caps text: `find("Student: JANE DOE, Grade 4")` returns `['DOE']`, so the surname survives de-identification. The changelog says "a reviewer accepted it"; confirm that a person made that decision, since `tests/test_match.py` was widened to allow it.
2. Six attestations rest on wording that none of the key's strings match (list below). They are defensible as concept attestations but are weaker than the rest.
3. Missed terms: "general education curriculum" (18 uses), "language impairment" (11) and "speech-language pathologist" (8) are the most frequent existing concepts Delaware's documents use but the layer does not attest.

## Non-confirmed entries

| Key | Term | Verdict | Correct citation | Problem | Evidence |
|---|---|---|---|---|---|
| ppps | (key) at 922.2.2.5 | weak | | Rule paraphrases; no ppps string appears. | "placed in private schools by their parents under the provisions of" |
| ppps | (key) at PSN p. 34 | weak | | Same: paraphrase only. | "privately placed by their parents" |
| pti | (key) at PSN p. 7 | weak | | Page names only PIC of Delaware, which `de_pic` already records. | "Parent Information Center of Delaware, Inc." |
| revoke | (key) at PSN p. 12 | weak | | Verb form; key strings are noun phrases. | "You can revoke your consent for the continued provision of special education" |
| code_conduct | (key) at PSN p. 29 | weak | | "code of conduct" is not one of the key's strings. | "violates a code of conduct" |
| home_instr | (key) at GUIDE p. 38 | weak | | "setting", not "placement" or "instruction". | "Homebound or hospital setting" |

Hand-confirmed after the script missed them (curly quotes, line breaks): `consent`, `braille`, `surrogate`, `implant` at 922.3.0; `de_relative_caregiver` and `de_secretary` at 922.3.0; the `de_dscyf` variant "Youth, and Their Families" at 922.3.0 (Ward of the State); "team classrooms" for `coteach` (GUIDE p. 38, where team classrooms are co-taught).

## Safety and typing

- "DOE": see point 1. `pii_level` high and `never_bare`, but the all-caps exception still lets it match bare.
- "PIC" is now ambiguous between `nh_pic` and `de_pic` (allowed; both regional).
- "PBS" (Positive Behavior Support) and "ESP" (educational surrogate parent) have common other meanings; harmless to protect, regional to DE.
- "Hearing panel", "Draft IEP", "Case-by-case determination", "Out-of-school suspension" are generic phrases; none is a name or place.
- `de_regs` preferred string "14 DE Admin. Code 922 to 929" contains the place token "DE"; the build already marks it high.

## Missed terms (existing concepts used two or more times in the documents, not attested)

1. General education curriculum (18 uses). 2. Language impairment, under `lang_dis`/Language disorder (11). 3. "exceptional children", the Exceptional student concept (12; mostly the ECR office name). 4. Speech-language pathologist (8). 5. Functional performance (6). 6. Mode of communication (6). 7. General education classroom, under Regular class (5). 8. Audiological evaluation (4). 9. Participating agency (4). 10. Service coordinator (3). 11. Sensory impairment (3). 12. Occupational and physical therapist (2 each). 13. Consideration of Special Factors (2). 14. Controlled substance (2). 15. Nondisabled peers (2). 16. Qualified examiner (2).

## Docstring

Accurate on sources, dates, page offsets and what was left out. No corrections needed.


## Resolution (applied 2026-10-08)

- "DOE": the maintainer (Jeremy Evans, confirmed 2026-10-08) decided that "Doe" is used almost only as a pseudonym and carries no risk of identifying a child. It is removed from `reference/names/census2000_surnames_10k.txt` and from the known all-caps collisions in `tests/test_match.py`. "DOE" stays in `de_doe`.
- Removed the weak `pti` attestation at PSN p. 7 (PIC is recorded as `de_pic`) and the `home_instr` attestation at GUIDE p. 38 (already attested at 922.3.0).
- Kept, as concept attestations in paraphrase: `ppps` (922.2.2.5, PSN p. 34), `revoke` (PSN p. 12), `code_conduct` (PSN p. 29). No document uses a literal key string for them.
- Added 17 missed terms, each checked at its citation: `func_perf` 925.3.1, `gen_curr` 925.4.2.1, `audiological_assess` 925.6.8.4.2, `gross_motor` 925.6.7.1, `program_mods` 925.7.1.4, `regular_class` 925.7.1.5, `part_agency` 925.8.2.2, `service_coord` 925.8.6, `annual_review` 925.11.4, `comm_mode` 922.3.0 (Consent), `controlled` PSN p. 31, `nondisabled` GUIDE p. 24, `special_class` GUIDE p. 38, `state_dir` GUIDE p. 46; and in `delaware_supplement` (moved after `iowa` in LAYERS, because Iowa defines these keys) `speech_path` 925.6.6.6, `phys_therapist` and `occ_therapist` 922.3.0.
- Not added: "language impairment" (in Delaware it is part of the category name "Speech or Language Impairment", already `sli`), "exceptional children" (part of the ECR office name), and other states' concepts (qualified examiner, Office of Special Education, comprehensive assessment system, Consideration of Special Factors).
