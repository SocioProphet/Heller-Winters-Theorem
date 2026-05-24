# Gaussian Integer Character Operator Diagnostic

Identifier: `HW-PRIME-GAUSSIAN-INT-001`  
Status: proposed  
Claim class: finite Gaussian-integer spectral diagnostic / cyclotomic-spin boundary  
Lane: prime/operator lane  
Depends on: `HW-PRIME-FINITE-OPERATOR-001`, `HW-PRIME-ANTISYM-OPERATOR-001`  
Non-claim: not RH, not GRH, not PNT, not a zero-location theorem, not a Yang-Mills mass-gap claim

## 1. Purpose

This artifact records a finite Gaussian-integer operator diagnostic on the `P(7)=210` character Hilbert space.

The diagnostic lifts rational primes that split in `Z[i]`:

```math
q=a^2+b^2
```

into unit Gaussian phases

```math
u_q=\frac{a+ib}{\sqrt q},
```

aggregates those phases by residue class modulo `210`, and evaluates the finite character transform over

```math
G_{210}=(\mathbb Z/210\mathbb Z)^\times.
```

This is a finite arithmetic structural diagnostic. It is not an analytic proof engine.

## 2. Gaussian prime-residue kernel

For cutoff `B=500`, define

```math
A_{\mathbb Z[i]}(h)
=
\sum_{\substack{q\le B \\ q\text{ prime} \\ q\bmod 210=h \\ q=a^2+b^2}}
\log(q)\frac{a+ib}{\sqrt q}.
```

Only split rational primes are included: `q=2` and primes `q=1 mod 4`. Rational primes `q=3 mod 4` are inert in `Z[i]` and are omitted from this finite Gaussian diagnostic.

The corresponding character eigenvalue for

```math
\chi\in\widehat{G_{210}}
```

is

```math
\lambda^{\mathbb Z[i]}_\chi
=
\sum_{h\in G_{210}}A_{\mathbb Z[i]}(h)\chi(h).
```

## 3. Character-table substrate

The diagnostic reuses the `P(7)=210` character table from the finite operator package.

The CRT generators are:

```text
alpha = 71   order 2
beta  = 127  order 4
gamma = 31   order 6
```

The group decomposes as

```math
G_{210}\cong C_2\times C_4\times C_6,
```

so all character values lie in

```math
\mu_{12}.
```

The distinguished character index is

```math
\varphi_{1,1,1}.
```

It is evaluated at the combined generator

```math
g_*=71\cdot127\cdot31\pmod{210}.
```

## 4. The `j=1/2` identification

The `SU(2)` fundamental representation has spin

```math
j=\frac12.
```

Its two `J_3` weights are

```math
\pm\frac12.
```

The spin-`j` character is

```math
\chi_j(\theta)=\frac{\sin((2j+1)\theta/2)}{\sin(\theta/2)}.
```

For `j=1/2`, this becomes

```math
\chi_{1/2}(\theta)=2\cos(\theta/2).
```

At the modular order-3 angle `theta=2*pi/3`,

```math
\chi_{1/2}(2\pi/3)=2\cos(\pi/3)=1.
```

The same one-half coordinate appears in the finite character table.

For the `P(7)=210` character parametrization,

```math
\chi_{j,k,l}(g)=(-1)^{j e_2}i^{k e_4}e^{i\pi l e_6/3},
```

where `(e_2,e_4,e_6)` is the discrete-log coordinate of `g` in the CRT generators.

For the distinguished character at the combined generator,

```math
\varphi_{1,1,1}(g_*)
=
\zeta_2\zeta_4\zeta_6
=(-1)(i)(e^{i\pi/3})
=e^{-i\pi/6}
=
\frac{\sqrt3}{2}-\frac{i}{2}.
```

Thus

```math
\operatorname{Im}(\varphi_{1,1,1}(g_*))=-\frac12=-j.
```

Also,

