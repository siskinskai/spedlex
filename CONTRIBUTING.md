# Contributing to SPEDLex

SPEDLex is an open, cited vocabulary of U.S. special-education terms.
De-identification tools use it to remove a child's personal information from
IEPs, evaluations and other special-education documents. The terms that give
those documents meaning stay in, so caregivers can use AI tools safely. The
[README](README.md) has the full background.

Thank you for helping. SPEDLex is only as good as the people who check it.
Most of the useful work involves no code.

**One rule above all: never paste real student information** into an
issue, pull request or commit: no names, IEP excerpts with identifiers,
school names or dates of birth. Describe the term and cite a public document.

## Ways to help

| You are... | You can... | How |
|---|---|---|
| A special educator, school psychologist, SLP, advocate or parent | Confirm or reject terms | [Reviewing records](#reviewing-records) |
| Anyone who spotted a problem | Report a wrong, missing or risky term | Issue forms: *Report a wrong term*, *Suggest a term* |
| Comfortable reading state documents | Add a state | [Adding a state](#adding-a-state) |
| A developer | Port the matcher, add an adapter, improve the build | [Development](#development) |

## Using an AI model

You're welcome, and expected, to use one. SPEDLex itself was started with
Claude Opus 5.5. Whatever model you use:

- **You're responsible** for what you submit. Read the draft against the
  documents before opening a pull request.
- **Record it.** Set `ASSISTED_BY` in your layer module (e.g.
  `"claude-opus-5-5"`, `"gpt-5"`, `"gemini-2.5-pro"`, or `"none"`) and name
  the model in your pull request.
- **Use the shared prompts** in [prompts/](prompts/): `add-state.md` to
  draft, `audit-layer.md` to check the draft with a different model or a
  fresh chat, and `precheck-review.md` to gather evidence for a review.
- **Give the model the documents.** Don't let it work from memory.
- **Models don't review.** Only people add rows to `sources/reviews.tsv`.

If a prompt let you down, fix it: see [prompts/README.md](prompts/README.md).
Coding agents working in the repository follow [AGENTS.md](AGENTS.md).

## Cite sources; don't copy them

SPEDLex cites documents. It never redistributes them.

**Why.** Many state guides and every advocacy-group document are copyrighted
by their publishers. Git history is permanent: a PDF committed once is
downloaded by everyone who clones the repository, forever, even after it is
deleted. And GitHub keeps every pull request permanently, even if it is closed
without merging.

**How.**
1. Save the documents you read in `.sources-cache/<xx>/` (git ignores it).
2. Add a row for each to `sources/documents.tsv`: its URL, the date you read
   it, its SHA-256 hash (`shasum -a 256 file.pdf`), and a Wayback Machine
   snapshot (save the URL at https://web.archive.org/save/).
3. Cite it in your layer module with its `doc_id` and a page or paragraph.
4. Put your layer report and audit in `provenance/<xx>/`.
5. Anyone can then get your sources with `python tools/fetch_sources.py`.

**If you committed a source document by accident:** don't delete it in a new
commit; that leaves it in the history. If you haven't pushed, undo the
commit (`git reset --soft HEAD~1`), unstage the file, and commit again. If
you have already pushed or opened a pull request, close it, don't push
again, and tell a maintainer in a new issue (without attaching the file).

## Development

```bash
git clone https://github.com/SiskinSkai/spedlex && cd spedlex
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
python -m spedlex.build --check   # data matches sources
pytest                            # invariants and matcher rules
```

Recommended: `pip install pre-commit && pre-commit install` stops a source
document at commit time. It is a convenience; the real guard is
`tests/test_repo_hygiene.py`, which runs in `pytest` and in CI.

`data/` and `docs/SOURCES.md` are **built**. Never edit them by hand: edit
`sources/`, run `python -m spedlex.build`, and commit the sources and the
rebuilt outputs together. CI fails if they disagree.

## Adding a state

Plan on a few hours to a weekend, depending on the state. You will read
three documents carefully.

**1. Claim it.** Open an *Add a state* issue so two people don't do the same
state.

**2. Find the three core documents.**

- The state's **procedural safeguards notice** (sometimes called Parent
  Rights or Notice of Procedural Safeguards). It's required by
  34 CFR 300.504, so every state has one.
- Its main **parent guide or IEP manual**.
- Its **special-education rule**, especially definitions and eligibility
  categories. Cornell LII and Justia mirror most state codes.

Add the state's alternate assessment and diploma pages if they name
programs. If a document can't be read, use an official mirror, a district's
copy of the same state document, or an older edition, and say so in the
module docstring.

**3. Copy the template.**

```bash
cp sources/states/_template.py sources/states/<state>.py
```

Fill in the docstring (every document, its date, and anything you couldn't
read), the `src()` helper, `JURISDICTION`, `LAYER_NAME`, `RETRIEVED` and
`ASSISTED_BY`.

Save each document in `.sources-cache/<xx>/` (never in the repository), add
one row per document to `sources/documents.tsv`, and put the row's `doc_id` on
every source `src()` returns. A document you saved but no record cites is
listed in the module's `UNCITED_DOCS` with the reason.

Using a model? Give it [prompts/add-state.md](prompts/add-state.md), the
template, an example layer, `data/spedlex.csv` and the documents (from
`.sources-cache/<xx>/`). It drafts
steps 3 and 4 for you. Then check the draft with
[prompts/audit-layer.md](prompts/audit-layer.md) in a fresh chat or a
different model, and read every new concept against its document yourself.

**4. Record what the state uses.** For each term in the documents:

- If it names something **already in the list**, add a `STRINGS` entry with
  the existing concept's key (the `key` column of `data/spedlex.csv`). Add
  any new surface forms with a regional tag:
  `("ed", [("emotional disability", S, XX)], src("RULE", "(3)"))`.
  An empty list just records that the state attests the concept.
- If it's **new**, add a `CONCEPTS` entry: a new key, the preferred term, a
  category, strings, a source, and options. Use `jurisdiction` if it exists
  only in this state, `broader` for a parent concept, and `flags` such as
  `"eponym"` or `"place_name"`.

Guidelines:

- Cite down to the paragraph or page.
- Acronyms are type `A` (`acronym`). They match case-sensitively.
- Keep legacy terms the documents still use, typed `L`.
- Never add single letters, person names on their own, or school or
  district names. A program named after a person (the Carson Smith
  scholarship) is fine as the full phrase, with `flags: ["eponym"]`.
- If an acronym already means something else in another state, tag both
  uses with their states. The build reports the ambiguity.

**5. Build and check.**

```bash
python tools/add_state.py <state>
pytest
```

`add_state.py` does five things:

- Adds the layer.
- Bumps the version in the package, `pyproject.toml` and `CITATION.cff`.
- Gives new concepts permanent IDs.
- Rebuilds the data, including the README's stats table.
- Prints how many concepts the state attested, how many are new, and any
  high-risk strings to double-check.

If the build fails, the script rolls its changes back. Fix the module and
run it again.

**6. Open a pull request** with `sources/states/<state>.py`,
`sources/states/__init__.py`, `sources/documents.tsv`, `data/`,
`docs/SOURCES.md`, `README.md`, the version bump, your layer report and audit
in `provenance/<xx>/`, and a CHANGELOG line. Never include the documents
themselves. You can also add a state card and a
comparison-table column to `site/template.html`.

## Reviewing records

Reviewing means confirming two things: that the term is really used this
way in special education, and that the cited source supports it.

1. Pick records with status `candidate` (the explorer can filter by state, so
   start with your own).
2. Open the citation and check the term appears as recorded.
3. Add a row to `sources/reviews.tsv`, tab-separated:

   ```
   concept_id	decision	reviewer	date	note
   SPED:000157	accept	your-github-handle	2026-10-15	on p. 1 of the Jan. 2025 notice
   ```

   `decision` is `accept` or `reject`. A reject needs a note saying why. The
   build enforces this.
4. Run `python -m spedlex.build` and open a pull request, or, if you'd rather
   not touch files, list your decisions in a *Review records* issue and a
   maintainer will add them.

One accept makes a record `expert_accepted`. Any reject makes it
`expert_rejected` until the disagreement is resolved. In your first pull
request, say briefly what your special-education background is, so
maintainers can weigh reviews.

**Prefer email?** Maintainers can send a state's open questions to experts as
a plain-text email, and reviewers just reply. See
[outreach/expert-review/](outreach/expert-review/README.md). Reviewers who opt
in are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md); you can ask to be added
to it whichever way you review.

## Changing an existing record

Edit the module that defines it: `sources/federal.py` for the federal core,
or the state module that added it (`version_added` and the first source
tell you which). Never change a concept's key or delete it outright. To
remove a concept, delete its entry and mark its row `retired` in
`data/concept_ids.tsv` (the one hand edit allowed in `data/`). Its ID is
never reused.

## Pull request checklist

- [ ] No real student information anywhere
- [ ] No source documents or text extracted from them (PDFs, Word files, saved pages, OCR text); new sources are rows in `sources/documents.tsv`
- [ ] Any AI model used is named in `ASSISTED_BY` and in the pull request
- [ ] `python -m spedlex.build --check` passes
- [ ] `pytest` passes
- [ ] New sources are cited to the page or paragraph, with URLs
- [ ] CHANGELOG.md updated

## Conduct

Everyone participating agrees to the [Code of Conduct](CODE_OF_CONDUCT.md).
