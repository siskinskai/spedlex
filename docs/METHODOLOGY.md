# Methodology

This document explains how SPEDLex is built, why each choice was made, and
where the list falls short. It has three readers in mind. One is deciding
whether to trust the list. One is extending it to a new state. One wants to
reproduce or critique the approach.

## 1. Goal and scope

**Why.** Caregivers (parents, guardians, and the educators and advocates who
support them) increasingly use AI tools to understand and answer
special-education documents. To do that safely, they first remove the child's
personal information. A de-identification tool, called a *scrubber*, replaces
names, dates and other identifiers before the text leaves their device. A
scrubber can only do this well if it can tell a special-education term from
a name. No shared vocabulary of those terms existed.

**Goal.** Give any de-identification tool a list of special-education terms
that are safe to protect from redaction. Attach enough evidence that a person
can check each one.

**A second use.** The structure that serves redaction (one concept, every
form it takes, each form tagged to the states whose documents use it, a
citation) is also what AI and writing tools need to name terms consistently:
to answer a Texas parent in Texas's words, expand an acronym correctly, avoid
a term the law replaced, and cite where a term comes from.
[USING-WITH-AI.md](USING-WITH-AI.md) describes that use. It adds no new
inclusion rule: a term is in the list for the reasons below, and the second
use takes the list as it is. What it adds is the `disfavored` flag (§4).

**What belongs in the list.** A term belongs if two things are true. It
appears in a regulation, a state document or (later) an evaluation instrument
or IEP corpus as a special-education concept. And a scrubber would plausibly
damage it. That covers:

- legal and procedural terms (FAPE, prior written notice, stay-put, ARD committee)
- disability categories and the health conditions the regulations name
- services, placements, IEP parts, evaluation and eligibility terms
- state agencies, assessments, diplomas and programs
- skill constructs, accommodations and (later) instruments and score terms

**What does not belong.** Three kinds of text stay out. General English words
that need no protection ("meeting", "teacher"). Definitions copied from
copyrighted glossaries. Anything that identifies a person, school or district.
Medical terms already covered by MeSH or SNOMED CT stay in the list when the
special-education regulations use them. The list maps them to those
vocabularies and does not redefine them.

**Unit of analysis: the concept, not the word.** One concept ID holds the
regulatory phrase, its acronym, plurals, older forms and each state's own
name for it. "PLAAFP", "PLOP" and "present levels" are one concept. This is
the UMLS model. It lets the list answer "which states use this?" and "what
did this used to be called?"

## 2. Sources and how they were chosen

Sources are ranked by authority. A record cites the strongest one available.

| Rank | Source type | Why |
|---|---|---|
| 1 | Federal regulation (34 CFR Part 300) | Binding everywhere. Every state's vocabulary is built on it. |
| 2 | State regulation | Binding in the state. Defines the state's own categories. |
| 3 | Procedural safeguards notice | Every state must publish one (34 CFR 300.504). It is the one document that exists in a comparable form in every state. |
| 4 | State guidance (parent guides, IEP manuals, assessment pages) | Shows the vocabulary families and teachers actually see. |
| 4b | Secondary guidance (an advocacy group's or a district's summary of state rules) | Used only when the state's own document couldn't be read. Recorded as `secondary_guidance`. |
| 5 | Controlled vocabularies, instrument catalogs, corpora | Planned. Needed for skills, tests and scores, which regulations barely mention. |

**The state recipe.** Each state is read from three documents: its
procedural safeguards notice, its main family or IEP guide, and its
special-education rule (definitions and eligibility). If a state's
assessment or graduation pages name alternate assessments or diplomas, those
are added. The same recipe in every state makes states comparable. When a
term is missing, the state's core documents don't use it. Nobody read
further in one state than in another.

**When a document can't be read.** Links break, PDFs are scanned images, and
some sites block automated access. The builder then tries three substitutes,
in this order: an official mirror (Cornell LII, Justia, a state register), a
district's posted copy of the same state document, or an older edition. Every
substitution goes in the state module's docstring, so a reader can see what
was and wasn't consulted. [SOURCES.md](SOURCES.md) lists every document cited.

