# SPEDLex

**An open, cited vocabulary of U.S. special-education terms, so privacy tools can remove a child's personal information from a document without destroying what the document says, and AI tools can name each term the way the reader's state does.**

[Explore the list](https://SiskinSkai.github.io/spedlex/) · [Download the data](data/) · [Use it with AI tools](docs/USING-WITH-AI.md) · [Methodology](docs/METHODOLOGY.md) · [Contribute](CONTRIBUTING.md)

[![CI](https://github.com/SiskinSkai/spedlex/actions/workflows/ci.yml/badge.svg)](https://github.com/SiskinSkai/spedlex/actions/workflows/ci.yml)

## Why this exists

Parents, guardians, educators and advocates now use AI tools for special
education. They ask for help to understand an evaluation report, prepare for
an IEP meeting, draft a letter, or compare this year's goals with last
year's. Those documents are full of a child's private information: names,
birth dates, diagnoses, school and family details. Pasting one into an AI
tool shares all of it.

The safe way is to **de-identify** the document first. A tool called a
*scrubber* finds personal information and replaces it ("[NAME]", "[DATE]")
before anything leaves the caregiver's device. Families, schools and
researchers are building these tools.

They share one problem. A scrubber has to tell a child's name from a
special-education term, so it needs to know the terms. Medicine has a shared
vocabulary for this: UMLS, MeSH and SNOMED CT. That is how a clinical
scrubber knows "Tourette syndrome" is a diagnosis and not a person.
**Special education has nothing like it.** A cautious scrubber deletes words
it doesn't recognize. The document comes out with "ARD committee", "PLAAFP",
"12:1+1 special class" and "Woodcock-Johnson IV" blacked out. That is safe,
but it is useless to the AI tool and to the caregiver. A careless scrubber
does the opposite. It lets a name through because the name was hiding inside
a term.

**SPEDLex is that missing vocabulary.** Each entry is a special-education
concept. It lists every form the concept takes in real documents. It cites
the regulation or state document that uses it. It carries a grade that says
how safely a tool can protect it without ever protecting a person's name.
Any de-identification tool can use it.

### The same vocabulary helps any AI tool that works with special education

To tell a term from a name, each record already holds everything an
official document calls the concept, which states use which name, the older
names, and a citation. That is also what an AI assistant needs to get the
wording right, and what general models often get wrong:

- **Name things the way the reader's state does.** Texas's "ARD committee",
  New York's "CSE", Connecticut's "PPT" and Indiana's "case conference
  committee" are all the federal "IEP Team". A tool that knows the reader's
  state can answer in that state's words.
- **Expand acronyms correctly.** CDE is a different agency in California and
  Colorado; SED means something different in New York and New Mexico.
- **Avoid outdated and disfavored terms.** Older forms are marked, and the
  few that shouldn't be used in new writing ("mental retardation") are
  flagged with the law that replaced them, while still being recognized in
  older documents.
- **Ground answers in sources.** A tool can attach a short, cited glossary
  of the terms in a document to its prompt, instead of relying on the
  model's memory.
- **Keep terms intact** in search, plain-language rewriting and
  translation, and build test sets from cited, state-specific terms.

[docs/USING-WITH-AI.md](docs/USING-WITH-AI.md) shows how, with a Python
API, a command line and an MCP server any compatible assistant can call.
Privacy stays first: everything runs locally, and the terms survive
de-identification, so a tool can scrub a document and still explain it.

**If you're a parent or caregiver,** SPEDLex isn't an app you run. It's a
building block inside the tools that protect your child's information. You
can still help. [The explorer](https://SiskinSkai.github.io/spedlex/) shows
every term. If your state's word for something is missing or wrong, the
[issue forms](https://github.com/SiskinSkai/spedlex/issues/new/choose) take a
minute and need no technical knowledge.

**If you build privacy or AI tools** for families, schools or researchers,
the data, a reference matcher and the terminology helpers are below, and
nothing here is tied to any one tool or model.

<!-- stats:start -->
## What's in it (v0.50.0)

| | |
|---|---|
| Concepts | 1,568: 156 from 34 CFR Part 300, 1412 added by state layers |
| Surface strings | 3,406 (phrases, acronyms, plurals, legacy and regional forms): 1,162 tagged to the states that use them, 25 older forms, 3 flagged as disfavored |
| States | 42: AK, AL, AR, AZ, CA, CO, CT, DC, DE, FL, GA, HI, IA, ID, IL, IN, KS, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NM, NV, NY, OH, OR, PA, TN, TX, UT, VA, WA, WV, WY |
| Documents cited | 199, listed in [docs/SOURCES.md](docs/SOURCES.md) |
| Review status | 779 checked against regulation text, 789 candidates awaiting a human check, 0 expert-accepted |
| Privacy risk | 1005 none, 237 low, 326 high |

13 more records are **illustrative placeholders** for later work
(test instruments, score terms). They're marked and excluded by default.

_This section is generated by `python -m spedlex.build`._
<!-- stats:end -->

## One record

```json
{
  "concept_id": "SPED:000102",
  "preferred_term": "Present levels of academic achievement and functional performance",
  "category": "iep_component",
  "strings": [
    {"text": "PLAAFP", "string_type": "acronym", "match": "phrase_cs"},
    {"text": "present levels of performance", "string_type": "legacy", "match": "phrase_ci"},
    {"text": "PLOP", "string_type": "acronym", "match": "phrase_cs"},
    {"text": "present levels", "string_type": "abbreviation", "match": "phrase_ci"}
  ],
  "sources": [{"source_type": "federal_regulation", "citation": "34 CFR 300.320(a)(1)", "jurisdiction": "US"}],
  "pii_risk": {"level": "none", "protect_rule": "phrase_or_token"},
  "review": {"status": "machine_validated"}
}
```

(Trimmed. Every field is explained in [docs/SCHEMA.md](docs/SCHEMA.md).)

## Using it in a tool

**Any language:** read [`data/spedlex.jsonl`](data/spedlex.jsonl) (one JSON
record per line) or [`data/spedlex.csv`](data/spedlex.csv) (one row per
string). Follow the matching rules in [docs/USING.md](docs/USING.md).

**Python:**

```bash
pip install "git+https://github.com/SiskinSkai/spedlex"
```

```python
from spedlex import Safelist

safelist = Safelist.from_default(
    jurisdictions={"US-TX"},          # federal terms plus Texas's
    household_names={"Rosa", "Georgia"},  # the people in this document always get redacted
)
masked, restore = safelist.protect(text)
clean = restore(your_scrubber(masked))   # your de-identification step
```

`protect()` swaps each protected span for a placeholder that no redaction
pattern can match, so your existing de-identification step runs unchanged. See
[docs/USING.md](docs/USING.md) for the rules the matcher applies and how to
port them.

**AI and writing tools:**

```python
from spedlex import Lexicon

lex = Lexicon.from_default(jurisdiction="NY")  # the reader's state
lex.lookup("ARD committee")[0]["use_for_reader"]   # 'Committee on Special Education'
issues = lex.check(model_draft)                    # disfavored, older, other-state, ambiguous terms
context = lex.glossary(document_text)              # a short, cited glossary for the prompt
```

The same functions are on the command line (`spedlex check draft.txt
--state TX`) and in an MCP server (`pip install "spedlex[mcp] @ git+https://github.com/SiskinSkai/spedlex"`,
then `spedlex-mcp`). See [docs/USING-WITH-AI.md](docs/USING-WITH-AI.md).

## How it was built

1. **Federal core.** Every defined term, heading and list item in the IDEA
   Part B regulations (34 CFR Part 300), with its acronyms and variants.
2. **State layers.** For each state: its procedural safeguards notice, its
   parent or IEP guide, and its special-education rules. A state either
   *attests* an existing concept (adding its own names for it) or adds a
   new one (its agencies, tests, diplomas, placements).
3. **Risk grading.** Every string is checked against common first names
   (Social Security Administration), common surnames (U.S. Census) and the
   patterns a typical scrubber uses. A concept whose strings could shelter
   a real name is only ever protected as a full phrase.
4. **Usage.** Older forms are typed `legacy`. A short, curated list in
   `sources/disfavored.tsv` flags forms that shouldn't be used in new
   writing, each with the law or rule behind it. Both are still matched,
   because older documents use them.
5. **Review.** Records start as `candidate` or `machine_validated` and move
   to `expert_accepted` when a special-education professional confirms them.

[docs/METHODOLOGY.md](docs/METHODOLOGY.md) explains each step, the
decisions behind it and its known limits.

## Built with AI, checked by people

SPEDLex was started by Jeremy Evans working with **Claude Opus 5.5**
(Anthropic, `claude-opus-5-5`). The model read the cited regulations and
state documents and drafted the records, the build pipeline and these docs.
Jeremy Evans directed the work and checked it. No independent
special-education expert has accepted a record yet. That is why most records
carry the status `candidate`, and why reviewers are the most valuable
contributors.

Contributions made with **any** AI model are welcome and expected:
Claude, ChatGPT, Gemini, an open-weights model, or a coding agent. The
project's rules are the same for all of them:

- A person is responsible for every contribution and checks it before
  submitting.
- Every source records which model helped (`assisted_by`, e.g.
  `claude-opus-5-5`, or `none`), so anyone can see and filter by it.
- Models work from documents you give them, never from memory, and every
  term is cited to a page or paragraph.
- A second model or a fresh chat checks the work before it's submitted.
- Only people make review decisions.

[prompts/](prompts/) has ready-made, model-neutral instructions for
drafting a state, auditing a draft, and pre-checking records for review.
Use them, and improve them: a better prompt helps every contributor after
you. Coding agents also read [AGENTS.md](AGENTS.md).

## What it is not

- **Not a guarantee.** Protecting a term never makes a document safe to
  share. SPEDLex makes de-identification tools less destructive, not more
  thorough. Caregivers should still read what a tool produces before sharing
  it.
- **Not a de-identification tool** by itself. It's the vocabulary such tools
  need.
- **Not legal advice** or an authoritative glossary. It records how terms
  are used, with citations, not what they mean in law. An AI tool that uses
  it should say so, show the citation, and send people to the source for
  meaning.
- **Not complete.** Most states, D.C. and the territories aren't covered yet,
  and neither are Part C, Section 504 or test instruments. See
  [docs/ROADMAP.md](docs/ROADMAP.md).

## Contributing

The most valuable contributions don't need code:

- **Review records.** If you work in special education, confirming that a
  candidate term is real and correctly cited is the single biggest help. You
  can do it by email, with no GitHub account: see
  [outreach/expert-review/](outreach/expert-review/README.md). Reviewers who
  opt in are thanked in [CONTRIBUTORS.md](CONTRIBUTORS.md).
- **Report a wrong or missing term** with the issue forms.
- **Add a state.** [CONTRIBUTING.md](CONTRIBUTING.md) walks through it. Most
  of the work is reading three documents carefully.
  [prompts/add-state.md](prompts/add-state.md) lets a model write the first
  draft.
- **Improve the prompts** in [prompts/](prompts/) based on what worked with
  your model.

## Repository layout

```
data/            the published list (built, so don't edit by hand)
  spedlex.jsonl  one concept per line
  spedlex.csv    one string per row
  concept_ids.tsv  permanent ID registry
  collision_report.csv  strings that hit a name list or scrubber pattern
sources/         what the list is built from
  disfavored.tsv strings flagged as not for new writing, with their basis
  federal.py     34 CFR Part 300 core
  states/        one module per state layer, with its sources in the docstring
  documents.tsv  manifest of source documents: URL, hash, archived snapshot
provenance/xx/   layer reports and audits for each state (our own notes)
.sources-cache/  local copies of source documents (git ignores it; never committed)
tools/           add a state, fetch and verify sources, build the site
spedlex/         Python package: build pipeline, risk grading, matcher (match.py),
                 terminology helpers (lexicon.py), command line, MCP server
schema/          JSON Schema for a concept record
reference/names/ name lists used for risk grading
site/            the explorer page
docs/            methodology, schema guide, data card, usage, sources
prompts/         instructions for AI models: draft, audit, pre-check
AGENTS.md        rules for AI coding agents working in the repo
```

## Citing

Use the "Cite this repository" button on GitHub or [CITATION.cff](CITATION.cff).
Releases are planned to be archived on Zenodo, which will give each one a DOI
(not set up yet).

## License

Code: [MIT](LICENSE). Data (everything in `data/`, `schema/` and the term
lists in `sources/`): [CC BY 4.0](LICENSE-DATA). Cited documents belong to
their publishers. SPEDLex stores terms and citations, not their text. Each
source is recorded with its URL, hash and an archived snapshot;
`tools/fetch_sources.py` downloads them.
