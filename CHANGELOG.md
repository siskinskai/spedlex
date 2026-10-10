# Changelog

All notable changes to SPEDLex. Versions follow
[METHODOLOGY.md §7](docs/METHODOLOGY.md#7-versioning): minor for new layers,
patch for corrections and reviews. Concept IDs never change between versions.

## [Unreleased]

Adds terminology helpers and the `disfavored` flag (0.46.0). SPEDLex's records
already list every form a concept takes, tagged to the states whose
documents use it; the new `spedlex.Lexicon` exposes that to AI and writing
tools: `lookup` (what a term names and what the reader's state calls it),
`annotate` (every term in a text, with citations), `check` (disfavored,
older, other-state and ambiguous terms, with suggestions) and `glossary` (a
short cited glossary for a model's prompt). The same functions are on the
command line (`python -m spedlex`, or `spedlex` once installed) and in an
optional MCP server (`spedlex[mcp]`, `spedlex-mcp`; Python 3.10+). New
guide: `docs/USING-WITH-AI.md`. The Safelist and its matching rules are
unchanged.

Strings may now carry `disfavored: true` with a `usage_note` and a
`usage_basis` (new optional schema fields, so a minor version). The flags
come from a new curated file, `sources/disfavored.tsv`; the build fails if a
row names an unknown concept or string, or the preferred term. Three strings
are flagged, drafted with Claude Opus 5.5 (`claude-opus-5-5`) and awaiting
the maintainer's check: "mental retardation" (Rosa's Law, 2010), "serious
emotional disturbance" (IDEA Amendments of 1997) and New Jersey's
"auditorily handicapped". Disfavored strings are still protected from
redaction. `data/spedlex.csv` gains two last columns, `disfavored` and
`usage_note`; `data/stats.json` gains `disfavored_strings`, `legacy_strings`
and `regional_strings`. The explorer strikes through disfavored forms.
README, METHODOLOGY, SCHEMA, USING, DATA_CARD, ROADMAP, AGENTS.md,
CONTRIBUTING.md, CITATION.cff and `prompts/add-state.md` (v1.4) describe the
wider use. No concept, string or ID changed.

Initial public commit of v0.45.0. Earlier development history (Oct 3-9, 2026,
drafted with claude-opus-5-5 and claude-sonnet-5-5) is kept privately. Source
documents (PDFs, saved pages, OCR text) are no longer stored in the repository:
they are cited through `sources/documents.tsv`, and the old `xx-docs/` folders
became `provenance/xx/` with only the layer reports, audits and source notes.
New guards: `tests/test_repo_hygiene.py` (no source documents or large files
tracked), `.gitignore` entries, an optional pre-commit config, a check in
`tools/add_state.py`, and matching rules in AGENTS.md, CONTRIBUTING.md, the
prompts and the pull request and issue templates. No concept, string or ID
changed.

Adds the source manifest (0.45.0). `sources/documents.tsv` records every source
document the layers were read from: URL, retrieval date, SHA-256 hash, size,
page count, rights category and (once filled in) a Wayback Machine snapshot.
Source documents themselves are cited, not stored; `tools/fetch_sources.py`
downloads them into `.sources-cache/` and checks each against its hash. Each
`sources[]` entry may now carry an optional `doc_id` pointing at its manifest
row (a new optional schema field, so a minor version), every state layer's
sources carry one, and the build fails if a `doc_id` is unknown or a manifest
row is neither cited nor declared in a module's `UNCITED_DOCS`. No concept,
string or ID changed.

Maintainer decisions (Jeremy Evans, 2026-10-08): twelve concepts first tagged
to one state but attested by another are now national (no single-state
jurisdiction; keys and IDs unchanged): `lpac`, `vision_future`, `state_ops`,
`state_sp_sch`, `consult_teacher`, `preschool_swd`, `parent_mentor`,
`resident_dist`, `nh_qual_examiner`, `nc_sps`, `nc_recp`, `in_transition_iep`.
The removal of "Doe" from the surname list is confirmed. `prompts/add-state.md`
is now v1.2: the goal is to cover terms likely to be screened, not to track
what is legally current. No strings changed.

Adds New Mexico (US-NM, 0.44.0): 6.31.2 NMAC, Children with Disabilities (as
amended 7/31/2023), the NMPED Special Education Procedural Safeguards notice
(rev. Dec. 2020), the IEP manual Developing Quality IEPs (rev. Oct. 2011) and
the High School Graduation Requirements Guidance (April 2025). The layer
attests 245 concepts and adds 47 new ones (45 New Mexico-specific). It was
drafted with Claude Opus 5.5 (`claude-opus-5-5`) and has not yet been audited;
see `provenance/nm/nm-layer-report-2026-10-09.md`. New regional ambiguities: SED
(US-NY, US-NM) and DVR (US-DE, US-NM).

Adds West Virginia (US-WV, 0.43.0): Board Policy 2419 (126CSR16, eff.
March 2023, a scanned rule read through OCR) and the WVDE Procedural
Safeguards notice (rev. Aug. 2024). The layer attests 277 concepts and adds 86
new ones (61 West Virginia-specific). It was drafted with Claude Sonnet 5.5
(`claude-sonnet-5-5`) and independently audited and corrected with Claude
Opus 5.5 (`claude-opus-5-5`); see `provenance/wv/wv-layer-audit-2026-10-09.md`.
The audit removed two variants neither document prints, the "Augmentative/
Alternative Communication Evaluation" string and two weak attestations;
fixed 16 page citations; changed the `wv_osp` preferred term to the notice's
wording; and added 22 existing concepts the documents use.

Matcher: a match that is a month name or abbreviation is no longer
protected when a number sits next to it, so the matcher cannot shelter part
of a date of birth. This came from the West Virginia audit: "APR" (Annual
Performance Report, new in 0.43.0) is also April, and it would have
protected "APR" in "DOB: APR 14, 2015". Away from numbers, "APR" is still
protected. Documented in METHODOLOGY.md §5 and USING.md (matching rule 7).
Adds `test_never_shelters_a_month_inside_a_date` and
`test_month_shaped_acronym_is_protected_away_from_dates`. Drafted with
Claude Opus 5.5 (`claude-opus-5-5`).

Adds a way to ask outside experts to review a state's entries by email, with
no GitHub needed. `tools/expert_review.py request <state>` builds a
plain-text email from the data: key questions, alternate names, unconfirmed
candidate terms and open prompts. Nevada is the worked example
(`outreach/expert-review/rounds/NV-20261008/`). `tools/expert_review.py reply`
reads a reply back into proposed `reviews.tsv` rows and a follow-up list; it
never writes `sources/reviews.tsv`. The email lets each expert choose to be
credited by name, role and affiliation, by name and role, or not at all.
Opted-in names go in the new `CONTRIBUTORS.md`; affiliation is kept out of
the review log. README and CONTRIBUTING link to both. Adds
`tests/test_expert_review.py`. No data changes. Drafted
with Claude Sonnet 5.5 (`claude-sonnet-5-5`).

## [0.42.0] - 2026-10-08

Adds the Wyoming layer (`wyoming`, US-WY) from the Wyoming Department of
Education's Chapter 7 rules, Services for Children with Disabilities
(effective 03/22/2010, shown as current on the Secretary of State's rules
portal on 10/08/2026), and its Notice of Procedural Safeguards (May 2025). It
attests 125 concepts and adds 10 (8 machine_validated, 2 candidate): the
Wyoming Department of Education (WDE) and its Special Education Programs
Division, UPLIFT, the Developmental Disabilities Division as Wyoming's
intermediate educational unit for preschool services, the Department of
Family Services, the Wyoming Severe Discrepancy Formula, developmental
preschool centers, and two national concepts first attested here,
inter-district placements and court-ordered placements.
Wyoming's "Cognitive Disability" label is recorded under intellectual
disability, and "home based education" under home education. The rule's PDF
from the portal is a scan, so its words were read from a second copy with an
OCR text layer; no parent guide was available as a file. Drafted
with Claude Sonnet 5.5 (`claude-sonnet-5-5`). Audited by Claude Opus 5.5
(`claude-opus-5-5`); the audit is in `provenance/wy/wy-layer-audit-2026-10-08.md`
and its fixes are applied: 16 more existing concepts are attested (among
them due process complaint, public agency and IEP Team), the
"disproportionate representation" attestation is removed because it is not
significant disproportionality, and the plural "preschool children with
disabilities" is added.

## [0.41.0] - 2026-10-08

Adds the Iowa layer (`iowa`, US-IA) from 281 IAC chapter 41 (Special
Education; IAC printed 12/10/25, amendments effective through January 14,
2026), the Iowa Department of Education's Procedural Safeguards Manual for
ages 3-21 (August 2023) and the undated "Special Education Terms and
Acronyms, Ages 3-21" sheet. It attests 278 concepts and adds 58 (31
machine_validated, 27 candidate), including the Iowa Department of
Education and its Bureau of Learner Strategies and Supports, the Area
Education Agency, the Board of Educational Examiners, ASK Resource Center,
Disability Rights Iowa, the AEA Family & Educator Partnership, Early
ACCESS, Iowa's "eligible individual" and "disability in obtaining an
education", "behavior disorder" for emotional disturbance, "head injury"
for traumatic brain injury, systematic progress monitoring, trial
placements, classroom clearance, special education instructional and
support services, the educational strategist and other AEA support roles,
the family support mentoring program, the Iowa School for the Deaf, and the
state's three model dispute resolution forms. New non-state concepts:
multicategorical, audiologist, occupational and physical therapist,
speech-language pathologist and their assistants, audiometrist, early
hearing detection and intervention, center for independent living,
augmentative and alternative communication, children and youth with
special health care needs, individual health plan and dyscalculia. Iowa
attests North Carolina's "systematic problem-solving process" concept
(same name, 41.313). "ECI" (Texas, Iowa) and "IDOE" (Indiana, Iowa) are
new allowed cross-state ambiguities. "Early ACCESS" is recorded as a
case-sensitive string so it does not collide with Colorado's "Early
Access" (gifted early entrance). Drafted with Claude Opus 5.5
(`claude-opus-5-5`). Audited in a fresh session by the same model; the audit
is in `provenance/ia/ia-layer-audit-2026-10-08.md` and its fixes are applied: seven
more existing concepts are attested, the Department of Human Services record
uses the sheet's own name, the plurals of AEA and eligible individual cite
where they appear, and the sheet's "EI" moves to a small `iowa_supplement`
layer.

## [0.40.0] - 2026-10-08

Adds the Delaware layer (`delaware`, US-DE) from 14 DE Admin. Code 922
(Purposes and Definitions) and 925 (Evaluations, Eligibility, IEPs), both
amended through April 1, 2025, the DDOE Procedural Safeguards Notice (July
2026) and the Parent Information Center of Delaware's "Parents Are the Key"
(2013). It attests 217 concepts and adds 37 (16 machine_validated, 21
candidate), including the Delaware Department of Education and its
Exceptional Children Resources office, the Delaware School for the Deaf and
the Delaware Autism Program, the Department of Services for Children, Youth
and Their Families, Delaware's "educational classification", the
twelve-month program, the Employment First Policy, the Diploma of Alternate
Achievement Standards, the Relative Caregiver's School Authorization, the
three-member due process hearing panel, SPARC, the state's mediation, due
process and state complaint forms, Child Development Watch and the former
DCAS and DSTP tests. New non-state concepts: auditory neuropathy spectrum
disorder, auditory brainstem response, cortical vision impairment, draft
IEP, educational diagnostician, case-by-case determination, out-of-school
suspension and community parent resource center. "PIC" is now an allowed
cross-state ambiguity (New Hampshire and Delaware). "DOE" is the rule's short
form for the Delaware Department of Education. "Doe" is removed from the
reference surname list by a maintainer's decision: it is used almost only as
a pseudonym, so it carries no risk of identifying a child. The acronym
"DDOE" appears only in the notice and guide, so it is attached in a small
`delaware_supplement` layer, which also attests three concepts the Iowa layer
defines and therefore runs after it. The guide is a
parent center's 2013 manual and is cited as secondary guidance. Drafted
with Claude Opus 5.5 (`claude-opus-5-5`). Audited in a fresh session by the
same model; the audit is in `provenance/de/de-layer-audit-2026-10-08.md` and its
fixes are applied: 17 more existing concepts are attested, and two weak
attestations (PTI on the notice's contact page, home instruction on guide
p. 38) are removed.

## [0.39.0] - 2026-10-08

Adds the Colorado layer (`colorado`, US-CO) from the ECEA Rules (1 CCR 301-8,
amendments through May 15, 2025), the CDE Procedural Safeguards Notice (April
2024) and the CDE IEP Procedural Guidance (July 2017). It attests 210 concepts
and adds 61 (33 machine_validated, 28 candidate), including the Colorado
Department of Education and its Exceptional Student Services Unit, Colorado's
Administrative Unit family (AU, AUR, AUA, alternate and multi-district AUs),
BOCES, the State Complaints Officer and Office of Administrative Courts, the
Communication Plan, Learning Media Plan, abbreviated school day, non-significant
and significant IEP changes, the State Recommended IEP, the Service Delivery
Statement, the charter school service models and the Advanced Learning Plan.
"CDE" and "SCO" are now allowed cross-state ambiguities (CDE: California and
Colorado; SCO: DC and Colorado). Drafted with Claude Sonnet 5.5
(`claude-sonnet-5-5`). Its "multilingual learner", "Other Health Impaired" and
"Summary of Performance" strings already existed untagged, so they are no
longer tagged US-CO; the tag had made them disappear for users who filter by
any other state.

## [0.38.0] - 2026-10-08

Applies the independent audits of the Alaska, Alabama, Arkansas, Arizona,
Indiana and Maryland layers (`*-docs/*-layer-audit-2026-10-08.md`). Of 948
audited entries, 946 were confirmed at their citation and 2 were misplaced;
none were not found.

Corrections: the Alaska and Alabama procedural safeguards rows for
parentally-placed private school children now cite p. 7, where the term
appears; Alaska's child find row cites 4 AAC 52.100 (the section heading);
Arkansas's Early Childhood Outcomes concept now cites GUIDE p. 85 and adds
"Early Childhood Outcomes Process" and "COS"; the Arizona docstring no longer
says the Arizona Schools for the Deaf and the Blind appear only broken
across glossary columns; the Maryland docstring names the source of the
Aug. 17, 2026 amendment date (53:16 Md. R. 687). New strings and attestations:
"early intervention" (Alabama), "early identification" (Maryland), Braille
(Alaska), and five Indiana definitions (homebound instruction, interim
alternative educational setting, travel training, certificate of completion,
early intervening services).

Adds 13 concepts in four supplement layers, following the
`pennsylvania_supplement` pattern: `alabama_supplement` (Child Count),
`arizona_supplement` (from R7-2-404: Arizona Schools for the Deaf and the
Blind, institutional voucher, home school district, State Placing Agency),
`indiana_supplement` (Indiana education scholarship account and its
education service plan, I-CHAMP, expedited evaluation, student with a print
disability, virtual instruction) and `maryland_supplement` (Certified
Orientation and Mobility Specialist, statewide assessment). Drafted and
audited with Claude Opus 5.5 (`claude-opus-5-5`); the same model drafted
the layers, so a second, independent review is still worthwhile.

## [0.37.0] - 2026-10-08

Adds the Arkansas layer (`arkansas`, US-AR) from 6 CAR pt. 130, Subpart 2
(Definitions), the ADE Part B Procedural Safeguards Notice (2006 federal model
with an Arkansas header) and the DESE Special Education Process Guide (March
14, 2023). It attests 158 concepts and adds 46 (17 machine_validated, 29
candidate), including the Division of Elementary and Secondary Education and
its Special Education Unit, Arkansas's resource, special class, integrated
classroom and school-based day treatment settings, the qualified-examiner
roles, the Evaluation/Programming Conference, the temporary IEP, the Arkansas
Alternate Assessment Participation Manual and the Alternate Pathway to
Graduation. "DESE" is now an allowed cross-state ambiguity (Massachusetts,
Missouri and Arkansas). Nine national concepts are new, among them
educational interpreter, data-based problem solving, record of access, Early
Childhood Outcomes and the Indicator 13 Checklist. Drafted with Claude Opus
5.5 (`claude-opus-5-5`).

## [0.36.0] - 2026-10-08

Adds the Alabama layer (`alabama`, US-AL) from Ala. Admin. Code ch. 290-8-9
(Supp. 13-3, effective Nov. 4, 2013, ALSDE copy), Alabama's Procedural
Safeguards (Special Education Rights) (January 2025) and Mastering the Maze,
Process 1 (August 2019). It attests 236 concepts and adds 55 (13
machine_validated, 42 candidate), including the Problem Solving Team (on
`sst`), the Alabama Alternate Assessment, the Alabama High School Diploma
and its three pathways, SETS, the Early Learning Progress Profile and the
state's gifted teams and plan. "SETS" is now an allowed cross-state
ambiguity (Kansas and Alabama). Thirteen national concepts are new, among them
psychometrist, coordinated early intervening services, OSEP, bus suspension,
in-school suspension, Carnegie unit (an eponym) and Head Start. Drafted with
Claude Opus 5.5 (`claude-opus-5-5`).

## [0.35.0] - 2026-10-08

Adds the Alaska layer (`alaska`, US-AK) from 4 AAC 52.100-52.790 (text from
the Alaska Legislature's Administrative Code site), DEED's Notice of
Procedural Safeguards: Parental Rights for Special Education (undated; file
dated March 2024), the Alaska Special Education Parents' Guide (June 2017)
and DEED's DLM alternate assessment page. It attests 149 concepts and adds 19
(5 machine_validated, 14 candidate), including DEED, Alaska's Infant
Learning Program, the Special Education Service Agency and the Alternate
Assessment Participation Checklist. Alaska's "cognitive impairment" and
"early childhood developmental delay" join `id` and `dd` as strings. Six
national concepts are new: fetal alcohol spectrum disorder, unilateral
placement, pull-out, gross motor, intelligence quotient and norm-referenced
test. Also adds `docs/COVERAGE.md`, which tracks the jurisdictions still
pending. Drafted with Claude Opus 5.5 (`claude-opus-5-5`).

## [0.34.0] - 2026-10-07

Adds the Maryland layer (`maryland`, US-MD) from COMAR 13A.05.01 (text from
the Library of Maryland Regulations), MSDE's Parental Rights: Maryland
Procedural Safeguards Notice (July 2024) and the Parent Information Series
guide to the IEP (2023). It attests 98 concepts and adds 16 (9
machine_validated, 7 candidate), including the Maryland Online IEP, the
Learning Continuity Plan and the Maryland Accommodations Manual. Virginia's
"Certificate of Program Completion" (`cert_completion`) is now a general
concept, because Maryland issues one by the same name. Drafted with Claude
Opus 5.5 (`claude-opus-5-5`).

## [0.33.0] - 2026-10-07

Adds the Arizona layer (`arizona`, US-AZ) from Ariz. Admin. Code R7-2-401
(Supp. 25-4), ADE's Procedural Safeguards Notice (Rev. 08-28-25), the
parent guide Traveling the Special Education Highway (2019) and the ESS
Glossary of Acronyms and Terms (May 2026). It attests 60 concepts and adds
14 (4 machine_validated, 10 candidate). Arizona's mild, moderate and severe
intellectual disability categories join `id` as strings, as Nevada's do.
Illinois's "Delegation of Rights" (`delegation`) is now a general concept,
because Arizona law uses it too. Drafted with Claude Opus 5.5
(`claude-opus-5-5`).

## [0.32.0] - 2026-10-07

Adds the Indiana layer (`indiana`, US-IN) from 511 IAC 7 (Article 7, May
2024 compilation), IDOE's Notice of Procedural Safeguards (Aug. 2025) and
the parent guide Navigating the Course (Aug. 2025). It attests 97 concepts
and adds 23 (13 machine_validated, 10 candidate), including "case
conference committee" (CCC) as Indiana's name for the IEP Team. DC's
"Educational representative" (`dc_educ_rep`) is now a general concept,
because Indiana appoints them too. Drafted with Claude Opus 5.5
(`claude-opus-5-5`).

Across 0.32.0 to 0.34.0 the list grows from 892 to 945 concepts and 27 to
30 states; high-risk concepts rise from 141 to 163. Two of those are older
concepts that now carry a string with a state name in it: "Maryland
Procedural Safeguards Notice" on the procedural safeguards notice concept
and "Arizona Office of Administrative Hearings" on the Office of
Administrative Hearings concept.

## [0.31.0] - 2026-10-07

Adds the Hawaii layer (`hawaii`, US-HI) from Hawaii Administrative Rules
Title 8, Chapter 60 (Board of Education copy), the HIDOE Procedural
Safeguards Notice (May 2022) and the brochure "Special Education: Is it for
your child?" (Nov. 2025). It attests 33 concepts and adds 11, all
candidate: the rule text attests existing concepts and adds Hawaii's
category labels, such as "speech or language disability", as synonyms. A
draft concept, "Conciliation" (SPED:000889), came only from the 2021 text
that the brochure's PDF hides behind the 2025 text, and was retired before
release. The place-name list now also matches "Hawaiʻi" spelled with the
ʻokina or an apostrophe (`reference/places/us_jurisdictions.tsv`), with a
test. Drafted with Claude Opus 5.5 (`claude-opus-5-5`).

## [0.30.0] - 2026-10-07

Adds the North Carolina layer (`north_carolina`, US-NC) from the State
Board's Policies Governing Services for Children with Disabilities (NC
1500-1508, rev. March 2021) and NCDPI's Notice of Procedural Safeguards
(July 2026). It attests 39 concepts and adds 13 (12 machine_validated, 1
candidate), including the four NC 1508-3.1 service levels and a general
multi-tiered system of support concept (`mtss`). MTSS is a school-wide
framework (NC 1500-2.25), not a synonym of response to intervention, so
"multi-tiered system of supports" and "MTSS" move from the federal `rti`
concept to `mtss`, and Kansas's "Kansas MTSS and Alignment" now has `mtss`
as its broader concept. Drafted with Claude Opus 5.5
(`claude-opus-5-5`).

## [0.29.0] - 2026-10-07

Adds the Ohio layer (`ohio`, US-OH) from DEW's Operating Standards for the
Education of Children with Disabilities (Ohio Adm.Code 3301-51, June 2025
booklet) and A Guide to Parent Rights in Special Education (April 2025). It
attests 46 concepts and adds 20 (13 machine_validated, 7 candidate),
including a general `charter_school` concept ("community school" in Ohio).
"State residential school" joins the existing state special schools
concept (a draft duplicate, SPED:000860, was retired before release).
New Hampshire's "Chartered public school" and DC's "Public charter school
LEA" now list `charter_school` as a broader concept; the DC concept keeps
`lea` as its other parent. To allow this, the build now resolves `broader`
after every layer is applied, so a parent may come from a later layer, and
`broader` may be a list of keys. Output for unchanged concepts is
byte-identical. Drafted with Claude Opus 5.5 (`claude-opus-5-5`).

Across 0.29.0 to 0.31.0 the list grows from 848 to 892 concepts and 24 to
27 states; high-risk concepts rise from 130 to 141.

## [0.28.0] - 2026-10-06

Adds the Connecticut layer (`connecticut`, US-CT) from CSDE's copy of the
Regulations of Connecticut State Agencies §§ 10-76a-1 to 10-76l-1 (rev.
2015), A Parent's Guide to Special Education in Connecticut (2021) and the
Procedural Safeguards Notice (rev. Mar. 2021). It attests 57 concepts and
adds 27 (11 machine_validated, 16 candidate). "Planning and placement team"
and "PPT" join the IEP Team concept as Connecticut synonyms, and "SRBI" joins
the existing scientific, research-based intervention concept (a draft
duplicate, SPED:000844, was retired before release). The New Jersey
concept "Speech-language specialist" (`nj_sls`) is now general, because New
Hampshire uses the title too. Drafted with Claude Opus 5.5
(`claude-opus-5-5`).

## [0.27.0] - 2026-10-06

Adds the New Hampshire layer (`new_hampshire`, US-NH) from the Department's
NH Special Education Reference Manual (Ed 1100 rules, accurate as of Oct.
20, 2023), the Special Education Procedural Safeguards Handbook (Dec. 2024)
and the Bureau of Special Education Support web page. It attests 52
concepts and adds 25 (21 machine_validated, 4 candidate). Drafted with
Claude Opus 5.5 (`claude-opus-5-5`).

## [0.26.0] - 2026-10-06

Adds the New Jersey layer (`new_jersey`, US-NJ) from N.J.A.C. 6A:14,
Parental Rights in Special Education (rev. June 2026) and NJDOE's Parental
Rights and Engagement page. It attests 94 concepts and adds 29 (17
machine_validated, 12 candidate). Drafted with Claude Opus 5.5
(`claude-opus-5-5`).

## [0.25.0] - 2026-10-06

Adds the Michigan layer (`michigan`, US-MI) from the Michigan
Administrative Rules for Special Education, MDE's Procedural Safeguards
Notice (updated Oct. 2018), the guidance "IEP Development: Special Education
Programs and Services" (May 2022) and the MI-Access page. It attests 93
concepts and adds 24 (17 machine_validated, 7 candidate). Drafted with
Claude Opus 5.5 (`claude-opus-5-5`).

Across 0.25.0 to 0.28.0 the list grows from 743 to 848 concepts and 20 to 24
states; high-risk concepts rise from 114 to 130, mostly agency and
assessment names that contain a state name. The acronym DDS now has three
state meanings (DC, NJ, CT) and DCYF two (WA, NH); the build reports both
as allowed ambiguities.

## [0.24.0] - 2026-10-04

Adds the District of Columbia layer (`district_of_columbia`, US-DC) from
OSSE's documents: 5-A DCMR Chapter 30, the IDEA Part B Notice of Procedural
Safeguards (rev. Aug. 2018), the Special Education Process Handbook
(SY2026-27), the 2026 parent brochure and the alternate assessments page.
It attests 189 existing concepts and adds 58 (29 machine_validated from the
regulation, 29 candidate). Drafted with Claude Opus 5.5 (`claude-opus-5-5`).
The build now flags U.S. place names automatically: any string containing
a state or territory name, or its postal code inside a longer string
("Strong Start DC", "MO DESE"), gives its concept the `place_name` reason
and a `high` grade, the same as a manual flag. The lists are in
`reference/places/`, hits are reported in `pii_risk.place_list_hits` and
`data/collision_report.csv`, and two new tests guard bare place names.
High-risk concepts rise from 17 to 114.

## [0.23.0] - 2026-10-03

First public release: 685 concepts from 34 CFR Part 300 and 19 states, a
reference matcher, documentation and contribution tooling. Claude Opus 5.5
helped build it, and every source records the assisting model in
`assisted_by`. `prompts/` holds model-neutral prompt templates for
contributors. `AGENTS.md` sets the rules for AI coding agents.

### Notes for anyone who used a pre-release copy
- Concept IDs are unchanged from 0.22.0.
- Output files were renamed from `seed_34cfr300.*` to `spedlex.*`.
- Sources now carry a `jurisdiction`, and advocacy-group or district
  summaries are typed `secondary_guidance` instead of `corpus`.
- The second Pennsylvania pass is now the `pennsylvania_supplement` layer.
- The reference scrubber used for collision testing no longer treats U.S.
  state names as first names. Rosa's Law is the one remaining collision.

## Development history (pre-release)

| Version | Layer |
|---|---|
| 0.1.0 | Federal core: 34 CFR Part 300 (156 concepts) and 13 illustrative placeholders |
| 0.2.0 | Texas: safeguards notice, ARD guide, 19 TAC §89.1040 |
| 0.3.0 | Nevada: parent rights notice, statewide IEP form, NAC 388 |
| 0.4.0 | Texas: STAAR Alternate 2 and accommodations guides, Dyslexia Handbook |
| 0.5.0 | Virginia |
| 0.6.0 | California |
| 0.7.0 | New York |
| 0.8.0 | Florida |
| 0.9.0 | Pennsylvania |
| 0.10.0 | Illinois |
| 0.11.0 | Massachusetts |
| 0.12.0 | Minnesota |
| 0.13.0 | Missouri |
| 0.14.0 | Louisiana |
| 0.15.0 | Kansas |
| 0.16.0 | Pennsylvania supplement: 22 Pa. Code §§14.101 and 16.1 |
| 0.17.0 | Utah |
| 0.18.0 | Washington |
| 0.19.0 | Tennessee |
| 0.20.0 | Idaho |
| 0.21.0 | Oregon |
| 0.22.0 | Georgia |
