# Arithmetic Volumetric Surface Runner v0.2

Claim class: `empirical`.

This artifact upgrades Arithmetic Volumetric Benchmark v0.1 from a definitional benchmark surface into an executable finite-window surface runner.

It generates a deterministic `Score(u,L)` grid over declared log-volume windows and emits:

```text
surface.json
summary.md
pfk_receipt.json
```

The score is finite-window instrumentation only. It is not theorem strength, not quantum volume, not a quantum hardware benchmark, not a quantum advantage claim, and not an RH/GRH claim.

Replay:

```bash
python3 scripts/run_arithmetic_volumetric_surface.py --artifact-dir empirical-claims/arithmetic-volumetric-benchmark-v0.2/results/fixture
python3 -m unittest discover -s tests -p test_arithmetic_volumetric_surface.py
```
