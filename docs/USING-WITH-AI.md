# Using SPEDLex in AI and writing tools

SPEDLex began as the vocabulary that de-identification tools need (see
[USING.md](USING.md)). The same records can do more. Each concept already lists
every name that official documents use for it, which states use which name,
the older names, and a citation. That is the information an AI tool needs
to keep special-education wording consistent and correct for its reader.

This guide is for people building chat assistants, document summarizers,
letter drafters, search tools, plain-language or translation tools and
evaluation sets that deal with special education.

## What it helps with

| Problem | What SPEDLex gives you | Function |
|---|---|---|
| A model explains "ARD committee" to a New York parent, or "CSE" to a Texas parent | Each state's own name for the concept, with a citation | `lookup`, `best_term` |
| A summary uses a term from the wrong state, or an outdated one | A check of the text: other-state, older and disfavored terms, with suggestions | `check` |
| An acronym means different things in different states (CDE, DESE, SED) | Both meanings, settled by the reader's state | `annotate`, `lookup` |
| A model answers about an IEP from memory | A short, cited glossary of the terms actually in the document, to put in the prompt | `glossary` |
| A search for "IEP team" misses documents that say "PPT" or "case conference committee" | Every form of the concept, for query expansion | `forms_by_jurisdiction` |
| A translation or plain-language rewrite mangles "12:1+1" or "ARD" | The spans that are terms, so the tool can keep them intact | `annotate` |
| You need to test whether a model knows state vocabulary | Cited question-and-answer pairs from the regional strings | `load()` |

## What it doesn't do

- **It doesn't define terms.** SPEDLex records how documents *name* a concept,
  not what the law requires. `definition_note`, where present, is a short note
  in the project's own words. For meaning, read the cited source.
- **It doesn't track what is legally current.** The goal is coverage of
  terms that appear in real documents. `legacy` marks older forms when a
  document says so; `disfavored` marks the few forms that should not be used
  in new writing. Neither list is complete.
- **A regional tag isn't exhaustive.** `regional: ["US-TX"]` means the Texas
  documents that were read use the form. Other states may too, and states not
  yet covered are unknown. So an "other-state" finding is a hint to check,
  not an error.
- **Most records aren't expert-reviewed yet.** Every result carries
  `review_status`. Show it, or filter on it, when a user may rely on the
  answer.
- **It isn't legal advice** and must not be used to decide eligibility,
  services or placement.

## Python

```python
from spedlex import Lexicon

lex = Lexicon.from_default(jurisdiction="NY")   # the reader's state; omit for national

lex.lookup("ARD committee")
# [{'concept_id': 'SPED:000003', 'preferred_term': 'IEP Team',
#   'use_for_reader': 'Committee on Special Education',
#   'forms_by_jurisdiction': {'US': ['IEP Team', ...], 'US-TX': ['ARD committee', ...], ...},
#   'citations': ['34 CFR 300.23', ...], 'review_status': 'machine_validated', ...}]

for issue in lex.check(draft):
    print(issue.kind, issue.text, issue.message, issue.suggestion)
# other_state  ARD committee  'ARD committee' is the term in US-TX; US-NY's documents say ...
# disfavored   mental retardation  Replaced in federal law by "intellectual disability" ...

prompt_context = lex.glossary(document_text)    # Markdown, one cited line per concept
```

| Method | Returns |
|---|---|
| `lookup(term)` | Every concept the form names, best fit for the reader's state first, as plain dicts. |
| `annotate(text)` | `Annotation`s: span, concept, category, string type, regional tags, the reader's state's own terms, disfavored flag, note, first citation, review status. An ambiguous form has `concept_id=None` and lists `candidates`. |
| `check(text)` | `Issue`s of kind `disfavored`, `legacy`, `other_state` or `ambiguous`, each with a message and, where possible, a suggestion. |
| `glossary(text, max_terms=40)` | A Markdown glossary of the terms in the text, for a prompt. Empty string if there are none. |
| `state_terms(concept_id, jurisdiction=None)` | The forms a state's documents use for the concept. |
| `best_term(concept_id, jurisdiction=None)` | One form to write: the state's own phrase for the same thing if it has one, else the national preferred term. It never returns an acronym, a plural or a `related` form, and it prefers a current name over a legacy one. |
| `forms_by_jurisdiction(concept_id)` | `{'US': [...], 'US-TX': [...], ...}`, without disfavored forms. |
| `concept(concept_id)` | The full record. |

