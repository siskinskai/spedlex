"""tools/fetch_sources.py: verify local copies and download paths without the network.

The manifest and cache here are temporary, and the "download" is a file:// URL,
so no real source document and no internet connection is involved.
"""
import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADER = ("doc_id jurisdiction title publisher edition_date url retrieved sha256 bytes pages "
          "wayback_url rights local_name notes").split()


def load_tool():
    spec = importlib.util.spec_from_file_location("fetch_sources", ROOT / "tools" / "fetch_sources.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_manifest(path, rows):
    lines = ["\t".join(HEADER)]
    for r in rows:
        lines.append("\t".join(r.get(h, "") for h in HEADER))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def row(tmp, **kw):
    data = b"fake source document, not a real PDF"
    base = {"doc_id": "xx-fake-2026", "jurisdiction": "US-XX", "title": "Fake", "publisher": "Nobody",
            "edition_date": "2026", "url": "", "retrieved": "2026-10-09", "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": str(len(data)), "pages": "1", "wayback_url": "", "rights": "state_guidance",
            "local_name": "fake.pdf", "notes": ""}
    base.update(kw)
    return base, data


def run(tool, tmp, rows, *extra):
    manifest = tmp / "documents.tsv"
    write_manifest(manifest, rows)
    return tool.main(["--manifest", str(manifest), "--cache", str(tmp / "cache"), *extra])


def test_check_passes_for_matching_local_copy(tmp_path, capsys):
    tool = load_tool()
    r, data = row(tmp_path)
    (tmp_path / "cache" / "xx").mkdir(parents=True)
    (tmp_path / "cache" / "xx" / "fake.pdf").write_bytes(data)
    assert run(tool, tmp_path, [r], "--check") == 0
    assert "ok" in capsys.readouterr().out


def test_check_fails_for_missing_or_altered_copy(tmp_path, capsys):
    tool = load_tool()
    r, data = row(tmp_path)
    assert run(tool, tmp_path, [r], "--check") == 1            # absent
    (tmp_path / "cache" / "xx").mkdir(parents=True)
    (tmp_path / "cache" / "xx" / "fake.pdf").write_bytes(data + b"x")
    assert run(tool, tmp_path, [r], "--check") == 1            # altered
    out = capsys.readouterr().out
    assert "MISSING" in out and "CHANGED" in out


def test_check_skips_unfetchable_rows(tmp_path):
    tool = load_tool()
    r, _ = row(tmp_path, notes="[not fetchable] saved web page")
    assert run(tool, tmp_path, [r], "--check") == 0


def test_download_saves_matching_file_and_flags_changed_one(tmp_path, capsys):
    tool = load_tool()
    good, data = row(tmp_path)
    src = tmp_path / "origin.bin"
    src.write_bytes(data)
    good["url"] = src.as_uri()
    assert run(tool, tmp_path, [good]) == 0
    assert (tmp_path / "cache" / "xx" / "fake.pdf").read_bytes() == data

    bad, _ = row(tmp_path, local_name="other.pdf", doc_id="xx-other-2026")
    src2 = tmp_path / "changed.bin"
    src2.write_bytes(b"the state edited this document")
    bad["url"] = src2.as_uri()
    assert run(tool, tmp_path, [bad]) == 1
    assert (tmp_path / "cache" / "xx" / "other.pdf.new").exists()
    assert not (tmp_path / "cache" / "xx" / "other.pdf").exists()
    assert "CHANGED" in capsys.readouterr().out


def test_federal_rows_use_the_us_folder(tmp_path):
    tool = load_tool()
    r, data = row(tmp_path, jurisdiction="US", doc_id="us-fake-2026")
    (tmp_path / "cache" / "us").mkdir(parents=True)
    (tmp_path / "cache" / "us" / "fake.pdf").write_bytes(data)
    assert run(tool, tmp_path, [r], "--check") == 0
