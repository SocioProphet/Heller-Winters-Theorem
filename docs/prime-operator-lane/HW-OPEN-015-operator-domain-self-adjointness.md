# HW-OPEN-015 — Operator Domain and Normal Spectral-Radius Target

Status: open operator-domain theorem target.  
Claim class: finite normal-operator facts plus infinite-domain obstruction map; not theorem-grade RH progress.  
Lane: prime/operator lane, Hilbert-Polya / operator-domain surface.  
Depends on: `HW-PRIME-FINITE-OPERATOR-001`, `HW-OPEN-005`, `HW-PRIME-WEIL-017`.

## Purpose

This document states Gate 3 of the Prime-Weil route in corrected operator language.

The earlier self-adjointness framing was too strong for the finite raw prime-residue operator. The finite convolution operator need not be self-adjoint because the raw prime-residue kernel need not satisfy:

```text
A_K(h) = conjugate(A_K(h^{-1})).
```

However, for finite abelian `G_P`, convolution operators are diagonalized by the character basis. Therefore the finite raw operator is normal:

```text
T_{P,K}^* T_{P,K} = T_{P,K} T_{P,K}^*.
```

The spectral theorem applies to normal operators. The proof gate is therefore not primarily self-adjointness. The proof gate is the spectral-radius/operator-norm bound.

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

The operator is self-adjoint iff:

```text
A_K(h) = conjugate(A_K(h^{-1}))
```

for all `h`.

The raw finite kernel generally fails this condition, so the raw operator is generally not self-adjoint.

## Finite normality fact

For finite abelian `G_P`, every convolution operator is diagonalized by the finite character basis:

```text
T_{P,K} chi = lambda_chi chi.
```

The eigenvalue is:

```text
lambda_chi = sum_{h in G_P} A_K(h) chi(h).
```

Because the same unitary Fourier basis diagonalizes `T_{P,K}` and `T_{P,K}^*`, finite convolution is normal.

Therefore:

```text
||T_{P,K}|| = max_chi |lambda_chi|.
```

For the nontrivial restriction:

```text
||T_{P,K}^perp|| = max_{chi != 1} |psi_{W_K}(chi)|.
```

This is the exact finite operator reformulation of the character-sum barrier.

## Correct Gate 3 statement

The operator route asks for an unconditional spectral-radius bound:

```text
||T_{P,K}^perp|| = O(10^(K/2) K^A).
```

In the current lane, this is equivalent to GRH-strength square-root cancellation for the associated character sums.

Thus the operator route is now a concrete normal-operator spectral-radius problem, not a vague Hilbert-Polya self-adjointness problem.

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

## Domain and normality problem

The key open problem is to define a dense domain:

```text
D(T_infty) subset H_infty
```

such that:

1. finite-cylinder functions lie in `D(T_infty)`;
2. `T_infty D(T_infty) subset H_infty`;
3. `T_infty` is closable;
4. the adjoint `T_infty^*` is explicitly describable;
5. the closure is normal, or the obstruction to normality is identified;
6. a spectral-radius/operator-norm bound at GRH scale is proved or the obstruction is identified.

Essential self-adjointness may still be useful for a symmetrized or transformed operator, but it is not the primary finite operator fact.

## Current obstruction

The finite operator is normal and explicitly diagonalized. This does not close the proof because the spectral-radius bound remains exactly the character-sum bound:

```text
max_{chi != 1} |psi_{W_K}(chi)| = O(10^(K/2) K^A).
```

The infinite obstruction is analytic:

- growth of the limiting kernel;
- choice of regularization;
- domain stability;
- adjoint-domain control;
- normality of the closure;
- spectral-radius bounds strong enough to imply the variance estimate.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not construct a Hilbert-Polya operator.

This document does not prove normality of an infinite limiting operator.

This document does not prove essential self-adjointness of any infinite operator.

This document does not prove an operator-norm bound at GRH scale.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.