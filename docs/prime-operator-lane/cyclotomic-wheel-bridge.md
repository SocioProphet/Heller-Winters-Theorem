# Cyclotomic Wheel Bridge

Identifier: `HW-PRIME-CYCLOTOMIC-001`  
Status: definition/proposition note  
Lane: prime/operator lane  
Claim class: C0 definitions + C3 elementary algebraic number theory  
Depends on: `HW-PRIME-CIRCLE-001`, `HW-CRIT-GEOM-001`, `HW-CRIT-GEOM-LEMMA-001`, `HW-CRIT-GEOM-HYP-001`  
Non-claim: not an RH proof, not a new primality algorithm, not a GRH claim

## 0. Claim boundary

This note upgrades the prime-wheel circle from a visual residue diagram to a cyclotomic-field object.

The central bridge is:

```math
\text{primorial wheel survivors}
\quad\longleftrightarrow\quad
\text{primitive roots of unity}
\quad\longleftrightarrow\quad
\text{Galois labels of a cyclotomic field}.
```

This is classical algebraic number theory applied as a coordinate layer for the prime/operator lane. It does not prove the Riemann Hypothesis, does not prove the Generalized Riemann Hypothesis, and does not replace classical primality testing.

## 1. Primorial wheel modulus

Let

```math
p
```

be a prime bound and define the primorial modulus

```math
P(p)=\prod_{q\le p} q,
```

where the product ranges over primes `q` up to `p`.

The corresponding wheel residue space is

```math
\mathbb Z/P(p)\mathbb Z.
```

The admissible wheel positions are the unit residue classes

```math
R(p)=\left(\mathbb Z/P(p)\mathbb Z\right)^\times.
```

Equivalently,

```math
a\in R(p)
\quad\Longleftrightarrow\quad
\gcd(a,P(p))=1.
```

This is the formal version of wheel survival: the residue class is not divisible by any prime in the wheel basis.

## 2. Roots of unity and the cyclotomic polynomial

Let

```math
m=P(p)
```

and choose a primitive `m`-th root of unity

```math
\zeta_m=e^{2\pi i/m}.
```

The `m`-th cyclotomic polynomial is

```math
\Phi_m(x)=\prod_{\substack{1\le a\le m \\ \gcd(a,m)=1}}(x-\zeta_m^a).
```

Therefore the roots of `Phi_m` are exactly the primitive `m`-th roots of unity:

```math
\operatorname{Roots}(\Phi_m)
=
\{\zeta_m^a:\gcd(a,m)=1\}.
```

For the primorial wheel modulus `m=P(p)`, this becomes

```math
\operatorname{Roots}(\Phi_{P(p)})
=
\{\zeta_{P(p)}^a:a\in R(p)\}.
```

Thus the admissible wheel positions are exactly the exponents indexing the primitive roots of the corresponding cyclotomic polynomial.

## 3. Primitive-root proposition

### Proposition 1 — wheel survivors as primitive roots

Let

```math
m=P(p).
```

The map

```math
a\bmod m \longmapsto \zeta_m^a
```

restricts to a bijection

```math
(\mathbb Z/m\mathbb Z)^\times
\cong
\operatorname{Roots}(\Phi_m).
```

### Proof

A power `zeta_m^a` is a primitive `m`-th root of unity if and only if its order is `m`.

The order of `zeta_m^a` is

```math
\frac{m}{\gcd(a,m)}.
```

Therefore `zeta_m^a` has order `m` if and only if

```math
\gcd(a,m)=1.
```

That is precisely the condition that `a mod m` lies in

```math
(\mathbb Z/m\mathbb Z)^\times.
```

So unit residues are exactly primitive-root exponents.

## 4. Cyclotomic field and Galois labels

The cyclotomic field attached to the wheel is

```math
K_m=\mathbb Q(\zeta_m).
```

Its Galois group is canonically identified with the unit group:

```math
\operatorname{Gal}(\mathbb Q(\zeta_m)/\mathbb Q)
\cong
(\mathbb Z/m\mathbb Z)^\times.
```

The automorphism corresponding to

```math
a\in(\mathbb Z/m\mathbb Z)^\times
```

is

```math
\sigma_a(\zeta_m)=\zeta_m^a.
```

Thus the prime-wheel survivor class `a` is simultaneously:

1. a unit residue modulo the primorial wheel;
2. an exponent of a primitive root of unity;
3. a root label of `Phi_m`;
4. a Galois automorphism label of `Q(zeta_m)`.

This is the algebraic upgrade from circle plot to cyclotomic field.

## 5. Square-root-complete cyclotomic field for a candidate integer

For a candidate integer `n>1`, define the square-root divisor horizon

```math
B(n)=\{q\text{ prime}:q\le\sqrt n\}.
```

Define the square-root-complete primorial modulus

```math
M(n)=\prod_{q\le\sqrt n}q.
```

The corresponding cyclotomic field is

```math
K_n=\mathbb Q(\zeta_{M(n)}).
```

This field is selected by the factor-pair fixed boundary

```math
d\longmapsto \frac nd,
\qquad
 d=\sqrt n.
```

