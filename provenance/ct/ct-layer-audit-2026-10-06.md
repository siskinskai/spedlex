# Audit: Connecticut layer (`sources/states/connecticut.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-06 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section or page of text extracted from the PDFs in this folder. Entries without a literal hit were checked by hand. Web pages were read through a fetch that returns quotes from the page, not the page itself.

Documents: Conn. Agencies Regs. §§ 10-76a-1 to 10-76l-1 (CSDE copy, rev. 2015-11-21), A Parent's Guide to Special Education in Connecticut (2021), Procedural Safeguards Notice (rev. Mar. 31, 2021).

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `iep_team` — Conn. Agencies Regs. § 10-76a-1(14) | Planning and placement team, PPT | confirmed |  |  | State Agencies. (14) “ Planning and placement team” or “PPT” means the individualized education program |
| 2 | `esy` — Conn. Agencies Regs. § 10-76a-1(7) | Extended school year services, extended school year, ESY, ESY services, twelve-month speci | confirmed |  |  | “Extended school day or extended school year services” means (A) special education and related services |
| 3 | `iee` — Conn. Agencies Regs. § 10-76a-1(8) | independent evaluation, Independent educational evaluation, IEE, IEE at public expense, in | confirmed |  |  | of Education. (8) “ Independent evaluation” means an evaluation performed by a certified or licensed |
| 4 | `iep` — Conn. Agencies Regs. § 10-76a-1(10) | Individualized education program, IEP, IEPs, individualized education plan, individual edu | confirmed |  |  | accordance with the child's individualized education program, and (iii) at no cost to the parents |
| 5 | `lre` — Conn. Agencies Regs. § 10-76a-1(12) | Least restrictive environment, LRE, peers without disabilities | confirmed |  |  | the IDEA. (12) “ Least restrictive environment” means least restrictive environment as described in the |
| 6 | `gifted` — Conn. Agencies Regs. § 10-76a-2(2) | Gifted and talented, gifted and talented pupil, mentally gifted, gifted student, intellect | confirmed |  |  | and placement team as gifted and talented on the basis of either performance on relevant |
| 7 | `referral` — Conn. Agencies Regs. § 10-76d-7 | Referral | confirmed |  |  | Sec. 10-76d-7. Sec. 10-76d-7. Referral (a) (1) Each board of education shall accept and process |
| 8 | `home_instr` — Conn. Agencies Regs. § 10-76d-15 | homebound and hospitalized instruction | confirmed |  |  | Sec. 10-76d-15. Sec. 10-76d-15. Homebound and hospitalized instruction (a) (1) Provision of instruction for verified |
| 9 | `autism` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Autism, autism spectrum disorder, ASD, autism spectrum disorders | confirmed |  |  | o o • • Autism Deaf-Blindness Developmental delay (in Connecticut for 3 to 5 year-olds, |
| 10 | `deafblind` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Deaf-blindness, deafblindness, deaf-blind, deaf/blind, dual sensory impairment, dual senso | confirmed |  |  | o • • Autism Deaf-Blindness Developmental delay (in Connecticut for 3 to 5 year-olds, inclusive) |
| 11 | `dd` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Developmental delay, DD, developmental delays, developmentally delayed, young child with a | confirmed |  |  | • • Autism Deaf-Blindness Developmental delay (in Connecticut for 3 to 5 year-olds, inclusive) Emotional |
| 12 | `ed` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Emotional disturbance, ED, emotional disability, serious emotional disturbance, EBD, emoti | confirmed |  |  | to 5 year-olds, inclusive) Emotional Disturbance Hearing Impairment (deaf or hard of hearing) Intellectual Disability |
| 13 | `hi` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Hearing impairment, hard of hearing, deaf or hard of hearing, deaf or hard-of-hearing, HI, | confirmed |  |  | year-olds, inclusive) Emotional Disturbance Hearing Impairment (deaf or hard of hearing) Intellectual Disability Multiple Disabilities |
| 14 | `id` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Intellectual disability, ID, mental retardation, mild intellectual disability, moderate in | confirmed |  |  | or hard of hearing) Intellectual Disability Multiple Disabilities Orthopedic Impairment Other Health Impairment (OHI) OHI/ADD/ADHD |
| 15 | `md` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Multiple disabilities, MD, multiple impairments, multiple impairment, severely multiply im | confirmed |  |  | of hearing) Intellectual Disability Multiple Disabilities Orthopedic Impairment Other Health Impairment (OHI) OHI/ADD/ADHD Specific Learning |
| 16 | `oi` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Orthopedic impairment, OI, physical impairment, physically impaired | confirmed |  |  | Intellectual Disability Multiple Disabilities Orthopedic Impairment Other Health Impairment (OHI) OHI/ADD/ADHD Specific Learning Disability Specific |
| 17 | `ohi` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Other health impairment, OHI, health impairment, other health-impairment, health impairmen | confirmed |  |  | Multiple Disabilities Orthopedic Impairment Other Health Impairment (OHI) OHI/ADD/ADHD Specific Learning Disability Specific Learning Disability/Dyslexia |
| 18 | `adhd` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | OHI/ADD/ADHD | confirmed |  | "OHI/ADD/ADHD" is the name of a CT reporting category under OHI; mapping to `adhd` is defensible but a reviewer may prefer `ohi` | Other Health Impairment (OHI) OHI/ADD/ADHD Specific Learning Disability Specific Learning Disability/Dyslexia Speech or Language Impairment |
| 19 | `sld` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Specific learning disability, learning disability, SLD, LD, specific learning disabilities | confirmed |  |  | Health Impairment (OHI) OHI/ADD/ADHD Specific Learning Disability Specific Learning Disability/Dyslexia Speech or Language Impairment Traumatic |
| 20 | `dyslexia` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Specific Learning Disability/Dyslexia | confirmed |  | "Specific Learning Disability/Dyslexia" is the SLD subcategory; mapping to `dyslexia` is defensible | OHI/ADD/ADHD Specific Learning Disability Specific Learning Disability/Dyslexia Speech or Language Impairment Traumatic Brain Injury Vision |
| 21 | `sli` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Speech or language impairment, speech-language impairment, SLI, speech impairment, speech  | confirmed |  |  | Disability Specific Learning Disability/Dyslexia Speech or Language Impairment Traumatic Brain Injury Vision Impairment The disability |
| 22 | `tbi` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Traumatic brain injury, TBI | confirmed |  |  | Speech or Language Impairment Traumatic Brain Injury Vision Impairment The disability must adversely affect your |
| 23 | `vi` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 11 | Vision Impairment | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | Impairment Traumatic Brain Injury Vision Impairment The disability must adversely affect your child's educational performance, |
| 24 | `pbis` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 8 | PBIS, Positive behavioral interventions and supports, positive behavior supports, positive | confirmed |  |  | Intervention and Supports ( PBIS): A framework to address challenging behaviors that includes functional assessment |
| 25 | `pwn` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 8 | Prior written notice, PWN, written notice, prior notice, Notice of Recommendation, Notice  | confirmed |  |  | redesigning interventions as necessary. Prior Written Notice (PWN): An explanation why the school district proposes |
| 26 | `mdr` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 8 | Manifestation determination, manifestation determination review, MDR, manifestation determ | confirmed |  |  | State Department of Education. Manifestation Determination: When a student with a disability behaves in a |
| 27 | `approved_priv` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 27 | approved private special education program | confirmed |  |  | LEARN. What is an approved private special education program? An approved private special education program |
| 28 | `surrogate` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 35 | Surrogate parent, surrogate parents, temporary surrogate, special education surrogate pare | confirmed |  |  | Special Education in Connecticut Surrogate Parents The Surrogate Parent Program is a federally mandated program |
| 29 | `safeguards_notice` — CSDE Procedural Safeguards Notice (rev. Mar. 2021), PDF p. 2 | Procedural safeguards notice, procedural safeguards, notice of procedural safeguards, Pare | confirmed |  |  | Procedural Safeguards Notice Required Under IDEA Part B Connecticut State Department of Education Bureau of |
| 30 | `ct_csde` — CSDE Procedural Safeguards Notice (rev. Mar. 2021), PDF p. 17 | Connecticut State Department of Education, CSDE | confirmed |  |  | a school district, the Connecticut State Department of Education (CSDE) or any other public agency |
| 31 | `ct_due_process_unit` — Conn. Agencies Regs. § 10-76h-1(f) | Due process unit | confirmed |  |  | of Education. (f) “ Due process unit” means the unit located within the Bureau of |
| 32 | `ct_resc` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 9 | Regional Educational Service Center, RESC | confirmed |  |  | to resolve the issue. Regional Educational Service Center (RESC): A Connecticut public educational authority formed |
| 33 | `ct_serc` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 50 | State Education Resource Center, SERC | confirmed |  |  | 06103 860-713-6543 Website: http://www.ct.gov/sde/ State Education Resource Center (SERC) 100 Roscommon Drive Middletown, CT 06457 |
| 34 | `ct_cpac` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 50 | Connecticut Parent Advocacy Center, CPAC | confirmed |  |  | at 860-713-6910, or the Connecticut Parent Advocacy Center (CPAC) at 860-739-3089. In many communities there |
| 35 | `ct_oec` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 51 | Office of Early Childhood, OEC | confirmed |  |  | Birth to Three System Office of Early Childhood (OEC) 450 Columbus Boulevard Hartford, CT 06103 |
| 36 | `ct_b23` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 7 | Birth to Three System, Connecticut Birth to Three System | confirmed |  |  | enrolled in the Connecticut Birth to Three System. 3 |
| 37 | `ct_ads` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 51 | Department of Aging and Disability Services, ADS | confirmed |  |  | Referral: 800-505-000 Website: http://www.birth23.org Department of Aging and Disability Services (ADS) 55 Farmington Avenue, 12th |
| 38 | `ct_besb` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 | Bureau of Education and Services for the Blind, BESB | confirmed |  |  | (ADS), which includes the Bureau of Education and Services for the Blind (BESB) and the |
| 39 | `ct_brs` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 | Bureau of Rehabilitation Services, BRS | confirmed |  |  | Blind (BESB) and the Bureau of Rehabilitation Services (BRS). • The term “transition services” is |
| 40 | `ct_dds` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 | Department of Developmental Services, DDS | confirmed |  | DDS now names three concepts (DC, NJ, CT). Reviewer decision | following adult service agencies: Department of Developmental Services (DDS), Department of Mental Health and Addiction |
| 41 | `ct_dmhas` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 | Department of Mental Health and Addiction Services, DMHAS | confirmed |  |  | of Developmental Services (DDS), Department of Mental Health and Addiction Services (DMHAS), Department of Public |
| 42 | `ct_dcf` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 35 | Department of Children and Families, DCF | confirmed |  |  | the jurisdiction of the Department of Children and Families (DCF) (foster children) or an unaccompanied |
| 43 | `ct_boe` — Conn. Agencies Regs. § 10-76a-1(1) | Board of education | confirmed |  |  | following meanings: (1) “ Board of education” or “board” means a public body or public |
| 44 | `ct_unified` — Conn. Agencies Regs. § 10-76a-1(1) | Unified school district | confirmed (checked by hand) |  |  | the unified school districts established pursuant to sections 17a-37, 17a-240 |
| 45 | `ct_tech_hs` — Conn. Agencies Regs. § 10-76a-1(1) | Technical high school system | confirmed |  |  | boards of education, the technical high school system, the unified school districts established pursuant to |
| 46 | `ct_private_sped` — Conn. Agencies Regs. § 10-76a-1(15) | Private special education program | confirmed |  |  | making process. (15) “ Private special education program” means any program that provides special education |
| 47 | `ct_child_req_sped` — Conn. Agencies Regs. § 10-76a-1(3) | Child requiring special education | confirmed |  |  | of age. (3) “A child requiring special education” means (A) a child with a disability; |
| 48 | `ct_ela` — Conn. Agencies Regs. § 10-76a-2(1) | Extraordinary learning ability | confirmed |  |  | following meanings: (1) “ Extraordinary learning ability” means a child identified by the planning and |
| 49 | `ct_otca` — Conn. Agencies Regs. § 10-76a-2(3) | Outstanding talent in the creative arts | confirmed |  |  | ability and children with outstanding talent in the creative arts. (3) “Outstanding talent in the |
| 50 | `ct_trial_placement` — Conn. Agencies Regs. § 10-76d-14 | Trial placement for diagnostic purposes | confirmed |  |  | Sec. 10-76d-14. Sec. 10-76d-14. Trial placement for diagnostic purposes Each board of education may use |
| 51 | `ct_medically_complex` — Conn. Agencies Regs. § 10-76d-15 | Medically complex | confirmed |  |  | a disability who is medically complex and the need for instruction to be provided in |
| 52 | `ct_srbi` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 9 | Scientific Research-Based Intervention, SRBI | confirmed |  | DUPLICATE CONCEPT: the list already has `srbi` (Scientific, research-based intervention). Add "Scientific Research-Based Intervention" and "SRBI" to `srbi` as STRINGS and retire this concept | furnish programs and services. Scientific Research-Based Intervention (SRBI): Connecticut's framework for response to intervention (RTI). |
| 53 | `ct_ctaa` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 | Connecticut Alternate Assessment, CTAA | confirmed |  |  | expected achievement levels appropriate. Connecticut Alternate Assessment (CTAA): is an assessment of English language arts |
| 54 | `ct_ctas` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 | Connecticut Alternate Science, CTAS | confirmed |  |  | the CSDE's testing window. Connecticut Alternate Science (CTAS): is an assessment of the Next Generation |
| 55 | `ct_ccs` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 | Connecticut Core Standards, CCS | confirmed |  |  | mathematics aligned to the Connecticut Core Standards (CCS) for eligible students with significant cognitive disabilities |
| 56 | `aba` — CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 | Applied behavior analysis, ABA | confirmed |  |  | alternative assessment formats, etc. Applied Behavior Analysis (ABA): Scientific method of intervention used to improve |
| 57 | `ct_advisory_opinion` — Conn. Agencies Regs. § 10-76h-6 | Advisory opinion | confirmed |  |  | Sec. 10-76h-6. Sec. 10-76h-6. Advisory opinion (a) The department may, within its discretion, offer the |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Trial placement | § 10-76d-14 (13 uses) | Short form on `ct_trial_placement` |
| Planning and Placement Team meeting | GUIDE (10 uses) | Synonym on the IEP meeting concept |
| Homebound | REG and GUIDE (8 uses) | Short form on `home_instr` |
| Transition planning | GUIDE (9 uses) | Synonym near `transition` |

