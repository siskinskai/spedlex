<!--
prompt: audit-layer
version: 1.1 (2026-10-09)
changes in 1.1: also checks doc_id against sources/documents.tsv and that no source file or long extract is in the change;
  the audit goes to provenance/{{xx}}/
tested with: none yet. Please report results in your pull request.
improve it: see prompts/README.md
-->

# Instructions: independently check a drafted state layer

Use this **after** a layer has been drafted (by a person or a model) and
**before** opening a pull request. It works best with a different model, or
at least a fresh conversation that never saw the drafting, so the work
isn't grading itself. Maintainers may run it on incoming pull requests too.

Copy everything below the line. Attach the drafted module, the same
documents it cites, and `data/spedlex.csv`.

---

You are auditing a drafted SPEDLex state layer: a Python module that lists
special-education terms from a state's documents, each with a citation.
SPEDLex is used by de-identification tools to protect special-education
terms while removing a child's personal information, so an invented term or
a term that could shelter a person's name is a real privacy risk.
You did not write it. Assume nothing in it is correct until you've checked
it against the attached documents.

## Inputs

- `MODULE`: the drafted `sources/states/<state>.py`.
- `DOCS`: the documents the module cites.
- `KEYS`: `data/spedlex.csv`, the concepts that already exist.

## Check every entry

For each entry in `STRINGS` and `CONCEPTS`:

1. **Is it there?** Find the term in DOCS at the cited page or paragraph.
   Verdict: `confirmed` (found at the citation), `misplaced` (found, but
   elsewhere: give the right citation), or `not_found`.
2. **Is it mapped right?** For STRINGS, is it really the same concept as
   the existing key in KEYS? For CONCEPTS, does an existing key in KEYS
   already cover it (a duplicate)?
3. **Is it safe?** Flag any string that is, or contains as a standalone
   word, a person's first name or surname, a place name, or a school or
   district name. Also flag any single letter and any eponym without
   `flags: ["eponym"]`.
4. **Is it typed right?** Acronyms are `A`. Outdated forms still in use are
   `L`. State-only strings carry the state's regional tag.

Then check the whole module:

- Terms the documents clearly use as special-education concepts that the
  module missed (list up to 20, most important first, with citations).
- Docstring accuracy: are the documents, dates and gaps described correctly?

## Output

1. A table: entry key | term | verdict | correct citation (if misplaced) |
   problem (mapping, safety, type) | evidence (a quote of 15 words or fewer).
2. Missed terms, with citations.
3. A short summary: counts of confirmed, misplaced and not_found, and the
   three most important fixes.

Also check the change against the manifest:

- every source's `doc_id` has a row in `sources/documents.tsv`, with the
  right jurisdiction, and no row is left without a citation or an
  `UNCITED_DOCS` entry;
- no source file (PDF, Word file, saved page, OCR text) and no long extract
  of source text appears anywhere in the change. Report any you find.

Save your audit as `provenance/{{xx}}/{{xx}}-layer-audit-<date>.md`.

Only report what you can point to in DOCS. If a document is unreadable or
missing, say which entries you therefore couldn't check rather than guessing.
