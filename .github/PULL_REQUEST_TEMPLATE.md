## What this changes

<!-- e.g. "Adds Ohio", "Corrects the citation for SPED:000214", "Reviews 30 Texas candidates" -->

## AI assistance

<!-- Which model(s) helped, and for what? e.g. "claude-opus-5-5 drafted the layer with prompts/add-state.md; gemini-2.5-pro audited it with prompts/audit-layer.md". Write "none" if none. -->

Model(s):

## Checklist

- [ ] No real student information anywhere
- [ ] No source documents or text extracted from them (PDFs, Word files, saved pages, OCR text); new sources are rows in sources/documents.tsv
- [ ] Any AI model used is named above and in `ASSISTED_BY`
- [ ] `python -m spedlex.build --check` passes
- [ ] `pytest` passes
- [ ] New sources are cited to the page or paragraph, with URLs
- [ ] CHANGELOG.md updated
