# Reference place lists

The build checks every safelist string against these lists to grade its
privacy risk (see `docs/METHODOLOGY.md`, "Grading privacy risk"). A place
name narrows where a child lives, so a string that contains one is graded
`high` with the reason `place_name`, the same as a manual `place_name` flag.

| File | What it holds |
|---|---|
| `us_jurisdictions.tsv` | The 50 states, the District of Columbia and the five inhabited territories, with their postal codes. U.S. government data (public domain). Hawaii is also listed with the ʻokina and the apostrophes that stand in for it ("Hawaiʻi", "Hawai‘i", "Hawai’i", "Hawai'i"). |
| `not_places.tsv` | Reviewed strings where a postal-code token means something else, such as "CT services" (consultant teacher). |

How a string is checked:

- **Full names** ("Georgia", "District of Columbia", "New York") are matched
  as whole words, ignoring case, anywhere in a string.
- **Postal codes** ("DC", "MO", "WA") are matched only when written in
  capitals and only inside a string of two or more words ("Strong Start DC",
  "MO DESE", "WA-AIM"). On their own, many of them are special-education
  acronyms ("ID", "MD", "HI", "VI"), so a one-word string is never read as a
  postal code. Dotted forms ("D.C.", "N.Y.") count as postal codes.

Cities, counties and other places ("St. Louis", "Staunton", "Vineland") are
not in these lists. Mark them with the manual `place_name` flag in the layer
module. Widening a list can only raise risk grades, never lower them.
