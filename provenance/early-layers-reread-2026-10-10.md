# Re-reading the early layers' sources (2026-10-10)

Auditor: claude-opus-5-5. Follow-up to `consistency-audit-2026-10-10.md` §3. The 19 layers built on Oct. 3 were made from web pages and PDFs that are not in `sources/documents.tsv`, so there is no saved copy to search. At the maintainer's direction, the text of those layers' own cited sources was read again, plus a few more sections of rules they already cite. The aim was to find terms the first pass should have recorded. The lexicon's purpose did not change.

## Method and its limits

Each source was read through a web fetch. A model extracted every acronym and its expansion, every named agency, program, form, assessment and statute, and every defined term, with the page or paragraph. Each candidate was checked against `data/spedlex.csv`, and only terms SPEDLex lacked were added. The fetch does not give a hashed copy, and its extraction was not checked word for word against the PDF. So every new record is `candidate`, even where the source is a regulation, and the supplements cite by URL like the layers they extend. **A reviewer should spot-check the citations, especially the page numbers, before these records are accepted.**

## What was read

| State | Sources read | Result |
|---|---|---|
| Texas | TEA Notice of Procedural Safeguards; TEA Parent's Guide to the ARD Process; 19 TAC §89.1040; 19 TAC §89.1055 (new) | `texas_supplement`, 20 concepts, 3 strings |
| California | CDE Notice of Procedural Safeguards (OAH page); 5 CCR §3001; Educ. Code §§56026, 56345, 56521.1 (new) | `california_supplement`, 16 concepts, 4 strings; includes the behavioral emergency report the layer had deferred |
| New York | NYSED Procedural Safeguards Notice (2017); 8 NYCRR §§200.1, 200.6 | `new_york_supplement`, 11 concepts, 1 string |
| Florida | Florida Part B Procedural Safeguards Notice; Fla. Admin. Code R. 6A-6.03411(1) | `florida_supplement`, 4 concepts |
| Pennsylvania | PDE Parent Guide (2008); 22 Pa. Code §§14.101, 14.105 | `pennsylvania_supplement_2`, 14 concepts |
| Illinois | ISBE Parent Guide; 23 Ill. Adm. Code §226.75 | `illinois_supplement`, 12 concepts, 1 string |
| Georgia | Ga. Comp. R. & Regs. 160-4-7-.06, -.21 (new) | `georgia_supplement`, 1 concept (Babies Can't Wait) |
| Massachusetts | A Parent's Guide to Special Education | `massachusetts_supplement`, 14 concepts, 1 string |
| Washington | OSPI Notice of Special Education Procedural Safeguards | `washington_supplement`, 3 concepts |
| Oregon | ODE Procedural Safeguards Notice K-21 | `oregon_supplement`, 1 concept |
| Minnesota | Minn. R. ch. 3525 | `minnesota_supplement`, 2 concepts |
| Kansas, Utah, Idaho, Nevada, Tennessee | each state's safeguards notice | nothing missing |
| Virginia, Louisiana | VAAP parent FAQ; Bulletin 1508 index | nothing missing worth adding ("Collections of Evidence", from the retired VAAP, was left out) |
| Missouri | the district copy the layer cites | no usable text; nothing added |

In total 0.51.0 adds 98 concepts and 10 strings, all `candidate`.

## Left out on purpose

- Local parent organizations and family resource centers named for counties or cities (the California notice lists 23).
- The Massachusetts Department of Mental Retardation, an older agency name that contains a disfavored term; whether to record it as legacy is the maintainer's call.
- The two-letter acronyms the sources use without spelling them out (e.g. EC for the California Education Code, IC), and the acronyms "PAL" and "ODE", whose expansions are not in the documents read.
- Statute section numbers, form numbers and contact details.

## Still to do

The early layers' sources remain outside the manifest. Saving copies into `.sources-cache/<xx>/` with rows in `sources/documents.tsv` would allow a verbatim audit with `prompts/audit-layer.md` and would let these records move from `candidate`.
