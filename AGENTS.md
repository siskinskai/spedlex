# Instructions for AI coding agents

This file is for AI models and coding agents working in this repository
(Claude Code, Codex, Copilot, Cursor and others). People are welcome to
read it too: it's the short version of CONTRIBUTING.md.

## What this repository is

SPEDLex is a cited, privacy-graded safelist of U.S. special-education terms.
De-identification tools use it to avoid redacting terms like "ARD committee"
or "PLAAFP" when they remove a child's personal information from a document,
so that caregivers (parents, guardians, educators, advocates) can use AI
tools with special-education documents safely.

The worst possible bug is a change that lets the safelist protect a person's
name. The second worst is an uncited or invented term.

## Hard rules

- **Never put student information anywhere:** no names, IEP text with
  identifiers, schools or dates of birth, in code, data, tests, commits or
  pull request text.
- **Never invent a term or a citation.** Every entry cites a document the
  person gave you, to the page or paragraph. If you can't see the document,
  ask for it. Don't work from memory.
- **Never edit generated files by hand:** `data/*` (except marking a row
  `retired` in `data/concept_ids.tsv`), `docs/SOURCES.md`, or the README
  block between `<!-- stats:start -->` and `<!-- stats:end -->`. Edit
  `sources/` and rebuild.
- **Never change or reuse a concept ID or key.**
- **Never weaken the safety tests** in `tests/test_match.py` to make a change
  pass. If a new all-caps acronym collides with a name, stop and tell the
  person. Adding it to the known list is a reviewer's decision.
- **Never write to `sources/reviews.tsv` on your own.** It records human
  expert decisions only.
- **Record your involvement.** Set `ASSISTED_BY` in any layer module you
  draft to your model's API identifier.
- **Never commit source documents.** That means PDFs, Word files, saved web
  pages, and OCR or extracted text, and it includes pasting long passages of
  their text into any file. Keep them only in `.sources-cache/<xx>/` (ignored
  by git). Record each document as a row in `sources/documents.tsv`: URL,
  retrieval date, SHA-256 hash and Wayback Machine snapshot. Cite it from the
  layer module by `doc_id`.
- **Stage files by name.** Never run `git add -A`, `git add .` or
  `git commit -a`. Run `git status` and `pytest` before every commit;
  `tests/test_repo_hygiene.py` fails if a source document is tracked.
- **If a source document was ever staged or committed, stop and tell the
  person before pushing.** GitHub keeps every pushed branch and pull request
  permanently, even after the file is deleted, so the only fix is to rewrite
  the branch *before* it is pushed.

## Layout

```
sources/federal.py        34 CFR Part 300 core (SEED) and placeholders (ILLUSTRATIVE)
sources/states/*.py       one module per state layer (_template.py shows the format)
sources/states/__init__.py  LAYERS: the order layers are applied
sources/reviews.tsv       human review decisions
sources/documents.tsv     source manifest: URL, hash and Wayback snapshot of every document read
spedlex/build.py          builds data/ from sources/ and checks it
spedlex/risk.py           privacy-risk grading
spedlex/match.py          reference matcher (Safelist)
spedlex/adapters/         scrubber collision adapters
data/                     built outputs and the permanent ID registry
provenance/<xx>/          layer reports and audits (our own work, not source text)
.sources-cache/<xx>/      local copies of source documents (git ignores it; never committed)
prompts/                  model-neutral instructions for drafting and checking work
```

## Commands

```bash
pip install -e ".[dev]"
python -m spedlex.build            # rebuild data/ after editing sources/
python -m spedlex.build --check    # must pass before you finish
pytest -q                          # must pass before you finish
python tools/add_state.py <state>  # register a new layer, assign IDs, rebuild, report
python tools/fetch_sources.py      # download the source documents into .sources-cache/ and verify their hashes
```

## Common tasks

- **Add a state:** follow [prompts/add-state.md](prompts/add-state.md) to
  draft `sources/states/<state>.py`, then run `python tools/add_state.py <state>`.
  Then run [prompts/audit-layer.md](prompts/audit-layer.md) in a fresh
  context, or ask the person to.
- **Fix a record:** edit the module that defines it (`version_added` and the
  first source tell you which), rebuild, and run the tests.
- **Change matching or risk logic:** update `docs/METHODOLOGY.md` and
  `docs/USING.md` in the same change, and add a test.

## When you finish

Tell the person what you changed, what you couldn't verify, and anything
risky (eponyms, acronyms that are also names, ambiguous acronyms). Remind
them to name your model in the pull request.
