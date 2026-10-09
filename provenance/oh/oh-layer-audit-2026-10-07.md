# Audit: Ohio layer (`sources/states/ohio.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-07 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section (and paragraph, where given) or page of text extracted from the PDFs in this folder, with ligatures normalized. Entries without a literal hit were checked by hand.

Documents: Operating Standards for the Education of Children with Disabilities (DEW, June 2025, Ohio Adm.Code 3301-51), A Guide to Parent Rights in Special Education (Apr. 2025).

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `autism` — Ohio Adm.Code 3301-51-01(B)(10) | Autism, autism spectrum disorder, ASD, autism spectrum disorders | confirmed |  |  | provider for the " Autism Scholarship Program" established by section 3310.41 of the Revised Code, |
| 2 | `id` — Ohio Adm.Code 3301-51-01(B)(10) | Intellectual disability, ID, mental retardation, mild intellectual disability, moderate in | confirmed |  |  | Code as having an intellectual disability , a hearing impairment (including deafness), a speech or |
| 3 | `deafblind` — Ohio Adm.Code 3301-51-01(B)(10) | Deaf-blindness, deaf-blind, deafblind, deafblindness, deaf/blind, dual sensory impairment, | confirmed |  |  | a specific learning disability, deaf-blindness, a developmental delay (for a child between the ages of |
| 4 | `deafness` — Ohio Adm.Code 3301-51-01(B)(10) | Deafness, deaf, deafness including hard of hearing | confirmed |  |  | a hearing impairment (including deafness), a speech or language impairment, a visual impairment (including blindness), |
| 5 | `ed` — Ohio Adm.Code 3301-51-01(B)(10) | Emotional disturbance, serious emotional disturbance, ED, emotional disability, EBD, emoti | confirmed |  |  | (including blindness), a serious emotional disturbance (referred to in this rule as "emotional disturbance"), an |
| 6 | `hi` — Ohio Adm.Code 3301-51-01(B)(10) | Hearing impairment, hard of hearing, deaf or hard of hearing, deaf or hard-of-hearing, hea | confirmed |  |  | intellectual disability , a hearing impairment (including deafness), a speech or language impairment, a visual |
| 7 | `md` — Ohio Adm.Code 3301-51-01(B)(10) | Multiple disabilities, MD, multiple impairments, multiple impairment, severely multiply im | confirmed |  |  | three and nine), or multiple disabilities, and who, by reason thereof, needs special education and |
| 8 | `oi` — Ohio Adm.Code 3301-51-01(B)(10) | Orthopedic impairment, OI, physical impairment, physically impaired, orthopedic disability | confirmed |  |  | as "emotional disturbance"), an orthopedic impairment, autism, traumatic brain injury, an other health impairment, a |
| 9 | `ohi` — Ohio Adm.Code 3301-51-01(B)(10) | Other health impairment, health impairment, other health-impairment, OHI, health impairmen | confirmed |  |  | traumatic brain injury, an other health impairment, a specific learning disability, deaf-blindness, a developmental delay |
| 10 | `sld` — Ohio Adm.Code 3301-51-01(B)(10) | Specific learning disability, learning disability, SLD, LD, specific learning disabilities | confirmed |  |  | other health impairment, a specific learning disability, deaf-blindness, a developmental delay (for a child between |
| 11 | `sli` — Ohio Adm.Code 3301-51-01(B)(10) | Speech or language impairment, speech or language impairments, speech-language impairment, | confirmed |  |  | impairment (including deafness), a speech or language impairment, a visual impairment (including blindness), a serious |
| 12 | `tbi` — Ohio Adm.Code 3301-51-01(B)(10) | Traumatic brain injury, TBI | confirmed |  |  | an orthopedic impairment, autism, traumatic brain injury, an other health impairment, a specific learning disability, |
| 13 | `vi` — Ohio Adm.Code 3301-51-01(B)(10) | visual impairment, visually impaired, Visual impairment including blindness, VI, visual im | confirmed |  |  | writing for individuals with visual impairments commonly known as standard English braille. (7) "Caseload for |
| 14 | `dd` — Ohio Adm.Code 3301-51-01(B)(10) | Developmental delay, DD, developmental delays, developmentally delayed, young child with a | confirmed |  |  | learning disability, deaf-blindness, a developmental delay (for a child between the ages of three and |
| 15 | `mdt` — Ohio Adm.Code 3301-51-01(B)(22) | evaluation team, Multidisciplinary team, MDT, multidisciplinary evaluation team | confirmed |  |  | child needs. (22) " Evaluation team" means the parents and a group of qualified professionals. |
| 16 | `referral` — Ohio Adm.Code 3301-51-01(B)(55) | Referral | confirmed |  |  | in the coordination of referral process from school to adult services systems; (g) Link appropriate |
| 17 | `resident_dist` — Ohio Adm.Code 3301-51-01(B)(58) | school district of residence | confirmed |  |  | their parents are protected. School district of residence (a) The child's school district of residence |
| 18 | `esa` — Ohio Adm.Code 3301-51-01(B)(18) | educational service center | confirmed (checked by hand) |  | Found inside (B)(18)(b), the "educational agency" definition; citation is right to the paragraph | (b) Juvenile justice facilities, educational service centers, county boards of |
| 19 | `surrogate` — Ohio Adm.Code 3301-51-01(B)(66) | Surrogate parent, surrogate parents, temporary surrogate, special education surrogate pare | confirmed |  |  | welfare; or (d) A surrogate parent who has been appointed in accordance with rule 3301-51-05 |
| 20 | `pti` — Ohio Adm.Code 3301-51-01(B)(49) | Parent training and information center, PTI, parent center, PTIC, PTIs | confirmed |  |  | this rule. (49) " Parent training and information center" means a center assisted under Sections |
| 21 | `ppps` — Ohio Adm.Code 3301-51-01(B)(50) | parentally placed nonpublic school children with disabilities | confirmed |  |  | the IDEA. (50) " Parentally placed nonpublic school children with disabilities" means children with disabilities |
| 22 | `eval_report` — Ohio Adm.Code 3301-51-06 | evaluation team report | confirmed |  |  | be summarized in an evaluation team report: (a) Review existing evaluation data on the child, |
| 23 | `itinerant` — Ohio Adm.Code 3301-51-11 | itinerant services, Itinerant instruction, Itinerant Preschool Services | confirmed |  |  | four hours. (d) " Itinerant services" for a preschool child who is eligible for special |
| 24 | `state_sp_sch` — Ohio Adm.Code 3301-51-01(B)(64) | state residential school | confirmed |  | Draft duplicate correctly merged here (SPED:000860 retired) | board policies. (64) " State residential school" means publicly funded residential educational services that are |
| 25 | `eval_report` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 5 | ETR | confirmed |  |  | evaluation team report ( ETR). An IEP is a document of statements that outlines the |
| 26 | `parent_mentor` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 13 | Parent mentor, parent mentors | confirmed |  |  | with you. Your local parent mentor, if your educational agency has one. 12 | A |
| 27 | `safeguards_notice` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 1 | A Guide to Parent Rights in Special Education | confirmed |  |  | A Guide to Parent Rights in Special Education Special Education Procedural Safeguards Notice April 2025 |
| 28 | `oh_dew` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 13 | Ohio Department of Education and Workforce | confirmed |  |  | resolve the problem. The Ohio Department of Education and Workforce's Oﬀice for Exceptional Children can |
| 29 | `oh_oec` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 13 | Office for Exceptional Children | confirmed |  |  | The Ohio Department of Education and Workforce's Office for Exceptional Children can get involved |
| 30 | `oh_sst` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 13 | State Support Team | confirmed |  |  | • • Your local State Support Team (Region #____) at (phone #____________). The parent and |
| 31 | `oh_ocecd` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 14 | Ohio Coalition for the Education of Children with Disabilities, OCECD | confirmed |  |  | For more information, contact_______________________________________. Ohio Coalition for the Education of Children with Disabilities (OCECD) o |
| 32 | `oh_county_bdd` — Ohio Adm.Code 3301-51-01(B)(14) | County board of developmental disabilities | confirmed |  |  | district, a nonpublic school, county board of developmental disabilities (county board of DD), other educational |
| 33 | `oh_odys` — Ohio Adm.Code 3301-51-01(B)(18) | Ohio Department of Youth Services | confirmed |  |  | enrollment school district, the Ohio department of youth services, or provider for the "Autism Scholarship |
| 34 | `oh_jvsd` — Ohio Adm.Code 3301-51-01(B)(44) | Joint vocational school district | confirmed |  |  | of youth services, and joint vocational school districts; (b) Juvenile justice facilities, educational service centers, |
| 35 | `oh_district_of_service` — Ohio Adm.Code 3301-51-01(B)(59) | School district of service | confirmed |  |  | of residence. (59) " School district of service" means a school district that is responsible |
| 36 | `charter_school` — Ohio Adm.Code 3301-51-01(B)(8) | Charter school, community school | confirmed |  | New general concept; "community school" is Ohio's legal name for a charter school (S, US-OH). Good | or funding. (8) " Charter school" or "community school" has the meaning given the term |
| 37 | `oh_chartered_nonpublic` — Ohio Adm.Code 3301-51-01(B)(9) | Chartered nonpublic school | confirmed |  |  | same meaning as " chartered nonpublic school." (9) "Chartered nonpublic school" means a school chartered |
| 38 | `oh_osd` — Ohio Adm.Code 3301-51-01(B)(64) | Ohio School for the Deaf | confirmed |  |  | of education, including the Ohio school for the deaf and the Ohio state school for |
| 39 | `oh_ossb` — Ohio Adm.Code 3301-51-01(B)(64) | Ohio State School for the Blind | confirmed |  |  | the deaf and the Ohio state school for the blind. (65) "Supplementary aids and services" |
| 40 | `oh_ohi_major` — Ohio Adm.Code 3301-51-01(B)(45) | Other health impairment - major | confirmed |  | Ohio funding categories under OHI; fine as narrower concepts | with disabilities. (45) " Other health impairment - major" means a child whose condition meets |
| 41 | `oh_ohi_minor` — Ohio Adm.Code 3301-51-01(B)(46) | Other health impairment - minor | confirmed |  |  | Revised Code. (46) " Other health impairment - minor" means a child whose condition meets |
| 42 | `oh_intervention_specialist` — Ohio Adm.Code 3301-51-11 | Intervention specialist, early childhood intervention specialist | confirmed |  |  | teacher and one licensed intervention specialist. (i) Both teachers are assigned to the classroom for |
| 43 | `oh_ttw` — Ohio Adm.Code 3301-51-09(H)(7) | Transition to Work endorsement | confirmed |  |  | either: (i) Obtain the Transition to Work endorsement as defined in rule 3301-24-05 of the |
| 44 | `oh_admin_review` — Ohio Adm.Code 3301-51-05(K)(1) | Administrative review | confirmed |  |  | (K) Dispute resolution (1) Administrative reviews (a) Administrative reviews are recommended, but cannot be used |
| 45 | `oh_early_complaint` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 14 | Early complaint resolution | confirmed |  |  | OCECD website at www.ocecd.org. Early Complaint Resolution Early complaint resolution is when you attempt to |
| 46 | `oh_autism_scholarship` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 36 | Autism Scholarship Program | confirmed |  |  | tell you about the Autism Scholarship Program and the Jon Peterson Scholarship Program. AUTISM SCHOLARSHIP |
| 47 | `oh_jon_peterson` — DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. 36 | Jon Peterson Special Needs Scholarship Program, Jon Peterson Scholarship | confirmed |  | Contains a person's full name (Jon Peterson). Correctly flagged eponym, so high/never_bare; a reviewer should accept it on purpose | box, or email autismscholarship@education.ohio.gov. JON PETERSON SPECIAL NEEDS SCHOLARSHIP PROGRAM If your child is receiving |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Preschool special education | Operating Standards, rule 3301-51-11 (20 uses) | Synonym on `ecse` |
| Open enrollment | 3301-51-01(B)(18) (2 uses) | Low priority |

## 3. Summary

- **47 entries: 47 confirmed, 0 misplaced, 0 not found.** 1 needed a hand check.
- **Safety:** no single letters, and no person's name standing alone as a term. Place names are graded automatically.
- **Build:** `build --check` passes and all 56 tests pass.

**Most important fixes**

1. **`VERSION_ADDED` is still "0.0.0".** The 20 new Ohio records are published with `version_added: 0.0.0`, while the CHANGELOG calls them 0.29.0. Set it to "0.29.0" and rebuild.
2. "Jon Peterson Special Needs Scholarship Program" contains a person's full name. It is correctly flagged as an eponym (high risk, phrase only), but a reviewer should accept it on purpose.
3. Add "preschool special education" (20 uses) to `ecse`.

**Docstring:** Accurate on documents, page counts, dates and the PR page offset (printed = PDF − 1). Every 3301-51-01(B) paragraph number I checked matches.

**Update (2026-10-07):** Fix 1 applied: `VERSION_ADDED` is now "0.29.0" and the 20 Ohio records carry it.
