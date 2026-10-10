# Maine (US-ME): layer report

Drafted with `claude-sonnet-5-5` on 2026-10-09 following `prompts/add-state.md`
(v1.4). A person must review it before merge. Module: `sources/states/maine.py`
(v0.48.0, 150 concepts attested, 55 new).

## 1. Documents read

| Code | Document | Read? |
|---|---|---|
| RULE | 05-071 Chapter 101, Maine Unified Special Education Regulation, Birth to Age Twenty-Two (MUSER), eff. July 26, 2024, posted 8.21.2024, 263 pp. (`me-muser-2024`) | Read through text extraction (`pdftotext -layout`). Sections I-XVII and Appendix 1 were read in the places that name terms (all definitions, all eligibility categories, settings, related services, program approval, dispute resolution headings and the Appendix). The finance tables in Section XVIII were scanned for named programs only. |
| EMERG | Chapter 101 Emergency Changes, Clean Copy, file name dated 6.12.2026, 264 pp. (`me-muser-emergency-2026`) | Compared with RULE sentence by sentence. It adds or removes no term, so it is recorded in the manifest and listed in `UNCITED_DOCS`. |

Missing, so Maine has no records from them: the English Procedural Safeguards
Notice (7.26.2024), the Procedural Manual (7.1.2024) and the Maine special
education glossary. Appendix 1 of the rule reproduces the notice of
procedural safeguards and was read, but it is the rule's own text and is typed
`state_regulation`. Whether the emergency changes of 2026 are in effect was not
checked. No Wayback snapshot is recorded for either document (archive.org
was not reachable from the drafting session). The contributor downloaded the
files on the day recorded as `RETRIEVED` (2026-10-09, taken from the
contributor's local date; the file timestamps are early 2026-10-10 UTC).

Page numbers are the numbers printed in the rule's page header. PDF page =
printed page + 7. Where a definition spans a page break, the cited page is the
page on which the cited string appears.

## 2. New concepts (55)

| Key | Term | Quote (≤15 words) | Citation |
|---|---|---|---|
| `me_muser` | Maine Unified Special Education Regulation | "obligate the unit as required in the MUSER at VI.2.B(4). If the IEP Team does" | Section VI(2), p. 62 |
| `me_cds` | Child Development Services | "agencies (LEAs) under IDEA. The Child Development Services (CDS) State Intermediate Educational Unit (IEU) is" | Section II(21), p. 7 |
| `me_doe` | Maine Department of Education | "Commissioner. The Commissioner of the Maine Department of Education reviews and approves all early intervention" | Section I(3), p. 2 |
| `me_state_agency_client` | State agency client | "delays. 40. State Agency Client. State agency client means a child of eligible school age" | Section II(40), p. 11 |
| `me_psp` | Primary service provider | "Child Development Services utilizes a Primary Service Provider (PSP) model to provide services in the" | Section X(1), p. 107 |
| `me_ed_tech` | Educational technician | "education personnel, or qualified contractors. An educational technician III approved by the Office of Certification" | Section X(1), p. 109 |
| `me_tutorial` | Tutorial instruction | "Special Education Regulation page 114 (4) Tutorial Instruction. The IEP Team may consider tutorial instruction" | Section X(2)(A)(4), p. 114 |
| `me_special_purpose_school` | Special purpose private school | "Disabilities Form (EF-S-01): (1) Special Purpose Private School in Maine. A special purpose private school" | Section XII(3)(A), p. 147 |
| `me_general_purpose_school` | General purpose private school | "Special Education Program in a General Purpose Private School (other than one used by the" | Section XII(3)(A), p. 147 |
| `me_special_purpose_service` | Special purpose service | "303.12(a)(13)] 39. Special Purpose Service. Special purpose service means a public or private program which" | Section II(39), p. 11 |
| `me_regional_program` | Regional special education program | "32. Regional Special Education Program. Regional special education program means a program established through a" | Section II(32), p. 9 |
| `me_eut` | Education in the Unorganized Territories | "IV.2.G][34 CFR 300.300(d)(4)(i,ii)] I. Education in the Unorganized Territories (EUT) (1) School privileges in the" | Section IV(4)(I), p. 38 |
| `me_mssm` | Maine School of Science and Mathematics | "Regulation page 39 J. Maine School of Science and Mathematics. The Maine School of Science" | Section IV(4)(J), p. 39 |
| `me_nta` | Neurocognitive Testing Assistant | "may be conducted by registered Neurocognitive Testing Assistants (NTAs) working under the supervision of a" | Section IV(2), p. 25 |
| `me_psych_board` | Board of Examiners of Psychologists | "pursuant to rules of the Board of Examiners of Psychologists. 3. Responsibility for Early Intervention" | Section IV(2), p. 25 |
| `me_mepa` | Maine Psychological Association | "may offer diagnostic impressions. The Maine Psychological Association (MePA) maintains a register for Neurocognitive Testing" | Section XI, p. 132 |
| `me_slp_board` | Maine Board of Speech, Audiology and Hearing | "pathologist licensed by the Maine Board of Speech, Audiology and Hearing, or speech and language" | Section X(2)(A)(3), p. 113 |
| `me_counsel_board` | Maine State Board of Counseling Professionals Licensure | "workers, psychologist, and other Maine State Board of Counseling Professionals Licensure qualified personnel to assist" | Section XI, p. 127 |
| `me_mpf` | Maine Parent Federation | "the Maine Department of Education (207-624-6650), Maine Parent Federation (1-800-870-7746), the Disability Rights Center (1-800-452-1948)" | Appendix 1, p. 219 |
| `me_drc` | Disability Rights Center | "(207-624-6650), Maine Parent Federation (1-800-870-7746), the Disability Rights Center (1-800-452-1948) and Southern Maine Parent Awareness" | Appendix 1, p. 219 |
| `me_smpa` | Southern Maine Parent Awareness | "Disability Rights Center (1-800-452-1948) and Southern Maine Parent Awareness (1-800-564-9696), and KIDS LEGAL (1-866-624-7787). A" | Appendix 1, p. 219 |
| `me_kids_legal` | KIDS LEGAL | "Southern Maine Parent Awareness (1-800-564-9696), and KIDS LEGAL (1-866-624-7787). A parent may file a dispute" | Appendix 1, p. 219 |
| `me_due_process_office` | Due Process Office | "the school administrative unit and the Due Process Office of the Maine Department of Education" | Section XVI(4), p. 162 |
| `me_due_process_coord` | Due Process Coordinator | "School Administrative Unit (SAU) and the Due Process Coordinator in the Department of Education of" | Section XVI(2), p. 159 |
| `me_notif_placement` | Notification of Placement for Children with Disabilities | "by filing a Notification of Placement for Children with Disabilities Form (EF-S-01): (1) Special Purpose" | Section XII(3)(A), p. 147 |
| `me_learning_results` | Maine's Learning Results | "district-wide tests, which are aligned with Maine's Learning Results. 5. Composite Score: Composite score means" | Section II(4), p. 3 |
| `housse` | HOUSSE | "may use • Per USDE 2006 guidance, HOUSSE may HOUSSE in limited cases. only be" | Section X(2)(A)(6), p. 116 |
| `me_atp` | Assistive technology professional | "a child's home or An Assistive Technology Professional (ATP) must meet other settings is required" | Section XI, p. 136 |
| `me_dhhs` | Maine Department of Health and Human Services | "other agency, including the Maine Department of Health and Human Services, the Maine Department of" | Section VI(2), p. 64 |
| `me_doc` | Department of Corrections | "or under the supervision of the Department of Corrections, including, but not limited to, a" | Section II(40), p. 12 |
| `me_dol` | Maine Department of Labor | "Health and Human Services, the Maine Department of Labor, the Maine Department of Corrections, the" | Section VI(2), p. 64 |
| `me_bvr` | Bureau of Vocational Rehabilitation | "of Public Safety, or the Bureau of Vocational Rehabilitation, of the responsibility to provide or" | Section VI(2), p. 64 |
| `me_long_creek` | Long Creek Youth Development Center | "community reintegration status from the Long Creek Youth Development Center or the Mountain View Youth" | Section II(40), p. 12 |
| `me_mountain_view` | Mountain View Youth Development Center | "Youth Development Center or the Mountain View Youth Development Center and who is placed, for" | Section II(40), p. 12 |
| `me_b2` | Birth to under age three | "Maine's correctional facilities. 42. B-2 (Birth to under age three). Birth through two is the" | Section II(42), p. 12 |
| `iep_case_manager` | IEP case manager | "rule. 19. Individualized Educational Program (IEP) Case Manager. The IEP service coordinator may oversee a" | Section II(19), p. 7 |
| `informed_clinical_opinion` | Informed clinical opinion | "up for the IEP process. 20. Informed Clinical Opinion. Informed clinical opinion must be used" | Section II(20), p. 7 |
| `diagnostic_impression` | Diagnostic impression | "[34 CFR 300.11] 8. Diagnostic Impression. Diagnostic impression means an interpretive statement based upon previous" | Section II(8), p. 4 |
| `composite_score` | Composite score | "Maine's Learning Results. 5. Composite Score: Composite score means a standardized score which summarizes performance" | Section II(5), p. 3 |
| `formative_assessment` | Formative assessment | "related services. [34 CFR 300.302] 12. Formative Assessment. For purposes of general education interventions, the" | Section II(12), p. 5 |
| `sb_interventions` | Scientifically based interventions | "children with disabilities. 33. Scientifically-based Interventions. Scientifically-based interventions means interventions that include teaching practices that" | Section II(33), p. 9 |
| `early_childhood_program` | Early childhood program | "Settings (1) For Children 3-5 (a) Early Childhood Program A program that includes at least" | Section X(2)(C)(1), p. 121 |
| `reverse_mainstream` | Reverse mainstream | "to:  Headstart;  Kindergarten;  Reverse Mainstream;" | Section X(2)(C)(1), p. 121 |
| `asthma` | Asthma | "chronic or acute health problems, such as asthma, attention deficit disorder, attention deficit hyperactivity disorder," | Section VII(2)(J), p. 81 |
| `diabetes` | Diabetes | "attention deficit disorder, attention deficit hyperactivity disorder, diabetes, epilepsy, a heart condition, hemophilia, lead poisoning," | Section VII(2)(J), p. 81 |
| `hemophilia` | Hemophilia | "hyperactivity disorder, diabetes, epilepsy, a heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, or" | Section VII(2)(J), p. 81 |
| `lead_poisoning` | Lead poisoning | "diabetes, epilepsy, a heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, or sickle cell" | Section VII(2)(J), p. 81 |
| `leukemia` | Leukemia | "epilepsy, a heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, or sickle cell anemia," | Section VII(2)(J), p. 81 |
| `nephritis` | Nephritis | "a heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, or sickle cell anemia, Tourette" | Section VII(2)(J), p. 81 |
| `rheumatic_fever` | Rheumatic fever | "condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, or sickle cell anemia, Tourette Syndrome and" | Section VII(2)(J), p. 81 |
| `heart_condition` | Heart condition | "attention deficit hyperactivity disorder, diabetes, epilepsy, a heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic" | Section VII(2)(J), p. 81 |
| `cerebral_palsy` | Cerebral palsy | "and impairments from other causes (e.g., cerebral palsy, amputations, and fractures or burns that cause" | Section VII(2)(I), p. 81 |
| `poliomyelitis` | Poliomyelitis | "congenital anomaly, impairments caused by disease (e.g., poliomyelitis, bone tuberculosis) and impairments from other causes" | Section VII(2)(I), p. 81 |
| `bone_tuberculosis` | Bone tuberculosis | "impairments caused by disease (e.g., poliomyelitis, bone tuberculosis) and impairments from other causes (e.g., cerebral" | Section VII(2)(I), p. 81 |
| `schizophrenia` | Schizophrenia | "personal or school problems. The term includes schizophrenia. The term does not apply to students" | Section VII(2)(E), p. 79 |

Not in the table: 95 attestations of concepts that already exist (see section 3).

## 3. Places I was unsure

- **Existing or new.** `School administrative unit` already exists as `nh_sau`
  (New Hampshire) and `Intermediate educational unit` as `wy_ieu` (Wyoming);
  Maine's `SAU`, `SAUs`, `IEU` and `State Intermediate Educational Unit` are added
  to those keys, tagged US-ME, except `SAU`, `SAUs` and `school administrative units`, which carry no
  regional tag because both New Hampshire and Maine use them. `wy_ieu`
  is the IDEA term (20 USC 1402(23), as the rule says) and is general.
  `Abbreviated school day` is attested on `co_abbrev_day`, which carries a
  Colorado tag, although the idea is general.
- **Synonym decisions.** `Positive Reinforcement Interventions and Supports`
  (Section II(27)) is added to `pbis` as a synonym; the rule ties it to
  functional behavioral assessments, but does not say it equals the federal
  PBIS term. `State ward` is added to `ward` (Section II(41)).
  `Teacher of the Deaf/Hearing Impaired` is added to `tdhh`.
  `Headstart` (one word) is added to `head_start` as a spelling variant.
  `Deafness, including hearing loss` and `Hearing loss` are the rule's titles
  for two separate categories; they are added to `deafness` and `hi`.
- **Wording-only attestations.** Several records attest an existing concept
  from a heading or a short phrase (for example `consult`, `home_instr`,
  `residential`, `special_class`, `related`, `om`, `counseling`, `child_count`,
  `ceis`). The string is in the cited place, but the definition may differ from
  the existing concept's wording.
- **Currency.** `hqt` (highly qualified teacher) and `HOUSSE` appear in the
  rule's table of "Federal Requirement / How Maine Meets the Requirement";
  those rules date from the 2001 No Child Left Behind era and may no longer
  apply. The names are recorded because they appear in current text.
  `Disability Rights Center` is the name in Appendix 1; the organization may be
  called something else now, and no other name is recorded.
- **Appendix 1** (the notice of procedural safeguards inside the rule) is cited as
  the rule. Its Maine organization names and phone numbers (not recorded) could
  be out of date.
- **Categories.** The rule combines some cited labels, for example "Deafness,
  including hearing loss" and "Visual impairment including blindness".
- **Health conditions.** The rule's definitions of other health impairment,
  orthopedic impairment and emotional disability list conditions (asthma, diabetes,
  hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, a heart
  condition, cerebral palsy, poliomyelitis, bone tuberculosis, schizophrenia).
  They are federal wording, not Maine-specific, and are added as general
  `health_condition` concepts broader than the category.

## 4. Risky entries

- **Acronyms.** `SAU` (also New Hampshire), `CDS` (Child Development Services; not
  checked against other states' use), `PSP`, `EUT`, `MSSM`, `NTA`/`NTAs`, `ATP`,
  `MePA`, `PDDNOS`, `EF-S-01` and `B-2`. None is a personal name or single letter.
  No ambiguity warning was raised for them by the build, but `CDS`, `ATP` and `PSP`
  also mean other things outside special education.
- **Place names.** Flagged `place_name`: Maine Unified Special Education
  Regulation, Maine Department of Education, Maine School of Science and
  Mathematics, Maine Psychological Association, Maine Board of Speech, Audiology
  and Hearing, Maine State Board of Counseling Professionals Licensure, Maine
  Parent Federation, Southern Maine Parent Awareness, Maine's Learning Results,
  Maine Department of Health and Human Services, Maine Department of Labor, Long
  Creek Youth Development Center and Mountain View Youth Development Center. The
  last two are state juvenile facilities named for places; only the full phrases
  are recorded. No eponyms.
- **Generic phrases.** `Department of Corrections`, `Due Process Office`,
  `Disability Rights Center`, `Special purpose service`, `Tutorial instruction`
  and `KIDS LEGAL` are short phrases that other documents may use for other
  bodies. `Heart condition` is flagged `common_english_word`.
- **Hand-picked cap.** The new all-caps strings did not trip the known-name test
  in `tests/test_match.py`; no change to that list was needed.

## 5. Terms left out

- Funding and finance terms: Essential Programs and Services (EPS), special
  education per-pupil rates, MEDMS, Medicaid targeted case management, tuition
  computation names (funding formulas, per the instructions).
- `Probes` (brief assessment of skills; common English word), `Team Meeting`,
  `regional site`, `Commissioner` and other generic words.
- PRAXIS II (a test brand), RESNA, Behavior Analyst Certification Board
  (a certifier, not a Maine concept) and certification codes such as 030, 035,
  079, 282 and 286.
- Regulation numbers (Chapter 115, 10-148 CMR 33), statute citations and telephone numbers.
- `DSM` and `ICD` as bare acronyms (the existing concept `dsm5` carries only
  "DSM-5"); `Asperger's Syndrome` and other DSM labels are attested.
- Part C eligibility conditions in Section VII(1)(A) other than fetal alcohol
  syndrome (chromosomal abnormalities, inborn errors of metabolism, severe
  attachment disorders and the like): general medical wording, not
  special-education concepts.
- `Educational Technician I` and `II` alone (the rule uses them only in a table
  and within phrases); `Educational Technician III` is recorded.
- `Maine Care` / `MaineCare` (a health program; the rule writes it as two words once).
- The 2026 emergency copy's new Section XVI(1-A) wording (private schools as
  parties in disputes) adds no new term.

## 6. Possibly disfavored

- `LEA` (local educational agency): Section I, p. 1, says all references to the
  LEA in federal language "have been replaced by references to the school
  administrative unit (SAU)". This is a rule-driven replacement, not an offensive
  term; for a person to decide whether `sources/disfavored.tsv` needs an entry.
- No other term is described as offensive or replaced. The rule keeps
  "Emotional Disability" and "Intellectual Disability"; it uses no older
  labels such as "mental retardation".
