#!/usr/bin/env python3
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "fixture"
        subprocess.run(
            [
                sys.executable,
                "scripts/run_phase_gate_candidate_c.py",
                "--x",
                "10000",
                "--replicates",
                "16",
                "--artifact-dir",
                str(out),
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        result = json.loads((out / "phase_gate_results.json").read_text())
        receipt = json.loads((out / "pfk_receipt.json").read_text())

        assert result["sequences"]["primes"]["count"] == 1229
        assert math.isclose(
            result["statistics"]["primes"]["max_sqrt_n_v"],
            18.00325097589416,
            rel_tol=0.0,
            abs_tol=1e-12,
        )
        assert result["invariant_audit"]["rotation_invariance"]["pass"] is True
        assert receipt["deterministic_result_sha256"] == result["deterministic_result_sha256"]
        assert receipt["deterministic_result_sha256"] == "ab70a276f21fae3e6d3b5e16ba08378c23d0d6a08574784b6e798ae51c3f7c2b"

    print("Candidate C fixture replay test passed.")


if __name__ == "__main__":
    main()
