<!--
prompt: setup-guided-review
version: 1.0 (2026-11-23)
written for: a coding agent working in this repository (Claude Code or similar)
tested with: none yet
improve it: see prompts/README.md
-->

# Instructions: set up a guided review process for the maintainer

You are setting up, and then running, a review process that walks the
SPEDLex maintainer through each review task **one step at a time**. Your
job is to prepare evidence, present one decision at a time, record exactly
what the maintainer decides, and carry out the mechanical steps afterward.
You never make a review decision yourself.

Read this whole file before you change anything. Where it says **ask**,
stop and ask the maintainer. Don't guess.

---

## 1. Who you're working for

- **The maintainer is Jeremy Evans.** His strength is careful legal review
  and research: reading a cited document at a pinpoint and judging whether
  it supports a record. He is not working through special-education experts.
  He has asked to be walked through each step, not handed a manual.
- **He decides; you record.** You may find the term, quote it briefly, say
  what you notice, and draft a note for him to approve. He picks the result.
- **Keep each step small.** Show one record, give him what he needs to
  decide, then ask one question. Don't present ten records at once.
- **Use plain words.** Say "the cited page" and "the record", not
  internal jargon, unless he uses it first.

## 2. Read these first, in this order

1. `AGENTS.md`: the hard rules. They override anything here.
2. `CONTRIBUTING.md`, sections "Checking sources" and "Reviewing records".
3. `docs/METHODOLOGY.md` §6 (Review): what each status means.
4. `tools/verify_queue.py`: the worklist and apply tool you'll build on.
5. `prompts/precheck-review.md`: the existing evidence-gathering prompt.
   Your per-record evidence step is a stricter version of it.
6. `provenance/verification/s504-split-2026-11-23.md`: a completed worked
   example of a problem found during review, turned into a proposal, decided
   by the maintainer and applied. Copy its shape for future problems.

## 3. Facts about the environment (check each; don't assume)

- **Repository:** `/Users/joevans3/SpedLex-Vault` on the maintainer's Mac,
  GitHub remote `SiskinSkai/spedlex`.
- **Branches:** work up to 2026-11-23 is on `split-section-504` (commits
  `8bc254f` source checks and skill, `acb154a` Section 504 split, v0.53.0).
  It may have been pushed and merged by the time you start. Run
  `git fetch origin` and `git log --oneline -5 origin/main` and branch from
  the newest base. **Ask** if unsure which branch to use.
- **Python:** use the repo's virtual environment directly:
  `.venv/bin/python -m spedlex.build --check` and
  `.venv/bin/python -m pytest -q`. Homebrew's Python blocks `pip install`
  outside a venv, and `pip install -e` has failed for him before; don't
  rely on it. If `.venv` is broken, rebuild it with `python3 -m venv .venv`
  and `.venv/bin/python -m pip install "jsonschema>=4.18" "pytest>=7"`.
- **If you run in a sandbox or VM rather than on the Mac:** `git push` is
  usually blocked there. Commit, then give the maintainer the exact
  Terminal commands to push. Git may also need permission to delete its own
  lock files; ask for it once if `git` fails with "Operation not permitted".
- **The repository sits inside an Obsidian vault.** Obsidian sometimes adds
  a `[[SpedLex]]` line to the top of Markdown files. Never commit it. A test
  (`test_no_note_app_wikilinks_in_tracked_markdown`) catches it; remove the
  line with `git restore <file>` if the file has no other changes.
- **Local copies of source documents** are in `.sources-cache/<xx>/`, which
  git ignores. As of 2026-11-23 copies exist for AK, AL, AR, AZ, CO, CT, DC,
  DE, HI, IA, IN, KY, MD, ME, MI, MS, NC, NH, NJ, NM, OH, US, VA, WV and WY.
  The early layers (CA, FL, GA, ID, IL, KS, LA, MA, MN, MO, NV, NY, OR, PA,
  TN, TX, UT, WA) have **no local copy**. Read those at the URL in their
  layer module (`sources/states/<state>.py`), and label that evidence
  "online" when you show it. Check `sources/documents.tsv` (`local_name`)
  rather than trusting this list.
- **Page numbers:** citations say either "p. N" (printed page) or "PDF p. N"
  (page index in the file). They can differ by several pages. Maine's
  "p. 2", for example, is PDF page 9. When the term isn't on the expected
  page, search nearby pages and report which page it's actually on.

## 4. The review functions, in order of priority

Set up and run them in this order. Each one ends with a check that the
build still passes.

| # | Function | What the maintainer decides | Where it's recorded |
|---|---|---|---|
| A | **Source checks** (the main loop) | For one citation: is the term there, naming this concept? `verified` or `problem` + note | Worklist CSV, then `sources/verifications.tsv` via `tools/verify_queue.py apply` |
| B | **Problem resolution** | How to fix each problem from A: correct a page, fix or move a string, or split a merged record | Layer modules in `sources/states/`, plus a proposal file in `provenance/verification/` for anything bigger than a one-line fix |
| C | **Wrap-up** | Approve the batch | Rebuild, test, CHANGELOG, commit; push instructions |
| D | *(Optional, ask first)* **Name-pair "judge" items** | Same concept, different, or related? | `sources/name_pair_triage.tsv`, 125 rows marked `judge` |