`Lexicon(records, jurisdiction=None, statuses=...)` takes the same `statuses`
argument as the Safelist. For answers people may act on, consider
`statuses={"machine_validated", "expert_accepted"}`.

Matching follows the Safelist's rules (whole phrases, case-sensitive
acronyms, `never_bare`, month names next to numbers skipped). Unlike the
Safelist, the Lexicon indexes every state's strings, so it can recognize
another state's term. `check` ignores short all-lowercase phrases from other
states ("team meeting"), which are too likely to be ordinary English.

## Command line

```bash
pip install "git+https://github.com/SiskinSkai/spedlex"
spedlex lookup "PPT" --state CT
spedlex check draft.txt --state TX          # or pipe text in: ... | spedlex check --state TX
spedlex annotate notes.txt --json
spedlex glossary iep.txt --state NY
```

`python -m spedlex` works the same way without installing the command.

## MCP server

Any assistant that speaks the [Model Context Protocol](https://modelcontextprotocol.io)
(Claude, IDE agents and others) can use SPEDLex as a set of tools. The server
needs Python 3.10 or later.

```bash
pip install "spedlex[mcp] @ git+https://github.com/SiskinSkai/spedlex"
```

Add it to your client's configuration, for example:

```json
{
  "mcpServers": {
    "spedlex": { "command": "spedlex-mcp" }
  }
}
```

| Tool | Does |
|---|---|
| `lookup_term(term, state)` | What a term names and what the reader's state calls it |
| `terms_in_text(text, state)` | Every term in a text, with citations |
| `check_text(text, state)` | Disfavored, older, other-state and ambiguous terms in a draft |
| `glossary_for_text(text, state)` | A cited glossary for grounding an answer |

The server runs on the user's machine with the bundled data. Text passed to
its tools is processed in memory and is never stored or sent anywhere.

## Patterns that work

**Ground, then answer.** Put the glossary in the prompt with an instruction
such as:

> The glossary below lists the special-education terms in the user's
> document and what their state calls each one. Use the state's terms in
> your answer. Expand an acronym the first time you use it. If the glossary
> marks a term as disfavored, don't use it yourself, but you may quote it.
> Don't treat the glossary as a legal definition.

**Check, then revise.** Run `check` on the model's draft and give the issues
back to the model for one revision pass. Don't replace terms automatically:
a quotation, a legal citation or a state rule's own wording should keep the
original term, and only the writer knows which is which.

**Scrub first, then annotate.** SPEDLex protects terms from the scrubber, so
a scrubbed document still contains them. Build the glossary from the
scrubbed text, and no personal information reaches the model or the
glossary.

**Expand queries.** For search over special-education documents, add
`forms_by_jurisdiction` for each concept in the query. Leave out acronyms
that are ambiguous unless the state is known.

## Other languages

Read `data/spedlex.jsonl`. Index every string of every record you keep (see
the matching rules in [USING.md](USING.md); skip the household-names rule,
which is only for redaction). Then:

1. **Resolve a form** that belongs to several concepts by the reader's
   state: prefer a string whose `regional` includes it, then an untagged
   string on a national concept or a concept of that state. If more than one
   remains, report the form as ambiguous.
2. **The reader's term** for a concept is the first string, other than
   acronyms, abbreviations and plurals, whose `regional` includes the reader's
   state and that isn't `disfavored`. If none exists, use `preferred_term`.
3. **Flag** a string with `disfavored: true` (show `usage_note`); a string
   of type `legacy`; and, only when the reader's state is covered by the
   data, a string whose `regional` tags all name other states, or a concept
   whose `jurisdiction` is another state.

`tests/test_lexicon.py` is a conformance checklist you can port.
