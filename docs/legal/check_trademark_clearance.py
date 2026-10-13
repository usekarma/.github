"""Offline artifact checks; does not perform or certify legal clearance."""

from pathlib import Path
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[2]
LEGAL = ROOT / "docs/legal"
ARTIFACTS = (
    "TRADEMARK_CLEARANCE_EXPERIMENT.md",
    "TRADEMARK_CLEARANCE_REPORT.md",
    "TRADEMARK_CLEARANCE_RISKS.md",
    "TRADEMARK_COUNSEL_QUESTIONS.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    evidence = json.loads(
        (LEGAL / "evidence/trademark-clearance-2026-10-13.json").read_text()
    )
    all_evidence = (
        evidence["official_records"] + evidence["queries"] + evidence["sources"]
    )
    ids = [item["evidence_id"] for item in all_evidence]
    require(len(ids) == len(set(ids)), "Duplicate evidence IDs")
    for item in all_evidence:
        require(item["retrieved_on"] == evidence["research_date"], "Date mismatch")
    for record in evidence["official_records"]:
        require(re.fullmatch(r"\d{8}", record["serial"]), "Invalid serial")
        require(record["serial"] in record["source_url"], "Serial/source mismatch")
        require(record["status"] and record["status_date"], "Missing status evidence")
        require(
            re.fullmatch(r"[0-9a-f]{64}", record["raw_response_sha256"]),
            "Missing response identity",
        )
    for query in evidence["queries"]:
        for run in query["runs"]:
            require(not run["timed_out"] and run["failed_shards"] == 0, "Failed query")
            require(run["total_relation"] == "eq", "Inexact query total")
            require(run["returned"] <= run["request"]["size"], "Page size mismatch")
            require(run["returned"] <= run["total"], "Impossible page count")
    bounded = next(q for q in evidence["queries"] if q["evidence_id"] == "E-Q05")
    require(
        bounded["unique_ids_retrieved"] == len(set(bounded["result_ids"]))
        == sum(run["returned"] for run in bounded["runs"])
        == bounded["runs"][0]["total"],
        "Bounded pagination incomplete or duplicated",
    )
    control = next(q for q in evidence["queries"] if q["evidence_id"] == "E-Q04")
    require(control["runs"][0]["returned"] > 0, "Positive control failed")
    for name in ARTIFACTS:
        path = LEGAL / name
        text = path.read_text()
        require("Status:" in text and evidence["research_date"] in text, name)
        require(text.endswith("\n"), f"Missing final newline: {name}")
        require(all(line.rstrip() == line for line in text.splitlines()), name)
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if not target.startswith(("https://", "http://", "#")):
                require((path.parent / target.split("#")[0]).exists(), target)
        for reference in re.findall(r"E-[A-Z]\d{2}", text):
            require(reference in ids, f"Unknown evidence reference: {reference}")
    for blob in evidence["protected_base_blobs"]:
        data = (ROOT / blob["path"]).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        require(actual == blob["sha"], f"Existing base file changed: {blob['path']}")
    report = (LEGAL / "TRADEMARK_CLEARANCE_REPORT.md").read_text()
    for mark in ("USEKARMA", "USE KARMA", "USEKARMA.DEV", "KARMA"):
        require(f"| {mark} |" in report, f"Missing individual mark assessment: {mark}")
    print(
        f"PASS: {len(ids)} evidence IDs; 18 official status records; bounded pagination; "
        "positive control; document dates/links/references; four-mark assessments; "
        f"{len(evidence['protected_base_blobs'])} existing base blobs unchanged."
    )


if __name__ == "__main__":
    main()
