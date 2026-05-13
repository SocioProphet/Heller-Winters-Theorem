#!/usr/bin/env python3
"""Arithmetic Volumetric Surface Runner v0.2.

Finite-window empirical runner for Score(u,L). This is not a theorem,
not quantum-volume equivalence, and not a quantum-advantage claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
import time
from pathlib import Path
from typing import Sequence

REGISTRY_PATH = Path("empirical-claims/arithmetic-volumetric-benchmark-v0.2/registry.json")
DEFAULT_ARTIFACT_DIR = Path("empirical-claims/arithmetic-volumetric-benchmark-v0.2/results/fixture")


def parse_float_csv(text: str) -> list[float]:
    values = [float(part.strip()) for part in text.split(",") if part.strip()]
    if not values:
        raise argparse.ArgumentTypeError("expected at least one numeric value")
    if any(value <= 0.0 for value in values):
        raise argparse.ArgumentTypeError("all values must be positive")
    return values


def canonical_json_sha256(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def corrected_mean_field(u: float, L: float) -> float:
    if u <= 0.0 or L <= 0.0:
        raise ValueError("u and L must be positive")
    leading = math.exp(u) / u * (math.exp(L) - 1.0)
    correction = math.exp(u) / (u * u) * (((L - 1.0) * math.exp(L)) + 1.0)
    return leading - correction


def benchmark_score(u: float, L: float) -> float:
    mf = corrected_mean_field(u, L)
    if mf < 0.0:
        raise ValueError(f"corrected mean field must be non-negative, got {mf}")
    return math.log1p(mf) / (1.0 + u * L)


def build_surface(u_values: Sequence[float], L_values: Sequence[float]) -> dict:
    cells = []
    for u in u_values:
        for L in L_values:
            mf = corrected_mean_field(u, L)
            cells.append({
                "u": u,
                "L": L,
                "x_start": math.exp(u),
                "x_end": math.exp(u + L),
                "corrected_mean_field": mf,
                "score": benchmark_score(u, L),
            })
    scores = [cell["score"] for cell in cells]
    return {
        "axes": {"u_values": list(u_values), "L_values": list(L_values)},
        "cells": cells,
        "summary": {
            "cell_count": len(cells),
            "score_min": min(scores),
            "score_max": max(scores),
            "score_mean": sum(scores) / len(scores),
        },
    }


def runtime_metadata(start_time: float, deterministic_runtime: bool) -> dict:
    if deterministic_runtime:
        return {
            "seconds": 0.0,
            "python": "deterministic-fixture",
            "platform": "deterministic-fixture",
        }
    return {
        "seconds": time.time() - start_time,
        "python": sys.version,
        "platform": platform.platform(),
    }


def write_outputs(result: dict, receipt: dict, artifact_dir: Path) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "surface.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (artifact_dir / "pfk_receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = result["surface"]["summary"]
    lines = [
        "# Arithmetic Volumetric Surface Run Summary",
        "",
        f"Artifact: `{result['artifact_id']}@{result['artifact_version']}`",
        f"Claim class: `{result['claim_class']}`",
        f"Deterministic hash: `{receipt['deterministic_result_sha256']}`",
        "",
        "## Surface summary",
        "",
        f"- cells: {summary['cell_count']}",
        f"- score min: {summary['score_min']}",
        f"- score max: {summary['score_max']}",
        f"- score mean: {summary['score_mean']}",
        "",
        "## Non-claim boundary",
        "",
    ]
    lines.extend(f"- {item}" for item in receipt["non_claim_boundary"])
    (artifact_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_surface(
    u_values: Sequence[float],
    L_values: Sequence[float],
    artifact_dir: Path,
    deterministic_runtime: bool = False,
) -> tuple[dict, dict]:
    start = time.time()
    registry = load_registry()
    deterministic_payload = {
        "artifact_id": registry["artifact_id"],
        "artifact_version": registry["artifact_version"],
        "claim_class": registry["claim_class"],
        "parent_benchmark": registry["parent_benchmark"],
        "parent_normalization": registry["parent_normalization"],
        "score_policy": registry["score_policy"],
        "claim_boundary": registry["claim_boundary"],
        "surface": build_surface(u_values, L_values),
    }
    digest = canonical_json_sha256(deterministic_payload)
    result = {
        **deterministic_payload,
        "deterministic_result_sha256": digest,
        "runtime": runtime_metadata(start, deterministic_runtime),
    }
    receipt = {
        "artifact_id": registry["artifact_id"],
        "artifact_version": registry["artifact_version"],
        "claim_class": registry["claim_class"],
        "deterministic_result_sha256": digest,
        "result_file": "surface.json",
        "summary_file": "summary.md",
        "runtime_mode": "deterministic-fixture" if deterministic_runtime else "observed-runtime",
        "non_claim_boundary": registry["claim_boundary"]["disallowed"],
    }
    write_outputs(result, receipt, artifact_dir)
    return result, receipt


def main() -> None:
    registry = load_registry()
    defaults = registry["default_grid"]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--u-values", type=parse_float_csv, default=defaults["u_values"])
    parser.add_argument("--L-values", type=parse_float_csv, default=defaults["L_values"])
    parser.add_argument("--artifact-dir", type=Path, default=DEFAULT_ARTIFACT_DIR)
    parser.add_argument(
        "--deterministic-runtime",
        action="store_true",
        help="write stable fixture runtime metadata for committed canonical outputs",
    )
    args = parser.parse_args()
    _, receipt = run_surface(
        args.u_values,
        args.L_values,
        args.artifact_dir,
        deterministic_runtime=args.deterministic_runtime,
    )
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
