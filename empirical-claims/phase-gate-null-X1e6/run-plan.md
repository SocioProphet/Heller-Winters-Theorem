# Candidate C Run Plan

Status: executable.

## Local fixture replay

```bash
python3 scripts/run_phase_gate_candidate_c.py \
  --x 10000 \
  --replicates 16 \
  --artifact-dir empirical-claims/phase-gate-null-X1e6/results/replay-fixture
```

Compare:

```text
results/replay-fixture/pfk_receipt.json
results/fixture/pfk_receipt.json
```

The field to compare is:

```text
deterministic_result_sha256
```

## Production-scale replay

```bash
python3 scripts/run_phase_gate_candidate_c.py \
  --x 1000000 \
  --replicates 16 \
  --artifact-dir empirical-claims/phase-gate-null-X1e6/results/X1e6-replay
```

## Promotion block

Even if replay succeeds, Candidate C remains empirical until:

1. the literature check is complete,
2. the formal statement is written,
3. the theorem/proof status is reviewed,
4. the claim ledger is updated.
