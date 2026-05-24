# HW-OPEN-014 — Coset Variance Theorem Target

Status: open theorem target / proof-gate surface.  
Claim class: open analytic theorem target, not theorem-grade progress.  
Lane: prime/operator lane, coset-variance / packet-energy surface.  
Depends on: `HW-PRIME-WEIL-014`, `HW-PRIME-WEIL-015`, `HW-OPEN-013`.

## Purpose

This document states the precise coset-variance theorem target exposed by the q=37 measurement.

The q=37 result showed that the first pre-registered orbit-quality model failed as a finite predictor. The corrected problem is not to refit a curve. The corrected problem is to understand the variance of prime mass between and within cosets of the base-10 orbit subgroup.

This is the current native proof gate for the Prime-Weil route.

## Section 1 — Setup

Let `q` be a prime with `gcd(q,10)=1` and define:

```text
G_q = (Z/qZ)^x,
H_q = <10> subset G_q,
d_q = |H_q| = ord_q(10),
I_q = [G_q : H_q] = (q-1)/d_q.
```

Let the cosets of `H_q` in `G_q` be:

```text
C_1, ..., C_{I_q}.
```

For a Richter window `W_K`, define the residue mass:

```text
M_K(r) = sum_{p in W_K, p == r mod q} log p.
```

Define the window coset mass:

```text
F_K(C_i) = sum_{r in C_i} M_K(r).
```

The coset masses partition the active prime-log mass:

```text
sum_i F_K(C_i) = sum_{p in W_K, q not dividing p} log p.
```

Define between-coset variance:

```text
Var_between(q,K) = sum_i (F_K(C_i) - mean_C F_K)^2.
```

Define within-coset variance:

```text
Var_within(q,K) = sum_i sum_{r in C_i} (M_K(r) - mean_{r in C_i} M_K)^2.
```

Non-cancelling characters are trivial on `H_q`; they are Fourier modes on the quotient `G_q/H_q` and therefore probe between-coset variance.

Cancelling characters are nontrivial on `H_q`; they probe within-coset structure and cancel over complete base-10 orbits.

## Section 2 — The theorem target

The target is:

```text
Coset Variance Theorem (target):
Var_between(q,K) / Var_within(q,K) = O(K^A)
```

unconditionally as `K -> infinity`, for a fixed exponent `A` in the scoped families.

Under a GRH-shaped square-root model, both variances are expected to live at the critical scale and the ratio should remain polynomially bounded, plausibly approaching a stable range after normalization.

Unconditionally, current methods can allow the between-coset component to be much larger than the within-coset component. The desired theorem would need to show that the quotient coset structure of `<10>` forces enough equidistribution to prevent super-polynomial growth of the ratio.

This is not implied by the finite orbit theorem alone. It requires analytic control of primes in coset unions.

## Section 3 — Proposed attack methods

### Method A — Dispersion method

Apply a dispersion-method / Linnik-style second-moment analysis to prime-counting errors weighted by coset indicators.

Target object:

```text
sum_i (F_K(C_i) - mean_C F_K)^2.
```

Current status: classical dispersion methods can produce nontrivial cancellation in some averaged settings, but the fixed-coset, fixed-modulus, Richter-window target still faces the square-root barrier. The expected gap remains a power of the main scale.

### Method B — Large sieve over quotient characters

The quotient group:

```text
G_q / H_q
```

has exactly the non-cancelling characters as its nontrivial dual modes.

Apply a large-sieve style bound to quotient characters rather than all characters.

Current status: this correctly isolates the non-cancelling packet, but the large sieve is strongest over varying moduli. For a fixed q-quotient packet, it packages the obstruction rather than closing it.

### Method C — Pretentious character distance

Use Granville-Soundararajan style pretentious distance to measure whether coset indicators correlate with low-complexity characters that create bias.

Current status: the controlling obstruction depends on zeros of the associated Dirichlet L-functions near the critical region. This restates the same GRH-sensitive obstruction in pretentious language.

### Method D — Explicit formula surrogate at small K

Use computationally verified zeros and explicit-formula truncation to estimate the coset variance at finite depths.

Current status: this can certify finite ranges when the required height is within verification bounds. It does not provide an asymptotic proof, and it cannot reach large resonant tower depths with current verification heights.

## Current conclusion

Methods A-D identify the barrier in four languages:

1. dispersion;
2. quotient-character large sieve;
3. pretentious distance;
4. explicit formula truncation.

None currently closes the proof.

The target remains meaningful because it is now exact: prove that between-coset variance cannot outrun within-coset variance faster than a polynomial in `K` without assuming GRH.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the Coset Variance Theorem.

This document does not prove an unconditional variance bound.

This document does not prove that any of Methods A-D closes the square-root barrier.

This document does not claim that finite q=37 measurements imply asymptotic coset equidistribution.

This document does not close `HW-OPEN-010`, `HW-OPEN-012`, or the square-root barrier identified in `HW-PRIME-WEIL-005`.
