"""The expert-review email: it builds for a state, covers every open question,
and a filled-in reply (quoted the way mail clients quote) reads back."""

import argparse
import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("expert_review", ROOT / "tools" / "expert_review.py")
er = importlib.util.module_from_spec(spec)
spec.loader.exec_module(er)

RECORDS = er.load_records()


@pytest.fixture()
def nevada(tmp_path, monkeypatch):
    monkeypatch.setattr(er, "ROUNDS", tmp_path)
    er.request(argparse.Namespace(state="NV", sender=None, greeting=None, reply_to=None, limit=0, stale_years=3))
    (rnd,) = list(tmp_path.iterdir())
    return json.loads((rnd / "key.json").read_text()), (rnd / "email.txt").read_text()


def test_every_open_nevada_candidate_is_asked(nevada):
    key, _ = nevada
    asked = {it["concept_id"] for it in key["items"].values() if it.get("concept_id") and it["part"] in ("A", "C")}
    candidates = {r["concept_id"] for r in RECORDS
                  if r["review"]["status"] == "candidate" and any(s.get("jurisdiction") == "US-NV" for s in r["sources"])}
    superseded = {e["replaces"] for e in er.read_extras("NV", "Nevada") if e["replaces"]}
    assert candidates - superseded <= asked


def test_every_item_points_at_a_real_concept(nevada):
    key, _ = nevada
    ids = {r["concept_id"] for r in RECORDS}
    assert {it["concept_id"] for it in key["items"].values() if it.get("concept_id")} <= ids


def test_email_has_no_unfilled_template_slots_and_leaves_sender_visible(nevada):
    _, email = nevada
    assert "{{" not in email
    assert "[YOUR NAME]" in email and "[FIRST NAME]" in email


def test_item_ids_are_unique_and_in_the_email(nevada):
    key, email = nevada
    for iid in key["items"]:
        assert len(re.findall(rf"^{iid}\.\s", email, re.M)) == 1


def test_unknown_state_is_refused():
    with pytest.raises(SystemExit):
        er.resolve_state("Atlantis")


def answered(email, answers, comments=None, quote="> ", credit="A"):
    """Fill in an email the way a person would, then quote it as a mail client does."""
    comments, out, cur, pending = dict(comments or {}, ), [], None, {}
    for line in email.splitlines():
        m = re.match(r"^([A-D]\d+)\.\s", line)
        if (m or not line.strip()) and cur in pending:  # a comment typed under a finished item
            out.append(quote + "           Comment: " + pending.pop(cur))
        if m:
            cur = m.group(1)
            if cur in answers and "[   ]" in line:
                line = line.replace("[   ]", f"[{answers[cur]}]", 1)
            if cur in comments and not cur.startswith("A"):
                pending[cur] = comments[cur]
        if line.strip() == "Name:":
            line = "Name: Pat Educator"
        if line.startswith("Role"):
            line += " school psychologist"
        if line.startswith("Affiliation"):
            line += " Example District"
        if line.startswith("Credit."):
            line = line.replace("[   ]", f"[{credit}]")
        if line.strip() == "Comment:" and cur in comments:
            line += " " + comments[cur]
        out.append(quote + line)
    return "\n".join(out)


def test_reply_round_trip(nevada, tmp_path):
    key, email = nevada
    c_items = [i for i, it in key["items"].items() if it["part"] == "C"]
    a_mapped = [i for i, it in key["items"].items() if it["part"] == "A" and it["maps_to_review"]]
    yes, no_with_reason, no_without = c_items[0], c_items[1], c_items[2]
    text = answered(email, {yes: "Y", no_with_reason: "n", no_without: "N", a_mapped[0]: "N", "B2": "?"},
                    {no_with_reason: "Not used here.", a_mapped[0]: "Now called something else."})
    keyfile = tmp_path / "key.json"
    keyfile.write_text(json.dumps(key))
    reply = tmp_path / "reply.txt"
    reply.write_text(text)
    er.reply(argparse.Namespace(key=str(keyfile), reply=str(reply), reviewer=None))

    rows = [line.split("\t") for line in (tmp_path / "reply.proposed-reviews.tsv").read_text().splitlines()[1:]]
    by_id = {r[0]: r for r in rows}
    assert by_id[key["items"][yes]["concept_id"]][1] == "accept"
    assert by_id[key["items"][no_with_reason]["concept_id"]][1:2] == ["reject"]
    assert by_id[key["items"][no_with_reason]["concept_id"]][4] == "Not used here."
    assert key["items"][no_without]["concept_id"] not in by_id, "a reject without a reason must not become a row"
    assert key["items"][a_mapped[0]]["concept_id"] not in by_id, "a No on a Part A item needs a person, not a reject"
    assert all(r[2] == "Pat Educator (school psychologist)" for r in rows), "affiliation must stay out of the review log"
    assert all(len(r) == 5 for r in rows)
    followups = (tmp_path / "reply.followups.md").read_text()
    assert "Now called something else." in followups and "reject needs a reason" in followups
    assert "| Nevada | Pat Educator, school psychologist, Example District |" in followups


def test_anonymous_when_not_credited(nevada, tmp_path):
    key, email = nevada
    first_c = next(i for i, it in key["items"].items() if it["part"] == "C")
    text = answered(email, {first_c: "Y"}, credit="C")
    (tmp_path / "key.json").write_text(json.dumps(key))
    (tmp_path / "r.txt").write_text(text)
    er.reply(argparse.Namespace(key=str(tmp_path / "key.json"), reply=str(tmp_path / "r.txt"), reviewer=None))
    row = (tmp_path / "r.proposed-reviews.tsv").read_text().splitlines()[1].split("\t")
    assert row[2].startswith("anonymous-NV-")


def test_name_and_role_only_leaves_affiliation_out(nevada, tmp_path):
    key, email = nevada
    first_c = next(i for i, it in key["items"].items() if it["part"] == "C")
    (tmp_path / "key.json").write_text(json.dumps(key))
    (tmp_path / "r.txt").write_text(answered(email, {first_c: "Y"}, credit="B"))
    er.reply(argparse.Namespace(key=str(tmp_path / "key.json"), reply=str(tmp_path / "r.txt"), reviewer=None))
    followups = (tmp_path / "r.followups.md").read_text()
    assert "| Nevada | Pat Educator, school psychologist |" in followups and "Example District" not in followups.split("CONTRIBUTORS")[1]
