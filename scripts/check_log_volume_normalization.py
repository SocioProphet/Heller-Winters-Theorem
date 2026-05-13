#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

REGISTRY_PATH = Path("empirical-claims/log-volume-normalization-v0.1/registry.json")
REQUIRED = {
    "normalization_id", "normalization_version", "claim_class", "coordinate",
    "base_policy", "window", "mean_field", "observable", "residual_definition",
    "phase_basis", "envelope_policy", "finite_window_scope", "claim_boundary",
    "fixtures", "replay_instructions"
}
BANNED = {
    "unproved global theorem promotion", "deterministic primality guarantee",
    "asymptotic speedup claim", "zero-location theorem"
}


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_required_fields(registry: dict) -> None:
    missing = REQUIRED.difference(registry)
    if missing:
        raise AssertionError(f"missing fields: {sorted(missing)}")


def check_base_gauge_invariance() -> dict:
    max_delta = 0.0
    for x in (3.0, 101.0, 10007.0, math.exp(30.0)):
        for gamma in (0.5, 1.0, 14.134725141):
            natural = gamma * math.log(x)
            for base in (2.0, math.e, 10.0, 16.0):
                displayed = (gamma * math.log(base)) * (math.log(x) / math.log(base))
                max_delta = max(max_delta, abs(natural - displayed))
    if max_delta >= 1e-10:
        raise AssertionError(f"base gauge delta too large: {max_delta}")
    return {"pass": True, "max_delta": max_delta}


def simpson_exp_over_v(u: float, L: float, panels: int = 4096) -> float:
    if panels % 2:
        panels += 1
    h = L / panels
    total = math.exp(u) / u + math.exp(u + L) / (u + L)
    for k in range(1, panels):
        v = u + k * h
        total += (4.0 if k % 2 else 2.0) * math.exp(v) / v
    return total * h / 3.0


def leading(u: float, L: float) -> float:
    return math.exp(u) / u * (math.exp(L) - 1.0)


def corrected(u: float, L: float) -> float:
    return leading(u, L) - math.exp(u) / (u * u) * (((L - 1.0) * math.exp(L)) + 1.0)


def check_mean_field_correction(fixtures: list[dict]) -> dict:
    cases = []
    for fixture in fixtures:
        u, L = float(fixture["u"]), float(fixture["L"])
        numeric = simpson_exp_over_v(u, L)
        e0 = abs(leading(u, L) - numeric)
        e1 = abs(corrected(u, L) - numeric)
        if e1 >= e0:
            raise AssertionError(f"correction failed: u={u}, L={L}, leading={e0}, corrected={e1}")
        cases.append({"u": u, "L": L, "leading_error": e0, "corrected_error": e1})
    return {"pass": True, "cases": cases}


def check_observable_separation(registry: dict) -> dict:
    policy = registry["envelope_policy"]
    if policy.get("psi_channel") != "exp(u/2)":
        raise AssertionError("psi channel envelope must be exp(u/2)")
    allowed = policy.get("prime_count_channel_allowed", [])
    if "no_envelope_claim" not in allowed:
        raise AssertionError("prime-count channel must allow no_envelope_claim")
    if "exp(u/2)" in allowed:
        raise AssertionError("prime-count channel must not inherit psi envelope directly")
    return {"pass": True}


def check_claim_boundary(registry: dict) -> dict:
    disallowed = set(registry["claim_boundary"]["disallowed_without_separate_proof_artifact"])
    missing = BANNED.difference(disallowed)
    if missing:
        raise AssertionError(f"missing banned claims: {sorted(missing)}")
    return {"pass": True}


def run_checks() -> dict:
    registry = load_registry()
    assert_required_fields(registry)
    return {
        "required_fields": {"pass": True},
        "base_gauge_invariance": check_base_gauge_invariance(),
        "mean_field_correction": check_mean_field_correction(registry["fixtures"]),
        "observable_separation": check_observable_separation(registry),
        "claim_boundary": check_claim_boundary(registry),
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
