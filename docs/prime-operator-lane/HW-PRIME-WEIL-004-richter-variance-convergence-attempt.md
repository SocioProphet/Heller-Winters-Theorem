# HW-PRIME-WEIL-004 — Richter Variance Convergence Attempt

Status: proof-attempt / analytic-obligation surface.  
Claim class: conjectural / proof obligation, not theorem-grade.  
Lane: prime/operator lane, Weil-positivity / fixed-modulus variance route.  
Depends on: `HW-PRIME-WEIL-003`, `HW-OPEN-008`, finite Parseval variance identity.

## Purpose

This document captures the proposed closing mechanism for the fixed-modulus Richter-window variance route.

The proposed mechanism combines:

1. the exact finite Parseval variance identity;
2. an explicit-formula lower-bound mechanism for an off-line zero;
3. an upper-bound profile when all relevant zeros lie on the critical line.

This document does not prove RH or GRH. It records the proposed convergence theorem and the analytic obligations that must be discharged before any promotion is possible.

## Setup

For a fixed modulus `P`, let `G_P` be the finite character group and let `W_K` be the Richter window.

The finite Parseval variance identity is:

```text
Var_P(W_K) = (1 / |G_P|) sum_{chi != 1} |psi_{W_K}(chi)|^2
```

The proposed explicit formula for a nontrivial character `chi` is:

```text
psi_{W_K}(chi)
  = sum_rho [ 10^((K-1)rho) (10^rho - 1) / rho ] + O(K^2)
```

where the sum ranges over the nontrivial zeros of `L(s, chi)`, with the usual explicit-formula convention and truncation/regularization obligations left explicit below.

## Proposed contradiction skeleton

Suppose an off-line zero exists:

```text
rho_0 = sigma_0 + i t_0,  sigma_0 > 1/2.
```

The corresponding zero contribution has magnitude:

```text
|A_K(rho_0)|
  = |10^((K-1)rho_0)(10^rho_0 - 1) / rho_0|
  = C_0 10^(K sigma_0)
```

where:

```text
C_0 = 10^(-sigma_0) |10^rho_0 - 1| / |rho_0| > 0.
```

If one could prove a usable lower bound:

```text
|psi_{W_K}(chi)| >= c 10^(K sigma_0)
```

for infinitely many `K`, or for all sufficiently large `K`, then Parseval gives:

```text
Var_P(W_K) >= (c^2 / |G_P|) 10^(2K sigma_0).
```

Under the critical-line explicit-formula upper-bound profile one expects:

```text
|psi_{W_K}(chi)| = O(10^(K/2) K^2)
```

and hence:

```text
Var_P(W_K) = O(|G_P| 10^K K^4).
```

Since `2 sigma_0 > 1`, the exponential factor:

```text
10^(K(2 sigma_0 - 1))
```

beats every polynomial in `K`. This is the intended contradiction engine.

## Classical input candidate: Omega theorem

The proposed closing input is a Cramer-Ingham / Landau-style Omega theorem for explicit-formula sums:

```text
If L(s, chi) has a zero rho_0 with Re(rho_0)=sigma_0>1/2,
then psi(x, chi) = Omega(x^sigma_0).
```

Windowed target:

```text
psi_{W_K}(chi) = Omega(10^(K sigma_0))
```

A windowed Omega theorem of this form would be sufficient to force the lower-bound side of the Parseval variance route along a subsequence of `K`.

Pointwise lower bounds for all sufficiently large `K` are stronger than Omega and are not established by the cited Omega input alone.

## Critical blockers

### B0 — Omega is not pointwise dominance

The classical Omega conclusion supplies infinitely many large values, not a pointwise lower bound for every sufficiently large window.

Blocked claim:

```text
|psi_{W_K}(chi)| >= c 10^(K sigma_0) for all large K
```

The admissible target is weaker unless separately proved:

```text
|psi_{W_K}(chi)| >= c 10^(K sigma_0) along an infinite subsequence of K.
```

The variance contradiction must be reformulated to use the subsequence version, or a separate pointwise dominance lemma must be proved.

### B1 — Maximal-real-part isolation is not automatic

The draft argument chooses a zero with maximal real part `sigma_0` and separates all other zero contributions as lower-order terms.

