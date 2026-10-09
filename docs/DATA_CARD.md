# Data card

A summary of the dataset in the format of *Datasheets for Datasets*
(Gebru et al., 2021). [METHODOLOGY.md](METHODOLOGY.md) has the detail.

## Motivation

- **Purpose.** To help caregivers (parents, guardians, and the educators and
  advocates who support them) use AI tools safely with special-education
  documents. Tools that remove a child's personal information before a
  document is shared need to know which words are special-education terms.
  SPEDLex gives them that list, so they can protect the terms without
  sheltering personal names.
- **Gap.** Medicine has the UMLS, MeSH and SNOMED CT. Special education has
  no comparable open, cited, machine-readable vocabulary.
- **Creators.** Started by Jeremy Evans. Contributors maintain it in the
  open.
- **Funding.** None.

## Composition

- **Instances.** At first release (v0.23.0): 685 attested concepts plus 13
  illustrative placeholders. Current counts are in the README and
  `data/stats.json`. Each has at least one surface string (1,768 in total),
  at least one source, and a privacy-risk grade.
- **Coverage.** Federal IDEA Part B regulations and 19 states at first
  release; the README lists the current states. Categories
  run from legal and procedural terms (172 concepts at first release) to
  Section 504 (2). `data/stats.json` has counts by category.
- **Labels.** Category, string type, match rule, regional tags, risk grade,
  review status.
- **Personal information.** None. The dataset holds terms and public
  document citations. Name lists are used during the build to grade risk
  but aren't part of the published records beyond the colliding token
  (e.g., `surname:English`).
- **Splits.** None. The `review.status` field separates reviewed records,
  candidates and placeholders.
- **Known errors.** Candidate records may have wrong page numbers. Some
  sources are older editions or district copies, each noted in the state
  module. See METHODOLOGY §9.

## Collection

- **Sources.** Public federal and state regulations, state procedural
  safeguards notices, parent guides, IEP manuals and assessment pages. Where
  a state document couldn't be read, a few advocacy-group or district
  summaries (typed `secondary_guidance`) fill in. [SOURCES.md](SOURCES.md)
  lists them all.
- **Process.** Documents were read and terms recorded with paragraph or page
  citations. The maintainer built the first release with Claude Opus 5.5
  (`claude-opus-5-5`), which read the documents and drafted records. Later
  contributors use models of their choice. Each source's `assisted_by` field
  names the model (or `none`). See METHODOLOGY §3.
- **Time frame.** Documents retrieved October 2026. Document dates range
  from 2008 to 2026.
- **Consent and ethics.** No human subjects. No IEPs or student records were
  used.

## Preprocessing

- Strings are recorded as written, with acronyms kept case-sensitive.
- No definitions are copied from copyrighted glossaries.
- Risk grading uses three inputs: SSA first names (1880–2008 top 1,000),
  Census 2000 surnames (10,000+ bearers), and the patterns of a reference
  scrubber. The scrubber is SCRUB, an offline de-identification tool for
  special-education documents and the first tool to use SPEDLex.

## Uses

- **Intended.**
  - Protecting special-education terms inside a de-identification pipeline.
  - Terminology research.
  - Cross-state comparison of special-education vocabulary.
  - A seed for NLP over IEPs.
- **Not intended.**
  - As a de-identification tool by itself.
  - As legal advice or an authoritative definition of any term.
  - To decide eligibility, services or placement for any student.
- **Risks.** Protecting a term that collides with a person's name. The
  grading, the household-names rule and CI's safety test exist to prevent
  this. Report any case you find.

## Distribution

- **Where.** GitHub (source and releases), the Python package, and, planned,
  Zenodo (archived releases with DOIs).
- **License.** Data: CC BY 4.0. Code: MIT.
- **Source documents are not redistributed.** The data cites them and records
  each one's URL, SHA-256 hash and an archived snapshot in
  `sources/documents.tsv`; `tools/fetch_sources.py` retrieves them.

## Maintenance

- **Maintainers.** See the GitHub repository.
- **Errors.** Report with the "Report a wrong term" issue form.
- **Updates.** New releases as states are added and records are reviewed.
  Concept IDs never change or get reused.
- **Contributions.** See [CONTRIBUTING.md](../CONTRIBUTING.md).
