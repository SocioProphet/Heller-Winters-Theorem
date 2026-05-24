# Finite Character Operator Diagnostic

Identifier: `HW-PRIME-FINITE-OPERATOR-001`  
Status: proposed  
Claim class: finite spectral diagnostic / Hilbert-Polya analogue boundary  
Lane: prime/operator lane  
Depends on: `HW-PRIME-HILBERT-EULER-001`, `HW-PRIME-CHARACTER-P210-001`, `HW-PRIME-AP-EXPLICIT-001`, `HW-ZERO-P210-CHARACTER-001`  
Non-claim: not RH, not GRH, not PNT, not PNT-AP, not a zero-location theorem, not a Yang-Mills mass-gap claim

## 1. Purpose

`HW-PRIME-HILBERT-EULER-001` records the finite topological accounting layer:

```math
G_P=(\mathbb Z/P\mathbb Z)^\times,
\qquad
\mathcal H_P=\mathbb C[G_P],
\qquad
\chi(\mathbb P(\mathcal H_P))=\varphi(P).
```

This artifact records the next layer: a finite operator diagnostic on

```math
\mathcal H_{210}=L^2(G_{210}).
```

The goal is to make the finite Hilbert-Polya-shaped analogy computable without upgrading it to theorem strength.

## 2. Correct symmetry for self-adjoint convolution

Let

```math
G_P=(\mathbb Z/P\mathbb Z)^\times
```

and let

```math
K_P:G_P\to\mathbb C
```

be a finite kernel. Define the convolution operator

```math
(T_Pf)(g)=\sum_{h\in G_P}K_P(h)f(gh).
```

A real-valued kernel is not enough to make `T_P` self-adjoint. The correct condition is

```math
K_P(h^{-1})=\overline{K_P(h)}.
```

For real-valued kernels this becomes

```math
K_P(h^{-1})=K_P(h).
```

This inversion symmetry is the finite group analogue of requiring the operator, not merely the weights, to respect the Hilbert-space adjoint.

## 3. Character diagonalization

Because `G_P` is finite abelian, its characters diagonalize every convolution operator.

For

```math
\chi\in\widehat{G_P},
```

we have

```math
T_P\chi=\lambda_\chi\chi,
```

where

```math
\lambda_\chi=\sum_{h\in G_P}K_P(h)\chi(h).
```

If

```math
K_P(h^{-1})=\overline{K_P(h)},
```

then all eigenvalues are real. For `P=210`, there are `48` characters and therefore `48` character eigenvalues.

## 4. `P(7)=210` CRT character coordinates

For

```math
P(7)=210,
```

the unit group decomposes as

```math
G_{210}\cong C_2\times C_4\times C_6.
```

The diagnostic uses the following CRT generators:

```text
alpha = 71   order 2
beta  = 127  order 4
gamma = 31   order 6
```

They are determined by the local generator choices:

```text
alpha: generator 2 in (Z/3Z)^*
beta:  generator 2 in (Z/5Z)^*
gamma: generator 3 in (Z/7Z)^*
```

The exponent of the group is

```math
\operatorname{exp}(G_{210})=\operatorname{lcm}(2,4,6)=12.
```

Therefore all character values lie in

```math
\mu_{12}.
```

## 5. Cyclotomic source of one-half

The primitive sixth root of unity is

```math
\zeta_6=e^{i\pi/3}=\frac12+\frac{i\sqrt3}{2}.
```

Thus

```math
\operatorname{Re}(\zeta_6)=\cos(\pi/3)=\frac12.
```

Since

```math
\mu_6\subset\mu_{12},
```

this one-half coordinate appears naturally inside the cyclotomic value field of the `P(7)=210` character system.

This is a finite cyclotomic source of the same real coordinate that appears in the critical-line normalization.

## 6. Involution distinction

The Riemann xi-function satisfies the holomorphic functional equation symmetry

```math
\xi(s)=\xi(1-s).
```

The critical line is not the fixed locus of the holomorphic map alone. The critical line is the fixed locus of the anti-holomorphic reflection

```math
s\mapsto1-\overline{s},
```

because

```math
s=1-\overline{s}
\quad\Longleftrightarrow\quad
\operatorname{Re}(s)=\frac12.
```

On the cyclotomic side, complex conjugation sends

```math
\zeta_6\mapsto\overline{\zeta_6}=\zeta_6^5
```

and fixes the real coordinate

```math
\operatorname{Re}(\zeta_6)=\frac12.
```

