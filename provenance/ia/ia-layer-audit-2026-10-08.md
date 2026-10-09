# Independent audit: sources/states/iowa.py (2026-10-08)

Method: followed `prompts/audit-layer.md` in a fresh session that did not see the drafting. The auditor is `claude-opus-5-5`, the same model that drafted this layer, so this is a fresh-context check, not a different-model check. Text was re-extracted by the auditor with `pdftotext -layout` (and `-raw` for the two-column terms sheet, whose terms wrap across lines). A script looked for every entry's strings at the cited rule or subrule heading (`281—41.n(...)` or `41.n(m)` at line start) or PDF page; every miss was read by hand. Quotes are 15 words or fewer.

## Summary counts

| Block | Entries | Confirmed | Weak (concept there, wording differs) | Misplaced (part) | Not found |
|---|---|---|---|---|---|
| STRINGS (37 extra strings) | 286 | 268 | 18 | 0 | 0 |
| CONCEPTS | 58 | 54 | 0 | 2 | 0 |

Two CONCEPTS also have a preferred term that appears in none of the three documents (below). Nothing is invented: every term is in the documents. All three documents were readable. Page counts in the docstring match the PDFs (108, 50 and 7 pages).

Three most important fixes:
1. **Constructed preferred terms.** `ia_dhs` "Iowa Department of Human Services" and `ia_early_access` "Iowa Early ACCESS" are not in any document. The terms sheet says "Department of Human Services" (p. 2) and "Early ACCESS" (p. 3). The Colorado audit fixed the same pattern (`co_cdec`) by using the document's wording as the preferred term.
2. **"Early ACCESS" typed as an acronym** so it matches case-sensitively. It is a program name, not an acronym. The changelog says this keeps it apart from Colorado's "Early Access", but Colorado's string is `phrase_ci`, so in Iowa text "Early ACCESS" still matches the Colorado concept (4 hits in Iowa's own documents). Not a privacy risk (both protect the phrase), but the concept label can be wrong.
3. **Misplaced strings:** "EI" appears only on the terms sheet (p. 3), not at 41.8; "eligible individuals" (plural) is not at 41.8; "area education agencies" and "AEAs" are not at 41.4 (both are elsewhere in the rule).

## Non-confirmed entries

STRINGS (all weak: the concept is at the citation, in wording none of the key's strings match)

| Key | Citation | Evidence |
|---|---|---|
| unilateral_pl | 41.148 | "the parents elected to place the child in a private school" |
| adr | 41.152(2) | "other alternative means of dispute resolution" |
| adr | PSN p. 26 | "mediation, or alternative means of dispute resolution" |
| print_disability | 41.210(4) | "other persons with print disabilities" (plural only) |
| revoke | 41.300(2) | "revokes consent in writing for the continued provision" |
| revoke | PSN p. 15 | "You may revoke your consent for continued special education" |
| sop | 41.305(5) | "a summary of the child's academic achievement and functional" |
| progress | 41.320(1) | "periodic reports on the progress the child is making" |
| removal_expl | 41.320(1) | "the extent, if any, to which the child will not participate" |
| prefs | 41.321(2) | "the child's preferences and interests are considered" |
| draft_iep | 41.322(7) | "“final” versus “draft” IEPs" (confirmed; quotes split the phrase) |
| comparable | 41.323(5) | "services comparable to those described in the" |
| strengths | 41.324(1) | "The strengths of the child" |
| parent_concerns | 41.324(1) | "The concerns of the parents for enhancing the education" |
| amendment | 41.324(1) | "a written document to amend or modify the" (confirmed; line break) |
| annual_review | 41.324(2) | "not less frequently than annually" (no "annual review"; same note as Colorado) |
| tvi | 41.324(6) | "a teacher with an endorsement to teach individuals who are blind" |
| safeguards_notice | GUIDE p. 7 | "Procedural Safeguards" (confirmed; wraps across lines) |

CONCEPTS

| Key | Term | Verdict | Correct citation | Problem | Evidence |
|---|---|---|---|---|---|
| ia_dhs | Iowa Department of Human Services | preferred not found | GUIDE p. 2 | Use "Department of Human Services". The department merged into HHS in 2023; the sheet predates it. | "Department of Human Services DHS Iowa's agency that provides public assistance" |
| ia_early_access | Iowa Early ACCESS | preferred not found; type | GUIDE p. 3 | Use "Early ACCESS"; it is typed `acronym` only to force case-sensitive matching. "EA" is two letters. | "Early ACCESS EA Iowa's system for providing early intervention" |
| ia_eligible_individual | EI; eligible individuals | misplaced | GUIDE p. 3 (EI) | "EI" usually means early intervention elsewhere; regional to IA, low risk. | "Eligible Individual EI" |
| ia_aea | area education agencies; AEAs | misplaced | elsewhere in ch. 41 | Plurals not in 41.4 itself. | "“Area education agency” or “AEA” is a political" |

Terms-sheet entries the script missed because the two-column layout wraps them were all confirmed by hand in raw text order: AIM/AEM and "Accessible Educational Materials", "Child Outcome Summary Process", "Educational Evaluation Report", "Postsecondary Expectations", "Postsecondary Summary", "Iowa Department of Education" with IDOE/IDE, "Iowa Administrative Code", "Iowa IDEA Information" (i3), IVRS, IDPH, CHSC, DCCH, SWVPP, TAP, AAC, IHP, "Speech Language Pathologist".

## Safety and typing

- No new string is a first name, surname or place on its own except state agency names containing "Iowa" (the build marks them high).
- "AIM" and "TAP" are common words in all caps; `find("we AIM to finish")` returns `AIM`. Harmless to privacy, regional to IA.
- "support services" (`ia_support_svc`) is a very generic phrase; it is flagged `common_english_word` and `phrase_only`. Acceptable.
- "Sp.Ed." is national; the collision report pairs it with the first name "Ed", but only the whole token "Sp.Ed." matches.
- "head injury" (for TBI) pairs with the surname "Head" in the collision report; low risk because it only matches as a phrase.

## Missed terms (existing concepts used two or more times, not attested)

1. Adversely affects educational performance (15). 2. Functional performance (8). 3. Language impairment, under Language disorder (5). 4. Adaptive behavior (4). 5. Qualified examiner (3). 6. Scientific, research-based intervention (3). 7. Consideration of Special Factors (2). 8. Vocational rehabilitation services (2). 9. Service coordinator (2). 10. Postsecondary education (2). Not missed on purpose: "child requiring special education" (Connecticut's string; the docstring explains), "nonpublic school" (California's certified-NPS concept, a different thing), "Instructional services" (Michigan's concept; Iowa's `ia_instr_svc` is narrower).

## Docstring

Accurate. Could add that the preferred terms of `ia_dhs` and `ia_early_access` are normalised forms, if they are kept.


## Resolution (applied 2026-10-08)

- `ia_dhs`: preferred term is now "Department of Human Services", the sheet's wording; the duplicate synonym is gone.
- `ia_early_access`: kept "Iowa Early ACCESS". Making "Early ACCESS" the preferred term would collide at build time with Colorado's "Early Access", and only acronym-type strings match case-sensitively in `spedlex/build.py`. The record's note now says both things.
- `ia_aea` cites 41.4 and 41.2(1), where both plurals appear; `ia_eligible_individual` cites 41.8 and 41.50 for the plural. "EI" moves to a new `iowa_supplement` layer cited to GUIDE p. 3.
- Added 7 missed terms: `adverse` 41.50(1), `adaptive` 41.50(6), `func_perf` 41.303(1), `srbi` 41.307(1), `vr_services` 41.34(3), `service_coord` 41.321(6), `postsec_ed` 41.43(1).
- Not added: "language impairment" (part of the category name, already `sli`) and "Consideration of Special Factors" / "Qualified examiner" (other states' concepts).
- The 18 weak attestations stay: they use the federal rule wording, as other layers' attestations of the same keys do.
