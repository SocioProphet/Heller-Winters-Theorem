# HW-PRIME-WEIL-008 — Geometric Chain and Barrier Location

Status: geometric barrier map / finite arithmetic visualization.  
Claim class: theorem-grade for the stated elementary identities; method-grade for the geometry dictionary.  
Lane: prime/operator lane, Richter-window / digit-cycle / variance-barrier surface.  
Depends on: `HW-PRIME-WEIL-005`, `HW-PRIME-WEIL-006`, `HW-PRIME-WEIL-007`.

## Purpose

This document records the geometric chain exposed by the Richter-window variance route, the base-10 orbit classification, and the Midy/complementary-pairs digit-sum law.

The exact content is elementary:

1. the unit circle and unit hyperbola are tangent at `(1,0)`;
2. the critical-line normalization `delta = 0` removes hyperbolic amplitude growth;
3. off-critical zeros introduce a hyperbolic amplitude factor;
4. even-period repetends split into complementary digit pairs under the Midy/complementary-pairs law;
5. base-10 full-orbit primes give complete finite Fourier cancellation over digit cycles.

The Poincare/Rodin language is a structural visualization of these exact arithmetic and analytic facts. It is not a proof of RH or GRH.

## Exact tangency

Parametrize the Euclidean unit circle by:

```text
C(theta) = (cos theta, sin theta).
```

At `theta=0`:

```text
C(0) = (1,0),
C'(0) = (0,1).
```

Parametrize the right branch of the unit hyperbola by:

```text
H(u) = (cosh u, sinh u).
```

At `u=0`:

```text
H(0) = (1,0),
H'(0) = (0,1).
```

Thus the unit circle and the unit hyperbola share the point `(1,0)` and the same tangent direction there.

This tangency is exact.

## Critical-line normalization

For a zero contribution with:

```text
rho = 1/2 + delta + i t,
```

write `x=e^u`. Then:

```text
x^rho / x^(1/2) = exp(delta u) exp(i t u).
```

When `delta = 0`, the normalized contribution is pure oscillation:

```text
exp(i t u) = cos(tu) + i sin(tu),
```

which lies on the Euclidean unit circle.

When `delta > 0`, the normalized contribution has amplitude:

```text
exp(delta u).
```

The amplitude can be written in hyperbolic coordinates:

```text
exp(delta u) = cosh(delta u) + sinh(delta u),
```

with:

```text
cosh^2(delta u) - sinh^2(delta u) = 1.
```

Thus the off-critical amplitude is exactly parameterized by the unit hyperbola.

This is the analytic meaning of the Euclidean-to-hyperbolic transition in this lane.

## Three structural regimes

The following table is a structural dictionary, not a literal Poincare-disk placement theorem.

| Regime | Orbit/digit structure | Analytic geometry | Rodin/mod-9 analogue |
|---|---|---|---|
| inside / center-like | `1/9`: trivial fixed digit `1`; no orbit | no amplitude growth | node `9` as fixed-axis picture |
| boundary / reset | `1/10`: base terminates; no unit orbit | tangency/reset surface | 9-node circle as boundary bookkeeping |
| outside / active orbit | `1/11`, `1/7`, `1/19`: nontrivial periods | hyperbolic amplitude appears when `delta>0` | active unit circuit `{1,2,4,8,7,5}` |

This table organizes analogies. The exact statements are the orbit classifications, digit-pair law, and hyperbolic amplitude parametrization above.

## Correct Poincare-disk language

The standard Poincare disk has hyperbolic space inside the disk and an ideal boundary circle.

The Rodin active circuit is not literally a geodesic on the boundary. Boundary paths are not geodesics in the interior metric. The correct statement is:

```text
The active mod-9 unit cycle is a finite sample of the ideal-boundary circle in the visualization dictionary.
```

Similarly, the Rodin axis `{3,6,9}` should not be called a Euclidean diameter as a theorem. The controlled visualization is:

```text
{3,6,9} is treated as a central-geodesic analogue, with node 9 as center/fixed-point bookkeeping.
```

This is geometry-language hygiene. It prevents a finite digit diagram from being promoted into a hyperbolic-geometry theorem.

## Midy / complementary-pairs layer

For even-period decimal repetends in the current prime examples, the repeating block splits into complementary digit pairs summing to `9`.

The digit-sum law is:

```text
digit_sum(1/p) = 9 * ord_p(10) / 2.
```

Examples:

| Fraction | Period | Digit sum | Interpretation |
|---|---:|---:|---|
| `1/9` | 1 | `1` | fixed identity digit |
| `1/10` | terminates | — | base reset |
| `1/11` | 2 | `9` | one complementary pair |
| `1/13` | 6 | `27` | three complementary pairs |
| `1/17` | 16 | `72` | eight complementary pairs |
| `1/19` | 18 | `81 = 9^2` | nine complementary pairs |

For `1/19`, the period is `18`, hence there are `9` complementary pairs, each summing to `9`. The digit sum is therefore `81`.

This is theorem-grade finite decimal arithmetic, not an analytic prime-distribution result.

## Character-sum duality

The digit-pair law and the finite character-cancellation theorem are dual descriptions of orbit balance.

Digit statement:

```text
repetend digits balance into complementary pairs around the base-10 midpoint.
```

Fourier statement:

```text
sum_{h in <10>} chi(h) = 0 unless chi is trivial on <10>.
```

For Category 3 primes, `<10>` is the full unit group, so every nontrivial character cancels over the complete digit orbit.

The actual Richter-window character sum is harder because primes in a value window do not arrive in deterministic digit-cycle order. This is why `HW-OPEN-010` remains open.

## Square-root barrier geometry

The variance route tracks whether the finite character-sum observable remains at critical-line scale.

Critical-line scale:

```text
delta = 0,
|x^rho / x^(1/2)| = 1.
```

Off-critical scale:

```text
delta > 0,
|x^rho / x^(1/2)| = exp(delta log x).
```

The square-root barrier is therefore the analytic boundary between:

```text
Euclidean oscillation at delta=0
```

and:

```text
hyperbolic amplitude growth at delta>0.
```

Proving that the Richter-window variance remains at critical-line scale would prove that no zero contributes hyperbolic amplitude growth. That is RH/GRH-strength. This document only locates the barrier geometrically; it does not cross it.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove that Rodin diagrams, digital-root geometry, torus winding, or Poincare-disk visualizations imply analytic number theory results.

This document does not claim the Rodin active circuit is literally a hyperbolic geodesic.

This document does not claim the Rodin axis is literally a Poincare-disk diameter theorem.

This document does not close the finite-to-asymptotic transition problem in `HW-OPEN-010`.

This document does not close the square-root barrier in `HW-PRIME-WEIL-005`.
