# Prime Log-Volume Spectral Normalization v0.1 Artifact

Claim class: `definitional`.

This artifact captures the v0.1 normalization contract for multiplicative prime windows in the canonical coordinate `u = ln(x)`. It locks base gauge, window convention, mean-field subtraction, residual-channel distinction, and claim-boundary guardrails for finite-window empirical work.

Replay:

```bash
python3 scripts/check_log_volume_normalization.py
python3 -m unittest discover -s tests -p test_log_volume_normalization.py
```
