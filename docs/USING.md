# Using SPEDLex

This guide is for people building de-identification tools ("scrubbers").
A scrubber is software that removes personal information from a document.
A caregiver might use one to share an IEP with an AI tool without sharing the
child's identity. SPEDLex tells such a tool which words are special-education
terms and should stay intact. Nothing here depends on any particular
scrubber.

## Where the safelist runs

Run the safelist **before** any redaction step. Otherwise a name dictionary
removes "Johnson" from "Woodcock-Johnson IV" before the safelist sees the
phrase.

1. **Protect.** Find safelisted spans. Replace each with a placeholder that
   no redaction pattern can match.
2. **Scrub.** Run your scrubber unchanged. That includes household names,
   pattern-based PII, name dictionaries and any fail-closed unknown-word pass.
3. **Restore.** Put the protected spans back.

The names of the people in the document (the student, parents, staff) always
take priority. Before matching, drop any safelist string that contains one.

## Python

```bash
pip install "git+https://github.com/SiskinSkai/spedlex"          # latest
pip install "git+https://github.com/SiskinSkai/spedlex@v0.23.0"  # pinned
```

The package has no dependencies and bundles the data.

```python
from spedlex import Safelist, load

safelist = Safelist.from_default(
    jurisdictions={"US-TX"},              # federal + Texas. Omit for all states.
    household_names={"Rosa", "Georgia"},  # people in this document
)

# Find spans
for m in safelist.find("The ARD committee reviewed the PLAAFP."):
    print(m.start, m.end, m.text, m.concept_id, m.preferred_term)

# Shield them from your scrubber
masked, restore = safelist.protect(text)
result = restore(my_scrubber(masked))
```

Options:

| Argument | Default | Effect |
|---|---|---|
| `jurisdictions` | `None` (all) | Keep federal concepts plus these states'. Drop strings tagged only to other states. |
| `household_names` | none | Drop any string containing one of these words, in any case. This is deliberately conservative. A student named Ed also drops the acronym "ED", because forms often print names in capitals. |
| `statuses` | candidate, machine_validated, expert_accepted | Add `"illustrative"` to include placeholders. Remove `"candidate"` for the reviewed core only. |

`load(path)` returns the raw records if you want to build your own matcher.

## Other languages: the matching rules

Read `data/spedlex.jsonl` (or `data/spedlex.csv`) and apply these rules.
`tests/test_match.py` is a good conformance checklist to port.

1. **Filter records** by `review.status`. Skip `illustrative` and
   `expert_rejected`. You can also filter by `jurisdiction`.
2. **Filter strings** by `regional` if you filtered jurisdictions.
3. **Case.** `phrase_ci` matches ignoring case. `phrase_cs` and `token_cs`
   match exact case.
4. **Boundaries.** An ASCII letter or digit must not come directly before or
   after a match. Punctuation such as `+`, `/`, `-` and `:` can be part of a
   string: "12:1+1", "E/BD", "TCAP-Alt".
5. **never_bare.** If the concept's `pii_risk.protect_rule` is `never_bare`,
   skip any string that is a single word, unless it is all capitals and
   case-sensitive. "Kaufman" is skipped. "KABC-II" and the full test name
   are kept.
6. **Household names.** Skip any string containing a household name as a word.
7. **Months in dates.** Skip a match whose text (minus a trailing period) is
   a month name or abbreviation (January to December; Jan, Feb, Mar, Apr,
   Jun, Jul, Aug, Sep, Sept, Oct, Nov, Dec) if a digit comes directly before
   it, allowing spaces and `. , / -` and an ordinal suffix ("14th"), or
   directly after it, allowing an optional period and spaces and `, / -`.
   "APR 14, 2015" is skipped; "its APR to OSEP" is kept.
8. **Longest match wins.** Collect all matches and take the longest first.
   Drop any match that overlaps one already taken.
9. **Placeholders.** Replace each span with something your scrubber can't
   match. The Python matcher uses one character from Unicode's
   Supplementary Private Use Area-A (U+F0000 upward) per span.

## Testing your own scrubber against the list

Before you deploy, check which safelist strings your scrubber would destroy.

1. Copy `spedlex/adapters/scrub.py` to `spedlex/adapters/yours.py`.
2. Replace its patterns with yours. Keep the contract: `NAME`,
   `NAME_DICT_PREFIX`, and `collisions(text)`, which returns a label for every
   pattern that matches any part of `text`.
3. Register it in `ADAPTERS` in `spedlex/adapters/__init__.py`.
4. Run `python -m spedlex.build --adapter yours --out /tmp/check`.
5. Read `/tmp/check/data/collision_report.csv`.

Four collisions turn up often:

- State names in first-name dictionaries ("Virginia Alternate Assessment
  Program")
- Eponyms in test names (Woodcock-Johnson, Kaufman)
- "Rosa's Law"
- Number patterns that catch class ratios

## Cautions

- Protecting a term only stops your scrubber from damaging it. It says
  nothing about whether the rest of the document is safe to release.
- Candidates are unreviewed. If false protection is costly for you, use
  `statuses={"machine_validated", "expert_accepted"}`.
- Pin a version. New releases add terms, and a term you didn't expect to be
  protected may become protected.
