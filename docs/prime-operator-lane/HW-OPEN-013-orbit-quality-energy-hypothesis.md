# HW-OPEN-013 — Orbit Quality Energy Hypothesis

Status: pre-registered falsifiable hypothesis surface.  
Claim class: conjectural diagnostic / next-computation target, not theorem-grade analytic progress.  
Lane: prime/operator lane, orbit-quality / packet-energy surface.  
Depends on: `HW-PRIME-WEIL-011`, `HW-PRIME-WEIL-012`, `HW-PRIME-WEIL-014`.

## Purpose

This document states the next testable hypothesis after the finite packet hierarchy and non-cancelling fraction theorem.

The prior diagnostics show that raw variance is affected by two different mechanisms:

1. character-count dilution as the primorial tower grows;
2. orbit quality of the base-10 subgroup `<10>` inside each local unit group.

`HW-OPEN-013` asks whether a count-normalized energy statistic can detect orbit quality in a stable way across later prime layers.

## Coset interpretation

Let:

```text
H_q = <10> subset (Z/qZ)^x,
d_q = |H_q| = ord_q(10),
I_q = [(Z/qZ)^x : H_q] = (q-1)/d_q.
```

Cancelling characters are nontrivial on `H_q`. They probe within-coset fluctuations and cancel over complete base-10 orbits.

Non-cancelling characters are trivial on `H_q`. They probe between-coset fluctuations and detect whether some cosets of `H_q` receive systematically more prime weight than others.

Thus the orbit-quality signal should depend primarily on the orbit period `d_q` and quotient index `I_q`, not raw primorial character count.

## Pre-registered model

The pre-registered model for the non-cancelling/cancelling energy-per-character ratio is:

```text
R(q) = 1 + 0.3439 / d_q,
```

where:

```text
d_q = ord_q(10).
```

The constant `0.3439` is calibrated from the `p=11`, `K=4` finite diagnostic before the `q=37` measurement. The model is now fixed and must not be changed after the q=37 computation.

This is a falsifiable finite-diagnostic model. It is not a theorem.

## Pre-registered predictions

For `q=13`:

```text
d_13 = ord_13(10) = 6,
R(13) = 1 + 0.3439 / 6 = 1.057316666...
```

For `q=37`:

```text
d_37 = ord_37(10) = 3,
R(37) = 1 + 0.3439 / 3 = 1.114633333...
```

These predictions are committed before the q=37 measurement.

## First falsifiable target

The natural next test prime is:

```text
q = 37.
```

For `q=37`:

```text
ord_37(10) = 3,
I_37 = (37-1)/3 = 12,
n_nc(37) = 11.
```

This is a partial-orbit prime with a large local non-cancelling quotient.

The next computation should measure:

```text
E_nc(37,K) / E_cancel(37,K)
```

using the same count-normalized statistic as `HW-PRIME-WEIL-011` and compare it against the pre-registered value:

```text
R(37) = 1.114633333...
```

## Relation to p=11

For `q=11`:

```text
ord_11(10) = 2,
I_11 = 5,
n_nc(11) = 4.
```

`HW-PRIME-WEIL-011` and `HW-PRIME-WEIL-012` computed count-normalized p=11 packet energies. Those results provide the calibration point for the orbit-quality energy hypothesis.

The p=11 data also show finite prime-race fluctuation: the non-cancelling/cancelling ratio rises through `K=4` and then inverts at `K=5`. Therefore the hypothesis must be robust to finite-window oscillation and cannot be a monotone finite-depth law.

## What would count as support

A future test supports the hypothesis if:

1. the model function remains fixed before measurement;
2. the p=37 non-cancelling packet is computed with the same count-normalized statistic;
3. the measured p=37 value is within the declared tolerance of `1.114633333...`;
4. the result is stable under at least one additional depth or one additional partial-orbit prime;
5. the non-claim boundary remains intact.

## What would falsify or refine it

The hypothesis is falsified or requires refinement if:

1. the p=37 measured value is far from `1.114633333...`;
2. finite-window prime-race oscillations dominate the predicted orbit-quality signal;
3. `R(q)=1+0.3439/d_q` fails on a second partial-orbit prime;
4. full-orbit packets do not separate from partial-orbit packets under count normalization;
5. raw character-count effects re-enter after normalization.

## Relation to the proof barrier

Even if the orbit-quality hypothesis is supported numerically, it does not prove RH or GRH.

A proof would still require an unconditional asymptotic bound for the relevant character sums or packet energies. The orbit-quality hypothesis is a diagnostic and model-selection surface, not a proof of the square-root bound.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove the p=37 packet-energy prediction.

This document does not claim that orbit quality alone determines energy concentration.

This document does not claim that finite-depth packet-energy data imply asymptotic behavior.

This document does not close the square-root barrier.