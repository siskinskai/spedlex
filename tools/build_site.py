"""Build the explorer page: site/template.html + data -> site/index.html.

usage: python tools/build_site.py   (the Pages workflow runs this on every push to main)
"""
import importlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from sources.states import LAYERS  # noqa: E402

records = [json.loads(line) for line in open(ROOT / "data" / "spedlex.jsonl", encoding="utf-8")]
stats = json.loads((ROOT / "data" / "stats.json").read_text())

states = {}
for name in LAYERS:
    mod = importlib.import_module(f"sources.states.{name}")
    j = mod.JURISDICTION
    st = states.setdefault(j, {"c": j[3:].lower(), "j": j, "name": mod.LAYER_NAME.split(" (")[0], "v": []})
    st["v"].append(mod.VERSION_ADDED)

page = (ROOT / "site" / "template.html").read_text()
for token, value in (("__DATA__", records), ("__STATES__", list(states.values())), ("__STATS__", stats)):
    assert token in page, token
    page = page.replace(token, json.dumps(value, ensure_ascii=False, separators=(",", ":")))
out = ROOT / "site" / "index.html"
out.write_text(page, encoding="utf-8")
print(f"wrote {out} ({len(page) // 1024} KB, {len(records)} records, {len(states)} states)")
