# Releasing (maintainers)

## One-time setup

1. Fill in the placeholders and commit:
   `python tools/set_owner.py --owner <github-user-or-org> --author "<Your Name>" --email <conduct-contact>`
2. Create the GitHub repository and push `main`.
3. **Pages:** Settings → Pages → Source: *GitHub Actions*. The explorer then
   publishes to `https://<owner>.github.io/spedlex/` on every push to `main`.
4. **Zenodo:** sign in to zenodo.org with GitHub, then turn on the
   repository under *GitHub* in your Zenodo account. Every GitHub release
   is then archived with its own DOI. Add the concept DOI badge to the
   README and a `doi:` line to `CITATION.cff` after the first release.
5. **Branch protection:** require the CI check on `main` so data and sources
   can't drift.
6. **Labels** used by the issue forms: `correction`, `new term`,
   `new state`, `review`.

## Each release

1. Make sure `main` is green and `CHANGELOG.md` has an entry for the
   version in `spedlex/__init__.py`. Check that `git count-objects -vH` hasn't
   grown unexpectedly (it should stay a few megabytes).
2. Tag and push: `git tag v0.24.0 && git push origin v0.24.0`.
3. The release workflow checks the tag matches the package version, runs
   the build check and tests, builds the wheel, bundles the data
   (`spedlex-data-v0.24.0.zip`), and creates the GitHub release. Zenodo
   picks it up from there.

## Versioning

See [docs/METHODOLOGY.md §7](docs/METHODOLOGY.md#7-versioning). Patch
releases (reviews, corrections) need a manual bump of `spedlex/__init__.py`,
`pyproject.toml` and `CITATION.cff`. `tools/add_state.py` bumps minor
versions for you.
