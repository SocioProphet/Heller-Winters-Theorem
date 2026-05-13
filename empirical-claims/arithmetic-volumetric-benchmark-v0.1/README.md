# Arithmetic Volumetric Benchmark v0.1 Artifact

Claim class: `definitional`.

Parent normalization: `prime-log-volume-spectral-normalization@0.1.0`.

This artifact defines a two-axis benchmark surface `Score(u,L)` for finite-window arithmetic signal volume. It is inspired by quantum-volume methodology only in the limited benchmarking sense: both approaches distinguish raw substrate size from usable signal-preserving volume.

It is not a quantum-volume benchmark, not a quantum hardware claim, not a quantum advantage claim, and not an RH/GRH claim.

Replay:

```bash
python3 scripts/check_arithmetic_volumetric_benchmark.py
python3 -m unittest discover -s tests -p test_arithmetic_volumetric_benchmark.py
```
