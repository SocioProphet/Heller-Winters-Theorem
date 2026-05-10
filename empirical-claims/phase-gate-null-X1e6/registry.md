# Phase Wα Registry Lock

Status: locked scaffold.

## Locked objects

### Sequence domain

Primary target:

```text
P(X) = {p prime : p <= X}
```

with

```text
X = 1e6.
```

### Alternate substrates

1. All integers.
2. Density-matched Poisson-thinned surrogate.
3. Wheel-preserving composite surrogate.

### Canonical coordinate

```math
u = \log x.
```

### Phase variable

All implementations must use the same declared phase map.

No implementation may redefine the phase operator locally.

### Circular-distance convention

All Kuiper/circular statistics must use the same orientation and wrap convention.

### Window discipline

Finite-window only.

No asymptotic language permitted.

### Statistic family

Primary statistic family:

- Kuiper statistic,
- circular discrepancy,
- rotationally-invariant residual.

### Basis declaration

All empirical and analytic comparisons must occur in the same declared basis.

### Normalization

Normalization constants must be declared once and reused globally.

No chapter-local normalization drift permitted.

## Registry freeze condition

After implementation begins:

- no statistic substitution,
- no window substitution,
- no normalization substitution,
- no convention substitution

without incrementing the registry version.
