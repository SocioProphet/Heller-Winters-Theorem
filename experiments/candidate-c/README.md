# Candidate C Native PFK Emission

Status: baseline loop-closure artifact.
Claim class: descriptive-grade infrastructure claim.

This experiment demonstrates that Candidate C can emit PFK-compatible receipts against the Heller-Godel canonical PFK surface at:

```text
SocioProphet/Heller-Godel @ 0ef1cab4c525fd004e38fa9a92f7e911acbbc976
```

## Scope

This is the baseline log-phase phase-gate only. It does not include arithmetic-coupled refinements.

The run uses:

```text
X = 10000
frequencies = {1, 2, 3}
seed = 20260510
```

## Receipts

```text
receipts/event_ir/candidate_c_baseline_events.json
receipts/proof_artifacts/candidate_c_baseline_proof_artifact.json
receipts/calibration_bundles/candidate_c_baseline_calibration_bundle.json
receipts/claim_ledger.jsonl
```

## Replay

```bash
python3 experiments/candidate-c/run.py --output-dir /tmp/candidate-c-pfk
python3 tests/test_candidate_c_emission.py
```

## Non-claims

This artifact does not claim RH, GRH, zero-location control, residual-envelope control, asymptotic convergence, or statistical novelty. It proves only that the native PFK receipt loop can close for Candidate C.
