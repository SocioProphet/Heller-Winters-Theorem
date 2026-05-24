# Finite Character Tables for Small Primorial Wheels

Identifier: `HW-PRIME-CHARACTER-TABLES-001`  
Status: finite examples note / notation sanity check  
Lane: prime/operator lane  
Claim class: C0 examples + C3 standard finite character background  
Depends on: `HW-PRIME-CYCLOTOMIC-001`, `HW-PRIME-CHARACTER-001`, `HW-PRIME-CHARACTER-EXAMPLES-001`  
Non-claim: not RH, not GRH, not a prime-equidistribution theorem, not an explicit-formula derivation

## 0. Claim boundary

This note records small finite character tables for primorial wheels. Its purpose is to make the bridge from wheel residues to character projectors concrete.

It does not prove RH, GRH, prime equidistribution, or any zero-location statement. It only gives finite group examples.

## 1. General finite character-table rule

For a modulus `m`, let

```math
G_m=(\mathbb Z/m\mathbb Z)^\times.
```

A Dirichlet character modulo `m`, restricted to the units, is a group homomorphism

```math
\chi:G_m\to\mathbb C^\times.
```

The finite character group is the dual group

```math
\widehat{G_m}=\operatorname{Hom}(G_m,\mathbb C^\times).
```

A character table records the values

```math
\chi(a)
```

for `a in G_m` and `chi in \widehat{G_m}`.

The character table is a finite Fourier transform on the wheel unit group.

## 2. Primorial wheel P(2)=2

For

```math
m=2,
```

we have

```math
G_2=(\mathbb Z/2\mathbb Z)^\times=\{1\}.
```

There is only the trivial character.

| residue `a` | `chi_0(a)` |
|---:|---:|
| 1 | 1 |

This wheel has no nontrivial character structure.

## 3. Primorial wheel P(3)=6

For

```math
m=6=2\cdot3,
```

we have

```math
G_6=(\mathbb Z/6\mathbb Z)^\times=\{1,5\}.
```

This group is cyclic of order `2`. Its character table is:

| residue `a` | `chi_0(a)` | `chi_6(a)` |
|---:|---:|---:|
| 1 | 1 | 1 |
| 5 | 1 | -1 |

Here `chi_6` is displayed modulo `6` but is induced from the primitive nontrivial character modulo `3`. Its conductor is `3`.

This is the smallest example where the display modulus and conductor differ.

## 4. Primorial wheel P(5)=30

For

```math
m=30=2\cdot3\cdot5,
```

we have

```math
G_{30}=(\mathbb Z/30\mathbb Z)^\times
=\{1,7,11,13,17,19,23,29\}.
```

By the Chinese remainder theorem,

```math
G_{30}\cong(\mathbb Z/3\mathbb Z)^\times\times(\mathbb Z/5\mathbb Z)^\times
\cong C_2\times C_4.
```

Therefore

```math
\widehat{G_{30}}\cong C_2\times C_4.
```

We can generate all characters from two basis characters:

1. `alpha`, the mod-3 sign character;
2. `beta`, a primitive mod-5 character with `beta(2)=i`.

Then every character on `G_30` has the form

```math
\chi_{j,k}=\alpha^j\beta^k,
\qquad
j\in\{0,1\},\quad k\in\{0,1,2,3\}.
```

## 5. Generator table for G_30

The generator values are:

| residue `a` | `alpha(a)` | `beta(a)` |
|---:|---:|---:|
| 1 | 1 | 1 |
| 7 | 1 | i |
| 11 | -1 | 1 |
| 13 | 1 | -i |
| 17 | -1 | i |
| 19 | 1 | -1 |
| 23 | -1 | -i |
| 29 | -1 | -1 |

All eight characters are obtained by multiplying powers of these two columns.

The full character family is:

```math
\{\chi_{0,0},\chi_{1,0},\chi_{0,1},\chi_{0,2},\chi_{0,3},\chi_{1,1},\chi_{1,2},\chi_{1,3}\}.
```

where

```math
\chi_{j,k}(a)=\alpha(a)^j\beta(a)^k.
```

## 6. Principal and induced characters in the P(5)=30 wheel

Not every character displayed modulo `30` has conductor `30`.

Examples:

| character | display modulus | conductor | note |
|---|---:|---:|---|
| `chi_{0,0}` | 30 | 1 | principal, induced from trivial conductor |
| `chi_{1,0}` | 30 | 3 | induced from nontrivial mod-3 character |
| `chi_{0,2}` | 30 | 5 | quadratic mod-5 character |
| `chi_{0,1}` | 30 | 5 | primitive complex mod-5 character |
| `chi_{1,1}` | 30 | 15 | product of primitive mod-3 and mod-5 components |

This is the concrete reason the conductor-normalization note requires separate fields for display modulus and conductor.

## 7. Character projectors on G_30

For a reduced residue class `a mod 30`, the finite character projector is

```math
1_{n\equiv a\pmod{30}}
=
\frac{1}{\varphi(30)}
\sum_{\chi\bmod 30}\overline{\chi(a)}\chi(n)
```

for `gcd(n,30)=1`.

Since

```math
\varphi(30)=8,
```

this becomes

```math
1_{n\equiv a\pmod{30}}
=
\frac18
\sum_{j=0}^{1}\sum_{k=0}^{3}
\overline{\chi_{j,k}(a)}\chi_{j,k}(n).
```

Thus each wheel sector is recovered by a finite character-phase projection.

## 8. Relation to roots of unity

The `P(5)=30` cyclotomic wheel uses

```math
\zeta_{30}=e^{2\pi i/30}.
```

The primitive root shell is

```math
\{\zeta_{30}^a:a\in G_{30}\}.
```

The character table is dual to this unit shell. The wheel has two complementary finite phase views:

| View | Object | Meaning |
|---|---|---|
| root shell | `zeta_30^a` for `a in G_30` | primitive cyclotomic positions |
| character table | `chi(a)` | finite phase projectors on unit residues |

This is the finite algebraic core behind the visual wheel.

## 9. Heller-Winters usage rule

When a future artifact discusses a primorial wheel, it should distinguish:

| Field | Example for `m=30` |
|---|---|
| wheel modulus | `m=30` |
| unit group | `G_30=(Z/30Z)^x` |
| root shell | `{zeta_30^a:gcd(a,30)=1}` |
| character group | `G_30^hat ~= C_2 x C_4` |
| display modulus | `30` |
| conductor | depends on character |
| projector formula | character orthogonality |

This prevents collapsing wheel positions, primitive roots, characters, and analytic conductors into one undifferentiated object.

## 10. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- finite character tables imply asymptotic prime equidistribution;
- display modulus equals conductor;
- wheel sector projection locates zeros;
- primorial wheels alone derive explicit formulas;
- small examples discharge theorem targets.

Permitted use:

```text
This note supplies finite character-table examples for small primorial wheels, showing how wheel sectors are represented by character projectors on the unit group.
```

## Citation form

```text
[HW-PRIME-CHARACTER-TABLES-001 @ <merge-sha>]       # finite character tables only
```

## Versioning

This is `HW-PRIME-CHARACTER-TABLES-001 v0.1`. Future revisions may add machine-generated tables for `P(7)=210`, Gauss sums, and explicit root-number conventions.