**The source manifest.** The documents themselves are not stored in the
repository, because most belong to their publishers. Instead
`sources/documents.tsv` has one row per document: where it was downloaded,
when it was read, its SHA-256 hash and size, its page count, a rights
category and a Wayback Machine snapshot. Records point to a row by `doc_id`.
The hash proves which version of a document was read; the snapshot lets
anyone get that version if the publisher changes or removes it;
`tools/fetch_sources.py` downloads the documents and checks each hash. Where
the archive refused a page, the row says `blocked` and the hash is the only
proof.

## 3. Extraction

Each document was read for three things:

- each defined term, rule heading, list item and named program
- the acronyms and variants the document uses for it
- a citation down to the paragraph (regulations) or page (PDFs)

Scanned documents with no text layer were read from text produced locally by
OCR; the OCR text is working material and is not published. Layer reports
and audits for each state are kept in `provenance/<xx>/`.

The `extraction.method` field records how a term was found:

- `regulatory_definition`: a defined term
- `regulatory_heading`: a section or list heading
- `regulatory_text`: named in the body
- `manual`: read from a guidance document

`termhood_cvalue` and `instrument_harvest` are reserved for the planned
corpus and instrument phases.

**AI assistance.** The maintainer built the first release with Claude Opus
5.5 (Anthropic, `claude-opus-5-5`). The model read the cited documents,
drafted the records and wrote the build pipeline. The maintainer chose the
sources and the method, directed each state and checked the results. Every
source in the data records the model that helped (`assisted_by`).
`data/stats.json` counts sources by model.

Later contributions will use a variety of models. To keep the list
trustworthy whichever model drafts it, the project relies on four things:

- **Documents, not recall.** A model works only from documents it is given.
  Every term is cited to a page or paragraph a person can check.
- **Independent checking.** A second model or a fresh conversation audits a
  draft against its documents before submission
  ([prompts/audit-layer.md](../prompts/audit-layer.md)).
- **Human responsibility and review.** A person submits and answers for every
  change. Only people make `expert_accepted` decisions.
- **Automated invariants.** The build and tests reject uncited sources,
  duplicate strings and changed IDs. They fail if any name would be protected
  on its own.

At first release, no independent expert had accepted a record. Treat the list
as a well-sourced first draft. The review statuses say the same.

## 4. Building records

**New concept or new name?** When a state uses a term, ask first whether it
names something already in the list. Texas's "ARD committee" is the federal
IEP Team. Massachusetts's "emotional impairment" is the federal "emotional
disturbance". Both become new strings on the existing concept, tagged with
the state (`regional: ["US-MA"]`), and the state's document joins the
concept's sources. A term becomes a new concept only when it names something
with no federal equivalent: a state agency, a state assessment, a diploma
type, a placement model.

**String types.** Each string has one type: `preferred`, `synonym`,
`acronym`, `abbreviation`, `spelling_variant`, `plural` or `legacy`. Legacy
forms are kept on purpose. Several states' rules still say "mental
retardation" or "serious emotional disturbance". A safelist that dropped
those forms would strip a state's own citations from an IEP.

**Disfavored forms.** A few strings carry `disfavored: true`, with a
`usage_note` and a `usage_basis`. The flag means the form shouldn't be used
in new writing, because the law replaced it or it is widely considered
stigmatizing. It doesn't change matching: the string is still protected
from redaction, because older documents and some state rules print it. The
flags live in one file, `sources/disfavored.tsv`, rather than in the layer
modules, because they are a judgment about usage, not a fact a single state
document attests. Each row names its basis, and a person checks it before it
is merged. The list starts small on purpose (three forms in 0.46.0) and
grows only with a basis: a statute or rule that replaced the term, or a
state or federal agency's published decision to stop using it. A renamed
agency or program is `legacy`, not disfavored.

**Case.** Phrases match without regard to case. Acronyms match only in exact
case. "ED" (emotional disturbance) is protected and the name "Ed" is not.

**Numbers.** New York names special classes by ratio ("12:1+1"). The list
protects them only as exact strings with non-alphanumeric characters on both
sides. "12:1" never matches inside a time like 12:15.

