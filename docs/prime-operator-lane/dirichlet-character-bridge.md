# Dirichlet Character Bridge

Identifier: `HW-PRIME-CHARACTER-001`  
Status: boundary note / analytic bridge scaffold  
Lane: prime/operator lane, with HPHD and theorem-target interfaces  
Claim class: C0 definitions + C3 standard analytic-number-theory background  
Depends on: `HW-PRIME-CYCLOTOMIC-001`, `HW-THM-001`, `HW-CRIT-GEOM-001`  
Non-claim: not RH, not GRH, not a zero-location claim, not a proof of prime equidistribution

## 0. Claim boundary

This note records the next bridge after the cyclotomic wheel bridge:

```math
(\mathbb Z/m\mathbb Z)^\times
\longrightarrow
\text{Dirichlet characters modulo }m
\longrightarrow
L(s,\chi).
```

The note does not prove the Generalized Riemann Hypothesis. It does not prove equidistribution of primes in arithmetic progressions. It does not assert a new explicit formula. It only records the standard interface between cyclotomic unit groups, character sums, and Dirichlet `L`-functions.

## 1. Unit group from the cyclotomic wheel

From `HW-PRIME-CYCLOTOMIC-001`, for a modulus

```math
m=P(p)=\prod_{q\le p}q,
```

the wheel survivor group is

```math
G_m=(\mathbb Z/m\mathbb Z)^\times.
```

The cyclotomic field is

```math
K_m=\mathbb Q(\zeta_m),
```

and its Galois group is

```math
\operatorname{Gal}(K_m/\mathbb Q)
\cong
G_m.
```

The automorphism attached to `a in G_m` is

```math
\sigma_a(\zeta_m)=\zeta_m^a.
```

This identifies wheel survivor positions with cyclotomic Galois labels.

## 2. Dirichlet characters

A Dirichlet character modulo `m` is a function

```math
\chi:\mathbb Z\to\mathbb C
```

such that:

1. `chi(n+m)=chi(n)`;
2. `chi(n)=0` if `gcd(n,m)>1`;
3. on the unit group `G_m`, `chi` is a group homomorphism:

```math
\chi:G_m\to\mathbb C^\times.
```

The nonzero values of a Dirichlet character are roots of unity.

Thus the character layer is the dual phase layer of the wheel unit group:

```math
\widehat{G_m}=\operatorname{Hom}(G_m,\mathbb C^\times).
```

## 3. Character orthogonality

Characters decompose residue-class information through orthogonality.

For `a,b in G_m`, the finite character orthogonality relation is

```math
\frac{1}{\varphi(m)}\sum_{\chi\bmod m}\chi(a)\overline{\chi(b)}
=
\begin{cases}
1,& a\equiv b\pmod m,\\
0,& a\not\equiv b\pmod m.
\end{cases}
```

This says residue-class selection can be expressed as a sum over character phases.

So the bridge is:

```math
\text{wheel residue class}
\quad\leftrightarrow\quad
\text{character projector}.
```

This is the analytic upgrade from a residue wheel to a Fourier-like finite phase decomposition.

## 4. Dirichlet L-functions

For a Dirichlet character `chi`, the Dirichlet `L`-function is initially defined for `Re(s)>1` by

```math
L(s,\chi)=\sum_{n=1}^{\infty}\frac{\chi(n)}{n^s}.
```

It also has an Euler product in the same half-plane:

```math
L(s,\chi)=\prod_p\left(1-\frac{\chi(p)}{p^s}\right)^{-1}.
```

The Euler product shows how the character weights prime phases:

```math
p\mapsto \chi(p).
```

Thus primes are no longer only counted or placed on a wheel. They are assigned finite cyclotomic phases through `chi`.

## 5. Prime classes and character-weighted counting

For a reduced residue class `a mod m`, prime-counting in that class can be studied using characters. A residue-class indicator can be written as

```math
1_{n\equiv a\pmod m}
=
\frac{1}{\varphi(m)}\sum_{\chi\bmod m}\overline{\chi(a)}\chi(n),
```

