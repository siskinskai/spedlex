# The concept record

SPEDLex is an open, cited vocabulary of U.S. special-education terms that
de-identification tools use to protect a child's privacy without destroying
a document's meaning, and that AI and writing tools can use to name terms
consistently (see the [README](../README.md)). The list is organized
as concept records.

Every line of `data/spedlex.jsonl` is one concept record. The record is
validated against
[`schema/sped_concept.schema.json`](../schema/sped_concept.schema.json)
(JSON Schema draft 2020-12). This page explains each field.

## Top level

| Field | Required | Type | Meaning |
|---|---|---|---|
| `concept_id` | yes | `SPED:` + 6 digits | Permanent ID, never reused. 900001 and up are illustrative placeholders. |
| `preferred_term` | yes | string | The name used in the strongest source, usually the federal regulation's wording. |
| `category` | yes | enum | One of 18 categories (below). |
| `definition_note` | no | string | A short note in the project's own words: context, a former name, a caution. Never copied from a glossary. |
| `broader` | no | list of IDs | Parent concepts. "GNETS" → "Continuum of alternative placements". "Audiology" → "Related services". |
| `strings` | yes | list | Every surface form (below). |
| `sources` | yes | list | Every document that attests the concept (below). |
| `cross_maps` | no | list | Mappings to other vocabularies (below). |
| `pii_risk` | yes | object | How safely the strings can be protected (below). |
| `review` | yes | object | Review status (below). |
| `extraction` | yes | object | How the record was found. |
| `jurisdiction` | yes | `US` or `US-XX` | `US` if the concept exists nationally. A state code if it exists only in that state (a state agency, a state test). |
| `version_added` | yes | semver | The release that introduced the concept. |

### Categories

`legal_procedural`, `disability_category`, `health_condition`,
`related_service`, `placement_setting`, `iep_component`,
`evaluation_eligibility`, `academic_skill`, `functional_skill`,
`instrument`, `instrument_subtest`, `score_metric`,
`accommodation_modification`, `discipline`, `transition`,
`early_intervention`, `section_504`, `personnel_role`.

## `strings[]`

| Field | Meaning |
|---|---|
| `text` | The exact surface form. |
| `string_type` | `preferred`, `synonym`, `acronym`, `abbreviation`, `spelling_variant`, `plural`, or `legacy` (an outdated form that still appears in current documents). |
| `match` | `phrase_ci`: the whole phrase, any case. `phrase_cs`: the whole phrase, exact case (used for acronyms). `token_cs`: reserved for single tokens with no risk. |
| `regional` | Optional list of jurisdictions where this form is used, when narrower than the concept. "ARD committee" is `["US-TX"]` on the national IEP Team concept. The list names the states whose documents were read and use the form; it is not exhaustive. |
| `disfavored` | Optional, always `true` when present. The form shouldn't be used in new writing: the law replaced it, or it is considered stigmatizing. It is still matched, because older documents and some state rules print it. Set from `sources/disfavored.tsv`, never in a layer module. |
| `usage_note` | Required with `disfavored`. Why, and what to say instead, in the project's own words. |
| `usage_basis` | Required with `disfavored`. The law, rule or document behind the flag. |

`legacy` (a string type) and `disfavored` (a flag) answer different
questions. `legacy` says a form is older: a former name for a program, an
agency or a category. `disfavored` says a form shouldn't be written any
more. A string can be both ("mental retardation"), and a renamed agency is
legacy without being disfavored. In terminology standards such as ISO 704
and TBX, `legacy` is close to a *superseded* term and `disfavored` to a
*deprecated* one; SPEDLex avoids "deprecated" because software readers
take it to mean the string will be removed, and it won't be.

"Whole phrase" means the match is not preceded or followed by a letter or digit.

## `sources[]`

