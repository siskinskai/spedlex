"""The agent skill (skill/SKILL.md, tools/build_skill.py)."""
import ast
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_skill", ROOT / "tools" / "build_skill.py")
build_skill = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_skill)


def test_skill_template_renders_completely():
    st = json.loads((ROOT / "data" / "stats.json").read_text())
    text = build_skill.render((ROOT / "skill" / "SKILL.md").read_text(encoding="utf-8"), st)
    assert text.startswith("---\nname: spedlex\ndescription: ")
    assert not re.search(r"\{[a-z_]+\}", text)
    assert f"{st['concepts']:,} U.S. special-education" in text


def test_skill_runtime_uses_only_the_standard_library():
    stdlib = getattr(sys, "stdlib_module_names", None)
    for name in build_skill.RUNTIME:
        tree = ast.parse((ROOT / "spedlex" / name).read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.level:
                assert node.module is None or node.module.split(".")[0] in {m[:-3] for m in build_skill.RUNTIME}, \
                    f"{name} imports .{node.module}, which the skill doesn't ship"
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                mods = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module]
                for m in mods:
                    if stdlib is not None:
                        assert m.split(".")[0] in stdlib, f"{name} imports {m}, which isn't standard library"


def test_coverage_pending_list_matches_the_built_states():
    st = json.loads((ROOT / "data" / "stats.json").read_text())
    text = (ROOT / "docs" / "COVERAGE.md").read_text()
    added = set(re.findall(r"^\| [^|]+? \| US-([A-Z]{2}) \| added \|", text, re.M))
    assert added == set(st["state_codes"]), "docs/COVERAGE.md disagrees with the built data"
