# Dirichlet Conductor and Completed L-Function Normalization

Identifier: `HW-PRIME-CHARACTER-CONDUCTOR-001`  
Status: boundary note / normalization scaffold  
Lane: prime/operator lane, with HPHD and theorem-target interfaces  
Claim class: C0 definitions + C3 standard analytic-number-theory background  
Depends on: `HW-PRIME-CHARACTER-001`, `HW-PRIME-CYCLOTOMIC-001`, `HW-CRIT-GEOM-LEMMA-001`  
Non-claim: not RH, not GRH, not a functional-equation proof, not an explicit-formula derivation

## 0. Claim boundary

This note records the normalization boundary required before using Dirichlet characters analytically.

The previous bridge note established the path

```math
(\mathbb Z/m\mathbb Z)^\times
\to
\widehat{(\mathbb Z/m\mathbb Z)^\times}
\to
L(s,\chi).
```

This note adds the conductor and completed-function discipline needed before any GRH-shaped or explicit-formula statement is made.

It does not prove the Riemann Hypothesis, the Generalized Riemann Hypothesis, a functional equation, prime equidistribution, or any zero-location theorem.

## 1. Characters modulo m

A Dirichlet character modulo `m` is periodic modulo `m`, vanishes on integers not coprime to `m`, and restricts to a group homomorphism on

```math
G_m=(\mathbb Z/m\mathbb Z)^\times.
```

The associated Dirichlet series is initially defined for `Re(s)>1` by

```math
L(s,\chi)=\sum_{n=1}^{\infty}\frac{\chi(n)}{n^s}.
```

For `Re(s)>1`, it has Euler product

```math
L(s,\chi)=\prod_p\left(1-\frac{\chi(p)}{p^s}\right)^{-1}.
```

The modulus `m` is not necessarily the analytic conductor. A character modulo `m` may be induced from a smaller modulus.

## 2. Induced characters and conductor

A character `chi` modulo `m` is induced from a character `chi*` modulo `f` if `f` divides `m` and, for integers coprime to `m`,

```math
\chi(n)=\chi^*(n).
```

The smallest such modulus `f` is the conductor of `chi`.

A character is primitive if its conductor equals its modulus.

Boundary rule:

```text
Any analytic use of L(s, chi) must specify the conductor f, not only the display modulus m.
```

This matters because completed `L`-functions, gamma factors, root numbers, and functional equations are naturally attached to primitive characters and their conductors.

## 3. Primitive normalization

Let `chi` be a primitive Dirichlet character of conductor `f`.

Define the parity parameter `a` by

```math
a=\begin{cases}
0,& \chi(-1)=1,\\
1,& \chi(-1)=-1.
\end{cases}
```

Thus `a=0` for even characters and `a=1` for odd characters.

The completed Dirichlet `L`-function is normalized as

```math
\Lambda(s,\chi)
=
\left(\frac{f}{\pi}\right)^{(s+a)/2}
\Gamma\left(\frac{s+a}{2}\right)L(s,\chi).
```

This is the normalization surface on which the functional equation and critical-line symmetry are formulated.

## 4. Functional-equation boundary

For a primitive character `chi` of conductor `f`, the completed function satisfies a functional equation of the form

```math
\Lambda(s,\chi)=\varepsilon(\chi)\Lambda(1-s,\overline{\chi}),
```

where `epsilon(chi)` is the root number and has absolute value `1`.

This note records the shape only. It does not prove the functional equation.

The critical axis associated with this completed function is again

```math
\operatorname{Re}(s)=\frac12.
```

The axis equivalences from `HW-CRIT-GEOM-LEMMA-001` apply as coordinate geometry:

```math
\operatorname{Re}(s)=\frac12
\Longleftrightarrow
s=1-\overline{s}
\Longleftrightarrow
|s|=|1-s|
\Longleftrightarrow
\tau=0.
```

But this does not assert that zeros of `L(s,chi)` lie on that axis.

## 5. Root number and Gauss-sum boundary

For primitive characters, the root number is built from the normalized Gauss sum.

The Gauss sum is

```math
\tau(\chi)=\sum_{a=1}^{f}\chi(a)e^{2\pi i a/f}.
```

The root number can be written using this Gauss sum and the parity parameter. Exact sign conventions vary by normalization; any theorem-strength use must declare the convention.

Boundary rule:

```text
If a future artifact uses epsilon(chi), it must declare the completed-function convention and Gauss-sum normalization in the same artifact.
```

This avoids silent sign, parity, and conjugation errors.

## 6. Trivial, principal, and nonprincipal cases

