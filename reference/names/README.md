# Reference name lists

The build checks every safelist string against these lists to grade its
privacy risk (see `docs/METHODOLOGY.md`). They are lowercase, one name per
line. They were derived once from the files below and are not updated
automatically.

| File | What it holds | Derived from | License |
|---|---|---|---|
| `ssa_first_names.txt` | 6,782 first names that reached the Social Security Administration's top 1,000 for either sex in any year from 1880 to 2008 | `baby-names.csv` in [hadley/data-baby-names](https://github.com/hadley/data-baby-names), compiled from SSA data | SSA data is a U.S. government work (public domain) |
| `census2000_surnames_10k.txt` | 3,286 surnames with at least 10,000 bearers in the 2000 Census | `most-common-name/surnames.csv` in [fivethirtyeight/data](https://github.com/fivethirtyeight/data), compiled from the U.S. Census Bureau's 2000 surname file | Census data is public domain. The FiveThirtyEight compilation is CC BY 4.0 |

One name was removed by a maintainer's decision: "doe" (2026-10-08). It is
used almost only as a pseudonym (John or Jane Doe), so it carries no risk of
identifying a real child, and keeping it flagged Delaware's "DOE" (Department
of Education) as a surname.

Known gaps: SSA lists favor names given to U.S.-born children before 2009.
Names that are common among recent immigrant families may be missing. A
contribution that adds a broader list (with a clear license) is welcome.
Widening a list can only raise risk grades, never lower them.

The default collision adapter (a copy of the patterns used by SCRUB, an
offline de-identification tool for special-education documents) has its
own name dictionary, in
`spedlex/adapters/scrub_first_names.txt`. It is the first-name list from
[dominictarr/random-name](https://github.com/dominictarr/random-name) (MIT),
which was taken from the public-domain Moby Word List by Grady Ward.
