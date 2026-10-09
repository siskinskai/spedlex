# Audit: Michigan layer (`sources/states/michigan.py`)

Prompt: `prompts/audit-layer.md` v1.0 · Audited 2026-10-06 · Auditor: claude-opus-5-5 in a fresh conversation that did not see the drafting. The draft's `ASSISTED_BY` is the same model, so the prompt's preferred setup (a different model) was not met. I did not read the drafter's `*-layer-report` file before auditing.

Method: every entry's strings were searched in the cited rule section or page of text extracted from the PDFs in this folder. Entries without a literal hit were checked by hand. Web pages were read through a fetch that returns quotes from the page, not the page itself.

Documents: MARSE (eff. June 27, 2024), MDE Procedural Safeguards Notice (10/16/18), MDE IEP Development guidance (May 2022), MI-Access web page.

## 1. Entries

| # | entry | term(s) checked | verdict | correct citation | problem | evidence (≤15 words) |
|---|---|---|---|---|---|---|
| 1 | `id` — Mich Admin Code, R 340.1705 | cognitive impairment | confirmed |  |  | R 340.1705 Cognitive impairment; determination. Rule 5. (1) Cognitive impairment shall be manifested during the |
| 2 | `ed` — Mich Admin Code, R 340.1706 | emotional impairment | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | R 340.1706 Emotional impairment; determination; evaluation report. Rule 6. (1) Emotional impairment shall be determined |
| 3 | `hi` — Mich Admin Code, R 340.1707 | hard of hearing, deaf or hard of hearing, deaf or hard-of-hearing, hearing loss, Hearing i | confirmed |  |  | R 340.1707 Deaf or hard of hearing. Rule 7. (1) The term "deaf or hard |
| 4 | `deafness` — Mich Admin Code, R 340.1707 | Deafness, deaf, deafness including hard of hearing | confirmed |  |  | affects educational performance. " Deafness" means a hearing loss that is so severe that the |
| 5 | `vi` — Mich Admin Code, R 340.1708 | Visual impairment including blindness, visual impairment, VI, visual impairment/blind, vis | confirmed |  |  | R 340.1708 Visual impairment including blindness definition; determination. Rule 8. (1) “Visual impairment including blindness” |
| 6 | `fva` — Mich Admin Code, R 340.1708 | Functional vision assessment | confirmed |  |  | to 333.18838. (b) A functional vision assessment by a teacher of students with visual impairment. |
| 7 | `lma` — Mich Admin Code, R 340.1708 | Learning media assessment | confirmed |  |  | visual impairment. (c) A learning media assessment by a teacher of students with visual impairment. |
| 8 | `tvi` — Mich Admin Code, R 340.1708 | teacher of students with visual impairment | confirmed |  |  | vision assessment by a teacher of students with visual impairment. (c) A learning media assessment |
| 9 | `oi` — Mich Admin Code, R 340.1709 | physical impairment | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | R 340.1709 " Physical impairment" defined; determination. Rule 9. (1) "Physical impairment" means severe orthopedic |
| 10 | `ohi` — Mich Admin Code, R 340.1709a | Other health impairment, health impairment, other health-impairment, OHI, health impairmen | confirmed |  |  | R 340.1709a " Other health impairment" defined; determination. Rule 9a. (1) "Other health impairment" means |
| 11 | `adhd` — Mich Admin Code, R 340.1709a | Attention deficit hyperactivity disorder, attention deficit disorder, ADHD, ADD, OHI/ADD/A | confirmed |  |  | Attention deficit disorder. (iii) Attention deficit hyperactivity disorder. (iv) Diabetes. (v) Epilepsy. (vi) A heart |
| 12 | `epilepsy` — Mich Admin Code, R 340.1709a | Epilepsy, seizure disorder | confirmed |  |  | disorder. (iv) Diabetes. (v) Epilepsy. (vi) A heart condition. (vii) Hemophilia. (viii) Lead poisoning. (ix) |
| 13 | `sickle` — Mich Admin Code, R 340.1709a | Sickle cell anemia | confirmed |  |  | (xi) Rheumatic fever. (xii) Sickle cell anemia. (b) The impairment adversely affects a student's educational |
| 14 | `sli` — Mich Admin Code, R 340.1710 | speech and language impairment | confirmed |  | Already on this concept for another state; the entry adds this state's regional tag, so keep it | R 340.1710 " Speech and language impairment" defined; determination. Rule 10. (1) A "speech and |
| 15 | `lang_dis` — Mich Admin Code, R 340.1710 | language impairment, language impairments, Language disorder, receptive language, expressi | confirmed |  |  | R 340.1710 "Speech and language impairment" defined; determination. Rule 10. (1) A "speech and language |
| 16 | `artic` — Mich Admin Code, R 340.1710 | articulation impairment, Articulation disorder, sound system disorder, sound system impair | confirmed |  |  | as a language impairment, articulation impairment, fluency impairment, or voice impairment. (2) A communication disorder |
| 17 | `fluency_dis` — Mich Admin Code, R 340.1710 | fluency impairment | confirmed |  |  | language impairment, articulation impairment, fluency impairment, or voice impairment. (2) A communication disorder shall be |
| 18 | `voice` — Mich Admin Code, R 340.1710 | voice impairment | confirmed |  |  | impairment, fluency impairment, or voice impairment. (2) A communication disorder shall be determined through the |
| 19 | `dd` — Mich Admin Code, R 340.1711 | early childhood developmental delay | confirmed |  |  | R 340.1711 " Early childhood developmental delay" defined; determination. Rule 11. (1) "Early childhood developmental |
| 20 | `sld` — Mich Admin Code, R 340.1713 | Specific learning disability, learning disability, SLD, LD, specific learning disabilities | confirmed |  |  | R 340.1713 Specific learning disability defined; determination. Rule 13. (1) "Specific learning disability" means a |
| 21 | `dyslexia` — Mich Admin Code, R 340.1713 | Dyslexia, Specific Learning Disability/Dyslexia | confirmed |  |  | injury, minimal brain dysfunction, dyslexia, and developmental aphasia. Specific learning disability does not include learning |
| 22 | `perceptual` — Mich Admin Code, R 340.1713 | Perceptual disabilities, perceptual disability | confirmed |  |  | including conditions such as perceptual disabilities, brain injury, minimal brain dysfunction, dyslexia, and developmental aphasia. |
| 23 | `mbd` — Mich Admin Code, R 340.1713 | Minimal brain dysfunction | confirmed |  |  | perceptual disabilities, brain injury, minimal brain dysfunction, dyslexia, and developmental aphasia. Specific learning disability does |
| 24 | `aphasia` — Mich Admin Code, R 340.1713 | Developmental aphasia | confirmed |  |  | brain dysfunction, dyslexia, and developmental aphasia. Specific learning disability does not include learning problems that |
| 25 | `discrepancy` — Mich Admin Code, R 340.1713 | Severe discrepancy, ability-achievement discrepancy, IQ-achievement discrepancy, discrepan | confirmed |  |  | the use of a severe discrepancy between intellectual ability and achievement. (b) Permit the use |
| 26 | `rti` — Mich Admin Code, R 340.1713 | Response to scientific, research-based intervention, response to intervention, RTI, RtI, m | confirmed |  |  | based on the child's response to scientific, research-based intervention. (c) Permit the use of other |
| 27 | `gen_teacher` — Mich Admin Code, R 340.1713 | general education teacher, Regular education teacher, gen ed teacher, regular classroom te | confirmed |  |  | following: (a) The student's general education teacher or, if the student does not have a |
| 28 | `md` — Mich Admin Code, R 340.1714 | severe multiple impairment | confirmed |  |  | R 340.1714 Severe multiple impairment; determination. Rule 14. (1) Students with severe multiple impairments shall |
| 29 | `autism` — Mich Admin Code, R 340.1715 | Autism, autism spectrum disorder, ASD, autism spectrum disorders | confirmed |  |  | R 340.1715 Autism spectrum disorder defined; determination. Rule 15. (1) Autism spectrum disorder is considered |
| 30 | `tbi` — Mich Admin Code, R 340.1716 | Traumatic brain injury, TBI | confirmed |  |  | R 340.1716 " Traumatic brain injury" defined; determination. Rule 16. (1) "Traumatic brain injury" means |
| 31 | `deafblind` — Mich Admin Code, R 340.1717 | Deaf-blindness, deafblindness, deaf-blind, deaf/blind, dual sensory impairment, dual senso | confirmed |  |  | R 340.1717 Deaf-blindness defined; determination. Rule 17. (1) Deaf-blindness means concomitant hearing impairment and visual |
| 32 | `tdhh` — Mich Admin Code, R 340.1717 | teacher of students with hearing impairment | confirmed |  |  | visual impairment. (c) A teacher of students with hearing impairment. History: 2004 AACS. R 340.1719 |
| 33 | `adaptive` — Mich Admin Code, R 340.1701a | Adaptive behavior, adaptive functioning, adaptive skills, adaptive behavior deficits | confirmed |  |  | these rules: (a) " Adaptive behavior" means a student's ability to perform the social roles |
| 34 | `mdt` — Mich Admin Code, R 340.1701b | multidisciplinary evaluation team | confirmed |  |  | R 340.1757. (b) " Multidisciplinary evaluation team" means a minimum of 2 persons who are |
| 35 | `cwd` — Mich Admin Code, R 340.1702 | student with a disability, Child with a disability, children with disabilities, pupil with | confirmed |  |  | R 340.1702 " Student with a disability" defined. Page 3 Courtesy of Michigan Administrative Rules |
| 36 | `evaluation` — Mich Admin Code, R 340.1721a | Evaluation, initial evaluation, individual evaluation, comprehensive evaluation, full and  | confirmed |  |  | R 340.1721a Initial evaluation. Rule 21a. (1) Each student suspected of having a disability shall |
| 37 | `plaafp` — Mich Admin Code, R 340.1721a | Present levels of academic achievement and functional performance, PLAAFP, present levels  | confirmed (checked by hand) |  | Rule uses the singular "present level of ..."; consider adding it as a spelling variant | (ii) A student's present level of academic achievement and functional performance. |
| 38 | `annual_goals` — Mich Admin Code, R 340.1721e | Measurable annual goals, annual goals, annual goal | confirmed |  |  | (a) A statement of measurable annual goals, including measurable short-term objectives. (b) A statement documenting |
| 39 | `sto` — Mich Admin Code, R 340.1721e | short-term objectives, short term objectives, Benchmarks or short-term objectives, STOs, b | confirmed |  |  | annual goals, including measurable short-term objectives. (b) A statement documenting that the individualized education program |
| 40 | `esy` — Mich Admin Code, R 340.1721e | Extended school year services, extended school year, ESY, ESY services, twelve-month speci | confirmed |  |  | education program team considered extended school year services. (c) For a child age 3 through |
| 41 | `regression` — Mich Admin Code, R 340.1721e | recoupment, Severe or substantial regression, substantial regression | confirmed |  |  | a reasonable period of recoupment. (ii) Data regarding the nature or severity of the disability |
| 42 | `resident_dist` — Mich Admin Code, R 340.1721e | district of residence | confirmed |  |  | of the intermediate school district of residence and the Michigan school for the deaf to |
| 43 | `iee` — Mich Admin Code, R 340.1723c | Independent educational evaluation, IEE, independent evaluation, IEE at public expense, in | confirmed |  |  | R 340.1723c Right to independent educational evaluation. Rule 23c. (1) Each public agency shall provide |
| 44 | `mediation` — Mich Admin Code, R 340.1724d | Mediation, prehearing mediation conference, pre-hearing mediation conference, mediation ag | confirmed |  |  | R 340.1724d Mediation. Rule 24d. (1) A parent or public agency may request a mediation |
| 45 | `dp_complaint` — Mich Admin Code, R 340.1724f | Due process complaint, due process, due process complaint notice | confirmed |  |  | R 340.1724f Due process complaints; procedures. Rule 24f. (1) A parent, a public agency, or |
| 46 | `iaes` — Mich Admin Code, R 340.1724f | Interim alternative educational setting, IAES, interim alternative education setting, alte | confirmed |  |  | Determination of an appropriate interim alternative educational setting by the individualized education program team. (i) |
| 47 | `mdr` — Mich Admin Code, R 340.1724f | Manifestation determination, manifestation determination review, MDR, manifestation determ | confirmed (checked by hand) |  | Concept present; the phrase "manifestation determination" is only in the PSN (pp. 43-47) | (g) Determination that behavior was not a manifestation of the student's disability. |
| 48 | `dp_hearing` — Mich Admin Code, R 340.1725e | administrative law judge, Impartial due process hearing, due process hearing, hearing offi | confirmed |  |  | R 340.1725e Administrative law judge; duties and authority. Rule 25e. (1) The administrative law judge |
| 49 | `prehearing` — Mich Admin Code, R 340.1725e | Pre-hearing conference, prehearing conference | confirmed |  |  | testimony. (d) Require a prehearing conference, if appropriate, to consider and take action regarding any |
| 50 | `adr` — Mich Admin Code, R 340.1725e | Alternative dispute resolution, ADR, informal conflict resolution | confirmed |  |  | of mediation or other alternative dispute resolution options. (v) The filing and disposition of requests |
| 51 | `surrogate` — Mich Admin Code, R 340.1725f | Surrogate parent, surrogate parents, temporary surrogate, special education surrogate pare | confirmed |  |  | R 340.1725f Surrogate parent. Rule 25f. Each public agency shall appoint persons to serve as |
| 52 | `state_complaint` — Mich Admin Code, R 340.1851 | State complaint, state complaint procedures, special education complaint, special educatio | confirmed |  |  | R 340.1851 Filing a state complaint. Rule 151. (1) A state complaint filed with the |
| 53 | `transition` — Mich Admin Code, R 340.1733 | Transition services, transition plan, coordinated set of activities, coordinated activitie | confirmed |  |  | for the provision of transition services. Special education teachers shall be assigned to supervise these |
| 54 | `home_instr` — Mich Admin Code, R 340.1746 | homebound and hospitalized services | confirmed |  |  | R 340.1746 Homebound and hospitalized services. Rule 46. (1) A district or intermediate district shall |
| 55 | `hospital_instr` — Mich Admin Code, R 340.1746 | Instruction in hospitals and institutions, hospital instruction | confirmed (checked by hand) |  | Rule says "hospitalized services"; concept match OK | A district or intermediate district shall provide homebound and hospitalized |
| 56 | `resource_room` — Mich Admin Code, R 340.1749a | resource program | confirmed |  |  | R 340.1749a Elementary level resource program. Rule 49a. (1) A district that provides a special |
| 57 | `sped_admin` — Mich Admin Code, R 340.1750 | director of special education, Special education administrator | confirmed |  |  | R 340.1750 Director of special education. Rule 50. (1) Local school districts or public school |
| 58 | `ecse` — Mich Admin Code, R 340.1755 | early childhood special education services | confirmed |  |  | R 340.1755 Early childhood special education services; 2 years 6 months through 5 years of |
| 59 | `para` — Mich Admin Code, R 340.1793 | paraprofessional personnel | confirmed |  |  | R 340.1793 Paraprofessional personnel; qualifications. Rule 93. Paraprofessional personnel employed in special education programs shall |
| 60 | `ifsp` — Mich Admin Code, R 340.1862 | Individualized family service plan, IFSP, individualized family support plan | confirmed |  |  | R 340.1862 Individualized family service plan; time lines; eligibility. Rule 162. (1) Eligibility for Michigan |
| 61 | `safeguards_notice` — MDE Procedural Safeguards Notice (updated 10/16/18), p. 1 | Procedural safeguards notice, procedural safeguards, notice of procedural safeguards, Pare | confirmed |  |  | Procedural Safeguards Notice Last updated: 10/16/18 Note: This document was updated to comply with Michigan |
| 62 | `pwn` — MDE Procedural Safeguards Notice (updated 10/16/18), p. 11 | Prior written notice, written notice, PWN, prior notice, Notice of Recommendation, Notice  | confirmed |  |  | Safeguards Notice General Information Prior Written Notice 34 CFR §300.503 Notice Your school district (the |
| 63 | `age_majority` — MDE Procedural Safeguards Notice (updated 10/16/18), p. 52 | age of majority, transfer of parental rights, rights at age of majority, Transfer of right | confirmed |  |  | of Parental Rights at Age of Majority 34 CFR §300.520 When a student with a |
| 64 | `continuum` — MDE, IEP Development: Special Education Programs and Services (May 2022), p. 4 | Continuum of alternative placements, continuum of placements, continuum of placement optio | confirmed |  |  | students. 34 CFR §300.320(a)(4) Continuum of Alternative Placements In accordance with 34 CFR §300.115, each |
| 65 | `itinerant` — MDE, IEP Development: Special Education Programs and Services (May 2022), p. 4 | Itinerant instruction, itinerant services | confirmed |  |  | as resource program or itinerant instruction) to be provided in conjunction with regular class placement. |
| 66 | `sdi` — MDE, IEP Development: Special Education Programs and Services (May 2022), p. 3 | Specially designed instruction, SDI | confirmed |  |  | §300.39(a)(1) special education means specially designed instruction, at no cost to the parents, to meet |
| 67 | `transport` — MDE, IEP Development: Special Education Programs and Services (May 2022), p. 5 | special transportation | confirmed |  |  | a school calendar year. Special Transportation After determining the programs and services, a student's IEP |
| 68 | `alt_assess` — MDE MI-Access page | Alternate assessment, alternate academic achievement standards, AA-AAAS | confirmed (web page) |  |  | (ALT) MI-Access is Michigan's alternate assessment system |
| 69 | `sig_cog` — MDE MI-Access page | Most significant cognitive disability, most significant cognitive disabilities, significan | confirmed (web page) |  |  | (ALT) designed for students with the most significant cognitive disabilities |
| 70 | `mi_mde` — MDE Procedural Safeguards Notice (updated 10/16/18), p. 3 | Michigan Department of Education, MDE | confirmed |  | MDE is also Minnesota's usual acronym (`mde_mn` doesn't carry it yet); regional tag keeps it to US-MI | Evaluation Individualized Education Program Michigan Department of Education Office of Special Education State Office of |
| 71 | `mi_isd` — MDE Procedural Safeguards Notice (updated 10/16/18), p. 28 | Intermediate school district, ISD | confirmed |  |  | is based; d. An intermediate school district plan; e. An individualized education program team report, |
| 72 | `mi_isd_plan` — Mich Admin Code, R 340.1832 | Intermediate school district plan | confirmed |  |  | areas. Rule 132. An intermediate school district plan for special education, or any modification thereof, |
| 73 | `mi_psa` — Mich Admin Code, R 340.1733 | Public school academy | confirmed |  |  | district, local school district, public school academy, and any other agency shall comply with all |
| 74 | `mi_pac` — Mich Admin Code, R 340.1838 | Parent advisory committee | confirmed |  |  | R 340.1838 Parent advisory committee. Rule 138. (1) A parent advisory committee shall be appointed |
| 75 | `mi_moahr` — Mich Admin Code, R 340.1724f | Michigan Office of Administrative Hearings and Rules | confirmed |  |  | the complaint to the Michigan office of administrative hearings and rules, which shall appoint an |
| 76 | `mi_offer_fape` — Mich Admin Code, R 340.1721b | Notice of an offer of a free appropriate public education | confirmed |  |  | an evaluation to the notice of an offer of a free appropriate public education or |
| 77 | `mi_operating_district` — Mich Admin Code, R 340.1721e | Operating district | confirmed |  |  | conduct, or authorize the operating district to conduct, each subsequent individualized education program team meeting |
| 78 | `mi_instr_services` — Mich Admin Code, R 340.1701b | Instructional services | confirmed |  |  | these rules: (a) " Instructional services" means services provided by teaching personnel that are specially |
| 79 | `mi_juvenile` — Mich Admin Code, R 340.1701c | Youth placed in a juvenile detention facility | confirmed |  |  | related services. (d) " Youth placed in a juvenile detention facility" means a student who |
| 80 | `mi_tc` — Mich Admin Code, R 340.1749 | Teacher consultant | confirmed |  |  | R 340.1749 Teacher consultant with a student caseload; responsibilities. Rule 49. (1) The teacher consultant |
| 81 | `mi_departmentalize` — Mich Admin Code, R 340.1749c | Departmentalization of special education programs, departmentalize | confirmed |  |  | R 340.1749c Departmentalization of special education programs. Rule 49c. (1) A school with more than |
| 82 | `mi_sci_program` — Mich Admin Code, R 340.1738 | Severe cognitive impairment program | confirmed |  |  | R 340.1738 Severe cognitive impairment program. Rule 38. A severe cognitive impairment program shall be |
| 83 | `mi_sxi_program` — Mich Admin Code, R 340.1748 | Severe multiple impairments program | confirmed |  |  | R 340.1748 Severe multiple impairments program. Rule 48. (1) A severe multiple impairment program shall |
| 84 | `mi_slp_provider` — Mich Admin Code, R 340.1745 | Authorized provider of speech and language services | confirmed |  |  | services provided by an authorized provider of speech and language services shall be based on |
| 85 | `mi_msd` — Mich Admin Code, R 340.1721e | Michigan School for the Deaf | confirmed |  |  | team shall consider the Michigan school for the deaf as a part of the total |
| 86 | `school_social_worker` — Mich Admin Code, R 340.1799f | School social worker | confirmed |  |  | R 340.1799f " School social worker" defined. Rule 1799f. "School social worker" means a school |
| 87 | `transition_coord` — Mich Admin Code, R 340.1799g | Transition coordinator | confirmed |  |  | R 340.1799g Transition coordinator; requirements. Page 49 Courtesy of Michigan Administrative Rules Rule 99g. (1) |
| 88 | `worksite_learning` — Mich Admin Code, R 340.1733 | Worksite-based learning | confirmed |  |  | transition services. (i) For worksite-based learning, there must be a written agreement signed by the |
| 89 | `mi_access` — MDE MI-Access page | MI-Access | confirmed (web page) |  | Graded high: "MI" is read as Michigan's postal code (correct) | (ALT) MI-Access is Michigan's alternate assessment system |
| 90 | `mi_fi` — MDE MI-Access page | Functional Independence | confirmed (web page) |  |  | (ALT) Functional Independence (FI), Supported Independence (SI), and Participation (P) |
| 91 | `mi_si` — MDE MI-Access page | Supported Independence | confirmed (web page) |  |  | (ALT) Functional Independence (FI), Supported Independence (SI), and Participation (P) |
| 92 | `mi_ace` — MDE MI-Access page | Alternate content expectations | confirmed (web page) |  |  | (ALT) MI-Access is based on Michigan's alternate content expectations |
| 93 | `mi_mstep` — MDE MI-Access page | M-STEP | confirmed (web page) |  | Weakest citation in the layer: the ALT page only links to M-STEP | (ALT) "General Assessments" link to M-STEP |

