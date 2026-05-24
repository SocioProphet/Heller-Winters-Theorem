# HW-OPEN-013 — Orbit Quality Energy Hypothesis

Status: open falsifiable hypothesis surface.  
Claim class: conjectural diagnostic / next-computation target, not theorem-grade analytic progress.  
Lane: prime/operator lane, orbit-quality / packet-energy surface.  
Depends on: `HW-PRIME-WEIL-011`, `HW-PRIME-WEIL-012`, `HW-PRIME-WEIL-014`.

## Purpose

This document states the next testable hypothesis after the finite packet hierarchy and non-cancelling fraction theorem.

The prior diagnostics show that raw variance is affected by two different mechanisms:

1. character-count dilution as the primorial tower grows;
2. orbit quality of the base-10 subgroup `<10>` inside each local unit group.

`HW-OPEN-013` asks whether a count-normalized energy statistic can detect orbit quality in a stable way across later prime layers.

## Hypothesis shape

Let `q` be a prime with `gcd(q,10)=1`, and let:

```text
d_q = ord_q(10),
I_q = (q-1) / d_q.
```

The local non-cancelling character count is:

```text
n_nc(q) = I_q - 1.
```

For the non-cancelling packet at the `q` layer, define count-normalized energy:

```text
E_nc(q,K) = (sum_{chi in NC(q)} |psi_{W_K}(chi)|^2) / |NC(q)|.
```

The orbit-quality hypothesis is that, after removing raw character-count growth, `E_nc(q,K)` is controlled by a function of the orbit quotient index `I_q` and the orbit period `d_q`, rather than by the size of the primorial character group alone.

A future PR must choose an explicit model function, for example:

```text
E_nc(q,K) ~ F(K, I_q, d_q)
```

and then test it against computed data.

This document does not select a final model function because the numerical prediction in the current discussion was redacted. The next computation must supply it explicitly.

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
E_nc(37,K)
```

at the deepest feasible Richter windows and compare it with the model prediction selected for `F`.

The hypothesis becomes meaningful only when the predicted value and measured value are both committed and CI-checked.

## Relation to p=11

For `q=11`:

```text
ord_11(10) = 2,
I_11 = 5,
n_nc(11) = 4.
```

`HW-PRIME-WEIL-011` and `HW-PRIME-WEIL-012` computed count-normalized p=11 packet energies. Those results provide the first calibration point for the orbit-quality energy hypothesis.

The p=11 data also show finite prime-race fluctuation: the non-cancelling/cancelling ratio rises through `K=4` and then inverts at `K=5`. Therefore the hypothesis must be robust to finite-window oscillation and cannot be a monotone finite-depth law.

## What would count as support

A future test supports the hypothesis if:

1. the model function `F` is fixed before measurement;
2. the p=37 non-cancelling packet is computed with the same count-normalized statistic;
3. the measured p=37 value is within the declared tolerance of the predicted value;
4. the result is stable under at least one additional depth or one additional partial-orbit prime;
5. the non-claim boundary remains intact.

## What would falsify or refine it

The hypothesis is falsified or requires refinement if:

1. the p=37 measured value is far from the declared prediction;
2. finite-window prime-race oscillations dominate the predicted orbit-quality signal;
3. the chosen `F(K,I_q,d_q)` fails on a second partial-orbit prime;
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

This document does not prove a p=37 packet-energy prediction.

This document does not claim that orbit quality alone determines energy concentration.

This document does not claim that finite-depth packet-energy data imply asymptotic behavior.

This document does not close the square-root barrier.
