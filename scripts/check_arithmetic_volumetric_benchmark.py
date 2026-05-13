#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

BENCHMARK_PATH = Path("empirical-claims/arithmetic-volumetric-benchmark-v0.1/registry.json")
PARENT_PATH = Path("empirical-claims/log-volume-normalization-v0.1/registry.json")
REQUIRED = {
    "benchmark_id", "benchmark_version", "claim_class", "parent_normalization",
    "axes", "base_policy", "quantum_volume_relation", "observable_channels",
    "scoring_policy", "fixtures", "claim_boundary", "replay_instructions"
}
BANNED = {
    "equivalence to quantum volume", "quantum hardware benchmark",
    "quantum advantage claim", "proof of RH or GRH",
    "deterministic primality guarantee", "asymptotic speedup claim"
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry(path: Path = BENCHMARK_PATH) -> dict:
    return load_json(path)


def assert_required_fields(registry: dict) -> None:
    missing = REQUIRED.difference(registry)
    if missing:
        raise AssertionError(f"missing fields: {sorted(missing)}")


def check_parent_normalization(registry: dict) -> dict:
    parent = registry["parent_normalization"]
    actual = load_json(PARENT_PATH)
    if parent["normalization_id"] != actual["normalization_id"]:
        raise AssertionError("parent normalization id mismatch")
    if parent["normalization_version"] != actual["normalization_version"]:
        raise AssertionError("parent normalization version mismatch")
    return {"pass": True}


def check_two_axis_surface(registry: dict) -> dict:
    axes = registry["axes"]
    if axes.get("scale_location") != "u" or axes.get("log_width") != "L":
        raise AssertionError("benchmark must preserve u and L axes")
    if axes.get("collapse_to_scalar_allowed") is not False:
        raise AssertionError("v0.1 must not collapse to scalar without a declared rule")
    return {"pass": True, "surface": axes.get("surface")}


def corrected_mean_field(u: float, L: float) -> float:
    leading = math.exp(u) / u * (math.exp(L) - 1.0)
    correction = math.exp(u) / (u * u) * (((L - 1.0) * math.exp(L)) + 1.0)
    return leading - correction


def fixture_score(u: float, L: float) -> float:
    return math.log1p(corrected_mean_field(u, L)) / (1.0 + u * L)


def check_fixture_scores(registry: dict) -> dict:
    scores = []
    for fixture in registry["fixtures"]:
        u, L = float(fixture["u"]), float(fixture["L"])
        score = fixture_score(u, L)
        if not math.isfinite(score) or score < 0.0:
            raise AssertionError(f"invalid score: u={u}, L={L}, score={score}")
        scores.append({"u": u, "L": L, "score": score})
    return {"pass": True, "scores": scores}


def check_quantum_volume_boundary(registry: dict) -> dict:
    relation = registry["quantum_volume_relation"]
    if relation.get("status") != "methodological_analogy_only":
        raise AssertionError("relation must be methodology-only analogy")
    for key in ("equivalence_to_quantum_volume", "quantum_hardware_benchmark", "quantum_advantage_claim"):
        if relation.get(key) is not False:
            raise AssertionError(f"must deny {key}")
    if "quantum_width_depth" not in relation.get("analogy", {}):
        raise AssertionError("analogy map incomplete")
    return {"pass": True}


def check_claim_boundary(registry: dict) -> dict:
    disallowed = set(registry["claim_boundary"]["disallowed_without_separate_proof_or_runtime_artifact"])
    missing = BANNED.difference(disallowed)
    if missing:
        raise AssertionError(f"missing banned claims: {sorted(missing)}")
    return {"pass": True}


def run_checks() -> dict:
    registry = load_registry()
    assert_required_fields(registry)
    return {
        "required_fields": {"pass": True},
        "parent_normalization": check_parent_normalization(registry),
        "two_axis_surface": check_two_axis_surface(registry),
        "fixture_scores": check_fixture_scores(registry),
        "quantum_volume_boundary": check_quantum_volume_boundary(registry),
        "claim_boundary": check_claim_boundary(registry),
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
