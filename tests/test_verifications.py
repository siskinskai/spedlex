"""Source checks (sources/verifications.tsv) and tools/verify_queue.py."""
import copy
import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest

from spedlex import Lexicon
from spedlex.build import VERIFICATION_COLUMNS, apply_reviews, apply_verifications

ROOT = Path(__file__).resolve().parents[1]
HEADER = "\t".join(VERIFICATION_COLUMNS) + "\n"


def rec(cid, status="candidate", citation="5-A DCMR § 3010.7"):
    return {"concept_id": cid, "preferred_term": cid, "review": {"status": status, "reviewers": 0},
            "sources": [{"source_type": "state_regulation", "citation": citation, "jurisdiction": "US-DC"}]}


def write(tmp_path, *rows):
    p = tmp_path / "verifications.tsv"
    p.write_text(HEADER + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    return p


def test_verified_upgrades_candidate_and_validated(tmp_path):
    recs = [rec("A"), rec("B", "machine_validated")]
    p = write(tmp_path, ["A", "verified", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", ""],
              ["B", "verified", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", ""])
    apply_verifications(recs, p)
    assert [r["review"]["status"] for r in recs] == ["source_verified", "source_verified"]
    assert recs[0]["review"]["verified_against"] == [
        {"citation": "5-A DCMR § 3010.7", "verifier": "J. Evans", "date": "2026-11-23"}]


def test_problem_blocks_upgrade_and_is_noted(tmp_path):
    recs = [rec("A")]
    p = write(tmp_path, ["A", "problem", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", "term not on that page"])
    apply_verifications(recs, p)
    assert recs[0]["review"]["status"] == "candidate"
    assert "term not on that page" in recs[0]["review"]["notes"]
    assert "verified_against" not in recs[0]["review"]


def test_latest_row_per_verifier_counts(tmp_path):
    recs = [rec("A")]
    p = write(tmp_path, ["A", "problem", "5-A DCMR § 3010.7", "J. Evans", "2026-11-20", "wrong page"],
              ["A", "verified", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", "page fixed"])
    apply_verifications(recs, p)
    assert recs[0]["review"]["status"] == "source_verified"


@pytest.mark.parametrize("row, message", [
    (["Z", "verified", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", ""], "unknown concept"),
    (["A", "ok", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", ""], "verified or problem"),
    (["A", "problem", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", ""], "needs a note"),
    (["A", "verified", "34 CFR 300.8", "J. Evans", "2026-11-23", ""], "not one of"),
    (["A", "verified", "5-A DCMR § 3010.7", "", "2026-11-23", ""], "verifier is required"),
    (["A", "verified", "5-A DCMR § 3010.7", "J. Evans", "11/23/2026", ""], "YYYY-MM-DD"),
])
def test_bad_rows_stop_the_build(tmp_path, row, message):
    with pytest.raises(SystemExit, match=message):
        apply_verifications([rec("A")], write(tmp_path, row))


def test_illustrative_records_cannot_be_verified(tmp_path):
    p = write(tmp_path, ["A", "verified", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", ""])
    with pytest.raises(SystemExit, match="illustrative"):
        apply_verifications([rec("A", "illustrative")], p)


def test_expert_decision_overrides_source_check(tmp_path):
    recs = [rec("A")]
    apply_verifications(recs, write(tmp_path, ["A", "verified", "5-A DCMR § 3010.7", "J. Evans", "2026-11-23", ""]))
    reviews = tmp_path / "reviews.tsv"
    reviews.write_text("concept_id\tdecision\treviewer\tdate\tnote\nA\treject\tDr. Lee\t2026-11-24\tnot a DC term\n")
    apply_reviews(recs, reviews)
    assert recs[0]["review"]["status"] == "expert_rejected"
    assert recs[0]["review"]["verified_against"]  # the source check stays on record


def test_committed_verifications_file_has_header():
    text = (ROOT / "sources" / "verifications.tsv").read_text(encoding="utf-8")
    assert text.splitlines()[0].split("\t") == VERIFICATION_COLUMNS


def test_lexicon_includes_source_verified_by_default():
    records = [json.loads(line) for line in (ROOT / "data" / "spedlex.jsonl").read_text().splitlines()]
    r = copy.deepcopy(next(x for x in records if x["review"]["status"] == "candidate"))
    r["review"]["status"] = "source_verified"
    assert Lexicon([r]).lookup(r["preferred_term"])


def test_queue_and_apply_round_trip(tmp_path):
    tool = ROOT / "tools" / "verify_queue.py"
    queue = tmp_path / "queue.csv"
    subprocess.run([sys.executable, str(tool), "queue", "--limit", "3", "--out", str(queue)], check=True,
                   capture_output=True)
    rows = list(csv.DictReader(queue.open(encoding="utf-8")))
    assert len(rows) == 3 and all(r["result"] == "" for r in rows)
    rows[0]["result"] = "verified"
    rows[1]["result"] = "problem"
    rows[1]["note"] = "cited page has a different term"
    with queue.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    before = (ROOT / "sources" / "verifications.tsv").read_text(encoding="utf-8")
    subprocess.run([sys.executable, str(tool), "apply", str(queue), "--verifier", "Test Person",
                    "--date", "2026-11-23"], check=True, capture_output=True)
    proposed = Path(str(queue) + ".proposed-verifications.tsv").read_text(encoding="utf-8").splitlines()
    assert proposed[0].split("\t") == VERIFICATION_COLUMNS and len(proposed) == 3
    assert (ROOT / "sources" / "verifications.tsv").read_text(encoding="utf-8") == before  # no --append