The square-root boundary is the geometric-mean closure of possible factor pairs. Once every prime up to `sqrt(n)` is represented in the wheel basis, the wheel is primality-complete in the classical trial-division sense.

## 6. Square-root-complete primitive-phase certificate

### Proposition 2 — cyclotomic form of trial division

Let `n>1`, let

```math
M(n)=\prod_{q\le\sqrt n}q,
```

and let

```math
\zeta=\zeta_{M(n)}.
```

Then

```math
n\text{ is prime}
\quad\Longleftrightarrow\quad
\zeta^n\text{ is a primitive }M(n)\text{-th root of unity}.
```

Equivalently,

```math
n\text{ is prime}
\quad\Longleftrightarrow\quad
\Phi_{M(n)}(\zeta^n)=0.
```

### Proof

The phase `zeta^n` is a primitive `M(n)`-th root of unity if and only if

```math
\gcd(n,M(n))=1.
```

By definition, `M(n)` contains every prime

```math
q\le\sqrt n.
```

If `n` is composite, then `n=ab` with `1<a<=b<n`, so

```math
a\le\sqrt n.
```

Therefore `n` has a prime divisor `q<=sqrt(n)`. This prime divisor appears in `M(n)`, so

```math
\gcd(n,M(n))>1.
```

Conversely, if

```math
\gcd(n,M(n))>1,
```

then some prime `q<=sqrt(n)` divides `n`, so `n` is composite.

Thus

```math
n\text{ prime}
\quad\Longleftrightarrow\quad
\gcd(n,M(n))=1.
```

Combining this with the primitive-root condition gives the proposition.

## 7. Partial-wheel warning

For a smaller primorial modulus

```math
P(p)=\prod_{q\le p}q
```

with

```math
p<\sqrt n,
```

the condition

```math
\zeta_{P(p)}^n\in\operatorname{Roots}(\Phi_{P(p)})
```

only means

```math
\gcd(n,P(p))=1.
```

That is partial wheel survival. It does not certify that `n` is prime.

The certification boundary requires

```math
p\ge\sqrt n
```

or, more precisely, that the wheel basis include every prime divisor candidate `q<=sqrt(n)`.

## 8. Primitive-phase density and sieve pressure

The degree of the cyclotomic polynomial is

```math
\deg \Phi_m=\varphi(m).
```

For a primorial modulus

```math
m=P(p)=\prod_{q\le p}q,
```

Euler's totient gives

```math
\varphi(P(p))
=
P(p)\prod_{q\le p}\left(1-\frac1q\right).
```

Therefore the density of primitive phases inside all `P(p)`-th roots of unity is

```math
\frac{\varphi(P(p))}{P(p)}
=
\prod_{q\le p}\left(1-\frac1q\right).
```

This is the same survival density as the primorial sieve. The harmonic/reciprocal layer appears through the factors

```math
1-\frac1q.
```

Thus reciprocal small-prime pressure is visible algebraically as the shrinking density of primitive cyclotomic phases.

## 9. Means-ladder interpretation

The bridge aligns with the means ladder:

| Layer | Mean / coordinate | Role |
|---|---|---|
| arithmetic | `A(0,1)=1/2` | critical-strip midpoint |
| geometric | `G(d,n/d)=sqrt(n)` | factor-pair fixed boundary |
| logarithmic | `u=log x` | multiplicative-to-additive transport |
| harmonic / reciprocal | `prod(1-1/q)` and `sum 1/q` | sieve survival and primitive-phase density |

The cyclotomic field is the algebraic layer where the geometric root boundary selects a modulus and the harmonic sieve pressure becomes primitive-root density.

## 10. Character bridge boundary

The group

```math
(\mathbb Z/m\mathbb Z)^\times
```

is also the natural domain of Dirichlet characters modulo `m`:

```math
\chi:(\mathbb Z/m\mathbb Z)^\times\to\mathbb C^\times.
```

Those characters take values in roots of unity and lead toward Dirichlet `L`-functions. This note does not develop that bridge. It only records the boundary:

```math
\text{wheel unit group}
\rightarrow
\text{cyclotomic Galois group}
\rightarrow
\text{Dirichlet character domain}.
```

A separate note should handle characters, conductor, primitive characters, and analytic `L(s,chi)` surfaces.

## 11. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- cyclotomic fields alone explain the distribution of primes;
- a partial wheel certifies primality;
- primitive roots of unity produce a new primality algorithm;
- the prime-circle plot is itself a theorem;
- Galois labels imply zeta-zero location;
- finite primitive-phase survival implies asymptotic prime density.

Permitted use:

```text
This note identifies the primorial wheel as the residue-level shadow of the cyclotomic field Q(zeta_{P(p)}), with wheel survivors corresponding to primitive roots of Phi_{P(p)} and Galois labels of the cyclotomic field.
```

## Citation form

```text
[HW-PRIME-CYCLOTOMIC-001 @ <merge-sha>]       # cyclotomic wheel bridge only
```

## Versioning

This is `HW-PRIME-CYCLOTOMIC-001 v0.1`. Future work may add a Dirichlet-character bridge, explicit conductor handling, examples for small primorials, or rendered diagrams connecting wheels, primitive roots, and Galois automorphisms.
