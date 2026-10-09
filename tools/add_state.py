"""Register a new state layer, give its concepts IDs, rebuild, and report.

usage: python tools/add_state.py <module>

Adds <module> to LAYERS (if missing), bumps the minor version (package,
pyproject, CITATION.cff), stamps the module's VERSION_ADDED, runs
`python -m spedlex.build --register`, and prints what the layer attested,
what it added, and any high-risk strings. If the build fails, every file
it touched is put back.
"""
import collections
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Refuse to run while a source document is tracked or staged. Keep this list in
# sync with tests/test_repo_hygiene.py (a test checks the extensions).
BLOCKED_EXT = {".pdf", ".doc", ".docx", ".rtf", ".odt", ".epub", ".htm", ".html",
               ".xls", ".xlsx", ".ppt", ".pptx", ".png", ".jpg", ".jpeg", ".tif", ".tiff"}
ALLOWED = {"site/template.html"}
BLOCKED_DIRS = re.compile(r"^([a-z]{2}-docs/|\.sources-cache/)")
try:
    _names = set()
    for _cmd in (["git", "ls-files"], ["git", "diff", "--cached", "--name-only"]):
        _names |= set(subprocess.run(_cmd, cwd=ROOT, check=True, capture_output=True, text=True).stdout.splitlines())
except (OSError, subprocess.CalledProcessError):
    _names = set()
_bad = sorted(n for n in _names if n not in ALLOWED and (Path(n).suffix.lower() in BLOCKED_EXT or BLOCKED_DIRS.match(n)))
if _bad:
    sys.exit("Source documents must not be committed. Unstage them, keep them in .sources-cache/, "
             "and cite them in sources/documents.tsv:\n  " + "\n  ".join(_bad))

mod = sys.argv[1] if len(sys.argv) == 2 else sys.exit(__doc__)
path = ROOT / "sources" / "states" / f"{mod}.py"
if not path.exists():
    sys.exit(f"{path} not found; copy sources/states/_template.py first")

layers = ROOT / "sources" / "states" / "__init__.py"
init = ROOT / "spedlex" / "__init__.py"
pyproj = ROOT / "pyproject.toml"
cff = ROOT / "CITATION.cff"
backup = {p: p.read_text() for p in (layers, init, pyproj, cff, path)}
if not re.search(r'^RETRIEVED = "\d{4}-\d{2}-\d{2}"', path.read_text(), re.M):
    sys.exit(f"set RETRIEVED in {path.name} to the date you read the documents (YYYY-MM-DD)")
t = layers.read_text()
if f'"{mod}"' not in t:
    t = t.replace("\n]\n", f'\n    "{mod}",\n]\n')
    layers.write_text(t)

old = re.search(r'__version__ = "(\d+)\.(\d+)\.(\d+)"', init.read_text())
module_text = path.read_text()
current = re.search(r'^VERSION_ADDED = "([^"]+)"', module_text, re.M).group(1)
if current in ("0.0.0", ""):
    version = f"{old.group(1)}.{int(old.group(2)) + 1}.0"
    init.write_text(init.read_text().replace(old.group(0), f'__version__ = "{version}"'))
    pyproj.write_text(re.sub(r'^version = "[^"]+"', f'version = "{version}"', pyproj.read_text(), flags=re.M))
    today = __import__("datetime").date.today().isoformat()
    c = re.sub(r'^version: "[^"]+"', f'version: "{version}"', cff.read_text(), flags=re.M)
    cff.write_text(re.sub(r'^date-released: "[^"]+"', f'date-released: "{today}"', c, flags=re.M))
    path.write_text(re.sub(r'^VERSION_ADDED = "[^"]*"', f'VERSION_ADDED = "{version}"', module_text, flags=re.M))
else:
    version = current

out = subprocess.run([sys.executable, "-m", "spedlex.build", "--register"], capture_output=True, text=True, cwd=ROOT)
print(out.stdout.strip())
if out.returncode:
    print(out.stderr.strip())
    for p, text in backup.items():
        p.write_text(text)
    sys.exit("build failed; all changes were rolled back. Fix the module and run again.")

sys.path.insert(0, str(ROOT))
juris = __import__(f"sources.states.{mod}", fromlist=["JURISDICTION"]).JURISDICTION
recs = [json.loads(line) for line in open(ROOT / "data" / "spedlex.jsonl")]
touched = [r for r in recs if any(s.get("jurisdiction") == juris for s in r["sources"])]
new = [r for r in recs if r["version_added"] == version]
print(f"\n{mod} ({juris}), version {version}: attests {len(touched)} concepts, {len(new)} new, "
      f"{len(touched) - len(new)} already in the list")
print("new records by review status:", dict(collections.Counter(r["review"]["status"] for r in new)))
for r in new:
    pr = r["pii_risk"]
    if pr["level"] == "high" or pr["scrubber_collisions"]:
        print(f"  check: {pr['level']} risk  {r['preferred_term']}  {pr['reasons']}  {pr['scrubber_collisions'][:2]}")
print("\nNext: add a CHANGELOG.md entry, then commit sources/, data/, docs/SOURCES.md, README.md and the version bump together.")
