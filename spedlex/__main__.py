"""Command line: python -m spedlex (or the `spedlex` command once installed).

    spedlex lookup "ARD committee" --state NY
    spedlex check letter.txt --state TX
    spedlex annotate notes.txt
    spedlex glossary iep.txt --state CT
"""

import argparse
import json
import sys

from .lexicon import Lexicon


def _read(path):
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


def main(argv=None):
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--state", help="the reader's state, e.g. TX or US-TX")
    common.add_argument("--json", action="store_true", help="print JSON")
    ap = argparse.ArgumentParser(
        prog="spedlex",
        description="Look up U.S. special-education terms, list them in a text, or check a text for "
                    "disfavored, older and other-state terms. Runs locally on the bundled SPEDLex data.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lookup", parents=[common], help="what a term names, and each state's name for it")
    p.add_argument("term")
    for name, helptext in (("annotate", "list the terms in a text"),
                           ("check", "flag disfavored, older, other-state and ambiguous terms"),
                           ("glossary", "a cited glossary to put in a model's prompt")):
        p = sub.add_parser(name, parents=[common], help=helptext)
        p.add_argument("file", nargs="?", default="-", help="text file, or - for standard input")
    args = ap.parse_args(argv)
    lex = Lexicon.from_default(jurisdiction=args.state)

    if args.cmd == "lookup":
        res = lex.lookup(args.term)
        if args.json:
            print(json.dumps(res, indent=2, ensure_ascii=False))
        elif not res:
            print(f"'{args.term}' is not in SPEDLex.")
        for d in ([] if args.json else res):
            print(f"{d['matched_form']} -> {d['preferred_term']} ({d['concept_id']}, {d['category']}, "
                  f"{d['jurisdiction']}, {d['review_status']})")
            if args.state:
                print(f"  write for {lex.jurisdiction}: {d['use_for_reader']}")
            if d["disfavored"]:
                print(f"  DISFAVORED: {d['usage_note']}")
            for j, forms in d["forms_by_jurisdiction"].items():
                print(f"  {j}: {', '.join(forms)}")
            if d["definition_note"]:
                print(f"  note: {d['definition_note']}")
            print(f"  source: {d['citations'][0]}")
        return 0 if res else 1

    text = _read(args.file)
    if args.cmd == "glossary":
        print(lex.glossary(text))
        return 0
    items = lex.annotate(text) if args.cmd == "annotate" else lex.check(text)
    if args.json:
        print(json.dumps([i.to_dict() for i in items], indent=2, ensure_ascii=False))
        return 0
    for i in items:
        if args.cmd == "annotate":
            label = i.preferred_term or "AMBIGUOUS: " + "; ".join(c["preferred_term"] for c in i.candidates)
            print(f"{i.start}-{i.end}\t{i.text}\t{label}\t{i.concept_id or ''}")
        else:
            print(f"{i.start}-{i.end}\t{i.kind}\t{i.text}\t{i.message}"
                  + (f"\tsuggest: {i.suggestion}" if i.suggestion else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