## 2. Missed terms

| Term | Where | Suggested handling |
|---|---|---|
| Intermediate district | R 340.1746 and elsewhere (4 uses) | Synonym on `mi_isd` |
| Severe cognitive impairment | MARSE (8 uses) | Category-level term; only the program (`mi_sci_program`) is listed |
| Constituent district | MARSE (1 use) | Relates to `mi_isd` |
| Present level of academic achievement and functional performance | R 340.1721a | Singular variant on `plaafp` |

## 3. Summary

- **93 entries: 93 confirmed, 0 misplaced, 0 not found.** Of the confirmed entries, 3 needed a hand check because the wording differs, and 7 rest on a web page.
- **Safety:** no single letters, no eponyms, and no person's name standing alone as a term. Place names are graded automatically.
- **Build:** `build --check` passes and all 53 tests pass with this layer in place.

**Most important fixes**

1. `mi_mstep` rests on a link to M-STEP from the MI-Access page; cite a page that names the test, if one is available.
2. MDE is also Minnesota's usual acronym. It's regional-tagged to US-MI here, which is enough today, but note it if Minnesota's layer ever adds MDE.

**Docstring:** Accurate on documents, page counts and dates. One wording point: the rule file says "Eff. June 27, 2024" (effective), not "promulgated".

**Correction (2026-10-06):** an earlier version of this report called some strings redundant because they already existed. They aren't: each adds this state's regional tag, without which a matcher filtered to the state drops the string. Keep them.
