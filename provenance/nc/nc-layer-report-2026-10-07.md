# North Carolina layer (v0.30.0): contributor report

Drafted 2026-10-07 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` and CONTRIBUTING.md. A person must review this before it is submitted.

## 1. Documents read
- **POL**: Policies Governing Services for Children with Disabilities, State Board policies NC 1500-1508, revised March 2021, 132 pp. Read in full: NC 1500-2 (definitions), NC 1501-13, NC 1504-1.12 to 1504-1.15 and NC 1508 (class size and service levels). The rest was read by section heading and searched.
- **PSN**: Notice of Procedural Safeguards: Parent Rights and Responsibilities in Special Education, updated July 2026, 44 pp. Pages 1-7 and 29 were read and the rest searched. It follows the federal model notice closely.
- **Missing**: North Carolina publishes no separate statewide parent guide; the PSN is the parent-facing document. I also read NCDPI's one-page "Quick Guide to Special Education Dispute Resolution Processes" but did not cite it, because it is a national CADRE document rather than North Carolina's own.
- **How the files were read**: same method as Ohio. Copies are in `.sources-cache/nc/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `nc_dpi` | North Carolina Department of Public Instruction | "State Reserve (a) The North Carolina Department of Public Instruction will provide Special State Reserve" | NC Policies Governing Services for Children with Disabilities, NC 1506-1.11 |
| `nc_ecd` | Exceptional Children Division | "application developed by the Exceptional Children Division and disseminated annually. The Exceptional Children Division reviews" | NC Policies Governing Services for Children with Disabilities, NC 1506-1.11 |
| `nc_ecac` | Exceptional Children's Assistance Center | "of the IDEA. The Exceptional Children’s Assistance Center (ECAC) is North Carolina’s parent training and" | NC Policies Governing Services for Children with Disabilities, NC 1500-2.28 |
| `nc_psu` | Public school unit | "Written Notice Notice Your public school unit must give you written notice (provide you certain" | NCDPI Notice of Procedural Safeguards (July 2026), PDF p. 7 |
| `nc_comp_assess` | Comprehensive assessment system | "NC 1500-2.5 Comprehensive Assessment System Comprehensive assessment system- The data gathered within this assessment system" | NC Policies Governing Services for Children with Disabilities, NC 1500-2.5 |
| `nc_sps` | Systematic problem-solving process | "NC 1500-2.40 Systematic Problem-Solving Process A systematic problem-solving process is a structured, methodical approach to" | NC Policies Governing Services for Children with Disabilities, NC 1500-2.40 |
| `nc_recp` | Regular Early Childhood Program | "Children with Disabilities (a) Regular Early Childhood Program (RECP), Separate, and Other Settings: Caseload requirements" | NC Policies Governing Services for Children with Disabilities, NC 1508-2 |
| `nc_general_skills` | Special Education General Skills | "Level of Service/Supports 1 Special Education General Skills – Services/supports provided to individuals who require" | NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 |
| `nc_targeted_skills` | Special Education Targeted Skills | "and curriculum assistance. 2 Special Education Targeted Skills - Services/supports provided to students who require" | NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 |
| `nc_sustained_support` | Special Education Sustained Support | "by the LEA. 3 Special Education Sustained Support – Services/supports outside the general education classroom" | NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 |
| `nc_intensive_needs` | Special Education Intensive Needs | "throughout the day. 4 Special Education Intensive Needs – Services/supports outside the general education classroom" | NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 |
| `nc_ocs` | Occupational Course of Study | "or physical needs. 5 Occupational Course of Study – Number of assistants (job coaches) will" | NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 |

All quotes come from text extracted with pdftotext, with line breaks collapsed. Page-header and contact-list text sometimes runs into a quote. Every new string and every attested key was checked automatically against the cited section or page, and all checks passed.

## 3. Unsure
- **Source type**: POL is State Board policy rather than an administrative code chapter. It is typed `state_regulation` because it is the state's binding special education rule set, which makes 11 records `machine_validated`.
- **The NC 1508-3.1 service levels** (General Skills, Targeted Skills, Sustained Support, Intensive Needs) are placed under the existing `level_support`, which is a Pennsylvania-origin concept.
- **`nc_psu`** (Public school unit) comes from the PSN. The policies, which are older, use "LEA" instead.
- **Strings added to existing concepts**: "Responsiveness to instruction" and "responsiveness to intervention" went on `rti`, and "Multi-tiered System of Support" on `rti` as a variant. There is a separate existing `srbi` concept, but North Carolina's terms match `rti` more closely.

## 4. Risky
- **Place names** (high risk): North Carolina Department of Public Instruction.
- **ECAC and RECP** are tagged US-NC. Neither collides with a given name in the test list.

## 5. Left out on purpose
- The State Board members and NCDPI staff named on POL pp. 2-3 (personal names with home towns).
- **NCDPI**: POL uses the acronym but never spells it out next to the full name.
- **The CADRE Quick Guide** (see Documents read).
- **Possible additions**: "Exceptional Children (EC)" program wording and "Department of Health and Human Services" as an LEA, both generic.

## Update (2026-10-07)

After the audit (`nc-layer-audit-2026-10-07.md`), MTSS became its own general concept, `mtss` (SPED:000895), cited to NC 1500-2.25 and `machine_validated`. "Multi-tiered System of Support" is no longer on `rti`, so the layer now adds 13 concepts (12 `machine_validated`, 1 `candidate`), not the 12 described above.
