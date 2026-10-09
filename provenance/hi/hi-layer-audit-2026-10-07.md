# Audit: Hawaii layer (`sources/states/hawaii.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-07 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section (and paragraph, where given) or page of text extracted from the PDFs in this folder, with ligatures normalized. Entries without a literal hit were checked by hand.

Documents: HAR Title 8 Chapter 60 (BOE copy, Eff 11/23/09), HIDOE Procedural Safeguards Notice (May 2022), HIDOE brochure "Special Education: Is it for your child?" (RS 26-0535, Nov. 2025).

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `autism` — Haw. Code R. § 8-60-39(a) | Autism, autism spectrum disorder, ASD, autism spectrum disorders | confirmed |  |  | §8-60-39 Eligibility criteria. (a)(1) Autism spectrum disorder. A student shall be eligible under the category |
| 2 | `deafness` — Haw. Code R. § 8-60-39(b) | deaf, Deafness, deafness including hard of hearing | confirmed |  |  | to subsection (e). (b) Deaf. A student shall be eligible under the disability category of |
| 3 | `deafblind` — Haw. Code R. § 8-60-39(c) | Deaf-blindness, deafblindness, deaf-blind, deaf/blind, dual sensory impairment, dual senso | confirmed |  |  | student's educational performance. (c) Deaf-blindness. A student shall be eligible under the category of deaf-blindness: |
| 4 | `dd` — Haw. Code R. § 8-60-39(d) | Developmental delay, DD, developmental delays, developmentally delayed, young child with a | confirmed |  |  | and educational needs. (d) Developmental delay. (1) A student, aged three through five, shall be |
| 5 | `ed` — Haw. Code R. § 8-60-39(e) | emotional disability | confirmed |  | "emotional disability" exists for other states; this entry adds US-HI (keep) | the student has an emotional disability pursuant to subsection (e). (b) Deaf. A student shall |
| 6 | `hi` — Haw. Code R. § 8-60-39(f) | Hearing impairment, hard of hearing, hearing loss, HI, DHH, deaf or hard of hearing, audit | confirmed |  |  | amplification; or (2) The hearing impairment adversely affects the student's educational performance. (g) Intellectual disability. |
| 7 | `id` — Haw. Code R. § 8-60-39(g) | Intellectual disability, ID, mental retardation, mild intellectual disability, moderate in | confirmed |  |  | student's educational performance. (g) Intellectual disability. A student shall be eligible under the disability category |
| 8 | `md` — Haw. Code R. § 8-60-39(h) | Multiple disabilities, MD, multiple impairments, multiple impairment, severely multiply im | confirmed |  |  | student's educational performance. (h) Multiple disabilities. (1) A student shall be eligible under the category |
| 9 | `oi` — Haw. Code R. § 8-60-39(i) | orthopedic disability | confirmed |  |  | in subsection (f); (iv) Orthopedic disability, as set forth in subsection (i); (v) Other health |
| 10 | `ohi` — Haw. Code R. § 8-60-39(j) | other health disability | confirmed |  | "other health disability" exists for US-MN; this entry adds US-HI (keep) | in subsection (i); (v) Other health disability, as set forth in subsection (j); or (vi) |
| 11 | `sld` — Haw. Code R. § 8-60-39(k) | Specific learning disability, learning disability, SLD, LD, specific learning disabilities | confirmed |  |  | student's educational performance. (k) Specific learning disability. (1) General. Specific learning disability means a disorder |
| 12 | `sli` — Haw. Code R. § 8-60-39(l) | speech or language disability | confirmed |  |  | or economic disadvantage. (l) Speech or language disability. A student shall be eligible under the |
| 13 | `tbi` — Haw. Code R. § 8-60-39(m) | Traumatic brain injury, TBI | confirmed |  |  | grammar, or both. (m) Traumatic brain injury. (1) A student shall be eligible under the |
| 14 | `vi` — Haw. Code R. § 8-60-39(n) | visual disability including blindness | confirmed |  |  | subsection (j); or (vi) Visual disability including blindness, as set forth in subsection (n); (2) |
| 15 | `charter_school` — Haw. Code R. § 8-60-2 | Charter school, charter schools, community school | confirmed |  |  | of that student. “ Charter school” means a public school as defined in both federal |
| 16 | `cwd` — Haw. Code R. § 8-60-2 | student with a disability, students with disabilities, Child with a disability, children w | confirmed |  |  | functional capabilities of a student with a disability. The term does not include a medical |
| 17 | `resolution` — Haw. Code R. § 8-60-2 | resolution session, Resolution meeting, resolution process, resolution period, resolution  | confirmed |  |  | with a disability. “ Resolution session” means a meeting convened within fifteen days of a |
| 18 | `sto` — Haw. Code R. § 8-60-2 | short-term objectives, benchmarks, short term objectives, Benchmarks or short-term objecti | confirmed |  |  | 8-60-23 through 8-60-25. “ Short-term objectives/benchmarks” means measurable intermediate performance steps that will enable parents, |
| 19 | `iaes` — Haw. Code R. § 8-60-2 | Interim alternative educational setting, IAES, interim alternative education setting, alte | confirmed |  |  | of the Act. “ Interim alternative educational setting” or “IAES” means a temporary placement for |
| 20 | `pwn` — Haw. Code R. § 8-60-2 | Prior written notice, PWN, written notice, prior notice, Notice of Recommendation, Notice  | confirmed |  |  | general education curriculum. “ Prior written notice” or “PWN” means written notification given to parents |
| 21 | `surrogate` — Haw. Code R. § 8-60-73 | Surrogate parent, surrogate parents, temporary surrogate, special education surrogate pare | confirmed |  |  | §8-60-73 Surrogate parents. (a) General. The department shall ensure that the rights of a student |
| 22 | `safeguards_notice` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 1 | Procedural safeguards notice, procedural safeguards, Parent Rights, notice of procedural s | confirmed |  |  | PROCEDURAL SAFEGUARDS NOTICE for Parents and Students Under The Individuals With Disabilities Education Act and |
| 23 | `hi_doe` — HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 | Hawai'i State Department of Education | confirmed |  | Stored only as "Hawai'i" with a straight apostrophe. The brochure also prints it with a curly quote or okina, which the matcher treats as different text, and the automatic place check misses the okina spellings (the manual flag covers this concept). Add variants and teach the place list the okina forms | your child? child? IsIsititfor Hawai'i State Department of Education Office of Student Support of Services |
| 24 | `hi_ossss` — HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 | Office of Student Support Services | confirmed |  |  | Education Exceptional Support Branch Office of Student Support Services Special Education Section Exceptional Support Branch |
| 25 | `hi_esb` — HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 | Exceptional Support Branch | confirmed |  |  | Hawaii State Department Education Exceptional Support Branch Office of Student Support Services Special Education Section |
| 26 | `hi_mcb` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 19 | Monitoring and Compliance Branch | confirmed |  |  | the complaint with the Monitoring and Compliance Branch, Attn: Complaints Management Program. A model can |
| 27 | `hi_cmp` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 19 | Complaints Management Program | confirmed |  |  | and Compliance Branch, Attn: Complaints Management Program. A model can be found at: https://www.hawaiipublicschools.org/DOE%20Forms/Special%20Education/WrittenComplaint.pdf |
| 28 | `hi_cas` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 19 | Complex Area Superintendent | confirmed |  |  | the complaint to the Complex Area Superintendent serving the student at the same time the |
| 29 | `hi_conciliation` — HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 | Conciliation | not_found (2025 edition) |  | Only in the hidden 2021 layer of the brochure. The visible Nov. 2025 text lists "mediation, facilitation, written complaint, or a due process impartial hearing". Drop it, or find a current source | (visible 2025 p. 1) These practices include: mediation, facilitation, written complaint, or a due process |
| 30 | `hi_ldah` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 | Leadership in Disabilities & Achievement of Hawaii | confirmed |  |  | TB1A Honolulu, HI 96821 Leadership in Disabilities & Achievement of Hawaii 245 N. Kukui Street, |
| 31 | `hi_drc` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 | Hawaii Disability Rights Center | confirmed |  |  | E-mail: info@ldahawaii.org Website: www.ldahawaii.org Hawaii Disability Rights Center 1132 Bishop Street, Suite 2102 Honolulu, HI |
| 32 | `hi_spin` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 | Special Parent Information Network | confirmed |  |  | E-mail: mcp@mediatehawaii.org Website: www.mediatehawaii.org Special Parent Information Network 1010 Richards Street, Room 118 Honolulu, HI |
| 33 | `hi_ccc` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 | Community Children's Council Office | confirmed |  |  | 40 OTHER SUPPORT SERVICES Community Children's Council Office 4680 Kalanianaole Hwy., TB1A Honolulu, HI 96821 |
| 34 | `hi_hfaa` — HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 | Hawaii Families as Allies | confirmed |  |  | (800) 499-4302 Website: www.legalaidhawaii.org Hawaii Families as Allies P.O. Box 1971 Aiea, HI 96701 Mediation |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Complex area | GUIDE and PSN (2 uses) | The Department's regional unit; `hi_cas` covers only its superintendent |
| Facilitation | GUIDE p. 1 (2025 text) | Listed with mediation as a resolution practice; may map to `iep_facil` |

