# X1e6 Preliminary Artifact Policy

Status: preliminary finite-window empirical run.  
Registry: `phase-gate-v0.1`.  
Claim class: empirical.

## Policy decision

The full raw `phase_gate_results.json` for this preliminary `X=1_000_000`, `B=16` run is treated as **regenerable-only** rather than committed as canonical raw data.

The committed canonical artifacts for this preliminary run are:

- `summary.md`
- `pfk_receipt.json`

The full raw JSON is reproducible from the runner and the deterministic receipt hash below.

## Regeneration command

```bash
python3 scripts/run_phase_gate_candidate_c.py \
  --x 1000000 \
  --replicates 16 \
  --artifact-dir empirical-claims/phase-gate-null-X1e6/results/X1e6-preliminary-regenerated
```

## Expected deterministic hash

```text
729da4e129e6f76b61bcb109629490d566468ec3387db71a80fb66edfb023105
```

## Rationale

This run is preliminary. The fixture raw JSON is committed and remains the canonical replay anchor. The `X=1e6` run will be superseded by a stronger control run under issue #29 with higher Monte Carlo depth. Until then, the correct policy is to preserve the summary, receipt, regeneration command, and expected hash without pretending the preliminary raw output is final.

## Non-claim boundary

This artifact does not claim RH, GRH, an asymptotic theorem, zero-location control, residual-envelope control, or novelty.
