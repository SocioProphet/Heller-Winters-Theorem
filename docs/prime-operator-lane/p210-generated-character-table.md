# P(7)=210 Generated Character Table Scaffold

Identifier: `HW-PRIME-CHARACTER-P210-001`  
Status: generated finite examples scaffold / notation sanity check  
Lane: prime/operator lane  
Claim class: C0 examples + C3 standard finite character background  
Depends on: `HW-PRIME-CHARACTER-TABLES-001`, `HW-PRIME-CHARACTER-EXAMPLES-001`, `HW-PRIME-CYCLOTOMIC-001`  
Non-claim: not RH, not GRH, not a prime-equidistribution theorem, not an explicit-formula derivation

## 0. Claim boundary

This note gives a deterministic scaffold for the first larger primorial wheel character table:

```math
P(7)=2\cdot3\cdot5\cdot7=210.
```

It is a finite algebra artifact. It does not prove RH, GRH, prime equidistribution, or any zero-location statement.

The purpose is to make the `P(7)=210` wheel reproducible without hand-waving: all characters are generated from three finite cyclic components.

## 1. Unit group

The unit group is

```math
G_{210}=(\mathbb Z/210\mathbb Z)^\times.
```

Its order is

```math
\varphi(210)=210\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac15\right)\left(1-\frac17\right)=48.
```

By the Chinese remainder theorem,

```math
G_{210}
\cong
(\mathbb Z/2\mathbb Z)^\times
\times
(\mathbb Z/3\mathbb Z)^\times
\times
(\mathbb Z/5\mathbb Z)^\times
\times
(\mathbb Z/7\mathbb Z)^\times.
```

Since the first factor is trivial,

```math
G_{210}\cong C_2\times C_4\times C_6.
```

Therefore the character group is also

```math
\widehat{G_{210}}\cong C_2\times C_4\times C_6.
```

There are `48` characters displayed modulo `210`.

## 2. Generator convention

We use three basis characters:

1. `alpha`, the mod-3 sign character;
2. `beta`, a primitive mod-5 character with `beta(2)=i`;
3. `gamma`, a primitive mod-7 character with `gamma(3)=omega_6`, where

```math
\omega_6=e^{2\pi i/6}.
```

Every displayed character modulo `210` is then

```math
\chi_{j,k,l}=\alpha^j\beta^k\gamma^l,
```

with

```math
j\in\{0,1\},\qquad k\in\{0,1,2,3\},\qquad l\in\{0,1,2,3,4,5\}.
```

Thus the full table has

```math
2\cdot4\cdot6=48
```

characters and `48` unit residues.

## 3. Discrete-log generation rule

For each reduced residue `a mod 210`, define exponents:

```math
e_3(a)\in\mathbb Z/2\mathbb Z,
\qquad
e_5(a)\in\mathbb Z/4\mathbb Z,
\qquad
e_7(a)\in\mathbb Z/6\mathbb Z.
```

They are determined by:

```math
a\equiv 2^{e_3(a)}\pmod3,
```

```math
a\equiv 2^{e_5(a)}\pmod5,
```

and

```math
a\equiv 3^{e_7(a)}\pmod7.
```

Then

```math
\alpha(a)=(-1)^{e_3(a)},
```

```math
\beta(a)=i^{e_5(a)},
```

and

```math
\gamma(a)=\omega_6^{e_7(a)}.
```

The full character value is

```math
\chi_{j,k,l}(a)
=
(-1)^{j e_3(a)}i^{k e_5(a)}\omega_6^{l e_7(a)}.
```

This formula is the deterministic character table. The table below supplies the exponent triples.

## 4. Reduced residue exponent table

