#!/usr/bin/env bash
set -euo pipefail

repo_root="$(pwd)"

if [[ ! -d ".git" ]]; then
  echo "Run this from the Heller-Winters repository root." >&2
  exit 1
fi

python3 tools/patch_programme_language.py || true

python3 scripts/run_phase_gate_candidate_c.py \
  --x 10000 \
  --replicates 16 \
  --artifact-dir empirical-claims/phase-gate-null-X1e6/results/replay-fixture

python3 tests/test_phase_gate_candidate_c.py

echo
echo "Candidate C capture applied and fixture replayed."
echo "Review with: git status && git diff --stat"
