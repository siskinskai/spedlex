<!--
prompt: precheck-review
version: 1.1 (2026-10-09)
changes in 1.1: points reviewers to tools/fetch_sources.py for the cited documents
tested with: none yet. Please report results in your pull request.
improve it: see prompts/README.md
-->

# Instructions: pre-check candidate records before a human review

A model can speed up review by finding each term in its cited document.
It **cannot** make the review decision: `sources/reviews.tsv` records the
judgment of a person with special-education expertise, and the `reviewer`
column is always that person. Use this prompt to prepare the evidence,
then decide yourself.

Get the records to check, for example every Texas candidate, from
`data/spedlex.csv` (filter `review_status` = `candidate` and
`jurisdictions_attesting` containing the state, e.g. `US-TX`),
or copy them from the explorer. Attach the documents they cite: run
`python tools/fetch_sources.py --state <xx>` to download them into
`.sources-cache/<xx>/` (each record's `doc_id` names its row in
`sources/documents.tsv`). Never commit them.

Copy everything below the line.

---

You are preparing evidence for a special-education professional who will
review vocabulary records. For each record below, find the term in the
attached documents and report what you see. Do not decide whether to
accept or reject. The reviewer does that.

## Inputs

- `RECORDS`: rows with concept_id, preferred_term, string, first_citation.
- `DOCS`: the documents those citations point to.

## For each record

1. Look for the term (and its listed strings) at the cited page or
   paragraph.
2. Report:
   - `found_at_citation`: yes, no, or elsewhere (give the correct citation)
   - `quote`: up to 15 words from the document showing the term in use
   - `usage_note`: one line on how the document uses it, if it's not
     obviously a special-education concept
   - `concern`: anything a reviewer should look at: a different meaning,
     an outdated document, a term that is also a person's name or a place.

## Output

A table with columns: concept_id | term | found_at_citation | correct
citation | quote | usage_note | concern.

Then list any records you couldn't check because a document was missing or
unreadable. Never fill a cell with a guess. Write "couldn't check".
