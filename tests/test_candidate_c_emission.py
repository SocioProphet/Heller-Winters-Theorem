#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "experiments" / "candidate-c" / "run.py"
UPSTREAM_SHA = "0ef1cab4c525fd004e38fa9a92f7e911acbbc976"

REQUIRED_EVENT_KEYS = {"id", "kind", "scope", "time", "props"}
REQUIRED_ARTIFACT_KEYS = {"artifact_id", "artifact_type", "claim_class", "inputs", "outputs", "non_claim_boundary"}
REQUIRED_CALIBRATION_KEYS = {"bundle_id", "domain", "controls", "acceptance"}
REQUIRED_CLAIM_KEYS = {"claim_id", "claim_class", "statement", "status", "evidence_refs", "non_claim_boundary"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_candidate_c_runner_emits_native_pfk_receipts() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "receipts"
        result = subprocess.run([sys.executable, str(RUNNER), "--output-dir", str(out)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        assert result.returncode == 0, result.stderr

        event_path = out / "event_ir" / "candidate_c_baseline_events.json"
        artifact_path = out / "proof_artifacts" / "candidate_c_baseline_proof_artifact.json"
        calibration_path = out / "calibration_bundles" / "candidate_c_baseline_calibration_bundle.json"
        claim_path = out / "claim_ledger.jsonl"

        assert event_path.exists()
        assert artifact_path.exists()
        assert calibration_path.exists()
        assert claim_path.exists()

        events = load_json(event_path)
        assert len(events) >= 5
        for event in events:
            assert REQUIRED_EVENT_KEYS.issubset(event)
            assert event["scope"] == "CANDIDATE_C"

        artifact = load_json(artifact_path)
        assert REQUIRED_ARTIFACT_KEYS.issubset(artifact)
        assert artifact["claim_class"] == "descriptive-grade"
        assert "not RH" in artifact["non_claim_boundary"]

        calibration = load_json(calibration_path)
        assert REQUIRED_CALIBRATION_KEYS.issubset(calibration)
        control_ids = {row["control_id"] for row in calibration["controls"]}
        assert {"N1", "N2", "S1", "S2", "S3"}.issubset(control_ids)

        claim_rows = [json.loads(line) for line in claim_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        assert len(claim_rows) == 1
        claim = claim_rows[0]
        assert REQUIRED_CLAIM_KEYS.issubset(claim)
        assert claim["claim_class"] == "descriptive-grade"
        assert claim["empirical_protocol"]["N1"] == "cramer_bernoulli"
        assert claim["empirical_protocol"]["N2"] == "wheel_admissible_composite"
        assert claim["provenance"]["upstream_sha"] == UPSTREAM_SHA
        assert "not theorem-grade" in claim["non_claim_boundary"]


if __name__ == "__main__":
    test_candidate_c_runner_emits_native_pfk_receipts()
    print("Candidate C native PFK emission test passed.")
