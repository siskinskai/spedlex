# Roadmap

SPEDLex is an open, cited vocabulary of U.S. special-education terms.
De-identification tools use it to remove a child's personal information from
IEPs, evaluations and other special-education documents. The terms that give
those documents meaning stay in, so caregivers can use AI tools safely. Its
value grows with every state, every reviewed term and every tool that adopts
it.

The items below run roughly in order of value. Each is a good place to
contribute. Comment on an existing issue or open a new one before you start
a large item.

## Coverage

- **The remaining states.** Every state not yet in the list, plus D.C.,
  Puerto Rico and the outlying territories. The recipe is fixed (see
  CONTRIBUTING.md) and each state now adds about ten new concepts. A state
  takes a few hours to a weekend. [COVERAGE.md](COVERAGE.md) tracks which
  states are added and which are pending.
- **Part C (early intervention).** 34 CFR Part 303: IFSPs, service
  coordination, natural environments, state lead agencies.
- **Section 504.** 34 CFR Part 104 and OCR guidance: 504 plans, 504
  coordinators, manifestation reviews under 504.
- **Instruments and scores.** Test names, subtests and score terms (standard
  score, percentile rank, scaled score) from publisher catalogs and test
  indexes. These carry the most eponyms (Wechsler, Woodcock, Kaufman), so
  each needs careful risk grading.
- **Spanish.** Many states publish their safeguards notice in Spanish.

## Quality

- **Expert review.** Move candidates to `expert_accepted`, starting with the
  most widely attested concepts.
- **Cross-maps.** Map concepts to MeSH, SNOMED CT, ERIC, CEDS and ICF-CY.
  Every `none_found` is evidence for the gap SPEDLex fills.
- **More usage flags.** Extend `sources/disfavored.tsv` where a statute,
  rule or agency decision replaced a term, and mark more `legacy` forms.
  Each row needs a basis and a person's check.
- **State-preferred forms.** Some states have renamed a federal category in
  their own rules (New York's "emotional disability", 2022). A way to mark a
  state's current preferred form, not just a form it uses, would sharpen the
  terminology helpers.
- **Three-letter acronyms and initials.** Two-letter acronyms are now
  protected only when the user confirms them (METHODOLOGY §4). The 259
  three-letter all-caps strings (IEP, LRE, OHI and others) could also be a
  student's three initials. Covering them all would mean many prompts, so
  this needs a policy decision: all of them, only those that are also common
  initials, or none.
- **Broader name lists.** Name lists that better represent recent immigrant
  families, to tighten risk grading.

## Field vocabulary

- **Corpus terms.** With a de-identified IEP corpus (or synthetic IEPs),
  extract the vocabulary teachers actually write ("push-in", "resource
  room", "sped") using termhood scoring, and attest it against the corpus.

## Tooling

- A JavaScript matcher and lexicon with the same conformance tests, for
  browser-only tools.
- An evaluation set built from the regional strings: cited questions that
  test whether a model knows each state's term.
- Example integrations for common AI frameworks (retrieval, guardrails).
- A Hugging Face dataset mirror.
- Integrations or example configs for common open-source scrubbers.
