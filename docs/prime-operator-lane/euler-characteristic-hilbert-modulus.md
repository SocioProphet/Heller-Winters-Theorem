# Euler Characteristic of the Finite Hilbert Modulus

Identifier: `HW-PRIME-HILBERT-EULER-001`  
Status: proposed  
Claim class: finite topological accounting proposition  
Lane: prime/operator lane  
Non-claim: not RH, not GRH, not PNT, not PNT-AP, not a zero-location theorem, not a Yang-Mills mass-gap claim

## 1. Proposition

Let

```math
G_P=(\mathbb Z/P\mathbb Z)^\times
```

and let

```math
\mathcal H_P=\mathbb C[G_P]
```

be the finite complex group-algebra Hilbert space of the wheel unit group.

Then

```math
\mathbb P(\mathcal H_P)\cong\mathbb{CP}^{\varphi(P)-1},
\qquad
\chi(\mathbb P(\mathcal H_P))=\varphi(P).
```

This is a finite topological accounting statement. It does not assert anything about analytic zero locations, prime asymptotics, conductor normalization, or Yang-Mills mass gaps.

## 2. Proof sketch

The group algebra has one basis vector for each unit residue:

```math
\mathcal H_P=\mathbb C[G_P]
\cong
\mathbb C^{|G_P|}.
```

Since

```math
|G_P|=\varphi(P),
```

we have

```math
\dim_\mathbb C\mathcal H_P=\varphi(P).
```

The projective space of an `n`-dimensional complex vector space is

```math
\mathbb{CP}^{n-1}.
```

Taking

```math
n=\varphi(P),
```

gives

```math
\mathbb P(\mathcal H_P)\cong\mathbb{CP}^{\varphi(P)-1}.
```

The complex projective space `CP^{n-1}` has a CW decomposition with one cell in each even real dimension

```math
0,2,4,\ldots,2(n-1).
```

Therefore its Euler characteristic is

```math
\chi(\mathbb{CP}^{n-1})=n.
```

Thus

```math
\chi(\mathbb P(\mathcal H_P))=\varphi(P).
```

## 3. `P(7)=210` worked example

For the first large primorial wheel used in this lane,

```math
P(7)=2\cdot3\cdot5\cdot7=210.
```

The wheel unit group is

```math
G_{210}=(\mathbb Z/210\mathbb Z)^\times.
```

Its order is

```math
\varphi(210)
=210\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac15\right)\left(1-\frac17\right)
=48.
```

The finite Hilbert space is

```math
\mathcal H_{210}=\mathbb C[G_{210}]\cong\mathbb C^{48}.
```

The projective Hilbert modulus is

```math
\mathbb P(\mathcal H_{210})\cong\mathbb{CP}^{47}.
```

Therefore

```math
\chi(\mathbb P(\mathcal H_{210}))
=
\chi(\mathbb{CP}^{47})
=
48
=
\varphi(210).
```

## 4. Connection to character projector normalization

The `P(7)=210` character scaffold displays `48` characters of

```math
G_{210}=(\mathbb Z/210\mathbb Z)^\times.
```

Equivalently,

```math
|\widehat{G_{210}}|=48.
```

The displayed characters

```math
\chi_{j,k,l}
```

form the finite Fourier basis dual to the residue basis of

```math
\mathcal H_{210}=\mathbb C[G_{210}].
```

Each character direction determines a rank-1 projective state

```math
[\chi_{j,k,l}]\in\mathbb P(\mathcal H_{210}).
```

Thus the `48` displayed character directions, the `48` unit residue sectors, and the Euler characteristic

```math
\chi(\mathbb P(\mathcal H_{210}))=48
```

are three views of the same finite accounting count.

The arithmetic-progression projector normalization

```math
1_{n\equiv a\pmod{210}}
=
\frac{1}{48}
\sum_{\chi\bmod 210}\overline{\chi(a)}\chi(n)
```

uses this finite count. The `1/48` factor is the normalized finite Fourier average over the displayed character Hilbert basis.

## 5. Conductor-stratification warning

The Euler characteristic above counts projective states of

```math
\mathcal H_{210}=\mathbb C[(\mathbb Z/210\mathbb Z)^\times].
```

It does not stratify analytic `L`-function zeros by conductor.

The display modulus

```math
210
```

does not imply analytic conductor

```math
210.
```

A displayed character modulo `210` may be induced from a primitive character of smaller conductor. The zero-registry schema enforces this distinction by requiring both `display_modulus` and `conductor` on every analytic surface.

Therefore the finite equality

```math
\chi(\mathbb P(\mathcal H_{210}))=48
```

must not be read as a statement about the number, location, multiplicity, ordering, or conductor distribution of `L`-function zeros.

## 6. Zero-registry connection

The zero-registry schema records analytic surfaces after the finite character layer has been declared. Its role is to prevent finite display bookkeeping from being confused with analytic theorem strength.

The `P(7)=210` registry fixture records a displayed character surface where the display modulus and conductor are intentionally distinct:

```math
\text{display modulus}=210,
\qquad
\text{conductor}=105.
```

This is compatible with the Euler-characteristic count because the count belongs to the finite projective character-state modulus, not to the analytic conductor-normalized zero surface.

In short:

```text
finite character count = projective Hilbert accounting;
zero registry = analytic surface bookkeeping;
these layers are connected but not identical.
```

## 7. Yang-Mills analogy boundary

See:

```text
docs/cross-repo/yang-mills-euler-boundary.md
```

The Yang-Mills analogy is proof-hygiene only. It concerns the discipline of separating state space, quotient, operator, spectrum, gap language, and claim status.

The finite arithmetic equality

```math
\chi(\mathbb P(\mathcal H_{210}))=48
```

does not imply a Yang-Mills mass gap, does not construct continuum Yang-Mills theory, and does not connect to the Osterwalder-Seiler reflection-positive Hilbert space used in the Yang-Mills theorem-track anchor.

## 8. Non-claims

This artifact explicitly does not claim:

1. RH.
2. GRH.
3. PNT.
4. PNT in arithmetic progressions.
5. Any zero-location theorem.
6. Any zero-counting theorem beyond the finite character-state accounting proposition above.
7. That display modulus equals conductor.
8. That a finite Euler characteristic stratifies `L`-function zeros.
9. A Yang-Mills mass gap.
10. A continuum Yang-Mills construction.
11. An Euler characteristic for an infinite-dimensional Hilbert space.
12. That the finite projective Hilbert modulus substitutes for the Osterwalder-Seiler Hilbert space.

## 9. Usage rule

Any future artifact citing `HW-PRIME-HILBERT-EULER-001` must specify whether it is using:

1. the finite wheel unit group;
2. the finite character Hilbert space;
3. the projective Hilbert modulus;
4. the Euler-characteristic accounting equality;
5. a conductor-normalized analytic surface;
6. a zero-registry declaration.

No artifact may collapse these layers without an explicit proof obligation and claim-class update.
