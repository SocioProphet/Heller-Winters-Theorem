# HW-OPEN-015 — Operator Domain and Essential Self-Adjointness Target

Status: open operator-domain theorem target.  
Claim class: finite operator facts plus infinite-domain obstruction map; not theorem-grade RH progress.  
Lane: prime/operator lane, Hilbert-Polya / operator-domain surface.  
Depends on: `HW-PRIME-FINITE-OPERATOR-001`, `HW-OPEN-005`, `HW-PRIME-WEIL-017`.

## Purpose

This document states Gate 3 of the Prime-Weil route: the operator-domain and essential-self-adjointness problem.

The finite operator has already been constructed and tested in:

```text
tools/check_finite_character_operator.py
```

The finite result is not the proof. In finite dimension, an inversion-symmetric real convolution kernel gives a self-adjoint matrix. The real problem is the infinite/profinite completion and whether the limiting operator has a canonical self-adjoint realization whose spectral bounds imply the needed variance control.

## Finite operator surface

For a finite unit group:

```text
G_P = (Z/PZ)^x,
H_P = l^2(G_P),
```

let `A_K(h)` be the prime-residue kernel in a Richter window or cutoff. The finite convolution operator is:

```text
(T_{P,K} f)(g) = sum_{h in G_P} A_K(h) f(g h).
```

With the standard inner product on `l^2(G_P)`, the adjoint is convolution by the inverse-reflected kernel:

```text
A_K^*(h) = conjugate(A_K(h^{-1})).
```

Thus `T_{P,K}` is self-adjoint in finite dimension iff:

```text
A_K(h) = conjugate(A_K(h^{-1}))
```

for all `h`.

The existing finite diagnostic enforces this by replacing the raw kernel with its inversion-symmetric part.

## Finite spectral facts

For finite abelian `G_P`, characters diagonalize convolution:

```text
T_{P,K} chi = lambda_chi chi.
```

The eigenvalue is:

```text
lambda_chi = sum_{h in G_P} A_K(h) chi(h).
```

If the kernel is real and inversion-symmetric, then the eigenvalues are real.

This is finite linear algebra. It does not prove any zero-location statement.

## Infinite completion target

The natural completion suggested by the finite tower is:

```text
H_infty = L^2(Z_hat^x, d mu_Haar)
```

or a closely related restricted/profinite completion compatible with the primorial system.

The infinite operator target is a formal convolution operator:

```text
(T_infty f)(g) = integral K(h) f(g h) d mu(h),
```

where `K` is the limiting arithmetic kernel obtained from prime-residue data after a specified regularization.

## Domain problem

The key open problem is to define a dense domain:

```text
D(T_infty) subset H_infty
```

such that:

1. finite-cylinder functions lie in `D(T_infty)`;
2. `T_infty D(T_infty) subset H_infty`;
3. `T_infty` is symmetric on `D(T_infty)`;
4. the adjoint `T_infty^*` is explicitly describable;
5. deficiency indices can be computed or bounded;
6. essential self-adjointness is proved or the obstruction is identified.

## Why this matters

If a canonical self-adjoint realization exists, then spectral radius and operator norm can be studied in a Hilbert-space framework rather than only through character-sum estimates.

However, self-adjointness alone is not enough. A proof route would still need a norm bound of the right scale:

```text
||T_{P,K}^perp|| = O(10^(K/2) poly(K)).
```

That bound is GRH-strength unless the operator structure supplies a new positivity or compactness mechanism.

## Current obstruction

The finite operator is self-adjoint after symmetrization, but the infinite kernel is not currently known to define a bounded or essentially self-adjoint operator on the proposed completion.

The obstruction is analytic:

- growth of the limiting kernel;
- choice of regularization;
- domain stability;
- adjoint-domain equality;
- spectral-radius bounds strong enough to imply the variance estimate.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not construct a Hilbert-Polya operator.

This document does not prove essential self-adjointness of `T_infty`.

This document does not prove an operator-norm bound at GRH scale.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.