## 3. Summary

- **57 entries: 57 confirmed, 0 misplaced, 0 not found.** Of the confirmed entries, 1 needed a hand check because the wording differs, and 0 rest on a web page.
- **Safety:** no single letters, no eponyms, and no person's name standing alone as a term. Place names are graded automatically.
- **Build:** `build --check` passes and all 53 tests pass with this layer in place.

**Most important fixes**

1. **Duplicate concept:** `ct_srbi` ("Scientific Research-Based Intervention", SRBI) is the existing `srbi` concept. Move both strings onto `srbi` as STRINGS, and mark `ct_srbi` retired in `data/concept_ids.tsv`.
2. DDS now names three different agencies (DC, NJ, CT). A reviewer should accept it on purpose.
3. "OHI/ADD/ADHD" → `adhd` and "Specific Learning Disability/Dyslexia" → `dyslexia` are defensible, but they are Connecticut's reporting-category labels, so a reviewer may prefer `ohi` and `sld`.

**Docstring:** Accurate on documents, page counts and dates. Every § 10-76a-1, 10-76a-2 and 10-76h-1 subdivision number matches. The GUIDE page offset (printed = PDF − 4) is correct.

**Correction (2026-10-06):** an earlier version of this report called some strings redundant because they already existed. They aren't: each adds this state's regional tag, without which a matcher filtered to the state drops the string. Keep them.

**Update (2026-10-07):** Fix 1 applied: "SRBI" and "Scientific Research-Based Intervention" are now strings on `srbi`, and `ct_srbi` (SPED:000844) is retired. Fixes 2 and 3 are left for a reviewer.
