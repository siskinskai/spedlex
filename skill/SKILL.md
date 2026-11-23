---
name: spedlex
description: Look up U.S. special-education terms (IEP, IDEA, Section 504, state names like ARD committee, CSE or PPT) with citations, use the reader's state's own wording, and check drafts for other-state, outdated or ambiguous terms. Use whenever you write, explain or summarize anything about special education, IEPs, evaluations or procedural safeguards.
---

# SPEDLex: cited special-education terms

SPEDLex {version} is an open vocabulary of {concepts} U.S. special-education
concepts and {strings} names for them, covering the federal IDEA Part B
regulations (34 CFR Part 300) and {states} states. Every record cites the
regulation or state document that uses the term. It runs locally from the
bundled data: nothing is sent anywhere.

It records **how official documents name things, not what they mean in
law.** Don't present a SPEDLex record as a legal definition or as legal
advice. Show the citation and send the reader to the source for meaning.

## When to use it

- **Before you write for a reader in a specific state.** States name the
  same thing differently: the federal "IEP Team" is the "ARD committee" in
  Texas, the "Committee on Special Education" in New York, the "PPT" in
  Connecticut and the "case conference committee" in Indiana. Look up the
  term and use the state's form.
- **When a document or question uses a term or acronym you aren't sure of.**
  Several acronyms mean different things in different states (CDE, SED,
  MDE, DESE and others). If the reader's state is unknown and the acronym is
  ambiguous, ask which state rather than guessing.
- **Before you send a draft.** Run `check` on it to catch other-state terms,
  outdated (`legacy`) terms and disfavored terms.
- **To ground an answer about a document.** Run `glossary` on the document's
  text and keep the result in your context, so your answer uses cited terms
  instead of memory.

## Commands

Run from this skill's folder. `--state` takes a two-letter code (`TX`) or
`US-TX`; leave it off for federal terms only. Add `--json` for structured
output.

```bash
python scripts/spedlex_cli.py lookup "ARD committee" --state NY   # what it names; each state's name
python scripts/spedlex_cli.py check draft.txt --state NY          # problems in a draft, with suggestions
python scripts/spedlex_cli.py glossary document.txt --state NY    # cited glossary for your prompt
python scripts/spedlex_cli.py annotate document.txt --state NY    # every term found, with spans
```

Use `-` instead of a file name to read standard input. In Python, put
`scripts/` on `sys.path` and use `from spedlex import Lexicon`
(`Lexicon.from_default(jurisdiction="US-NY")`, then `lookup`, `check`,
`glossary`, `annotate`, `best_term`).

## How much to trust a record

Each result carries a review status. Say so when it matters:

| Status | Meaning |
|---|---|
| `machine_validated` | Drawn from regulation text; the build checked the string and citation against that text. |
| `source_verified` | A person opened the cited document and confirmed the term there. |
| `candidate` | Drawn from a state document by text extraction; no person has checked the citation yet. |
| `expert_accepted` | A special-education professional confirmed it. |

This copy has: {status_line}.

## Rules

- **Never paste a child's information anywhere** to use this skill. The
  commands run locally; keep it that way.
- **Don't invent terms or citations.** If SPEDLex has no record, say so and
  use the plain federal term, or ask.
- **Keep older documents readable.** A `legacy` or disfavored term in a
  document the reader has is still recognized; use the current term in
  what you write, and explain the change if it helps.
- **Coverage is incomplete.** {missing} have no state layer yet; Part C
  (early intervention) and most of Section 504 are not covered. For those,
  use federal terms and say the state's wording wasn't checked.

Source, data license (CC BY 4.0) and methodology:
https://github.com/SiskinSkai/spedlex