for `gcd(a,m)=1` and `gcd(n,m)=1`.

This means arithmetic-progression prime counting is transformed into character-weighted prime sums.

The Heller-Winters interpretation is:

```text
wheel sector selection becomes character-phase projection.
```

## 6. Conductor and primitive characters

A character modulo `m` may be induced from a smaller modulus. The smallest such modulus is the conductor.

Primitive characters are characters not induced from a proper divisor of `m`.

This is important because analytic conductor, functional equation, and completed `L`-function behavior are naturally attached to primitive characters.

This note does not develop the full conductor theory. It records the boundary rule:

```text
Any analytic claim involving L(s, chi) must specify whether chi is primitive, induced, and what its conductor is.
```

## 7. Character bridge to GRH-shaped surfaces

The Riemann zeta function is the trivial-character case over modulus `1`:

```math
\zeta(s)=L(s,\chi_0)
```

in the appropriate trivial-character sense.

For nontrivial Dirichlet characters, the Generalized Riemann Hypothesis concerns nontrivial zeros of `L(s,chi)` and asks that they lie on the critical line:

```math
\operatorname{Re}(s)=\frac12.
```

This uses the same critical-axis geometry developed in:

- `HW-CRIT-GEOM-001`;
- `HW-CRIT-GEOM-LEMMA-001`;
- `HW-CRIT-GEOM-HYP-001`.

But this note does not assert GRH. It only records that character-weighted analytic surfaces inherit the same critical-axis coordinate grammar once the relevant completed `L`-function is in view.

## 8. Relation to the means ladder

The means ladder appears as follows:

| Layer | Object | Role |
|---|---|---|
| arithmetic | `1/2` | critical-axis midpoint for zeta and L-function strips |
| geometric | `sqrt(n)` | finite divisor horizon selecting square-root-complete wheels |
| logarithmic | `n^{-s}=e^{-s log n}` | analytic transport into Dirichlet series and Euler products |
| harmonic / reciprocal | `p^{-s}`, `1/p`, sieve products | prime reciprocal pressure and Euler product weighting |

The character bridge is where the harmonic/reciprocal prime layer becomes phase-weighted:

```math
p^{-s}
\quad\leadsto\quad
\chi(p)p^{-s}.
```

## 9. Heller-Winters bridge summary

The intended architecture is:

```math
\text{primorial wheel}
\to
G_m=(\mathbb Z/m\mathbb Z)^\times
\to
\mathbb Q(\zeta_m)
\to
\operatorname{Gal}(\mathbb Q(\zeta_m)/\mathbb Q)
\to
\widehat{G_m}
\to
L(s,\chi).
```

In words:

```text
prime-wheel survivors become cyclotomic Galois labels; their dual characters become phase projectors; those projectors define character-weighted L-functions.
```

## 10. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- character sums locate zeros;
- wheel residue structure implies prime equidistribution;
- finite character orthogonality proves asymptotic prime distribution;
- the cyclotomic bridge gives a new primality algorithm;
- all L-function conductors are already handled;
- the zeta critical-line target is discharged.

Permitted use:

```text
This note records the standard boundary from cyclotomic wheel unit groups to Dirichlet characters and Dirichlet L-functions, preserving claim separation between finite residue-phase structure and analytic zero-location problems.
```

## 11. Future work

Future notes may add:

1. primitive character and conductor details;
2. completed Dirichlet `L`-function normalization;
3. explicit formula for primes in arithmetic progressions;
4. finite character table examples for small primorial moduli;
5. rendered diagrams connecting wheel sectors, characters, and `L(s,chi)` surfaces.

## Citation form

```text
[HW-PRIME-CHARACTER-001 @ <merge-sha>]       # Dirichlet character bridge only
```

## Versioning

This is `HW-PRIME-CHARACTER-001 v0.1`. It is a boundary scaffold only. Analytic uses require separate theorem-target or proof artifacts.