**Not part of this process:**
- `expert_accepted`/`expert_rejected` (`sources/reviews.tsv`): those are for
  special-education professionals. Never write to that file.
- Adding rows to `sources/disfavored.tsv`: only when he asks, with a cited
  legal basis (AGENTS.md).

## 5. What to build (setup)

Do these once, on a new branch named `guided-review`. Show the maintainer
the result of each before moving on.

### 5.1 An evidence helper: `tools/review_evidence.py`

A small, standard-library script (it may call `pdftotext`/`pdfinfo` if
they're installed, and must say clearly if they aren't). Given a concept ID,
or a worklist CSV and row number, it should:

1. Load the record from `data/spedlex.jsonl` and pick the citation the
   worklist row names (column `citation`).
2. Find the document: `doc_id` → `sources/documents.tsv` → `local_name` in
   `.sources-cache/<xx>/`. If there's no local copy, print the URL and the
   words `NO LOCAL COPY: read online` and stop.
3. Work out the page. Handle "p. N", "PDF p. N", "pp. N-M" and section
   citations ("Section I(2)", "§ 3010.7"). For a printed page, look for a
   matching page header or footer in a few PDF pages around N.
4. Search that page for every form in the record (case-insensitive;
   allow for line breaks inside a phrase). If none are found, search ±3
   pages, then the whole document, and report where the term actually is.
5. Print a short report **to the screen only**: page found on, which forms
   matched, and up to three lines of context per match.

Rules:
- **Never write extracted source text to a file**, and never paste long
  passages into anything committed. AGENTS.md forbids committing source
  text. Showing a few lines on screen during review is fine.
- Add tests in `tests/test_review_evidence.py` for the citation parsing
  ("p. 19", "PDF p. 35", "pp. 115-118", "Section I(2), p. 2"). Don't make
  the tests depend on `.sources-cache` being present.
- Optionally make it `python tools/verify_queue.py evidence <csv> <row>`
  instead of a new file; ask which he prefers.

### 5.2 A session script: `prompts/guided-review.md`

Model-neutral instructions any agent can follow to run a review session
(the flow in section 6). Add it to the table in `prompts/README.md`, with
"Who decides: the maintainer (source checks) / a person (all review)".

### 5.3 A one-command start (ask first)

**Ask** whether he wants a personal skill (for example `spedlex-review`)
so he can start a session by name. If yes, and the environment offers a
skill-proposal tool, propose a skill whose instructions are: "Run the
guided review session in `prompts/guided-review.md` in the SpedLex-Vault
repository." Don't write skill files to disk yourself.

### 5.4 One clarification to CONTRIBUTING (ask first)

A source check is recorded on the whole record, but checks one citation.
Propose adding a fourth item to what `verified` means in
CONTRIBUTING.md, "Checking sources": *nothing in the forms column
obviously names a different thing* (a plan vs. the law, a team vs. a
meeting). This is what caught the Section 504 problem. Add it only if
he agrees.

### 5.5 Refresh the worklist

The worklist `provenance/verification/queue-2026-11-23.csv` predates the
0.53.0 split (its row 4 describes the old, merged Section 504 record). Run
`python tools/verify_queue.py queue` for a fresh one. Keep the old file; it
shows what was queued then. **Ask** whether he wants to work through the
national ranking (default), one state (`--state TX`), or a fixed number.

## 6. The session flow (what "walk me through it" means)

### 6.1 Start of session (2-3 short messages)

1. **Where things stand.** One short table from `data/stats.json`
   (`by_review_status`), plus the worklist in use and how many rows have a
   `result` filled in. Read the CSV to count; don't remember it.
2. **Set the session.** Ask, with options: how many records this
   session (5 / 10 / 20, default 10), and whether to continue the current
   worklist or start a new one.
3. **Pre-check the batch silently** before showing the first record: run
   the evidence helper on each row, so each step is instant. Pre-checking
   is preparation, not a decision.

### 6.2 One record at a time

For each row, send one message shaped like this:

```
Record 3 of 10 · rank 7 in the worklist
SPED:000207  Expedited due process hearing  (discipline; cited by 25 jurisdictions)
Forms to look for: Expedited due process hearing | expedited hearing
Citation: OSSE IDEA Part B Notice of Procedural Safeguards (rev. Aug. 2018), p. 36
Document: .sources-cache/dc/... (local copy)

What I found: on p. 36, "expedited due process hearing" appears in the heading
of the discipline section. Short quote: "...[under 15 words]..."
Anything to look at: none / the term is on p. 37, not 36 / a listed form
names something else / the document is from 2018 (check it's current)
```

Then ask **one** question, with these options (use a multiple-choice tool
if you have one):

- **Verified**: the term is at the cited page, naming this concept.
- **Problem: wrong page**: the term is in the document, on another page.
- **Problem: a form names something else**: the record merges concepts,
  or a form is wrong.
- **Problem: other**: he types what's wrong.
- **Skip for now.**
- **Stop the session.**

