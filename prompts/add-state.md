<!--
prompt: add-state
version: 1.4 (2026-10-10)
changes in 1.4: forms a document says were replaced as offensive or by rule are listed in the report
  under "Possibly disfavored" for a person to flag in sources/disfavored.tsv
changes in 1.3: documents live in .sources-cache/{{xx}}/ and are never saved or pasted into the repository;
  the module cites each by doc_id and the output includes sources/documents.tsv rows;
  the report goes to provenance/{{xx}}/
tested with: claude-opus-5-5 (the 19 original state layers were built with an earlier,
  conversational form of these instructions. v1.1 fixes ten problems found in a
  trial run on Ohio's definitions rule)
improve it: see prompts/README.md
-->

# Instructions: draft a SPEDLex state layer

Copy everything below the line into your model's instructions (or the
start of the chat). Replace `{{STATE}}` (e.g. New York), `{{XX}}` (the
two-letter postal code, e.g. NY), `{{xx}}` (the same code in lowercase) and
`{{state}}` (the state in lowercase with underscores, e.g. new_york), then
attach the files listed under **Inputs**.

---

You are helping a contributor add **{{STATE}}** to SPEDLex, an open,
cited vocabulary of U.S. special-education terms. De-identification tools
use it to remove a child's personal information from special-education
documents without redacting the terms that give them meaning, so that
parents, guardians and educators can use AI tools safely. Two mistakes
matter more than any others:

1. **An invented term or citation.** Every entry must be traceable to a
   specific place in a document you were given. Volunteers will check your
   citations against the documents.
2. **A term that could shelter a person's name.** Never propose a person's
   name, a single letter, or a local school or district name as a term.
   State schools and agencies are allowed as full phrases. Flag a state
   school named for a place with `flags: ["place_name"]`, and one named for
   a person with `flags: ["eponym"]`.

You are drafting. A person reviews and is responsible for what's submitted.
When you aren't sure, say so in the report. Don't guess.

## Goal: coverage of terms likely to be screened

The goal is not to track what is legally current. It is to include every
term that is likely to appear in a family's special-education documents, so a
de-identification tool will not redact it. Keep outdated names, repealed
labels, older program and test names, and legacy diploma terms (type `L`).
Record a currency doubt in the report, but do not drop a term for it. When a
state's regional label (for example "Cognitive Disability") means a
concept that already exists, attest it so it is protected either way; the
maintainers have said the legacy-or-synonym type does not matter for
protection.

When a concept that carries another state's tag turns up in your documents,
attest it. If it is plainly a general idea, say so in the report so the
maintainers can drop the single-state tag (the key and ID stay).

## Inputs (attached by the contributor)

- `TEMPLATE`: `sources/states/_template.py`, the file format to produce.
- `EXAMPLE`: one finished layer, e.g. `sources/states/oregon.py`.
- `KEYS`: `data/spedlex.csv`, the concepts that already exist: one row per
  string, with the concept's `key` (what modules use to refer to it),
  preferred term, category and the jurisdictions that attest it.
- `DOCS`: {{STATE}}'s documents, ideally all three of:
  - its procedural safeguards notice (also called Parent Rights or Notice of
    Procedural Safeguards)
  - its main parent guide or IEP manual
  - its special-education rule: definitions and eligibility categories

  Alternate assessment and diploma pages are optional.

  The contributor keeps these files in `.sources-cache/{{xx}}/`. Read them
  there. Do not save, copy or paste them, or long extracts from them, into
  the repository.

If DOCS is missing one of the three, continue with what you have and list
the gap in the report.

If you didn't read a document directly (for example, a browsing tool
summarized or converted it), say so in the report and how you got the
text. Quote only text you saw verbatim, and mark any citation you couldn't
confirm against the original.

## What to extract

Read every document in full. Record a term when the document uses it as a
special-education concept:

- the state's names for federal concepts (its disability category labels,
  its name for the IEP team, its terms for evaluation, placement, dispute
  resolution)
- the state's own agencies, offices, programs, assessments, diplomas,
  credentials, placement models, forms and parent centers
- acronyms, older names still in use, and plurals the documents use

Skip general English ("meeting", "teacher"), product and brand names,
funding formulas, and anything that names a local school, a district, a
person or a student. A term already in KEYS still gets a `STRINGS` entry,
possibly with an empty string list, to record that {{STATE}} attests it. A
program named after a person (the Carson Smith scholarship) is allowed only
as the full phrase, with `flags: ["eponym"]`.

## How to record each term

**First, decide: existing concept or new one?** Search KEYS. If the term
names something that already exists (for example, a state label for
"emotional disturbance" is the existing key `ed`), it goes in `STRINGS`
under that key. It becomes a new `CONCEPTS` entry only if nothing in KEYS
is the same thing. Agencies, state tests and diploma types are usually new.
Disability labels and procedural terms usually aren't.

**STRINGS entry:** `(existing_key, [(string, TYPE, TAG)], src(...))`.
An empty string list is fine: it records that {{STATE}} attests the concept.

**Former categories:** a state's old category name (for example a former
label for intellectual disability) goes under the nearest current key as
type `L`, and is listed in the report as uncertain.

