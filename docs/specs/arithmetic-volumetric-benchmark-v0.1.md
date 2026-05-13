# Arithmetic Volumetric Benchmark v0.1

Status: definitional / empirical-harness benchmark. Claim class: definitional.

This specification defines a two-axis arithmetic benchmark surface inspired by quantum-volume methodology. It is a benchmarking analogy only, not quantum volume and not a quantum hardware claim.

## Axes

The surface is indexed by:

```text
u = logarithmic scale location
L = multiplicative window width
Score(u,L) = finite-window benchmark score
```

The canonical window is inherited from Prime Log-Volume Spectral Normalization v0.1:

```text
W(u,L) = [exp(u), exp(u+L)]
```

A compliant artifact must keep the two-axis surface explicit and must not collapse it to one scalar unless a scalarization rule is declared.

## Quantum-volume relation

Quantum volume asks how much circuit width/depth can be executed before noise destroys useful signal. Arithmetic volumetric benchmarking asks how much multiplicative arithmetic window structure remains after canonical mean-field subtraction and residual normalization.

The analogy map is:

```text
quantum width/depth        -> arithmetic u/L surface
hardware noise            -> density drift and normalization error
successful circuit volume -> replayable residual signal volume
```

## Claim boundary

This is not equivalent to quantum volume. It is not a quantum hardware benchmark, not a quantum advantage claim, and not an RH/GRH claim. Any later mapping to quantum circuits requires a separate compiler/runtime artifact.
