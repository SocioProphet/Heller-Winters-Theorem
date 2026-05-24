# HW-OPEN-009 — Windowed Omega Theorem Target

Status: proof-target document.  
Claim class: open analytic theorem target / partial diagonal-moment route.  
Lane: prime/operator lane, fixed-modulus Richter-window variance route.  
Depends on: `HW-PRIME-WEIL-004`, `HW-PRIME-WEIL-005`, finite Parseval variance identity.

## Purpose

This document isolates the missing analytic input identified by `HW-PRIME-WEIL-004` and `HW-PRIME-WEIL-005`:

```text
windowed Omega behavior for Richter-window character sums.
```

The target is narrower than an unconditional variance bound and separable from the square-root-barrier question.

## Target statement

Let `chi` be a nontrivial Dirichlet character and suppose `L(s, chi)` has a zero:

```text
rho_0 = sigma_0 + i t_0,    sigma_0 > 1/2.
```

For Richter windows `W_K`, define:

```text
psi_{W_K}(chi)
```

as the Chebyshev-weighted character sum over the decimal digit-depth window.

The target is a subsequence/windowed Omega statement:

```text
|psi_{W_K}(chi)| >= c 10^(K sigma_0)
```

for infinitely many `K`, or preferably for a positive-density subsequence of `K`, with `c>0` depending on the character and the zero data.

This is weaker than pointwise dominance for all large `K` and is the correct input needed by the fixed-modulus Parseval variance route.

## Why this is the right target

`HW-PRIME-WEIL-005` records that the variance route needs an off-line-zero lower bound along the Richter windows.

The classical cumulative Omega theorem says that an off-line zero forces large oscillations in cumulative prime sums. The current obstacle is transferring that information to the fixed decimal/Richter window family.

The windowed Omega theorem is exactly this transfer.

## Explicit-formula window term

The Richter-window explicit formula has the model form:

```text
psi_{W_K}(chi)
  = sum_rho A_K(rho) + error_K
```

with:

```text
A_K(rho) = 10^((K-1)rho) (10^rho - 1) / rho.
```

For the selected off-line zero `rho_0`:

```text
|A_K(rho_0)| = C_0 10^(K sigma_0)
```

where:

```text
C_0 = 10^(-sigma_0) |10^rho_0 - 1| / |rho_0| > 0.
```

The goal is not to prove that this single term dominates pointwise for every `K`. The goal is to prove that the full window sum has Omega-size along sufficiently many windows.

## Path A — Direct phase route

The direct route studies the exponential polynomial formed by the zero terms:

```text
sum_rho c_rho 10^(K rho)
```

and attempts to show non-cancellation for infinitely many `K`.

This route can depend on phase properties of zero ordinates, such as rational independence or almost-periodicity arguments.

Status: open. This route is not needed if Path B succeeds.

## Path B — Cesaro / second-moment route

The promising route is to average the squared normalized window sum over `K`.

A target normalized second moment is:

```text
(1/N) sum_{K=1}^N |psi_{W_K}(chi)|^2 / 10^(2K sigma_0).
```

The diagonal contribution from `rho_0` is positive and has a geometric-series normalization. In the single-zero model, it gives a positive limiting lower contribution of the form:

```text
C_0^2 * positive_geometric_factor.
```

Therefore, in the single-dominant-zero model, the normalized second moment has positive lower density and implies:

```text
|psi_{W_K}(chi)| >= c 10^(K sigma_0)
```

for a positive-density subsequence of windows.

## What Path B still owes

The diagonal term is the correct spine, but theorem-grade promotion requires controlling the full mean square, not only writing the diagonal contribution.

Open obligations:

1. State the exact truncated/windowed explicit formula with error term.
2. Choose the zero set included in the second moment and justify truncation.
3. Prove that lower-real-part zeros are negligible after normalization.
4. Handle zeros with the same real part as `rho_0`, including conjugates and multiplicities.
5. Control off-diagonal cross terms in the Cesaro mean or prove a positive lower bound for the resulting exponential-polynomial mean square.
6. Show the explicit-formula error does not cancel the zero contribution at the normalized mean-square level.
7. Convert positive normalized second moment into an infinite or positive-density subsequence lower bound.

The key advantage of Path B is that it does not require pointwise phase control for every `K` and should not require irrationality assumptions if the mean-square lower bound is established directly.

## Relation to the variance route

If the windowed Omega theorem is proved, then an off-line zero gives:

```text
|psi_{W_K}(chi)| >= c 10^(K sigma_0)
```

along infinitely many windows. Parseval then gives:

```text
Var_P(W_K) >= (c^2 / |G_P|) 10^(2K sigma_0)
```

along that subsequence.

Combined with a hypothetical unconditional critical-scale variance bound:

```text
Var_P(W_K) = O_P(10^K K^A),
```

this would contradict `sigma_0 > 1/2`.

Thus this theorem target discharges the lower-bound side of the variance route. It does not by itself supply the missing unconditional upper bound.

## Status of the main barrier

`HW-PRIME-WEIL-005` remains the controlling barrier map.

Even if `HW-OPEN-009` is proved, the GRH proof still needs an unconditional critical-scale variance upper bound or another non-circular closure mechanism.

The windowed Omega theorem is necessary for the reverse direction of the variance characterization. It is not sufficient by itself to prove GRH.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the windowed Omega theorem.

This document does not prove the unconditional critical-scale variance bound.

This document does not close `HW-PRIME-WEIL-004` or `HW-PRIME-WEIL-005`.

This document does not construct a Hilbert-Polya operator.

This document does not promote the prime/operator lane to theorem-grade RH progress.