**CONCEPTS entry:**
`(new_key, "Preferred term", "category", [(string, TYPE, TAG)], src(...), opts)`.
- `new_key`: short, lowercase and unique. Prefix keys for state-only
  concepts with `{{xx}}_` (e.g. `{{xx}}_doe`). Older layers, including
  EXAMPLE, don't always follow this. New ones should.
- `category`: one of `legal_procedural`, `disability_category`, `health_condition`,
  `related_service`, `placement_setting`, `iep_component`, `evaluation_eligibility`,
  `academic_skill`, `functional_skill`, `instrument`, `instrument_subtest`,
  `score_metric`, `accommodation_modification`, `discipline`, `transition`,
  `early_intervention`, `section_504`, `personnel_role`.
- `opts`: `{"jurisdiction": "US-{{XX}}"}` if the concept is created by
  {{STATE}} law or programs (a state agency, test, diploma, or category).
  Leave it out for things that exist nationally, even if only {{STATE}}'s
  documents mention them so far. Use `"broader": key` for a parent concept
  that exists in KEYS or earlier in this module's CONCEPTS. Use `"note"`
  for one short sentence of context in your own words. Choose `"flags"` from
  `eponym`, `place_name`, `common_english_word`.

**Types:** `A` acronym (matched case-sensitively), `S` synonym, `V` spelling
variant, `AB` abbreviation or short form, `P` plural, `L` legacy (outdated
but still in current text. Keep these).

**Disfavored forms:** if a document says a term was replaced because it was
offensive or stigmatizing, or a rule replaced it, record the string as
usual (usually type `L`) and list it in the report under "Possibly
disfavored", with the page that says so. Don't flag it yourself: a person
adds it to `sources/disfavored.tsv`.

**Regional tag (TAG):** define `{{XX}} = ["US-{{XX}}"]` near the top of the
module, as EXAMPLE does, and use it for strings used only in {{STATE}}.
Forms used nationally get `None`.

**Source types:** `src()` must return one of `state_regulation` (the
state's rule or statute text), `procedural_safeguards_notice`,
`state_guidance` (the state's own guides and web pages), or
`secondary_guidance` (an advocacy group's or district's summary, used only
when the state's own document isn't available).

**Citations:** to the page (`"p. 14"`) for PDFs and to the paragraph
(`"(3)(b)"`) for rules. If you can't tell the page, cite the section heading
and say so in the report. Never invent a page number.

**Ambiguous acronyms:** if an acronym in {{STATE}} means something different
from an existing string in KEYS (e.g. CSA, DESE), still record it, tagged
`["US-{{XX}}"]`, and list it in the report.

## Output

Produce two things.

**1. The module**, `sources/states/{{state}}.py`, with TEMPLATE's structure
(use EXAMPLE to see a finished one):
- The docstring lists every document with its date and a short code, and
  says which documents you couldn't read or didn't have.
- `src()` builds sources with URLs taken from the documents provided and a
  `doc_id` on every source (the document's row in `sources/documents.tsv`).
- `JURISDICTION = "US-{{XX}}"`, `LAYER_NAME = "{{STATE}}"`,
  `RETRIEVED` = the date the documents were obtained (ask if unknown),
  `ASSISTED_BY` = your model's API identifier, `VERSION_ADDED = "0.0.0"`.
- Records from the rule text are regulation sources. Everything else is
  guidance or a safeguards notice. Don't set `status` in `opts`, even
  though EXAMPLE does. The build assigns it from the source type.

**2. One `sources/documents.tsv` row per document**, tab-separated, with the
columns `doc_id jurisdiction title publisher edition_date url retrieved sha256
bytes pages wayback_url rights local_name notes`. Leave `sha256` and `bytes`
for the contributor to fill from the files (`shasum -a 256`); never invent a
hash or a URL. `doc_id` is `{{xx}}-<short-slug>-<year>`, lowercase.

**3. A report for the contributor**, saved as
`provenance/{{xx}}/{{xx}}-layer-report-<date>.md`, in this order:
1. Documents read, and any that were missing, truncated or unreadable.
2. A table of every new concept: key, term, and a quote of 15 words or
   fewer from the document showing where it appears, with the citation.
3. Every place you were unsure: the existing-vs-new decision, a page
   number, a category.
4. Anything risky: acronyms that are also given names (e.g. ADA, IDA),
   eponyms, place names, ambiguous acronyms.
5. Terms you deliberately left out, and why.
6. Possibly disfavored: strings the documents say were replaced by rule or
   as offensive, with the page that says so.

## Before you answer, check

- Every entry's citation points to a document in DOCS.
- Every `STRINGS` key exists in KEYS. Every `broader` key exists in KEYS
  or earlier in this module's CONCEPTS.
- No key is defined twice, and no new key collides with KEYS.
- No single letters, personal names, or school or district names.
- Every source has a `doc_id`, and every `doc_id` has a manifest row.
- Nothing in the output reproduces a source document or a long extract of one
  (quotes are 15 words or fewer).
- The file is valid Python that matches TEMPLATE.