| Field | Meaning |
|---|---|
| `source_type` | `federal_regulation`, `federal_statute`, `federal_guidance`, `state_regulation`, `state_guidance`, `procedural_safeguards_notice`, `secondary_guidance` (an advocacy group's or district's summary of state rules, used when the state's own document couldn't be read), `controlled_vocabulary`, `instrument_catalog`, `corpus` (real documents such as IEPs, planned, and used today only by illustrative placeholders). |
| `citation` | Human-readable citation to the paragraph or page, e.g. `34 CFR 300.320(a)(1)` or `Idaho Procedural Safeguards Notice (2026), p. 21`. |
| `url` | Where the document was read. Sometimes a mirror or district copy. The state module's docstring says why. |
| `doc_id` | Optional. The document's row in `sources/documents.tsv` (URL, retrieval date, SHA-256 hash, archived snapshot), e.g. `wv-psn-2024`. Absent for web pages that were not saved. |
| `retrieved` | Date the document was read. |
| `jurisdiction` | Whose document it is: `US` or `US-XX`. A concept with sources from five state jurisdictions is attested by five states. |
| `assisted_by` | The AI model that helped read this source and draft the record (its API identifier, e.g. `claude-opus-5-5`), or `none`. |

## `cross_maps[]`

| Field | Meaning |
|---|---|
| `system` | `ERIC`, `CEDS`, `ICF-CY`, `MeSH`, `SNOMEDCT`, `LCSH`, `ICD-10-CM`. |
| `code`, `label` | The target concept, when mapped. |
| `relation` | `exact`, `broad`, `narrow`, `related`, `none_found`, or `pending`. `none_found` is evidence for the coverage gap SPEDLex exists to fill. Most records are still `pending`. |

## `pii_risk`

| Field | Meaning |
|---|---|
| `level` | `none`, `low`, or `high`. |
| `protect_rule` | `phrase_or_token` (safe anywhere), `phrase_only` (only the full string), or `never_bare` (the risky word is protected only inside the full phrase). |
| `reasons` | Why: `eponym`, `common_first_name`, `surname`, `place_name`, `common_english_word`, `contains_number`, `collides_with_scrubber_pattern`, `possible_initials`. |
| `scrubber_collisions` | Which patterns of the reference scrubber (the build's collision adapter, described in [USING.md](USING.md)) fire on which string, e.g. `NAME_COMMON_DICT:Rosa <- 'Rosa's Law'`. |
| `name_list_hits` | Which tokens appear in the SSA first-name or Census surname lists, e.g. `surname:English <- 'Limited English proficient'`. |
| `place_list_hits` | Which U.S. state or territory names or postal codes appear in the strings, e.g. `place:DC <- 'Strong Start DC'`. |
| `possible_initials` | Two-letter all-caps strings that could be a person's initials, each as `{"text": "LS", "ask_in": ["US-MS"]}`. `ask_in` is where the string is an acronym: its `regional` tags, or else the concept's jurisdiction (`US` means every state). A scrubber may ask the user there; otherwise the bare string is not protected. Empty for most concepts. |

[METHODOLOGY.md §5](METHODOLOGY.md#5-grading-privacy-risk) explains how the grade is assigned.

## `review`

| Field | Meaning |
|---|---|
| `status` | `candidate`, `machine_validated`, `expert_accepted`, `expert_rejected`, or `illustrative`. |
| `reviewers` | How many people have recorded a decision. |
| `notes` | What a reviewer said, or what still needs checking. |

## `extraction`

| Field | Meaning |
|---|---|
| `method` | `regulatory_definition`, `regulatory_heading`, `regulatory_text`, `manual`, and, for later phases, `termhood_cvalue` and `instrument_harvest`. |
| `score`, `corpus_frequency` | Reserved for corpus-derived records. |

## Other files in `data/`

| File | Contents |
|---|---|
| `spedlex.csv` | One row per string with its concept ID and source key (the key layer modules use to refer to it), type, match rule, regional tags, attesting jurisdictions, first citation, risk, status, the disfavored flag, the usage note and (last column) `ask_if_initials_in`: for a two-letter acronym that could be initials, the jurisdictions where a scrubber may ask the user about it. Good for spreadsheets. |
| `concept_ids.tsv` | The permanent ID registry: key, ID, preferred term, `active` or `retired`. |
| `collision_report.csv` | Every scrubber and name-list hit, one per row. |
| `stats.json` | Counts by category, risk, status and state. |
