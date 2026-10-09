# Audit: North Carolina layer (`sources/states/north_carolina.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-07 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section (and paragraph, where given) or page of text extracted from the PDFs in this folder, with ligatures normalized. Entries without a literal hit were checked by hand.

Documents: Policies Governing Services for Children with Disabilities (NC 1500-1508, rev. Mar. 2021), NCDPI Notice of Procedural Safeguards (July 2026).

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `autism` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(1) | Autism, autism spectrum disorder, ASD, autism spectrum disorders | confirmed |  |  | NC 1503-3.5 as having autism, deaf-blindness, deafness, developmental delay (applicable only to children ages three |
| 2 | `deafblind` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(2) | Deaf-blindness, deafblindness, deaf-blind, deaf/blind, dual sensory impairment, dual senso | confirmed |  |  | 1503-3.5 as having autism, deaf-blindness, deafness, developmental delay (applicable only to children ages three through |
| 3 | `deafness` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(3) | Deafness, deaf, deafness including hard of hearing | confirmed |  |  | as having autism, deaf-blindness, deafness, developmental delay (applicable only to children ages three through seven), |
| 4 | `dd` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(4) | Developmental delay, DD, developmental delays, developmentally delayed, young child with a | confirmed |  |  | having autism, deaf-blindness, deafness, developmental delay (applicable only to children ages three through seven), hearing |
| 5 | `ed` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(5) | emotional disability | confirmed |  |  | other health impairment, serious emotional disability, specific learning disability, speech or language impairment, traumatic brain |
| 6 | `hi` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(6) | Hearing impairment, hard of hearing, HI, DHH, deaf or hard of hearing, auditory impairment | confirmed |  |  | ages three through seven), hearing impairment, intellectual disability, multiple disabilities, orthopedic impairment, other health impairment, |
| 7 | `id` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(7) | Intellectual disability, mental retardation, ID, mild intellectual disability, moderate in | confirmed |  |  | through seven), hearing impairment, intellectual disability, multiple disabilities, orthopedic impairment, other health impairment, serious emotional |
| 8 | `md` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(8) | Multiple disabilities, MD, multiple impairments, multiple impairment, severely multiply im | confirmed |  |  | hearing impairment, intellectual disability, multiple disabilities, orthopedic impairment, other health impairment, serious emotional disability, specific |
| 9 | `oi` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(9) | Orthopedic impairment, physical impairment, OI, physically impaired, orthopedic disability | confirmed |  |  | intellectual disability, multiple disabilities, orthopedic impairment, other health impairment, serious emotional disability, specific learning disability, |
| 10 | `ohi` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(10) | Other health impairment, health impairment, other health-impairment, OHI, health impairmen | confirmed |  |  | multiple disabilities, orthopedic impairment, other health impairment, serious emotional disability, specific learning disability, speech or |
| 11 | `sld` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(11) | Specific learning disability, learning disability, SLD, LD, specific learning disabilities | confirmed |  |  | impairment, serious emotional disability, specific learning disability, speech or language impairment, traumatic brain injury, or |
| 12 | `sli` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(12) | Speech or language impairment, speech-language impairment, SLI, speech impairment, speech  | confirmed |  |  | disability, specific learning disability, speech or language impairment, traumatic brain injury, or visual impairment (including |
| 13 | `tbi` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(13) | Traumatic brain injury, TBI | confirmed |  |  | speech or language impairment, traumatic brain injury, or visual impairment (including blindness), and who, by |
| 14 | `vi` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.4(b)(14) | Visual impairment including blindness, visual impairment, VI, visual impairment/blind, vis | confirmed |  |  | by birth trauma. (14) Visual impairment including blindness means an impairment in vision that, even |
| 15 | `pe` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.1 | Physical education, adapted physical education, APE, specially designed physical education | confirmed |  |  | NC 1500-2.1 Adapted Physical Education (a) Children with disabilities shall have equal access to the |
| 16 | `dyslexia` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.9 | Dyslexia, Specific Learning Disability/Dyslexia | confirmed |  |  | NC 1500-2.9 Dyslexia Dyslexia is a specific learning disability that is neurobiological in origin. It |
| 17 | `rti` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.25 | Multi-tiered System of Support | confirmed |  | "Multi-tiered System of Support" is mapped to `rti` as a spelling variant. NC 1500-2.25 defines MTSS as a school-improvement framework "for all", distinct from responsiveness to instruction (NC 1500-2.33). Make it its own concept (no `mtss` exists yet) | NC 1500-2.25 Multi-tiered System of Support (MTSS) MTSS is a multi-tiered framework which promotes school |
| 18 | `rti` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.33 | responsiveness to instruction, responsiveness to intervention | confirmed |  | "Multi-tiered System of Support" is mapped to `rti` as a spelling variant. NC 1500-2.25 defines MTSS as a school-improvement framework "for all", distinct from responsiveness to instruction (NC 1500-2.33). Make it its own concept (no `mtss` exists yet) | NC 1500-2.33 Responsiveness to Instruction/Responsiveness to Intervention Responsiveness to instruction/responsiveness to intervention is the practice |
| 19 | `screening` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.43 | universal screening, Screening for instructional purposes | confirmed |  |  | NC 1500-2.43 Universal Screening Universal screening includes administering measures or collecting other data to allow |
| 20 | `pti` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.28 | Parent training and information center, PTI, parent center, PTIC, PTIs | confirmed |  |  | NC 1500-2.28 Parent Training and Information Center Parent training and information center means a center |
| 21 | `state_panel` — NC Policies Governing Services for Children with Disabilities, NC 1501-13.1 | Council on Educational Services for Exceptional Children | confirmed |  | NC's state advisory panel; the concept is high risk because of another state's string, not this one | (referred to as The Council on Educational Services for Exceptional Children) for the purpose of |
| 22 | `charter_school` — NC Policies Governing Services for Children with Disabilities, NC 1502-10 | charter schools | confirmed |  |  | NC 1502-10 TREATMENT OF CHARTER SCHOOLS AND THEIR STUDENTS ...................................... 55 NC 1502-10 Treatment of |
| 23 | `sro` — NC Policies Governing Services for Children with Disabilities, NC 1504-1.15 | impartial review officer | confirmed |  | "impartial review officer" is the SEA-appointed reviewer of OAH decisions, so `sro` fits | SEA must appoint an impartial review officer to conduct an impartial review of the findings |
| 24 | `itinerant` — NC Policies Governing Services for Children with Disabilities, NC 1508-2 | Itinerant Preschool Services | confirmed |  |  | teacher, 2 assistants. (c) Itinerant Preschool Services: Services to preschool children with disabilities are often |
| 25 | `safeguards_notice` — NCDPI Notice of Procedural Safeguards (July 2026), PDF p. 1 | Parent Rights and Responsibilities in Special Education | confirmed |  |  | Notice of Procedural Safeguards Parent Rights and Responsibilities in Special Education The Individuals with Disabilities |
| 26 | `oah` — NCDPI Notice of Procedural Safeguards (July 2026), PDF p. 29 | Office of Administrative Hearings, OAH | confirmed |  |  | to the North Carolina Office of Administrative Hearings. Impartial Administrative Law Judge At a minimum, |
| 27 | `dp_hearing` — NCDPI Notice of Procedural Safeguards (July 2026), PDF p. 29 | Impartial due process hearing, due process hearing, impartial hearing, administrative law  | confirmed |  |  | 34 CFR §300.511 - Impartial Due Process Hearing General Whenever a due process complaint is |
| 28 | `nc_dpi` — NC Policies Governing Services for Children with Disabilities, NC 1506-1.11 | North Carolina Department of Public Instruction | confirmed |  |  | State Reserve (a) The North Carolina Department of Public Instruction will provide Special State Reserve |
| 29 | `nc_ecd` — NC Policies Governing Services for Children with Disabilities, NC 1506-1.11 | Exceptional Children Division | confirmed |  |  | application developed by the Exceptional Children Division and disseminated annually. The Exceptional Children Division reviews |
| 30 | `nc_ecac` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.28 | Exceptional Children's Assistance Center, ECAC | confirmed |  |  | of the IDEA. The Exceptional Children's Assistance Center (ECAC) is North Carolina's parent training and |
| 31 | `nc_psu` — NCDPI Notice of Procedural Safeguards (July 2026), PDF p. 7 | Public school unit | confirmed |  |  | Written Notice Notice Your public school unit must give you written notice (provide you certain |
| 32 | `nc_comp_assess` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.5 | Comprehensive assessment system | confirmed |  |  | NC 1500-2.5 Comprehensive Assessment System Comprehensive assessment system- The data gathered within this assessment system |
| 33 | `nc_sps` — NC Policies Governing Services for Children with Disabilities, NC 1500-2.40 | Systematic problem-solving process | confirmed |  |  | NC 1500-2.40 Systematic Problem-Solving Process A systematic problem-solving process is a structured, methodical approach to |
| 34 | `nc_recp` — NC Policies Governing Services for Children with Disabilities, NC 1508-2 | Regular Early Childhood Program, RECP | confirmed |  |  | Children with Disabilities (a) Regular Early Childhood Program (RECP), Separate, and Other Settings: Caseload requirements |
| 35 | `nc_general_skills` — NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 | Special Education General Skills | confirmed |  |  | TA Level of Service/Supports Special Education General Skills – Services/supports provided to individuals who require |
| 36 | `nc_targeted_skills` — NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 | Special Education Targeted Skills | confirmed |  |  | and curriculum assistance. 2 Special Education Targeted Skills - Services/supports provided to students who require |
| 37 | `nc_sustained_support` — NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 | Special Education Sustained Support | confirmed |  |  | by the LEA. 3 Special Education Sustained Support – Services/supports outside the general education classroom |
| 38 | `nc_intensive_needs` — NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 | Special Education Intensive Needs | confirmed |  |  | throughout the day. 4 Special Education Intensive Needs – Services/supports outside the general education classroom |
| 39 | `nc_ocs` — NC Policies Governing Services for Children with Disabilities, NC 1508-3.1 | Occupational Course of Study | confirmed |  |  | Core Course of Study Occupational Course of Study Extended Content Standards 10 Students 14 Students |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Homebound | POL (7 uses) | Short form on `home_instr` |
| Extended content standards | POL (2 uses) | Alternate standards concept |
| Head Start | POL (2 uses) | Low priority |

## 3. Summary

- **39 entries: 39 confirmed, 0 misplaced, 0 not found.**
- **Safety:** no single letters, and no person's name standing alone as a term. Place names are graded automatically.
- **Build:** `build --check` passes and all 56 tests pass.

**Most important fixes**

1. **MTSS is mapped to RTI.** "Multi-tiered System of Support" is on `rti` as a spelling variant, but NC 1500-2.25 defines MTSS as a school-wide improvement framework "for all". Responsiveness to instruction is a separate definition (NC 1500-2.33). Make MTSS its own general concept; none exists yet.
2. Add "homebound" to `home_instr`.

**Docstring:** Accurate on documents, page counts, dates and the PSN page offset (printed = PDF − 1). All 14 NC 1500-2.4(b) category numbers match. Leaving out the CADRE quick guide (not North Carolina's own document) was the right call.

**Update (2026-10-07):** Fix 1 applied: MTSS is now its own general concept, `mtss` (SPED:000895), cited to NC 1500-2.25. "multi-tiered system of supports" and "MTSS" moved there from the federal `rti` concept, and Kansas's `kmtss` now points to `mtss`.
