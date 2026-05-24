# HW-PRIME-PROFINITE-001 — Profinite Inductive Limit

Identifier: `HW-PRIME-PROFINITE-001`  
Status: finite-to-profinite completion diagnostic  
Claim class: governance / finite-infinite boundary tracking  
Mathematical content added by this document: scoped construction and open-problem framing only

This document records the primorial inductive system, its profinite completion, and the open essential-self-adjointness question for the prime-operator lane.

It does not construct a Hilbert-Pólya operator and does not prove RH or GRH.

## 1. The primorial inductive system

Let

```text
P_k = product of the first k primes.
```

The primorial sequence gives finite unit groups

```text
G_{P_k} = (Z/P_k Z)^x.
```

Reduction modulo `P_k` gives surjective group homomorphisms

```text
G_{P_{k+1}} ->> G_{P_k}.
```

The dual Hilbert-space direction is injective:

```text
H_{P_k} -> H_{P_{k+1}}.
```

A function `f in H_{P_k}` lifts to `f_tilde in H_{P_{k+1}}` by

```text
f_tilde(g) = f(g mod P_k).
```

Thus the lift is constant on fibers of the reduction map `G_{P_{k+1}} -> G_{P_k}`.

The finite operators `T_{P_k}` are compatible along the system: `T_{P_{k+1}}` restricted to functions constant on fibers of the surjection recovers `T_{P_k}` at the lower level, up to the declared finite-cutoff normalization and tail terms.

## 2. The profinite completion

The inverse limit of the surjective system is the profinite completion of the finite unit-group tower:

```text
Z_hat^x = varprojlim_k G_{P_k}.
```

This is a compact profinite group. Its Haar measure `mu_Haar` is the unique translation-invariant probability measure.

As a topological compact group, `Z_hat^x` has cardinality `2^{aleph_0}`. The direct limit of the finite Hilbert spaces consists of locally constant functions on `Z_hat^x`.

Those locally constant functions are dense in

```text
L^2(Z_hat^x, d mu_Haar),
```

which is a separable infinite-dimensional Hilbert space. This is the natural completion of the primorial inductive system.

## 3. The limit operator

The formal limit operator `T_infinity` on `L^2(Z_hat^x, d mu_Haar)` is convolution by a kernel `K_infinity` built from prime embeddings weighted by `log p`.

The continuous characters of `Z_hat^x` are exactly the finite-conductor Dirichlet characters, assembled across all primorial levels.

Formally, the eigenvalue of `T_infinity` under a character `chi` is the prime-weighted character sum

```text
lambda_chi = sum_p (log p) chi(p).
```

After the required analytic continuation or regularization, this is governed by the logarithmic derivative of the corresponding Dirichlet `L`-function:

```text
-L'/L(0, chi),
```

with the usual caution that the unregularized prime sum is not an ordinary convergent series at `s=0`.

The finite operators `T_{P_k}` are finite-primorial restrictions. Their finite eigenvalues approximate the regularized limit eigenvalue with tail error governed by

```text
sum_{p > P_k} (log p) chi(p),
```

again in the analytically continued / regularized sense. This is the same Stieltjes-tower correction surface recorded in `HW-OPEN-001`.

## 4. Essential self-adjointness question

The Hilbert-Pólya conjecture in this language asks whether there is a self-adjoint operator on `L^2(Z_hat^x, d mu_Haar)` or a related natural Hilbert space whose spectrum equals the set of nontrivial zero ordinates of the relevant Dirichlet `L`-functions.

The naive convolution operator `T_infinity` is symmetric on the dense domain of locally constant functions when its kernel satisfies the inversion-symmetry condition

```text
K(g^{-1}) = conjugate(K(g)).
```

This is the infinite-level analogue of the finite inversion-symmetry condition already established for finite `T_P` in `HW-PRIME-FINITE-OPERATOR-001`.

The question of essential self-adjointness on the dense domain

```text
union_k H_{P_k}
```

depends on the `L^2(Z_hat^x)` growth of `K_infinity`. That growth is controlled by the same Stieltjes tower that controls finite operator eigenvalue approximation in `HW-OPEN-001` and by the Borel-Laplace summability question scoped in the Yang-Mills Lane VIII Borel-Stieltjes document.

The cardinality gap from `HW-OPEN-004` is resolved at the arithmetic-completion level: finite operators live at `aleph_0`, while `L^2(Z_hat^x, d mu_Haar)` is built over a compact profinite group of cardinality `2^{aleph_0}`. Profinite Haar measure is the canonical measure that makes this the natural completion of the finite arithmetic system without requiring Osterwalder-Schrader distributional machinery.

## 5. Connection to the embedding stack

In the `HG-DOC-002` embedding stack, the profinite inductive limit sits between Level 1 finite Hilbert spaces and Level 7 lattice Hilbert spaces.

It is the natural analytic completion of the finite arithmetic program: the first object above the finite/infinite boundary that is still canonically defined from the arithmetic structure without requiring gauge theory, Wilson loops, transfer matrices, or Osterwalder-Schrader axioms.

This makes `L^2(Z_hat^x, d mu_Haar)` a candidate arithmetic-completion surface, not a Yang-Mills physical Hilbert space.

## 6. Non-claims

This document does not construct the Hilbert-Pólya operator.

This document does not prove RH or GRH.

This document does not prove that the spectrum of `T_infinity` equals the zero ordinates.

This document does not bridge to Yang-Mills without a typed connection.

This document does not assert essential self-adjointness of `T_infinity`.

This document does not assert ordinary convergence of the unregularized prime sum at `s=0`.
