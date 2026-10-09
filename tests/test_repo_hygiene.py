"""Repository hygiene: source documents and large files never enter git.

Runs locally with pytest (before you push) and in CI. A pull request that
reaches GitHub with a source document in it is stored by GitHub permanently,
so run pytest before every push.
"""
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_EXT = {".pdf", ".doc", ".docx", ".rtf", ".odt", ".epub", ".htm", ".html",
               ".xls", ".xlsx", ".ppt", ".pptx", ".png", ".jpg", ".jpeg", ".tif", ".tiff"}
ALLOWED = {"site/template.html"}                     # reviewed exceptions only
TXT_ALLOWED_DIRS = ("reference/", "spedlex/adapters/", "outreach/")   # name lists and e-mail templates
LARGE_OK_DIRS = ("data/", "reference/")
MAX_BYTES = 1_000_000
BLOCKED_DIRS = re.compile(r"^([a-z]{2}-docs/|\.sources-cache/)")


def tracked_files():
    try:
        out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True,
                             capture_output=True).stdout
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("not a git checkout")
    return [p for p in out.decode().split("\0") if p]


def test_no_source_documents_tracked():
    bad = [p for p in tracked_files()
           if p not in ALLOWED and (Path(p).suffix.lower() in BLOCKED_EXT or BLOCKED_DIRS.match(p))]
    assert not bad, ("Source documents must not be committed. Unstage them, keep them in "
                     ".sources-cache/, and cite them in sources/documents.tsv:\n  " + "\n  ".join(bad))


def test_no_stray_text_dumps():
    bad = [p for p in tracked_files()
           if p.endswith(".txt") and not p.startswith(TXT_ALLOWED_DIRS)]
    assert not bad, "Text files outside reference/ look like extracted source text:\n  " + "\n  ".join(bad)


def test_no_large_files():
    bad = [p for p in tracked_files()
           if not p.startswith(LARGE_OK_DIRS) and (ROOT / p).is_file()
           and (ROOT / p).stat().st_size > MAX_BYTES]
    assert not bad, "Files over 1 MB outside data/ and reference/:\n  " + "\n  ".join(bad)


def test_add_state_guard_blocks_the_same_extensions():
    """tools/add_state.py can't be imported (it runs on import), so check its list by text."""
    text = (ROOT / "tools" / "add_state.py").read_text(encoding="utf-8")
    missing = [e for e in sorted(BLOCKED_EXT) if f'"{e}"' not in text]
    assert not missing, f"tools/add_state.py's blocked list is out of sync with this test: {missing}"