**Ambiguity across states.** Some acronyms mean different things in
different states. CSA is Virginia's Children's Services Act and also the
California Spanish Assessment. DESE is the education department of both
Massachusetts and Missouri. The build allows a string on two concepts only
when each use is tagged to a different state, and it reports every case.
Any other duplicate is an error and fails the build.

**Single letters are never safelisted.** Nevada's IEP form codes services as
A, C or D. Protecting those would shelter initials.

**Permanent IDs.** Concept IDs (`SPED:000102`) live in
`data/concept_ids.tsv`. They never change and are never reused. A removed
concept is marked `retired` and its ID stays reserved. IDs from 900001 up
are reserved for illustrative placeholders.

## 5. Grading privacy risk

A safelist can do harm in exactly one way: by sheltering a real identifier
from redaction. So every concept gets a risk grade that limits how its
strings may be used.

The build checks each string against five things:

- **SSA first names.** Names in the Social Security Administration top 1,000
  in any year from 1880 to 2008.
- **Census surnames.** Surnames with at least 10,000 bearers in the 2000
  Census.
- **A reference scrubber's patterns.** These cover phone numbers, SSNs,
  emails, addresses, record IDs, medication doses and a first-name
  dictionary. A pluggable adapter supplies them. The default adapter copies
  the patterns of SCRUB, an offline de-identification tool for
  special-education documents and the first tool to use SPEDLex.
  [USING.md](USING.md) shows how to test any other scrubber.
- **U.S. place names.** The names of the 50 states, the District of
  Columbia and the five inhabited territories ("Georgia Milestones",
  "District of Columbia Public Charter School Board"), and their postal codes
  written in capitals inside a longer string ("Strong Start DC", "MO DESE",
  "WA-AIM"). A place name narrows where a child lives. A one-word string is
  never read as a postal code, because many codes are also
  special-education acronyms ("ID", "MD", "HI"). Reviewed exceptions, such as
  "CT services" (consultant teacher), are listed in
  `reference/places/not_places.tsv`.
- **Manual flags.** These mark eponyms ("Tourette", "Kaufman"), other place
  names such as cities and counties ("Vineland", "St. Louis") and common
  English words.

| Level | When | Rule | Meaning |
|---|---|---|---|
| `high` | A single-word string is itself a name, a string contains a U.S. place name, the concept carries an eponym or place-name flag, or the scrubber's name dictionary fires | `never_bare` | The risky word is protected only inside its full phrase. "Kaufman Assessment Battery for Children" is protected. "Kaufman" alone never is. |
| `low` | Any other name-list hit, scrubber hit, number or flag | `phrase_only` | Protect only the full string. |
| `none` | Nothing found | `phrase_or_token` | Safe to protect wherever it appears. |

**The all-caps exemption.** "LEA", "ADA", "IDA", "REED" and "TEA" are also
given names. The list stores them as case-sensitive acronyms, so protecting
"LEA" cannot shelter "Lea". The case rule is the guard. These strings are
graded `low`, not `high`. The same rule covers postal codes that are also
special-education acronyms: "ID", "MD", "HI", "VI" and "PR" (percentile
rank) are protected only in capitals and are never read as places on their
own.

**Household names always win.** A tool using SPEDLex should pass in the names
of the people in the document. The matcher drops any safelist string that
contains one. A child named Braille or Georgia is still redacted.

**Months next to numbers are never protected.** Some acronyms are spelled
like a month: "APR" is the Annual Performance Report, and also April. The
matcher skips any match that is a month name or abbreviation when a number
sits directly before or after it ("APR 14, 2015", "14-APR-15", "APR 2015"),
because that is a date and may be a date of birth. The rule does not depend
on the record, so a month-shaped acronym added later is covered too. Away
from numbers ("submitted its APR to OSEP") the acronym is still protected.
The cost is that a real acronym next to a year ("FFY 2022 APR") is left to
the scrubber, which may redact it. Over-redaction is the safe direction.

**The safety property, tested on every change.** The matcher never protects
a first name or surname from the reference lists on its own, such as "Rosa"
or "Johnson" written as a name. The only name-shaped strings it protects are
a fixed, reviewed set of all-caps acronyms. A new one fails CI until a
reviewer adds it on purpose. See `tests/test_match.py`.