The structural analogy is involutive symmetry around a one-half coordinate. It is not a proof of RH.

## 7. Modular elliptic-point convention

The point

```math
e^{i\pi/3}=\frac12+\frac{i\sqrt3}{2}
```

and the standard modular-domain boundary representative

```math
e^{2\pi i/3}=-\frac12+\frac{i\sqrt3}{2}
```

are boundary-paired order-3 elliptic representatives under modular translation conventions.

The safe claim is only that

```math
\cos(\pi/3)=\frac12
```

appears simultaneously as:

1. the real coordinate of a sixth root of unity;
2. the midpoint of the critical strip;
3. the fixed real coordinate of the anti-holomorphic critical-line reflection;
4. the real part of a modular order-3 elliptic boundary representative under a chosen translate.

This is structural resonance, not theorem evidence.

## 8. Prime-residue kernel diagnostic

The executable checker uses cutoff

```text
B = 500
```

and raw prime-residue weights

```math
A_{210}(h)=\sum_{\substack{q\le B \\ q\text{ prime} \\ q\bmod 210=h}}\log q.
```

It then defines the inversion-symmetric kernel

```math
K_{210}(h)=\frac12\left(A_{210}(h)+A_{210}(h^{-1})\right).
```

This gives a self-adjoint finite convolution operator on

```math
\mathcal H_{210}=L^2(G_{210}).
```

The cutoff is a diagnostic parameter. This is not a general-purpose high-performance number-theoretic primitive; the CRT/discrete-log table is built by brute force over the `48` residues of `G_210`.

## 9. Computed diagnostic outputs

The checker verifies:

```text
phi(210) = 48
exp(G_210) = 12
alpha = 71, beta = 127, gamma = 31
48 CRT discrete-log coordinates
inversion symmetry of K_210
48 character eigenvalues
real spectrum to numerical tolerance
character diagonalization by direct convolution action
```

For cutoff `B=500`, the spectrum has:

```text
48 eigenvalues, all real to tolerance
minimum real eigenvalue negative
maximum real eigenvalue positive
not symmetric about 0
```

The absence of generic symmetry about `0` is intentional. Self-adjointness gives real eigenvalues. Symmetry about `0` would require an additional anti-commuting involution or parity condition that is not present in this diagnostic kernel.

## 10. Selberg analogy boundary

The Selberg trace formula is an established bridge between hyperbolic geometry and spectral data. It relates Laplacian eigenvalues to closed geodesic lengths in a precise analytic setting.

This artifact does not invoke the Selberg trace formula as a proof engine. It builds a finite arithmetic analogue in which a declared finite operator has a character-diagonal spectrum.

The analogy is:

| Selberg / hyperbolic side | Heller-Winters finite side |
|---|---|
| Laplacian eigenvalues | character eigenvalues of `T_210` |
| geodesic-length data | wheel residue / prime-residue kernel data |
| spectral transform | finite character transform |
| analytic trace formula | finite convolution diagonalization |

This is diagnostic scaffolding for Hilbert-Polya-style reasoning, not RH evidence.

## 11. Status table

| Statement | Status |
|---|---|
| `cosh(it)=cos(t)` | established |
| `zeta_6=e^{i*pi/3}`, `Re(zeta_6)=1/2` | established |
| characters of `G_210` take values in `mu_12` | established |
| `H_210 ~= C^48` | established |
| `chi(P(H_210))=48` | established |
| inversion-symmetric finite convolution operators are self-adjoint | established |
| character basis diagonalizes finite abelian convolution operators | established |
| this finite operator models the actual Hilbert-Polya operator at theorem grade | conjectural / diagnostic only |
| this implies RH or GRH | false / forbidden |
| this implies Yang-Mills mass gap | false / forbidden |

## 12. Non-claims

This artifact explicitly does not claim:

1. RH.
2. GRH.
3. PNT.
4. PNT in arithmetic progressions.
5. Any zero-location theorem.
6. That the finite spectrum models the actual Hilbert-Polya operator at theorem grade.
7. That the spectrum is symmetric about `0`.
8. That a finite spectral diagnostic proves any spectral-gap theorem.
9. That display modulus equals conductor.
10. That the zero-registry schema supplies Yang-Mills spectral data.
11. A Yang-Mills mass gap.
12. A continuum Yang-Mills construction.

## 13. Implementation reference

Executable checker:

```text
tools/check_finite_character_operator.py
```

Tests:

```text
tests/test_finite_character_operator.py
```

Make target:

```text
make check-finite-character-operator
```
