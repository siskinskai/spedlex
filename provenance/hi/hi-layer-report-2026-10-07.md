# Hawaii layer (v0.31.0): contributor report

Drafted 2026-10-07 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` and CONTRIBUTING.md. A person must review this before it is submitted.

## 1. Documents read
- **RULE**: Hawaii Administrative Rules, Title 8, Chapter 60, Provision of a Free Appropriate Public Education for a Student with a Disability. This is the Board of Education PDF, 108 pp.; its sections show "Eff 11/23/09". §§ 8-60-2 (definitions) and 8-60-39 (eligibility criteria) were read in full and the other sections read by heading and searched. I did not check for amendments after the dates the file shows.
- **PSN**: HIDOE Procedural Safeguards Notice for Parents and Students, May 2022, 44 pp. Pages 1-2, 19-21 and 44 were read in full and the rest searched. Citations use PDF pages; the printed numbers are four lower.
- **GUIDE**: HIDOE brochure "Special Education: Is it for your child?", RS 26-0535, November 2025, 2 pp. Read in full. Its page 1 also carries text from the June 2021 edition behind the 2025 text. Cited terms were checked against the 2025 text, though one quote (`hi_esb`) runs into the 2021 date.
- **How the files were read**: the rule came from the Board of Education's Administrative Rules page and the PSN and brochure from HIDOE's Parent Rights and Child Find pages, using the same method as Ohio. Copies are in `.sources-cache/hi/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `hi_doe` | Hawai'i State Department of Education | "it for your child? Hawai'i State Department of Education Office of Student Support Services Exceptional" | HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 |
| `hi_ossss` | Office of Student Support Services | "State Department of Education Office of Student Support Services Exceptional Support Branch Special Education Section" | HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 |
| `hi_esb` | Exceptional Support Branch | "of Student Support Services Exceptional Support Branch Special Education Section June 2021 If parent(s)/legal guardian(s)" | HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 |
| `hi_mcb` | Monitoring and Compliance Branch | "the complaint with the Monitoring and Compliance Branch , Attn: Complaints Management Program. A model" | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 19 |
| `hi_cmp` | Complaints Management Program | "and Compliance Branch, Attn: Complaints Management Program . A model can be found at: https://www.hawaiipublicschools.org/DOE%20Forms/Special%20Education/WrittenComplaint.pdf" | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 19 |
| `hi_cas` | Complex Area Superintendent | "the complaint to the Complex Area Superintendent serving the student at the same time the" | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 19 |
| `hi_conciliation` | Conciliation | "practices include: mediation, facilitation, conciliation , written complaint and a due process impartial hearing. For" | HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. 1 |
| `hi_ldah` | Leadership in Disabilities & Achievement of Hawaii | "familypartnerships@k12.hi.us Website: https://www.hawaiipublicschools.org/ParentsAndStudents/ SupportForParents/Pages/CCC.aspx Leadership in Disabilities & Achievement of Hawaii 245 N. Kukui Street," | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 |
| `hi_drc` | Hawaii Disability Rights Center | "E-mail: info@ldahawaii.org Website: www.ldahawaii.org Hawaii Disability Rights Center 1132 Bishop Street, Suite 2102 Honolulu, HI" | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 |
| `hi_spin` | Special Parent Information Network | "E-mail: webinfo@hsba.org Website: https://hsba.org Special Parent Information Network 1010 Richards Street, Room 118 Honolulu, HI" | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 |
| `hi_ccc` | Community Children's Council Office | "40 OTHER SUPPORT SERVICES Community Children's Council Office 4680 Kalanianaole Hwy., TB1A Honolulu, HI 96821" | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 |
| `hi_hfaa` | Hawaii Families as Allies | "(800) 499-4302 Website: www.legalaidhawaii.org Hawaii Families as Allies P.O. Box 1971 Aiea, HI 96701 Telephone:" | HIDOE Procedural Safeguards Notice (May 2022), PDF p. 44 |

All quotes come from text extracted with pdftotext, with line breaks collapsed. Page-header and contact-list text sometimes runs into a quote. Every new string and every attested key was checked automatically against the cited section or page, and all checks passed.

## 3. Unsure
- **All 12 new concepts are `candidate`**, because they come from the PSN and the brochure. The rule's contribution is attestation plus Hawaii's category labels: "speech or language disability", "orthopedic disability", "visual disability including blindness", "emotional disability" and "other health disability".
- **"Other health disability"** was already on `ohi` typed as a plural with a Minnesota tag. Re-adding it only adds the Hawaii tag, but the existing type looks wrong and a reviewer may want to retype it as a synonym.
- **`hi_doe`'s preferred term** uses the ʻokina spelling as printed in the 2025 brochure ("Hawai'i"). It is flagged `place_name` by hand, since the automatic list may not match that spelling.
- **`hi_conciliation`** is flagged `common_english_word`. The brochure lists it as a resolution practice but does not define it.

## 4. Risky
- **Place names** (high risk): Hawai'i State Department of Education, Leadership in Disabilities & Achievement of Hawaii, Hawaii Disability Rights Center, Hawaii Families as Allies.
- **Complex Area Superintendent** is a role title, not a person, so it is safe to add.

## 5. Left out on purpose
- Complex area office names and phone numbers (place names with contact details).
- Legal Aid Society of Hawaii, Hawaii State Bar Association and Mediation Center of the Pacific, which are general providers listed only as contacts.
- "Special Education Section", which is too generic as a phrase.
- **"Partially-sighted"**, a sub-criterion of visual disability in § 8-60-39(n). A reviewer could add it under `vi`.

## Update (2026-10-07)

After the audit (`hi-layer-audit-2026-10-07.md`), `hi_conciliation` was removed, because it appears only in the brochure's superseded 2021 text, and its ID (SPED:000889) was retired. The layer now adds 11 `candidate` concepts, not 12. The place-name list now matches the ʻokina and apostrophe spellings of "Hawaiʻi", so a future Hawaiian term is graded automatically; `hi_doe` keeps its manual `place_name` flag.