**What scrubber collisions revealed.** The reference scrubber's first-name
dictionary contained "Virginia", "Florida", "Georgia" and "Carolina". It
redacted the middle of 17 concepts, including the Virginia Alternate
Assessment Program and the Georgia Milestones. That scrubber has since
removed state names from its dictionary. "Rosa" (Rosa's Law) is still a real
collision, and the phrase stays protected. Any scrubber with a first-name
list probably has the same problem. Run the collision report against yours
(see [USING.md](USING.md)).

## 6. Review

| Status | Meaning |
|---|---|
| `machine_validated` | Drawn from regulation text. The build checked the string and citation against that text. |
| `candidate` | Drawn from a PDF or web page by text extraction. A human still needs to check the page reference. |
| `expert_accepted` | A reviewer with special-education expertise confirmed the term is used this way and the citation supports it. |
| `expert_rejected` | A reviewer found it wrong. The record stays in the data so nobody re-adds it, and matching excludes it. |
| `illustrative` | A placeholder showing the shape of a future record. Matching excludes it by default. |

Reviews are recorded in `sources/reviews.tsv`, one row per decision, and the
build applies them. [CONTRIBUTING.md](../CONTRIBUTING.md) explains how to
review.

## 7. Versioning

- **Minor** (0.23.0 → 0.24.0): a new state layer or a batch of new concepts.
- **Patch** (0.23.0 → 0.23.1): corrections, reviews and new strings on existing concepts.
- **Major**: a schema change that breaks existing readers.

Concept IDs are stable across all versions. `version_added` on each record
names the release that introduced it. Each GitHub release is archived on
Zenodo with its own DOI.

## 8. What 19 states showed

- **Procedural vocabulary converges.** The first state (Texas) added 60 new
  concepts. By the eighth, half to two-thirds of what a state uses was
  already in the list. Across the last four, each state added about ten.
  What stays new is each state's agencies, assessments, diplomas,
  credentials and placement names.
- **States rename the federal categories.** Many of the 19 states rename
  emotional disturbance (emotional disability, emotional/behavioral
  disorder, emotional impairment). Several split or rename speech and
  language impairment. Several fold gifted students into the same framework,
  for example Florida's "exceptional student", Kansas's "exceptional child",
  Louisiana's "exceptionality" and Tennessee's "intellectually gifted"
  category.
- **Skill and testing vocabulary is a separate, larger pool.** One pass
  through Texas's assessment guides and Dyslexia Handbook added 84 new
  concepts, almost all reading and writing skills and testing supports.
  Regulations barely touch this vocabulary. Covering it needs instrument
  catalogs and real IEPs.

## 9. Known limitations and biases

- **Coverage.** 19 states at first release (the README lists the current
  ones), not all 50. No Part C (early intervention, 34 CFR Part 303)
  core, no Section 504 core, and no instrument, subtest or score vocabulary
  beyond placeholders.
- **Review.** At first release (v0.23.0), 391 records were unreviewed
  candidates and none was expert-accepted. The README has current counts.
- **Document vintage.** Some state documents are old. Pennsylvania's parent
  guide is from 2008 and Nevada's IEP form is from 2018. Newer program names
  may be missing.
- **Name lists.** The SSA list favors names given to U.S.-born children
  before 2009. Names common among recent immigrant families may be missing.
  That would under-grade risk for a term that collides with one. Broader
  lists are welcome.
- **English only.** Spanish-language notices and IEPs aren't covered.
- **Regional tags aren't exhaustive.** A form tagged to Texas is known to
  appear in the Texas documents that were read. Other states may use it,
  and nothing is known about states not yet covered. Tools that say "this
  is another state's term" should treat that as a hint.
- **Currency isn't tracked.** The list aims to cover terms likely to appear
  in documents, not to say which are legally current. `legacy` and
  `disfavored` are recorded when a source or a law makes the change clear,
  and both are incomplete.
- **No definitions.** Records name concepts and cite sources; they don't
  define them. AI tools that use the list should send people to the cited
  source for meaning.
- **Field use.** The list records terms from official documents. How
  teachers actually write ("sped", "resource room", "push-in") comes later,
  from a corpus.
