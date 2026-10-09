# Wyoming layer (v0.42.0): contributor report

Drafted 2026-10-08 with Claude Sonnet 5.5 (`claude-sonnet-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` has **not** been run: it should be run in a fresh conversation, ideally with a different model. Build: `python -m spedlex.build --check` passes and `pytest -q` passes (79 tests). The layer attests 110 concepts and adds 10 (8 machine_validated, 2 candidate). There are no string conflicts and no new cross-state acronym ambiguities.

## 1. Documents read
- **RULE**: WDE Chapter 7, Services for Children with Disabilities (reference 206.0002.7.03222010, effective 03/22/2010, shown as current on the rules portal on 10/08/2026). The portal copy `WY-7767.pdf` (31 pp.) is a scan with no text layer, so the words came from `WY-Chapter-7-Rules.pdf` (30 pp., OCR text layer). **The two were not compared page by page.** Read in full with `pdftotext`. The OCR has errors (WDE appears as "WOE"; some words are garbled in the disability category text), so each string was checked against the surrounding wording. Citations are by section, e.g. § 4(d)(x).
- **PSN**: WDE Special Education Programs Division, *Notice of Procedural Safeguards* (May 2025, 36 pp.), the Wyoming courts' hosted copy. Read in full with `pdftotext`; PDF page = printed page. It is mostly the federal model notice, so nearly all entries only attest existing concepts.
- **Missing**: no main parent guide or IEP manual. The WDE "Parents Guide to Special Education" web page could be opened by a fetch tool but not saved with page numbers, so nothing was taken from it. Alternate assessment and diploma pages were not provided. The rule dates from 2010, so newer WDE terms are likely absent.
- A script checked that each attested concept's wording appears on its cited page (PSN) or in the rule text. Six had no literal hit and were checked by hand: `ppps` (§ 4(a)(iii), "parentally enrolled in a private … school"), `mbd` (§ 4(d)(x), OCR "minir,al brain dysfunction"), `artic` (§ 4(d)(xi)(A)(I), "Articulation"), `revoke` (§ 6(b), "revocation of parental consent"), `disprop` (§ 9(d)(iii), "Disproportionate representation") and `homeless` (PSN p. 21, "homeless child or youth"). All are wording differences, not different concepts.

## 2. New concepts
| Key | Term | Quote (≤15 words) | Citation |
|---|---|---|---|
| `wy_wde` | Wyoming Department of Education | "the Wyoming Department of Education (WDE)" | Rule § 2(a) |
| `wy_sepd` | Special Education Programs Division | "Special Education Programs Division" | PSN p. 1 |
| `wy_uplift` | UPLIFT | "UPLIFT 307-274-8861" (listed under Wyoming Parent Advocacy Organizations) | PSN p. 3 |
| `wy_ddd` | Developmental Disabilities Division | "Department of Health, Developmental Disabilities Division (Division)" | Rule § 9(b) |
| `wy_ieu` | Intermediate educational unit | "the Division shall be deemed an intermediate educational unit" | Rule § 9(b) |
| `wy_dfs` | Department of Family Services | "The Department of Family Services (DFS) shall pay residential and treatment costs" | Rule § 5(i)(i) |
| `wy_swdf` | Wyoming Severe Discrepancy Formula | "Wyoming Severe Discrepancy Formula" | Rule § 4(d)(x)(E)(I) |
| `wy_dev_preschool` | Developmental preschool center | "transitioning from developmental preschool centers in the state of Wyoming" | Rule § 5(f)(iii) |
| `wy_interdistrict` | Inter-district placement | "Inter-district placements." | Rule § 5(g) |
| `wy_court_placement` | Court-ordered placement | "court ordered placements of children in private residential treatment facilities" | Rule § 5(i)(i) |

New strings on existing concepts: "Cognitive Disability" (`id`, synonym, tagged US-WY) and "home based education" (`home_education`, tagged US-WY).

## 3. Unsure
- **"Cognitive Disability"** is Wyoming's current label for intellectual disability; Indiana's copy of the same string is typed legacy. I typed Wyoming's as synonym. Reviewer to confirm.
- **`wy_ddd`** is parented to `wy_ieu`, and `wy_ieu` to `esa`, because the rule says the Division "shall function as an educational service agency." `wy_ieu`, `wy_interdistrict` and `wy_court_placement` have no `jurisdiction` since the ideas exist elsewhere; only the first has a federal-law origin (34 CFR 300.12). Reviewer to decide whether `wy_ieu` should be US-WY.
- **Parent center**: the PSN lists "Parent Information Center/Parent Education Network" (WPIC). I only attested `pti` (p. 22 is the model-notice sentence about parent training and information centers, not WPIC's name). The name itself was not recorded because "Parent Information Center" is already a New Hampshire concept (`nh_pic`) and "Parent Education Network" a Pennsylvania one (`pen`).
- **Page citations** in the PSN are PDF pages. They match the printed numbers. Rule citations are by section because the rule's printed pages are "7-N".
- **Attestations by a scanned/OCR rule** are marked machine_validated like other rule text, but the OCR was not proofed against the portal scan.

## 4. Risky
- **Auto-flagged high risk (place_name):** Wyoming Department of Education and Wyoming Severe Discrepancy Formula, because "Wyoming" is the state name. Both are full-phrase terms.
- **`UPLIFT`** is an ordinary English word used as an organization's name; flagged `common_english_word`. The notice does not say what UPLIFT stands for (if anything), and I did not guess.
- **`WDE`** and **`DFS`** are new acronyms tagged US-WY. DFS is not in the existing list; neither collides with a name that I could find, but the allowed-collision test is the authority.
- No eponyms, no acronyms that are also given names.

## 5. Left out
- Legal-aid providers, law school clinics and the Wyoming State Bar service in the PSN (not special-education terms).
- All addresses, phone numbers, web addresses, and the Office for Civil Rights regional office.
- The OHI conditions not already in SPEDLex (asthma, diabetes, heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever) and orthopedic examples (cerebral palsy, etc.): federal wording, not Wyoming's.
- Speech eligibility numbers (85% mastery, 1.5 standard deviations, 5% of words) and the Appendix A score table.
- Grade-span definitions (elementary, middle, high school), "private school" and "preschool children with disabilities" as defined, except `preschool_swd` which is attested.
- Monitoring and enforcement terms (§ 9: needs assistance, needs intervention, corrective action plan, compliance agreement, high-risk grantee) and § 8 funding terms.
- "Department of Health" as its own concept (generic wording in the rule).