```math
\frac{1}{2i}=-\frac{i}{2},
\qquad
\operatorname{Im}\left(\frac{1}{2i}\right)=-\frac12.
```

The Catalan singularity relation is

```math
\rho_2=\frac{1}{2(2j+1)}\bigg|_{j=1/2}=\frac14,
```

and

```math
\left(\frac{1}{2i}\right)^2=-\frac14=-\rho_2.
```

The finite structural chain is therefore:

| Object | Appearance of one-half | Role |
|---|---|---|
| `j=1/2` SU(2) representation | `J_3` weights `+/-1/2` | fundamental spin quantum number |
| Critical line | `Re(s)=1/2` | fixed locus of `s -> 1-conj(s)` |
| `varphi_{1,1,1}(g_*)` | imaginary part `-1/2` | finite character value at combined generator |
| `cos(pi/3)` | `1/2` | real part of `zeta_6`, modular elliptic coordinate |
| `1/(2i)` | imaginary part `-1/2` | base imaginary half-unit |

This is a finite arithmetic structural coincidence. It is not a proof that `varphi_{1,1,1}` encodes `SU(2)` representation theory.

A precise Casimir-compatible identity is recorded in the tests:

```math
\left(\operatorname{Im}(\varphi_{1,1,1}(g_*))\right)^2+\frac12
=
\frac14+\frac12
=
\frac34
=
j(j+1)\quad (j=1/2).
```

The character value itself remains a root of unity and therefore has unit norm:

```math
|\varphi_{1,1,1}(g_*)|^2=1.
```

The unit-norm fact and the `SU(2)` Casimir value are not the same statement.

## 5. Gaussian eigenvalue of the distinguished character

The finite Gaussian eigenvalue of the distinguished character is

```math
\lambda^{\mathbb Z[i]}_{1,1,1}
=
\sum_{h\in G_{210}}A_{\mathbb Z[i]}(h)\varphi_{1,1,1}(h).
```

This eigenvalue is the finite arithmetic spectral coordinate attached to the `varphi_{1,1,1}` character under the Gaussian integer kernel.

It is a cutoff-dependent finite partial sum. It is not a zero ordinate and not a Hilbert-Polya operator eigenvalue at theorem grade.

## 6. Transfer and Yang-Mills analogy boundary

The `j=1/2` representation is the fundamental spinor representation of `SU(2)`. In strong-coupling lattice `SU(2)` reasoning, Wilson-loop calculations naturally involve the fundamental representation and factors related to `2j+1=2`.

This artifact records only a finite arithmetic analogy:

```math
\varphi_{1,1,1}(g_*)=e^{-i\pi/6}
```

has imaginary part `-1/2`, while the `j=1/2` representation has weights `+/-1/2`.

No theorem-grade bridge is asserted between the Gaussian finite operator and continuum Yang-Mills theory.

## 7. Operational substrate

Executable checker:

```text
tools/check_gaussian_integer_operator.py
```

Tests:

```text
tests/test_gaussian_integer_operator.py
```

Make target:

```text
make check-gaussian-integer-operator
```

The checker reuses the existing `P(7)=210` finite character substrate:

```text
build_dlog_table
character_value
eigenvalue_for_character
raw_prime_residue_kernel
reduced_residues
```

## 8. Non-claims

This artifact explicitly does not claim:

1. RH.
2. GRH.
3. PNT.
4. PNT in arithmetic progressions.
5. Any zero-location theorem.
6. That `varphi_{1,1,1}` encodes `SU(2)` representation theory at theorem grade.
7. That the finite Gaussian eigenvalue is a Hilbert-Polya eigenvalue.
8. That finite Gaussian spectral coordinates determine Riemann zero ordinates.
9. A Yang-Mills mass gap.
10. A continuum Yang-Mills construction.
11. That display modulus `210` equals analytic conductor.
12. That the Gaussian integer kernel supplies zero-registry zero locations.