## 3. Summary

- **34 entries: 33 confirmed, 0 misplaced, 1 not found** (conciliation, which is only in the brochure's superseded 2021 layer).
- **Safety:** no single letters, and no person's name standing alone as a term. Place names are graded automatically.
- **Build:** `build --check` passes and all 56 tests pass.

**Most important fixes**

1. **Spelling of Hawai'i.** `hi_doe` is stored only with a straight apostrophe. The brochure also uses a curly quote and the okina (ʻ), and the matcher treats those as different text. Add those spellings as variants.
2. **The automatic place check misses the okina spellings** ("Hawaiʻi", "Hawai‘i", "Hawai'i"). `hi_doe` is safe because it was flagged by hand, but a future Hawaiian term would be missed. Add the variants to `reference/places/us_jurisdictions.tsv`.
3. **"Conciliation" (`hi_conciliation`) comes from the superseded 2021 edition.** The brochure PDF hides its 2021 text behind the 2025 text. I rendered page 1: the visible 2025 list is "mediation, facilitation, written complaint, or a due process impartial hearing". The docstring says only terms also in the 2025 text are cited, so drop this concept or cite a current source. The other three brochure-cited names are visible on the 2025 cover.

**Docstring:** Accurate on documents, page counts and dates. Every § 8-60-39 category letter matches. Leaving out the complex area office names, the Legal Aid Society, the State Bar and the Mediation Center was the right call.

**Update (2026-10-07):** Fixes applied: `hi_conciliation` was removed and its ID (SPED:000889) retired. The place list now includes "Hawaiʻi", "Hawai‘i", "Hawai’i" and "Hawai'i", with a test. No variant spellings were added to `hi_doe`: on checking, the brochure prints the Department's name only with a straight apostrophe (the curly form is on the island name in the phone list), so other spellings would be uncited.