For any problem, draft a one-line note (for example "Term is on p. 37, not
p. 36" or "'504 plan' is the plan, not the law; split") and **ask him to
approve or edit it.** Never write a note he hasn't seen.

Record his answer **immediately** in the worklist CSV: `result`
(`verified` or `problem`) and `note`. Write exactly what he chose. Saving
after every record means a session can stop at any time without losing
work. The CSV is the session's state; no other file is needed.

If he asks to see the page himself, give him the local path and page
number (or the URL). If you're on his Mac, open the PDF for him.

### 6.3 End of session

1. **Summarize** in one short table: verified / problem / skipped.
2. **Dry run:** `python tools/verify_queue.py apply <csv> --verifier
   "Jeremy Evans"`. It writes `<csv>.proposed-verifications.tsv` and
   checks every row. Show him the counts and any errors.
3. **Ask** "Add these to the record?" Only on a yes, run it again with
   `--append`, then `python -m spedlex.build`, then the build check and
   tests. Show the new status counts.
4. **Problems found:** list them and offer function B (section 7) now or
   next time.
5. **Offer** function C (wrap-up).

## 7. Problem resolution (function B)

Walk the problems one at a time, the same way. For each, say which kind it
is and what the fix would be, then ask.

| Kind | Fix | Size |
|---|---|---|
| Wrong page | Change the page in the record's source in its layer module (`version_added` and the first source tell you which module). Then queue the record again for a fresh check. | One line |
| Wrong or missing form | Edit the string in the layer module that adds it. Cite the document that actually has it. | One line |
| Unsupported form | The cited document doesn't contain the string. Move it to a layer whose document does, or remove it. | Small |
| Merged concepts | Write a proposal like `s504-split-2026-11-23.md`: a citation-by-citation table, the proposed records and a numbered list of decisions. Implement only after he decides. | Large |

Rules for fixes:
- **Never change or reuse a concept ID.** A split keeps the old ID for one
  meaning and registers new IDs (`python -m spedlex.build --register`).
- New concepts added to an existing layer module set
  `"version_added": "<next minor version>"` in their opts, and the package
  version is bumped in `spedlex/__init__.py`, `pyproject.toml` and
  `CITATION.cff` (METHODOLOGY §7: new concepts are a minor version;
  corrections alone are a patch).
- A layer can only refer to concepts defined by itself or an earlier layer
  (order: `sources/states/__init__.py`, `LAYERS`). Within one module,
  `STRINGS` is applied before `CONCEPTS`.
- If a test about `sources/name_pair_triage.tsv` fails after a fix, update
  the affected row to record his decision (see the Texas IAP row from
  2026-11-23). Don't delete rows.
- Record the change in `CHANGELOG.md` under `[Unreleased]`, and name the
  model.

## 8. Wrap-up (function C)

1. `git status`: show what changed. Remove any `[[SpedLex]]` lines.
2. `python -m spedlex.build --check` and `pytest -q` must both pass.
3. Stage files **by name** (never `git add .` or `-A`). Commit with a
   message that names the model, after he says to commit.
4. Push only when he says so. If pushing is blocked, give him the exact
   Terminal commands, including `gh pr create`, and remind him to name the
   model in the pull request.

## 9. Function D: name-pair judge items (optional)

`sources/name_pair_triage.tsv` has 125 rows marked `judge`. Each asks
whether a state's name (for example a state's term for the IEP team) is the
same concept as the federal one, a different one, or related. They were set
aside for experts, but many can be decided from the state's own documents.
**Ask** whether he wants to take these on. If yes, use the same
one-at-a-time flow with options *same / related / different / leave for
an expert*. His decisions change the triage file's decision column and,
for *related*, the string's type in the layer module. Run the tests after
each batch.

## 10. Hard rules (repeat of AGENTS.md, plus this process)

- Never decide a review result, and never write `result` or `note` without
  his explicit choice in the same conversation.
- Never write to `sources/reviews.tsv`. Write to `sources/verifications.tsv`
  only through `verify_queue.py apply --append`, after his yes.
- Never invent a term, page or citation. If you can't find it, say
  "couldn't find it" and show where you looked.
- Never commit source documents or extracted text. Quotes shown to him
  stay under 15 words.
- Never put student information anywhere.
- Never weaken a test to make a change pass. If an all-caps acronym
  collides with a name, stop and tell him.
- Label every piece of evidence as "local copy" or "online", and every page
  as "printed" or "PDF".

## 11. Done when

- `tools/review_evidence.py` (or the `evidence` subcommand) works on a local
  copy and on an online-only source, with tests passing.
- `prompts/guided-review.md` exists and is listed in `prompts/README.md`.
- A fresh worklist exists.
- **A pilot session of three records** has been run with the maintainer,
  end to end: evidence → his decision → CSV → dry-run apply → (on his yes)
  append → rebuild → tests.
- He has answered the questions in 5.3, 5.4 and 5.5.
- The work is on the `guided-review` branch, committed only if he said
  so, with push instructions given if pushing was blocked.

Finish by telling him what you built, what you couldn't verify, and the
one command or phrase that starts the next session.
