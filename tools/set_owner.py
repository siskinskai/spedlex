"""Fill in the placeholders left for whoever publishes the repository.

usage: python tools/set_owner.py --owner GITHUB_USER_OR_ORG --author "Full Name" --email contact@example.org

Replaces OWNER, AUTHOR_NAME and CONTACT_EMAIL in every text file, then
rebuilds the site. Run once, before the first push, and commit the result.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", "__pycache__", "node_modules"}
SUFFIXES = {".md", ".py", ".toml", ".cff", ".yml", ".yaml", ".html", ".json", ".txt"}

ap = argparse.ArgumentParser()
ap.add_argument("--owner", required=True)
ap.add_argument("--author", required=True)
ap.add_argument("--email", required=True, help="where code-of-conduct reports go")
args = ap.parse_args()

subs = {"OWNER": args.owner, "AUTHOR_NAME": args.author, "CONTACT_EMAIL": args.email}
changed = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix not in SUFFIXES or SKIP & set(path.parts) or path == Path(__file__).resolve():
        continue
    if path.parent.name == "data" or path.name == "index.html":
        continue
    text = path.read_text(encoding="utf-8")
    new = text
    for k, v in subs.items():
        new = new.replace(f"/{k}/", f"/{v}/").replace(f"{k}.github.io", f"{v}.github.io")
        if k != "OWNER":
            new = new.replace(k, v)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed.append(str(path.relative_to(ROOT)))
print("updated:", *changed, sep="\n  ")
remaining = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
             if p.is_file() and p.suffix in SUFFIXES and not SKIP & set(p.parts) and p.parent.name != "data"
             and p.name != "index.html" and p != Path(__file__).resolve() and "OWNER" in p.read_text(encoding="utf-8", errors="ignore")]
if remaining:
    print("check these by hand, they still mention OWNER:", *remaining, sep="\n  ")
subprocess.run([sys.executable, str(ROOT / "tools" / "build_site.py")], check=True)
