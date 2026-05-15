#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Sequence

UPSTREAM_SHA = "988307215ad38ccb16514311222184a1b757752b"
LIMIT = 10000
SEED = 20260510
FREQUENCIES = [1.0, 2.0, 3.0]
TWO_PI = 2.0 * math.pi


def canonical_sha256(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sieve_primes(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def theta(n: int, omega: float) -> float:
    return (omega * math.log(n) / TWO_PI) % 1.0


def kuiper_uniform(values: Sequence[float]) -> float:
    xs = sorted(values)
    n = len(xs)
    d_plus = 0.0
    d_minus = 0.0
    for i, x in enumerate(xs, start=1):
        d_plus = max(d_plus, i / n - x)
        d_minus = max(d_minus, x - (i - 1) / n)
    return d_plus + d_minus


def statistic(sequence: Sequence[int]) -> dict:
    by_frequency = {}
    for omega in FREQUENCIES:
        value = kuiper_uniform([theta(n, omega) for n in sequence])
        by_frequency[str(omega)] = {
            "kuiper_v": round(value, 15),
            "sqrt_n_v": round(math.sqrt(len(sequence)) * value, 15),
        }
    return {
        "count": len(sequence),
        "by_frequency": by_frequency,
        "max_sqrt_n_v": max(row["sqrt_n_v"] for row in by_frequency.values()),
    }


def build_result() -> dict:
    primes = sieve_primes(LIMIT)
    all_integers = list(range(2, LIMIT + 1))
    cramer_rng = random.Random(SEED)
    cramer = [n for n in all_integers if cramer_rng.random() < min(1.0, 1.0 / math.log(n))]
    prime_set = set(primes)
    wheel_candidates = [n for n in all_integers if math.gcd(n, 30) == 1 and n not in prime_set]
    wheel = sorted(random.Random(SEED + 2000).sample(wheel_candidates, len(primes)))
    return {
        "limit": LIMIT,
        "seed": SEED,
        "frequencies": FREQUENCIES,
        "statistics": {
            "primes": statistic(primes),
            "all_integers": statistic(all_integers),
            "cramer_bernoulli": statistic(cramer),
            "wheel_admissible_composite": statistic(wheel),
        },
    }


def write_json(path: Path, payload: object) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return file_sha256(path)


def emit(output_dir: Path) -> dict:
    result = build_result()
    result_hash = canonical_sha256(result)
    event_path = output_dir / "event_ir" / "candidate_c_baseline_events.json"
    artifact_path = output_dir / "proof_artifacts" / "candidate_c_baseline_proof_artifact.json"
    calibration_path = output_dir / "calibration_bundles" / "candidate_c_baseline_calibration_bundle.json"
    claim_path = output_dir / "claim_ledger.jsonl"

    events = [
        {"id": "cc-001", "kind": "PHASE_MAP", "scope": "CANDIDATE_C", "time": {"clock": "MONO", "t": 1}, "props": {"operator_id": "PFK-OP-010", "limit": LIMIT, "frequencies": FREQUENCIES, "upstream_sha": UPSTREAM_SHA}},
        {"id": "cc-002", "kind": "NULL_MODEL", "scope": "CANDIDATE_C", "time": {"clock": "MONO", "t": 2}, "props": {"operator_id": "PFK-OP-020", "nulls": ["all_integers", "cramer_bernoulli", "wheel_admissible_composite"], "seed": SEED}},
        {"id": "cc-003", "kind": "STATISTIC", "scope": "CANDIDATE_C", "time": {"clock": "MONO", "t": 3}, "props": {"operator_id": "PFK-OP-050", "statistic": "max_omega_sqrt_n_kuiper_uniform", "claim_class": "descriptive-grade", "result_sha256": result_hash}},
        {"id": "cc-004", "kind": "CALIBRATION", "scope": "CANDIDATE_C", "time": {"clock": "MONO", "t": 4}, "props": {"operator_id": "PFK-OP-030", "bundle_id": "CB-CANDIDATE-C-BASELINE-001"}},
        {"id": "cc-005", "kind": "CLAIM_LEDGER_EMISSION", "scope": "CANDIDATE_C", "time": {"clock": "MONO", "t": 5}, "props": {"operator_id": "PFK-OP-001", "claim_id": "HW-CAND-C-NATIVE-PFK-001", "claim_class": "descriptive-grade"}},
    ]
    event_hash = write_json(event_path, events)

    calibration = {
        "bundle_id": "CB-CANDIDATE-C-BASELINE-001",
        "domain": "candidate-c-log-phase",
        "controls": [
            {"control_id": "N1", "description": "Cramer-Bernoulli random-density surrogate declared"},
            {"control_id": "N2", "description": "wheel-admissible composite alternate substrate declared"},
            {"control_id": "S1", "description": "single baseline window declared for loop-closure only"},
            {"control_id": "S2", "description": "base-stability deferred to follow-up"},
            {"control_id": "S3", "description": "perturbation-stability deferred to follow-up"},
        ],
        "acceptance": {"schema_valid": True, "event_ir_sha256": event_hash, "result_sha256": result_hash},
        "non_claim_boundary": ["loop closure only", "not RH", "not GRH", "not theorem-grade", "not statistical novelty"],
    }
    calibration_hash = write_json(calibration_path, calibration)

    artifact = {
        "artifact_id": "HW-CAND-C-PFK-ARTIFACT-001",
        "artifact_type": "ProofArtifact",
        "claim_class": "descriptive-grade",
        "inputs": [
            {"path": str(event_path.relative_to(output_dir)), "sha256": event_hash},
            {"path": str(calibration_path.relative_to(output_dir)), "sha256": calibration_hash},
        ],
        "outputs": [{"path": str(claim_path.relative_to(output_dir)), "claim_id": "HW-CAND-C-NATIVE-PFK-001", "result_sha256": result_hash}],
        "non_claim_boundary": ["not RH", "not GRH", "not zero-location", "not asymptotic", "not theorem-grade"],
        "provenance": {"upstream": "SocioProphet/Heller-Godel", "upstream_sha": UPSTREAM_SHA},
    }
    artifact_hash = write_json(artifact_path, artifact)

    claim = {
        "claim_id": "HW-CAND-C-NATIVE-PFK-001",
        "claim_class": "descriptive-grade",
        "statement": "Candidate C baseline log-phase apparatus emits schema-compatible PFK receipts for a finite X=10000 loop-closure run.",
        "status": "emitted",
        "evidence_refs": [
            {"kind": "EventIR", "path": str(event_path.relative_to(output_dir)), "sha256": event_hash},
            {"kind": "ProofArtifact", "path": str(artifact_path.relative_to(output_dir)), "sha256": artifact_hash},
            {"kind": "CalibrationBundle", "path": str(calibration_path.relative_to(output_dir)), "sha256": calibration_hash},
        ],
        "non_claim_boundary": ["not RH", "not GRH", "not theorem-grade", "not statistical novelty"],
        "empirical_protocol": {"N1": "cramer_bernoulli", "N2": "wheel_admissible_composite", "S1": "single_window_loop_closure_only", "S2": "deferred", "S3": "deferred"},
        "provenance": {"operators_invoked": ["PFK-OP-001", "PFK-OP-010", "PFK-OP-020", "PFK-OP-030", "PFK-OP-050"], "upstream_sha": UPSTREAM_SHA},
    }
    claim_path.parent.mkdir(parents=True, exist_ok=True)
    claim_path.write_text(json.dumps(claim, sort_keys=True) + "\n", encoding="utf-8")

    return {"event_ir_sha256": event_hash, "proof_artifact_sha256": artifact_hash, "calibration_bundle_sha256": calibration_hash, "result_sha256": result_hash}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("experiments/candidate-c/receipts"))
    args = parser.parse_args()
    print(json.dumps(emit(args.output_dir), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