The principal character modulo `m` is not automatically primitive unless `m=1` in the primitive sense relevant to the zeta function.

The trivial character yields the Riemann zeta function surface:

```math
\zeta(s).
```

Nonprincipal characters yield Dirichlet `L`-functions whose analytic continuation and functional equations require the primitive conductor normalization.

Boundary rule:

```text
Do not treat principal, primitive, and induced characters as interchangeable.
```

## 7. Critical strip and GRH-shaped target

For primitive Dirichlet characters, the GRH-shaped target concerns nontrivial zeros of `L(s,chi)` and the line

```math
\operatorname{Re}(s)=\frac12.
```

In Heller-Winters notation, a theorem target must distinguish:

1. the character `chi`;
2. its display modulus `m`;
3. its conductor `f`;
4. its parity `a`;
5. whether `chi` is primitive or induced;
6. the completed-function normalization;
7. the zero class under discussion.

A valid target shape is:

```math
L(\rho,\chi)=0
\quad\Longrightarrow\quad
\operatorname{Re}(\rho)=\frac12,
```

where `rho` ranges over the declared nontrivial zero class of the declared primitive/completed surface.

This note does not assert that implication.

## 8. Euler product and reciprocal phase weighting

In the half-plane `Re(s)>1`, the Euler product

```math
L(s,\chi)=\prod_p\left(1-\chi(p)p^{-s}\right)^{-1}
```

shows the phase-weighted reciprocal prime layer.

The ordinary reciprocal pressure

```math
p^{-s}
```

is replaced by

```math
\chi(p)p^{-s}.
```

Thus the harmonic/reciprocal layer from the means ladder becomes character-weighted:

```math
\text{prime reciprocal pressure}
\to
\text{cyclotomic phase-weighted reciprocal pressure}.
```

## 9. Logarithmic transport

The Dirichlet series term can be written

```math
n^{-s}=e^{-s\log n}.
```

The logarithmic coordinate is still

```math
u=\log n.
```

A character-weighted term becomes

```math
\chi(n)e^{-s u}.
```

So the character bridge inserts finite cyclotomic phase data into the same logarithmic transport layer used by the zeta and explicit-formula surfaces.

## 10. Interface to explicit formulas

A future explicit-formula note for arithmetic progressions must not start from a raw wheel diagram. It must pass through the character layer:

```math
1_{n\equiv a\pmod m}
=
\frac{1}{\varphi(m)}\sum_{\chi\bmod m}\overline{\chi(a)}\chi(n)
```

for reduced residue classes.

Then prime sums in residue classes become character-weighted sums, and zeros of the corresponding `L(s,chi)` surfaces enter the formula.

This note does not derive that explicit formula. It only records the required normalization boundary.

## 11. Heller-Winters normalization checklist

Any future analytic artifact using Dirichlet characters must include:

| Field | Required declaration |
|---|---|
| display modulus | `m` |
| conductor | `f` |
| primitive status | primitive / induced |
| parity | `a=0` even or `a=1` odd |
| completed function | exact `Lambda(s,chi)` normalization |
| root number | convention for `epsilon(chi)` |
| zero class | trivial / nontrivial / exceptional cases |
| claim class | diagnostic / theorem target / proof artifact |

This table is a gate against overclaiming and normalization drift.

## 12. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- a functional equation has been proved inside this repository;
- all conductor cases have been discharged;
- induced and primitive characters can be used interchangeably;
- a finite wheel diagram proves prime equidistribution;
- a character sum locates zeros;
- root numbers have been normalized without an explicit convention.

Permitted use:

```text
This note supplies the conductor, parity, primitive-character, and completed-function normalization boundary required before using Dirichlet L-functions in Heller-Winters analytic artifacts.
```

## 13. Relationship to existing artifacts

This note extends:

- `HW-PRIME-CYCLOTOMIC-001` — cyclotomic wheel and Galois labels;
- `HW-PRIME-CHARACTER-001` — Dirichlet character bridge;
- `HW-CRIT-GEOM-LEMMA-001` — critical-axis coordinate equivalence;
- `HW-THM-001` — RH-shaped theorem-target discipline.

## Citation form

```text
[HW-PRIME-CHARACTER-CONDUCTOR-001 @ <merge-sha>]       # conductor/completed L-function normalization only
```

## Versioning

This is `HW-PRIME-CHARACTER-CONDUCTOR-001 v0.1`. Future work may add explicit conductor examples, small character tables, completed-function derivation references, and an explicit formula note for primes in arithmetic progressions.
