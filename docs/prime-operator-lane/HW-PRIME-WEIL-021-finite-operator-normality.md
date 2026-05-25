# HW-PRIME-WEIL-021 — Finite Operator Normality Theorem

Status: finite theorem surface.  
Claim class: theorem-grade finite abelian convolution fact; no infinite operator theorem.  
Lane: prime/operator lane, finite operator / spectral-radius surface.  
Depends on: `HW-OPEN-015`, `HW-PRIME-WEIL-018`, `HW-PRIME-WEIL-020`.

## Purpose

This document records the clean finite operator theorem produced by the Prime-Weil lane.

The earlier self-adjointness framing was too strong for the raw finite prime-residue convolution operator. The correct finite theorem is normality.

For finite abelian `G_P`, every convolution operator on `l^2(G_P)` is unitarily diagonalized by the character basis. Therefore the raw prime-window operator is normal, even when it is not self-adjoint.

## Finite setup

Let:

```text
G_P = (Z/PZ)^x
```

and let:

```text
H_P = l^2(G_P)
```

with the normalized or counting inner product.

For a finite kernel `A: G_P -> C`, define the convolution operator:

```text
(T_A f)(g) = sum_{h in G_P} A(h) f(g h).
```

The prime-window operator is the special case where `A(h)` is a Chebyshev/log-prime residue mass in a Richter window or cutoff.

## Theorem

For finite abelian `G_P`, the convolution operator `T_A` is normal:

```text
T_A^* T_A = T_A T_A^*.
```

Moreover, the character basis diagonalizes `T_A`. For each character `chi` of `G_P`:

```text
T_A chi = lambda_chi chi,
```

where:

```text
lambda_chi = sum_{h in G_P} A(h) chi(h).
```

Therefore:

```text
||T_A|| = max_chi |lambda_chi|.
```

On the nontrivial character subspace:

```text
||T_A^perp|| = max_{chi != 1} |lambda_chi|.
```

For the prime-window kernel, this is exactly:

```text
||T_{P,K}^perp|| = max_{chi != 1} |psi_{W_K}(chi)|.
```

## Proof

Because `G_P` is finite abelian, its irreducible representations are one-dimensional characters and form an orthogonal basis of `l^2(G_P)`.

Convolution by `A` commutes with every right translation. Equivalently, the finite Fourier transform on `G_P` sends convolution to pointwise multiplication:

```text
Fourier(T_A f)(chi) = lambda_chi Fourier(f)(chi).
```

Thus `T_A` is unitarily equivalent to a diagonal multiplication operator. Every diagonal operator is normal. Its operator norm is the maximum absolute value of its diagonal entries.

This proves the finite theorem.

## Self-adjointness comparison

The adjoint kernel is:

```text
A^*(h) = conjugate(A(h^{-1})).
```

Therefore `T_A` is self-adjoint iff:

```text
A(h) = conjugate(A(h^{-1}))
```

for every `h`.

Self-adjointness is a special case. The raw prime-window kernel need not satisfy this inversion symmetry. But normality still holds in the finite abelian setting.

## Consequence for the proof barrier

The finite operator route is now exact:

```text
GRH-scale control for the packet
<=>
operator-norm / spectral-radius bound at square-root scale.
```

The remaining target is:

```text
||T_{P,K}^perp|| = O(10^(K/2) K^A).
```

This is not automatically implied by normality. Normality gives the spectral theorem and identifies the norm; it does not bound the eigenvalues.

## Infinite boundary

This theorem is finite. It does not construct an infinite Hilbert-Polya operator.

For an infinite or profinite completion, one must still specify:

1. the Hilbert space completion;
2. the limiting or regularized kernel;
3. a dense domain;
4. closability;
5. normality of the closure;
6. the spectral-radius bound.

Those remain open in `HW-OPEN-015`.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not construct a Hilbert-Polya operator.

This document does not prove normality of an infinite limiting operator.

This document does not prove an operator-norm bound at GRH scale.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.