# Connecticut layer (v0.28.0): contributor report

Drafted 2026-10-06 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md` and CONTRIBUTING.md. A person must review this before it is submitted.

## 1. Documents read
- **REG**: Regulations of Connecticut State Agencies, Children Requiring Special Education, §§ 10-76a-1 to 10-76l-1. This is CSDE's PDF copy, revised 2015-11-21, 44 pp. Read in full: 10-76a-1, 10-76a-2, 10-76d-1, d-2, d-6, d-7, d-10, d-14 to d-17, 10-76h-1 and h-6. The other sections were read by heading. eRegulations was not checked for amendments after 2015.
- **GUIDE**: A Parent's Guide to Special Education in Connecticut, 2021, 60 pp. Cited by PDF page; the printed numbers are four lower. Pages 5-11, 24, 27, 32, 35 and 50-51 were read in full and the rest searched.
- **PSN**: Procedural Safeguards Notice Required Under IDEA Part B, revised March 31, 2021, 45 pp. Pages 1-4 and 17 were read and the rest searched.
- **How the files were read**: all three were linked from CSDE's "Special Education Legal and Due Process" page, downloaded through the browser, checked by SHA-256 and converted to text. Copies are in `.sources-cache/ct/`.

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer, from the extracted text) | Citation |
|---|---|---|---|
| `ct_csde` | Connecticut State Department of Education | "Under IDEA Part B Connecticut State Department of Education 14 State Complaint Procedures Differences Between" | CSDE Procedural Safeguards Notice (rev. Mar. 2021), PDF p. 17 |
| `ct_due_process_unit` | Due process unit | "of Education. (f) “ Due process unit ” means the unit located within the Bureau" | Conn. Agencies Regs. § 10-76h-1(f) |
| `ct_resc` | Regional Educational Service Center | "to resolve the issue. Regional Educational Service Center (RESC): A Connecticut public educational authority formed" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 9 |
| `ct_serc` | State Education Resource Center | "06103 860-713-6543 Website: http://www.ct.gov/sde/ State Education Resource Center (SERC) 100 Roscommon Drive Middletown, CT 06457" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 50 |
| `ct_cpac` | Connecticut Parent Advocacy Center | "at 860-713-6910, or the Connecticut Parent Advocacy Center (CPAC) at 860-739-3089. In many communities there" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 50 |
| `ct_oec` | Office of Early Childhood | "Birth to Three System Office of Early Childhood (OEC) 450 Columbus Boulevard Hartford, CT 06103" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 51 |
| `ct_b23` | Birth to Three System | "enrolled in the Connecticut Birth to Three System ." | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 7 |
| `ct_ads` | Department of Aging and Disability Services | "Referral: 800-505-000 Website: http://www.birth23.org Department of Aging and Disability Services (ADS) 55 Farmington Avenue, 12th" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 51 |
| `ct_besb` | Bureau of Education and Services for the Blind | "(ADS), which includes the Bureau of Education and Services for the Blind (BESB) and the" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 |
| `ct_brs` | Bureau of Rehabilitation Services | "Blind (BESB) and the Bureau of Rehabilitation Services (BRS). • The term “transition services” is" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 |
| `ct_dds` | Department of Developmental Services | "following adult service agencies: Department of Developmental Services (DDS), Department of Mental Health and Addiction" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 |
| `ct_dmhas` | Department of Mental Health and Addiction Services | "of Developmental Services (DDS), Department of Mental Health and Addiction Services (DMHAS), Department of Public" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 32 |
| `ct_dcf` | Department of Children and Families | "the jurisdiction of the Department of Children and Families (DCF) (foster children) or an unaccompanied" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 35 |
| `ct_boe` | Board of education | "following meanings: (1) “ Board of education ” or “board” means a public body or" | Conn. Agencies Regs. § 10-76a-1(1) |
| `ct_unified` | Unified school district | "high school system, the unified school district s established pursuant to sections 17a-37, 17a-240 and" | Conn. Agencies Regs. § 10-76a-1(1) |
| `ct_tech_hs` | Technical high school system | "boards of education, the technical high school system , the unified school districts established pursuant" | Conn. Agencies Regs. § 10-76a-1(1) |
| `ct_private_sped` | Private special education program | "making process. (15) “ Private special education program ” means any program that provides special" | Conn. Agencies Regs. § 10-76a-1(15) |
| `ct_child_req_sped` | Child requiring special education | "of age. (3) “A child requiring special education ” means (A) a child with a" | Conn. Agencies Regs. § 10-76a-1(3) |
| `ct_ela` | Extraordinary learning ability | "following meanings: (1) “ Extraordinary learning ability ” means a child identified by the planning" | Conn. Agencies Regs. § 10-76a-2(1) |
| `ct_otca` | Outstanding talent in the creative arts | "ability and children with outstanding talent in the creative arts . (3) “Outstanding talent in" | Conn. Agencies Regs. § 10-76a-2(3) |
| `ct_trial_placement` | Trial placement for diagnostic purposes | "Sec. 10-76d-14. Trial placement for diagnostic purposes Each board of education may use trial placement" | Conn. Agencies Regs. § 10-76d-14 |
| `ct_medically_complex` | Medically complex | "a disability who is medically complex and the need for instruction to be provided in" | Conn. Agencies Regs. § 10-76d-15 |
| `ct_srbi` | Scientific Research-Based Intervention | "furnish programs and services. Scientific Research-Based Intervention (SRBI): Connecticut’s framework for response to intervention (RTI)." | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 9 |
| `ct_ctaa` | Connecticut Alternate Assessment | "expected achievement levels appropriate. Connecticut Alternate Assessment (CTAA): is an assessment of English language arts" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 |
| `ct_ctas` | Connecticut Alternate Science | "the CSDE’s testing window. Connecticut Alternate Science (CTAS): is an assessment of the Next Generation" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 |
| `ct_ccs` | Connecticut Core Standards | "mathematics aligned to the Connecticut Core Standards (CCS) for eligible students with significant cognitive disabilities" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 |
| `aba` | Applied behavior analysis | "alternative assessment formats, etc. Applied Behavior Analysis (ABA): Scientific method of intervention used to improve" | CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. 6 |
| `ct_advisory_opinion` | Advisory opinion | "Sec. 10-76h-6. Advisory opinion (a) The department may, within its discretion, offer the parties to" | Conn. Agencies Regs. § 10-76h-6 |

All quotes come from text extracted with pdftotext (or page text for web pages), with line breaks collapsed. Page-header text sometimes runs into a quote. Every new string and every attested key was checked automatically: the string had to appear in the cited section or page. All checks passed.

## 3. Unsure
- **PPT**: "Planning and placement team" and "PPT" were added to the existing `iep_team` as Connecticut synonyms, the same way Texas's ARD committee and New York's CSE are handled. No new concept was made.
- "OHI/ADD/ADHD" was put on `adhd` and "Specific Learning Disability/Dyslexia" on `dyslexia`, both tagged US-CT. GUIDE p. 11 lists them as separate eligibility categories. Either could arguably go on `ohi` or `sld` instead.
- "Vision Impairment" was already a string on `vi` tagged US-MA. Re-adding it only adds the US-CT tag; the verifier marks it REDUNDANT, which is expected.
- `ct_boe` ("Board of education") is a common phrase, tagged to Connecticut because the rule defines it broadly. A reviewer may want `common_english_word`.
- `aba` (Applied behavior analysis) was made a national concept under `iep_component`, next to `pbis`. Another category may fit better.
- `ct_b23` is filed under `ct_oec` (Office of Early Childhood) because GUIDE p. 51 lists Birth to Three under the OEC.

## 4. Risky
- **DDS** now has three meanings (DC, NJ, CT), and the build reports it.
- **Place names** (high risk, automatic): Connecticut State Department of Education, Connecticut Parent Advocacy Center, Birth to Three System (via its synonym "Connecticut Birth to Three System"), Connecticut Alternate Assessment, Connecticut Alternate Science and Connecticut Core Standards.
- **Acronyms tagged US-CT**: CSDE, RESC, SERC, CPAC, OEC, ADS, BESB, BRS, DMHAS, DCF, SRBI, CTAA, CTAS and CCS. "ADS", "CCS" and "DCF" also stand for other things outside Connecticut. "ABA" is untagged. None collides with a given name in the test list.

## 5. Left out on purpose
- **Bureau of Special Education / BSE**: the list's `bse` concept is Pennsylvania's bureau, and its preferred term is the bare phrase "Bureau of Special Education". A CT concept with the same preferred term would clash. Suggest a reviewer either make `bse` generic or give CT its own key with a distinct preferred term.
- The six named RESCs (ACES, CES, CREC, EASTCONN, EdAdvance, LEARN). They are regional bodies, close to district names.
- Department of Public Health (DPH), a generic agency name.
- The PSN's equal-opportunity contact (a personal name) and all addresses and phone numbers.