| residue `a` | `e3` | `e5` | `e7` |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 11 | 1 | 0 | 4 |
| 13 | 0 | 3 | 3 |
| 17 | 1 | 1 | 1 |
| 19 | 0 | 2 | 5 |
| 23 | 1 | 3 | 2 |
| 29 | 1 | 2 | 0 |
| 31 | 0 | 0 | 1 |
| 37 | 0 | 1 | 2 |
| 41 | 1 | 0 | 3 |
| 43 | 0 | 3 | 0 |
| 47 | 1 | 1 | 5 |
| 53 | 1 | 3 | 4 |
| 59 | 1 | 2 | 1 |
| 61 | 0 | 0 | 5 |
| 67 | 0 | 1 | 4 |
| 71 | 1 | 0 | 0 |
| 73 | 0 | 3 | 1 |
| 79 | 0 | 2 | 2 |
| 83 | 1 | 3 | 3 |
| 89 | 1 | 2 | 5 |
| 97 | 0 | 1 | 3 |
| 101 | 1 | 0 | 1 |
| 103 | 0 | 3 | 5 |
| 107 | 1 | 1 | 2 |
| 109 | 0 | 2 | 4 |
| 113 | 1 | 3 | 0 |
| 121 | 0 | 0 | 2 |
| 127 | 0 | 1 | 0 |
| 131 | 1 | 0 | 5 |
| 137 | 1 | 1 | 4 |
| 139 | 0 | 2 | 3 |
| 143 | 1 | 3 | 1 |
| 149 | 1 | 2 | 2 |
| 151 | 0 | 0 | 4 |
| 157 | 0 | 1 | 1 |
| 163 | 0 | 3 | 2 |
| 167 | 1 | 1 | 3 |
| 169 | 0 | 2 | 0 |
| 173 | 1 | 3 | 5 |
| 179 | 1 | 2 | 4 |
| 181 | 0 | 0 | 3 |
| 187 | 0 | 1 | 5 |
| 191 | 1 | 0 | 2 |
| 193 | 0 | 3 | 4 |
| 197 | 1 | 1 | 0 |
| 199 | 0 | 2 | 1 |
| 209 | 1 | 2 | 3 |

## 5. Sector projector for the 210 wheel

For a reduced residue class `a mod 210`, the finite character projector is

```math
1_{n\equiv a\pmod{210}}
=
\frac{1}{48}
\sum_{j=0}^{1}\sum_{k=0}^{3}\sum_{l=0}^{5}
\overline{\chi_{j,k,l}(a)}\chi_{j,k,l}(n),
```

for `gcd(n,210)=1`.

This is the `P(7)=210` finite Fourier projector on the wheel unit group.

## 6. Cyclotomic root shell

The associated cyclotomic field is

```math
\mathbb Q(\zeta_{210}).
```

The primitive root shell is

```math
\{\zeta_{210}^a:a\in G_{210}\}.
```

The 48 residues in the exponent table index both:

1. primitive `210`-th roots of unity;
2. Galois automorphism labels of `Q(zeta_210)`;
3. inputs to the finite character table.

Thus the `P(7)=210` wheel is simultaneously a residue wheel, primitive-root shell, Galois label set, and finite character-transform domain.

## 7. Conductor warning

The `48` characters displayed modulo `210` do not all have conductor `210`.

A character

```math
\chi_{j,k,l}=\alpha^j\beta^k\gamma^l
```

has conductor equal to the product of the prime-power components on which it is nontrivial, with the component conductor inherited from the corresponding primitive factor.

Examples:

| character | display modulus | conductor | note |
|---|---:|---:|---|
| `chi_{0,0,0}` | 210 | 1 | principal |
| `chi_{1,0,0}` | 210 | 3 | mod-3 sign component only |
| `chi_{0,2,0}` | 210 | 5 | quadratic mod-5 component |
| `chi_{0,0,3}` | 210 | 7 | quadratic mod-7 component |
| `chi_{1,1,0}` | 210 | 15 | mod-3 and mod-5 components |
| `chi_{1,1,1}` | 210 | 105 | nontrivial on 3, 5, and 7 |

Any analytic use must normalize by conductor, not merely by display modulus.

## 8. Heller-Winters usage rule

Use this artifact only as finite algebra scaffolding.

A later explicit-formula artifact may use the projector in Section 5, but it must pass through the conductor and completed-`L`-function normalization discipline in `HW-PRIME-CHARACTER-CONDUCTOR-001`.

## 9. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- the `210` wheel proves prime equidistribution;
- finite character projectors locate analytic zeros;
- display modulus `210` is always the conductor;
- finite residue tables discharge asymptotic theorem targets.

Permitted use:

```text
This note supplies a deterministic generated character-table scaffold for the P(7)=210 primorial wheel, including exponent triples and the finite sector projector.
```

## Citation form

```text
[HW-PRIME-CHARACTER-P210-001 @ <merge-sha>]       # P(7)=210 finite character table scaffold only
```

## Versioning

This is `HW-PRIME-CHARACTER-P210-001 v0.1`. Future revisions may add a script that regenerates the exponent table, Gauss sums, root-number conventions, and machine-checkable projector identities.
