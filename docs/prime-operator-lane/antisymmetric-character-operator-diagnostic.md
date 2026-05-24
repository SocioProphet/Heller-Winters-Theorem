# Antisymmetric Character Operator Diagnostic

Identifier: `HW-PRIME-ANTISYM-OPERATOR-001`  
Status: proposed  
Claim class: finite spectral diagnostic / antisymmetric transfer-kernel boundary  
Lane: prime/operator lane  
Depends on: `HW-PRIME-FINITE-OPERATOR-001`  
Non-claim: not RH, not GRH, not PNT, not a zero-location theorem, not a Yang-Mills mass-gap claim

## 1. Purpose

This artifact records the antisymmetric decomposition of the `P(7)=210` prime-residue kernel used by the finite character-operator diagnostic.

The prior finite operator artifact defined the inversion-symmetric kernel

```math
K^{+}(h)=\frac12\left(A(h)+A(h^{-1})\right)
```

and checked the corresponding self-adjoint convolution diagnostic.

This artifact defines the antisymmetric companion

```math
K^{-}(h)=\frac12\left(A(h)-A(h^{-1})\right).
```

The split separates time-symmetric and time-antisymmetric arithmetic contributions in the finite residue model.

## 2. Kernel decomposition

Let

```math
G_{210}=(\mathbb Z/210\mathbb Z)^\times.
```

For cutoff `B=500`, define the raw prime-residue kernel

```math
A(h)=\sum_{\substack{q\le B \\ q\text{ prime} \\ q\bmod 210=h}}\log q.
```

Then

```math
A(h)=K^{+}(h)+K^{-}(h),
```

where

```math
K^{+}(h)=\frac12\left(A(h)+A(h^{-1})\right),
\qquad
K^{-}(h)=\frac12\left(A(h)-A(h^{-1})\right).
```

The two components satisfy

```math
K^{+}(h^{-1})=K^{+}(h),
\qquad
K^{-}(h^{-1})=-K^{-}(h).
```

Equivalently,

```math
K^{+}(h)+K^{-}(h)=A(h),
\qquad
K^{+}(h)-K^{-}(h)=A(h^{-1}).
```

## 3. Self-adjointness and skew-adjointness

`HW-PRIME-FINITE-OPERATOR-001` established the symmetric condition:

```math
K^{+}(h^{-1})=K^{+}(h).
```

The convolution operator by `K^+` is self-adjoint and has real eigenvalues.

For the antisymmetric component,

```math
K^{-}(h^{-1})=-K^{-}(h).
```

The raw convolution operator

```math
(C_{K^-}f)(g)=\sum_{h\in G_{210}}K^{-}(h)f(gh)
```

is skew-Hermitian. Therefore its raw eigenvalues are purely imaginary, up to numerical tolerance.

The self-adjoint antisymmetric diagnostic is

```math
T^{-}=-i C_{K^-}.
```

This is the operator whose spectrum is checked as real and symmetric about zero.

This distinction is mandatory: a real inversion-antisymmetric kernel does not itself produce a self-adjoint convolution operator. The factor `-i` converts the skew-Hermitian generator into a self-adjoint finite diagnostic.

## 4. Why the spectrum is symmetric

For a character

```math
\chi\in\widehat{G_{210}},
```

the raw antisymmetric convolution eigenvalue is

```math
\mu_\chi=\sum_{h\in G_{210}}K^{-}(h)\chi(h).
```

Because

```math
K^{-}(h^{-1})=-K^{-}(h)
```

and

```math
\overline{\chi(h)}=\chi(h^{-1}),
```

the conjugate character satisfies

```math
\mu_{\overline{\chi}}=-\mu_\chi.
```

For the self-adjoint diagnostic

```math
\lambda_\chi=-i\mu_\chi,
```

the corresponding eigenvalues satisfy

```math
\lambda_{\overline{\chi}}=-\lambda_\chi.
```

Thus the checked finite diagnostic spectrum is symmetric about zero.

## 5. Transfer-matrix analogy boundary

The decomposition

```math
A=K^{+}+K^{-}
```

has the following finite diagnostic interpretation:

| Component | Finite arithmetic role | Analogy boundary |
|---|---|---|
| `K^+` | inversion/time-symmetric kernel | symmetric part of a transfer matrix |
| `K^-` | inversion/time-antisymmetric kernel | antisymmetric contribution / CP-violating-type diagnostic |
| `-i C_{K^-}` | self-adjoint antisymmetric generator | finite spectral diagnostic only |

Keeping `K^+` and `K^-` separate mirrors the discipline of separating time-reflection-even and time-reflection-odd contributions in Osterwalder-Seiler-style reasoning.

This is only an analogy about decomposition discipline. It does not import Yang-Mills theorem strength and does not identify the finite arithmetic Hilbert space with the Osterwalder-Seiler Hilbert space.

## 6. Operational substrate

Executable checker:

```text
tools/check_antisymmetric_character_operator.py
```

Tests:

```text
tests/test_antisymmetric_character_operator.py
```

Make target:

```text
make check-antisymmetric-character-operator
```

The checker imports from `tools/check_finite_character_operator.py` and reuses the existing finite arithmetic substrate:

```text
raw_prime_residue_kernel
reduced_residues
build_dlog_table
character_indices
eigenvalue_for_character
inversion_symmetric_kernel
spectrum_summary
```

It does not duplicate the finite character-table or residue-kernel machinery.

## 7. Verified finite diagnostics

For `P=210` and cutoff `B=500`, the checker verifies:

```text
K^-(h) + K^-(h^-1) = 0
K^-(h) = 0 for self-inverse residues h^2 = 1 mod 210
48 character eigenvalues
raw antisymmetric convolution spectrum is imaginary
-i times raw antisymmetric convolution has real spectrum
self-adjoint antisymmetric spectrum is symmetric about 0
K^+ + K^- = A
K^+ - K^- = A(h^-1)
```

## 8. Non-claims

This artifact explicitly does not claim:

1. RH.
2. GRH.
3. PNT.
4. PNT in arithmetic progressions.
5. Any zero-location theorem.
6. That finite spectral symmetry implies RH.
7. That this finite operator models the actual Hilbert-Polya operator at theorem grade.
8. A Yang-Mills mass gap.
9. A continuum Yang-Mills construction.
10. That the finite arithmetic Hilbert space is the Osterwalder-Seiler Hilbert space.
11. That display modulus `210` equals analytic conductor.
12. That the antisymmetric spectrum supplies zero-registry zero locations.
