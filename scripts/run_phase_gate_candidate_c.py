#!/usr/bin/env python3
"""Candidate C phase-gate empirical runner.

This script is intentionally finite-window and empirical. It does not prove
RH, GRH, any residual envelope, or any asymptotic statement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import statistics
import sys
import time
from pathlib import Path
from typing import List, Sequence

TWO_PI = 2.0 * math.pi
DEFAULT_FREQUENCIES = [1.0, 2.0, 3.0, 5.0, 8.0]
DEFAULT_SEED = 20260510
REGISTRY_VERSION = "phase-gate-v0.1"
ARTIFACT_ID = "phase-gate-null-X1e6"


def sieve_primes(limit: int) -> List[int]:
    """Return all primes <= limit."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    root = int(limit ** 0.5)
    for p in range(2, root + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def theta(n: int, omega: float, offset: float = 0.0) -> float:
    """Registry v0.1 phase map theta_omega(n)."""
    return ((omega * math.log(n) / TWO_PI) + offset) % 1.0


def phases(sequence: Sequence[int], omega: float, offset: float = 0.0) -> List[float]:
    return [theta(n, omega, offset=offset) for n in sequence]


def kuiper_uniform_from_phases(values: Sequence[float]) -> float:
    """One-sample Kuiper statistic against Uniform[0,1)."""
    n = len(values)
    if n == 0:
        return float("nan")

    xs = sorted(values)
    inv_n = 1.0 / n
    d_plus = 0.0
    d_minus = 0.0

    for i, x in enumerate(xs, start=1):
        plus = i * inv_n - x
        minus = x - (i - 1) * inv_n
        if plus > d_plus:
            d_plus = plus
        if minus > d_minus:
            d_minus = minus

    return d_plus + d_minus


def statistic_for_sequence(
    sequence: Sequence[int],
    frequencies: Sequence[float] = DEFAULT_FREQUENCIES,
) -> dict:
    """Compute per-frequency and aggregate T(S)."""
    n = len(sequence)
    by_frequency = {}
    scaled = []

    for omega in frequencies:
        v = kuiper_uniform_from_phases(phases(sequence, omega))
        sqrt_n_v = math.sqrt(n) * v if n else float("nan")
        by_frequency[str(omega)] = {
            "kuiper_v": v,
            "sqrt_n_v": sqrt_n_v,
        }
        if n:
            scaled.append(sqrt_n_v)

    return {
        "count": n,
        "by_frequency": by_frequency,
        "max_sqrt_n_v": max(scaled) if scaled else float("nan"),
    }


def cramer_bernoulli_sequence(limit: int, seed: int) -> List[int]:
    """Cramer-style Bernoulli surrogate with p(n)=min(1,1/log n)."""
    rng = random.Random(seed)
    out: List[int] = []
    for n in range(2, limit + 1):
        p = 1.0 / math.log(n)
        if p > 1.0:
            p = 1.0
        if rng.random() < p:
            out.append(n)
    return out


def wheel_composite_control(
    limit: int,
    target_count: int,
    seed: int,
    modulus: int = 30,
) -> List[int]:
    """Count-matched sample from composites coprime to 30."""
    prime_set = set(sieve_primes(limit))
    candidates = [
        n
        for n in range(2, limit + 1)
        if math.gcd(n, modulus) == 1 and n not in prime_set
    ]

    if target_count > len(candidates):
        raise ValueError(
            f"not enough wheel-compatible composites: need {target_count}, "
            f"available {len(candidates)}"
        )

    rng = random.Random(seed)
    sample = rng.sample(candidates, target_count)
    sample.sort()
    return sample


def all_integers(limit: int) -> List[int]:
    return list(range(2, limit + 1))


def rotation_invariance_audit(
    sequence: Sequence[int],
    frequencies: Sequence[float] = DEFAULT_FREQUENCIES,
    offset: float = 0.123456789,
) -> dict:
    """Check Kuiper statistic invariance under circular phase rotation."""
    by_frequency = {}

    for omega in frequencies:
        base = kuiper_uniform_from_phases(phases(sequence, omega, offset=0.0))
        rotated = kuiper_uniform_from_phases(phases(sequence, omega, offset=offset))
        by_frequency[str(omega)] = {
            "base": base,
            "rotated": rotated,
            "abs_delta": abs(base - rotated),
        }

    max_abs_delta = max(v["abs_delta"] for v in by_frequency.values()) if by_frequency else float("nan")
    return {
        "offset": offset,
        "tolerance": 1e-12,
        "by_frequency": by_frequency,
        "max_abs_delta": max_abs_delta,
        "pass": bool(max_abs_delta < 1e-12),
    }


def empirical_p_value_ge(observed: float, null_values: Sequence[float]) -> float:
    return (1 + sum(1 for value in null_values if value >= observed)) / (len(null_values) + 1)


def deterministic_hash(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def run_artifact(limit: int, replicates: int, seed: int) -> tuple[dict, dict]:
    start = time.time()

    primes = sieve_primes(limit)
    sequences = {
        "primes": primes,
        "all_integers": all_integers(limit),
        "cramer_bernoulli_seed0": cramer_bernoulli_sequence(limit, seed),
        "wheel_composite_count_matched_seed0": wheel_composite_control(limit, len(primes), seed),
    }

    statistics_by_sequence = {
        name: statistic_for_sequence(sequence)
        for name, sequence in sequences.items()
    }

    cramer_values = []
    wheel_values = []

    for b in range(replicates):
        cramer = cramer_bernoulli_sequence(limit, seed + 1000 + b)
        wheel = wheel_composite_control(limit, len(primes), seed + 2000 + b)
        cramer_values.append(statistic_for_sequence(cramer)["max_sqrt_n_v"])
        wheel_values.append(statistic_for_sequence(wheel)["max_sqrt_n_v"])

    observed = statistics_by_sequence["primes"]["max_sqrt_n_v"]

    deterministic_payload = {
        "artifact_id": ARTIFACT_ID,
        "registry_version": REGISTRY_VERSION,
        "claim_class": "empirical",
        "limit": limit,
        "fixture": limit == 10_000,
        "replicates": replicates,
        "seed": seed,
        "frequencies": DEFAULT_FREQUENCIES,
        "phase_map": "theta_omega(n) = frac(omega * log(n) / (2*pi))",
        "primary_statistic": "T(S) = max_omega sqrt(|S|) * KuiperUniform({theta_omega(n): n in S})",
        "sequences": {
            name: {"count": len(sequence)}
            for name, sequence in sequences.items()
        },
        "statistics": statistics_by_sequence,
        "null_distributions": {
            "cramer_bernoulli": {
                "replicates": replicates,
                "values": cramer_values,
                "mean": statistics.fmean(cramer_values) if cramer_values else None,
                "p_value_ge_prime": empirical_p_value_ge(observed, cramer_values),
            },
            "wheel_composite_count_matched": {
                "replicates": replicates,
                "values": wheel_values,
                "mean": statistics.fmean(wheel_values) if wheel_values else None,
                "p_value_ge_prime": empirical_p_value_ge(observed, wheel_values),
            },
        },
        "invariant_audit": {
            "rotation_invariance": rotation_invariance_audit(primes),
            "parity": {
                "applicable": False,
                "reason": "registry v0.1 phase statistic is not parity-sector decomposed",
            },
        },
        "basis_consistency": {
            "basis": "circular phase basis [0,1)",
            "analytic_target": "Uniform[0,1) only for one-sample Kuiper statistic; no RH-linked analytic target used",
            "comparison_rule": "all reported comparisons computed in same phase basis and same statistic",
        },
        "non_claim_boundary": [
            "not RH",
            "not GRH",
            "not asymptotic",
            "not zero-location",
            "not a residual-envelope theorem",
        ],
    }

    det_hash = deterministic_hash(deterministic_payload)

    result = {
        **deterministic_payload,
        "deterministic_result_sha256": det_hash,
        "runtime": {
            "seconds": time.time() - start,
            "python": sys.version,
            "platform": platform.platform(),
        },
    }

    receipt = {
        "artifact_id": ARTIFACT_ID,
        "registry_version": REGISTRY_VERSION,
        "claim_class": "empirical",
        "limit": limit,
        "replicates": replicates,
        "seed": seed,
        "deterministic_result_sha256": det_hash,
        "result_file": "phase_gate_results.json",
        "summary_file": "summary.md",
        "basis": deterministic_payload["basis_consistency"],
        "non_claim_boundary": deterministic_payload["non_claim_boundary"],
    }

    return result, receipt


def write_summary(result: dict, receipt: dict, out_dir: Path) -> None:
    stats = result["statistics"]
    nulls = result["null_distributions"]
    lines = [
        "# Candidate C Phase-Gate Run Summary",
        "",
        f"Registry version: `{result['registry_version']}`",
        f"Claim class: `{result['claim_class']}`",
        f"X: `{result['limit']}`",
        f"Replicates: `{result['replicates']}`",
        f"Deterministic hash: `{receipt['deterministic_result_sha256']}`",
        "",
        "## Sequence counts",
        "",
    ]
    for name, meta in result["sequences"].items():
        lines.append(f"- `{name}`: {meta['count']}")

    lines.extend([
        "",
        "## Primary statistic T(S)",
        "",
    ])
    for name, values in stats.items():
        lines.append(f"- `{name}`: {values['max_sqrt_n_v']}")

    lines.extend([
        "",
        "## Null gates",
        "",
        f"- Cramér-Bernoulli empirical p-value, `T(null) >= T(primes)`: {nulls['cramer_bernoulli']['p_value_ge_prime']}",
        f"- Wheel-composite empirical p-value, `T(null) >= T(primes)`: {nulls['wheel_composite_count_matched']['p_value_ge_prime']}",
        "",
        "## Invariant audit",
        "",
        f"- Rotation invariance pass: {result['invariant_audit']['rotation_invariance']['pass']}",
        f"- Rotation max abs delta: {result['invariant_audit']['rotation_invariance']['max_abs_delta']}",
        "",
        "## Non-claim boundary",
        "",
    ])
    for item in result["non_claim_boundary"]:
        lines.append(f"- {item}")

    (out_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--x", type=int, default=10_000, help="finite window upper bound")
    parser.add_argument("--replicates", type=int, default=16, help="Monte Carlo replicate count")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="base deterministic seed")
    parser.add_argument(
        "--artifact-dir",
        type=Path,
        default=Path("empirical-claims/phase-gate-null-X1e6/results/fixture"),
        help="output directory",
    )
    args = parser.parse_args()

    args.artifact_dir.mkdir(parents=True, exist_ok=True)

    result, receipt = run_artifact(limit=args.x, replicates=args.replicates, seed=args.seed)

    (args.artifact_dir / "phase_gate_results.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (args.artifact_dir / "pfk_receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_summary(result, receipt, args.artifact_dir)

    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
