"""Package SPEDLex as an agent skill: a folder with SKILL.md, the data and the lookup code.

  python tools/build_skill.py            writes build/skill/spedlex/ and dist/spedlex-skill.zip

The skill runs with the Python standard library only. Upload the zip as a
Claude skill, or copy build/skill/spedlex/ into any agent's skills folder. The text
lives in skill/SKILL.md; this tool fills in the counts from data/stats.json
and docs/COVERAGE.md, so rebuild the data first (python -m spedlex.build).
build/ and dist/ are ignored by git; the release workflow attaches the zip to
each GitHub release.
"""

import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "skill" / "spedlex"
ZIP = ROOT / "dist" / "spedlex-skill.zip"
RUNTIME = ["__init__.py", "__main__.py", "lexicon.py", "match.py"]   # standard library only
STATUS_WORDS = [("machine_validated", "machine-validated"), ("source_verified", "source-verified"),
                ("candidate", "candidates"), ("expert_accepted", "expert-accepted")]

CLI = '''"""Run the SPEDLex command line from this skill folder: python scripts/spedlex_cli.py --help"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from spedlex.__main__ import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
'''


def pending_jurisdictions():
    rows = re.findall(r"^\| ([^|]+?) \| US-[A-Z]{2} \| pending \|", (ROOT / "docs" / "COVERAGE.md").read_text(), re.M)
    return rows


def render(template, st):
    by = st["by_review_status"]
    status_line = ", ".join(f"{by.get(k, 0):,} {word}" for k, word in STATUS_WORDS)
    pending = pending_jurisdictions()
    missing = ", ".join(pending[:-1]) + " and " + pending[-1] if len(pending) > 1 else "".join(pending) or "No jurisdictions"
    values = {"version": "v" + st["version"], "concepts": f"{st['concepts']:,}", "strings": f"{st['strings']:,}",
              "states": str(st["states"]), "status_line": status_line, "missing": missing}
    for key, value in values.items():
        template = template.replace("{" + key + "}", value)
    left = re.findall(r"\{[a-z_]+\}", template)
    if left:
        raise SystemExit(f"skill/SKILL.md has unfilled placeholders: {left}")
    return template


def main():
    st = json.loads((ROOT / "data" / "stats.json").read_text())
    if OUT.exists():
        shutil.rmtree(OUT)
    pkg = OUT / "scripts" / "spedlex"
    (pkg / "_data").mkdir(parents=True)
    for name in RUNTIME:
        shutil.copy2(ROOT / "spedlex" / name, pkg / name)
    shutil.copy2(ROOT / "data" / "spedlex.jsonl", pkg / "_data" / "spedlex.jsonl")
    (OUT / "scripts" / "spedlex_cli.py").write_text(CLI, encoding="utf-8")
    (OUT / "SKILL.md").write_text(render((ROOT / "skill" / "SKILL.md").read_text(encoding="utf-8"), st), encoding="utf-8")
    for name in ("LICENSE", "LICENSE-DATA"):
        shutil.copy2(ROOT / name, OUT / name)
    ZIP.parent.mkdir(parents=True, exist_ok=True)
    ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(OUT.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                z.write(p, p.relative_to(OUT.parent))
    print(f"wrote {OUT.relative_to(ROOT)}/ and {ZIP.relative_to(ROOT)} ({ZIP.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
