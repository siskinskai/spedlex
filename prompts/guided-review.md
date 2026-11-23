<!--
prompt: guided-review
version: 1.0 (2026-11-23)
written for: a coding agent working in this repository (Claude Code or similar)
tested with: none yet
improve it: see prompts/README.md
-->

# Instructions: run a guided review session

You walk the maintainer through source checks **one record at a time**. You
prepare the evidence, ask one question, record exactly what he chooses, and
run the mechanical steps afterward. You never decide a result yourself.

Read `AGENTS.md` first; its rules override this file. A source check asks
one thing: does the cited document, at the cited page or paragraph, contain
the term, naming this concept? (CONTRIBUTING.md, "Checking sources".)

Use plain words: "the cited page", "the record". Keep each message short.

## Before you start

- Python: use the repo's `.venv/bin/python`. If it isn't usable, see
  `prompts/setup-guided-review.md` §3.
- `.venv/bin/python -m spedlex.build --check` must pass before the session
  starts. If it doesn't, stop and tell him.
- Work on a branch (not `main`). Run `git status`; if the tree has changes
  you didn't make, tell him before going on.

## 1. Start of session

1. **Where things stand.** One small table from `data/stats.json`
   (`by_review_status`), the worklist in use, and how many of its rows have a
   `result` (read the CSV; don't count from memory).
2. **Set the session.** Ask: how many records (5 / 10 / 20, default 10), and
   continue the current worklist or start a new one
   (`python tools/verify_queue.py queue`, optionally `--state TX` or
   `--limit N`; keep older worklists).
3. **Pre-check the batch quietly.** For each unfilled row, in rank order:
   `python tools/review_evidence.py <csv> <rank>`. It prints to the screen
   only. Never save its output to a file.

## 2. One record at a time

Send one message per record:

```
Record 3 of 10 · rank 7 in the worklist
SPED:000207  Expedited due process hearing  (discipline; cited by 25 jurisdictions)
Forms to look for: <the forms column>
Citation: <citation>
Evidence: local copy | online · <printed or PDF page>
File: /Users/joevans3/SpedLex-Vault/<local path>  (or the URL, if online)

What I found: <where the term is, and a quote under 15 words>
Anything to look at: none / term is on a different page / a listed form
names something else / the document looks old
```

Then ask **one** question, as a multiple-choice question if you have a tool
for it:

- **Verified**: the term is at the cited page, naming this concept.
- **Problem: wrong page**: the term is in the document, on another page.
- **Problem: a form names something else**: merged concepts, or a wrong form.
- **Problem: other**: he types what's wrong.
- **Skip for now.**
- **Stop the session.**

Rules for every record:

- Say whether the evidence is "local copy" or "online", and whether a page is
  "printed" or "PDF". Citations like "p. 2" are printed pages and can be
  several PDF pages off.
- If the helper finds nothing, say "couldn't find it" and say where you
  looked. If the evidence is online, read the URL yourself (WebFetch or a
  browser) before presenting it, and label it "online".
- For any problem, draft a one-line note and **ask him to approve or edit
  it**. Never write a note he hasn't seen.
- Save his answer to the worklist CSV **right away**: set `result`
  (`verified` or `problem`) and `note` to exactly what he chose. The CSV is
  the session's state, so he can stop at any time. Edit only those two cells
  of that row (use the csv module, not hand-edited text).
- Always give the **full path** of a local copy as it is on his Mac
  (`/Users/joevans3/SpedLex-Vault/` + the path the helper prints), with the
  page number and whether it is printed or PDF. For online evidence give the
  URL. He needs this to check the page himself.
- If he wants to look at the page himself, give him the path and page number
  or the URL, and open the PDF if you're on his Mac.
- Skipped rows stay blank.

## 3. End of session

1. Summarize in one small table: verified / problem / skipped.
2. **Dry run:** `python tools/verify_queue.py apply <csv> --verifier "Jeremy Evans"`.
   It writes `<csv>.proposed-verifications.tsv` and checks every row. Show
   him the counts and any errors.
3. Ask "Add these to the record?" **Only on a yes**, run it again with
   `--append`, then `python -m spedlex.build`, `python -m spedlex.build --check`
   and `pytest -q`. Show the new `by_review_status` counts.
4. List the problems. Offer problem resolution (below) now or next time.
5. Offer the wrap-up.

## 4. Problem resolution

Walk the problems one at a time. Say which kind it is and what the fix would
be, then ask.

| Kind | Fix | Size |
|---|---|---|
| Wrong page | Change the page in the record's source in its layer module (`version_added` and the first source tell you which). Queue the record again for a fresh check. | One line |
| Wrong or missing form | Edit the string in the layer module that adds it, citing the document that has it. | One line |
| Unsupported form | The cited document doesn't contain the string. Move it to a layer whose document does, or remove it. | Small |
| Merged concepts | Write a proposal shaped like `provenance/verification/s504-split-2026-11-23.md`: a citation-by-citation table, the proposed records, a numbered list of decisions. Implement only after he decides. | Large |

- Never change or reuse a concept ID. A split keeps the old ID for one
  meaning and registers new IDs (`python -m spedlex.build --register`).
- New concepts in an existing layer module set `"version_added"` to the next
  minor version. Bump the version in `spedlex/__init__.py`, `pyproject.toml`
  and `CITATION.cff` (METHODOLOGY §7: new concepts are a minor version,
  corrections alone a patch).
- A layer can refer only to concepts defined by itself or an earlier layer
  (`LAYERS` in `sources/states/__init__.py`).
- If a test about `sources/name_pair_triage.tsv` fails after a fix, update the
  affected row to record his decision. Don't delete rows.
- Add a line to `CHANGELOG.md` under `[Unreleased]` and name the model.

## 5. Wrap-up

1. `git status`. Remove any `[[SpedLex]]` line Obsidian added
   (`git restore <file>` if the file has no other changes).
2. `python -m spedlex.build --check` and `pytest -q` must pass.
3. Stage files **by name**. Commit, with the model named in the message, only
   after he says to.
4. Push only when he says so. If pushing is blocked, give him the exact
   Terminal commands, including `gh pr create`, and remind him to name the
   model in the pull request.

## 6. Optional: name-pair "judge" items

`sources/name_pair_triage.tsv` has rows marked `judge`: is a state's name the
same concept as the federal one, a different one, or related? **Ask** before
starting. Same one-at-a-time flow, with options *same / related / different /
leave for an expert*. His decisions change the triage file's decision column
and, for *related*, the string's type in the layer module. Run the tests
after each batch.

## Hard rules

- Never decide a result, and never write `result` or `note` without his
  explicit choice in this conversation.
- Never write to `sources/reviews.tsv` (expert decisions only). Write to
  `sources/verifications.tsv` only through `verify_queue.py apply --append`,
  after his yes.
- Never add a row to `sources/disfavored.tsv` unless he asks, with a legal
  basis (AGENTS.md).
- Never invent a term, page or citation.
- Never commit source documents or extracted text. Quotes shown to him stay
  under 15 words.
- Never put student information anywhere.
- Never weaken a test. If an all-caps acronym collides with a name, stop and
  tell him.