This requires a precise isolation statement. The supremum of real parts of off-line zeros need not be attained globally without additional restrictions. Even if a zero `rho_0` is chosen, there may be zeros with larger real part or sequences of real parts approaching a supremum.

Acceptable alternatives:

1. work with a chosen zero and control all zeros with larger real part;
2. prove a strip-local maximal zero statement under a finite-height truncation;
3. use an Omega theorem that avoids isolating one globally maximal zero.

### B2 — Same-line and near-line cancellation

Even if a zero `rho_0` has maximal real part in a controlled region, other zeros with the same real part, conjugate zeros, or near-maximal real part may contribute oscillatory terms of comparable size.

A triangle-inequality lower bound:

```text
|main term + other terms| >= |main term| - |other terms|
```

is only useful after proving the other terms are strictly lower order or non-cancelling. This is not automatic.

A valid proof needs one of:

1. an Omega theorem already incorporating cancellation;
2. a non-cancellation lemma for the windowed zero sum;
3. a subsequence selection argument controlling phases.

### B3 — Zero-density input alone is not enough

Zero-density estimates can bound the number of zeros in regions, but they do not by themselves prevent cancellation or prove pointwise dominance.

The proposed obligation:

```text
sum_{rho != rho_0} |A_K(rho)| = O(10^(K(sigma_0 - epsilon)))
```

requires an actual gap in real parts away from `sigma_0`, plus a summable height-weight estimate. A general density theorem does not imply such a fixed epsilon gap unless the region and zero selection have already supplied it.

### B4 — GRH upper bound cannot be used inside the contradiction as stated

The contradiction skeleton compares an off-line-zero lower bound against a critical-line upper-bound profile.

This is valid only if the upper-bound profile is derived for the same object under a hypothesis that excludes the off-line zero. As a proof by contradiction, one must phrase the upper bound as the target theorem's implication, not as an independently available bound while assuming an off-line zero.

The correct form is:

```text
If all zeros for the relevant character lie on Re(s)=1/2, then Var_P(W_K)=O(10^K K^4).
```

This does not directly contradict the off-line lower bound unless the same variance is otherwise known to satisfy the upper bound unconditionally. Therefore the route needs an unconditional variance upper bound, or a different logical closure.

## Obligations recorded from the draft

### Obligation A — Supremum / maximal-zero handling

Original draft obligation:

```text
Show that the supremum of real parts is attained, or replace the argument by a local/truncated maximal-zero argument.
```

Current status: open. A compactness/discreteness argument is available only on bounded-height rectangles. A global maximal real part requires further justification or should be avoided.

### Obligation B — Remainder zero-sum control

Original draft obligation:

```text
Bound the contribution of all other zeros below the selected real part using density and height estimates.
```

Current status: open. A density estimate alone does not prove the required lower-order bound unless an isolation gap or phase/non-cancellation mechanism is supplied.

## Revised proof obligation map

To promote `HW-PRIME-WEIL-004`, the following must be supplied:

1. a precise windowed explicit formula with all truncation and endpoint errors declared;
2. a valid Omega or lower-bound theorem for the Richter window sum;
3. a logical closure that does not compare an off-line-zero assumption to a GRH-only upper bound unless an unconditional upper bound is available;
4. a cancellation-safe treatment of all zero contributions;
5. a finite-modulus Parseval transfer from character lower bounds into variance lower bounds;
6. a claim-grade ledger entry specifying exactly whether the result is RH, GRH for one character, or a conditional diagnostic.

## Current safe theorem-candidate statement

Safe candidate, not proved here:

```text
If a windowed Omega lower bound of size 10^(K sigma_0) is established for a character sum psi_{W_K}(chi) from an off-critical zero with sigma_0>1/2, and if an unconditional variance upper bound of critical-line size is also available for the same windows, then the Parseval variance identity gives an exponential-vs-polynomial contradiction.
```

This is a conditional convergence mechanism, not a proof of RH.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove a windowed Omega theorem.

This document does not prove a pointwise lower bound for all large `K`.

This document does not prove cancellation control for same-real-part or near-maximal zeros.

This document does not close `HW-OPEN-001` or construct a Hilbert-Polya operator.

This document does not promote the prime/operator lane to a completed theorem.
