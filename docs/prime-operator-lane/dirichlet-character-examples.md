# Dirichlet Character Examples

Identifier: `HW-PRIME-CHARACTER-EXAMPLES-001`  
Status: examples note / normalization sanity check  
Lane: prime/operator lane, with HPHD and theorem-target interfaces  
Claim class: C0 examples + C3 standard finite character background  
Depends on: `HW-PRIME-CHARACTER-001`, `HW-PRIME-CHARACTER-CONDUCTOR-001`  
Non-claim: not RH, not GRH, not a conductor theorem, not an explicit-formula derivation

## 0. Claim boundary

This note gives small finite examples for the Dirichlet-character bridge and conductor-normalization boundary.

It does not prove RH, GRH, prime equidistribution, a functional equation, or an explicit formula. Its purpose is to prevent notation drift by giving concrete primitive and induced character cases.

## 1. Modulus 3: the nontrivial real character

The unit group is

```math
(\mathbb Z/3\mathbb Z)^\times=\{1,2\}.
```

There are two characters modulo `3`.

The principal character is

```math
\chi_0(n)=
\begin{cases}
1,& \gcd(n,3)=1,\\
0,& \gcd(n,3)>1.
\end{cases}
```

The nontrivial character is

```math
\chi_3(n)=
\begin{cases}
0,& 3\mid n,\\
1,& n\equiv 1\pmod 3,\\
-1,& n\equiv 2\pmod 3.
\end{cases}
```

It is primitive of conductor `3`.

Its parity is odd because

```math
\chi_3(-1)=\chi_3(2)=-1.
```

So in the conductor-normalization convention,

```math
a=1.
```

The completed-function surface is therefore

```math
\Lambda(s,\chi_3)
=
\left(\frac{3}{\pi}\right)^{(s+1)/2}
\Gamma\left(\frac{s+1}{2}\right)L(s,\chi_3).
```

This is an example of a primitive odd real character.

## 2. Modulus 4: the nontrivial real character

The unit group is

```math
(\mathbb Z/4\mathbb Z)^\times=\{1,3\}.
```

The nontrivial character modulo `4` is

```math
\chi_4(n)=
\begin{cases}
0,& 2\mid n,\\
1,& n\equiv 1\pmod 4,\\
-1,& n\equiv 3\pmod 4.
\end{cases}
```

It is primitive of conductor `4`.

Its parity is odd because

```math
\chi_4(-1)=\chi_4(3)=-1.
```

So

```math
a=1.
```

The completed-function surface is

```math
\Lambda(s,\chi_4)
=
\left(\frac{4}{\pi}\right)^{(s+1)/2}
\Gamma\left(\frac{s+1}{2}\right)L(s,\chi_4).
```

This is the character associated with the mod-4 split between numbers congruent to `1` and `3`.

## 3. Modulus 5: even and odd nontrivial characters

The unit group is cyclic:

```math
(\mathbb Z/5\mathbb Z)^\times=\{1,2,3,4\}
\cong C_4.
```

Let `2` be a generator modulo `5`:

```math
2^0\equiv1,
\quad
2^1\equiv2,
\quad
2^2\equiv4,
\quad
2^3\equiv3
\pmod 5.
```

Characters are determined by the image of `2`, which may be any fourth root of unity:

```math
\chi(2)\in\{1,-1,i,-i\}.
```

The quadratic character modulo `5` is the character with

```math
\chi_5(2)=-1.
```

It has values

```math
\chi_5(1)=1,
\quad
\chi_5(2)=-1,
\quad
\chi_5(4)=1,
\quad
\chi_5(3)=-1.
```

Since

```math
-1\equiv4\pmod5
```

and

```math
\chi_5(4)=1,
```

this quadratic character is even:

```math
a=0.
```

Its conductor is `5`, so the completed-function surface is

```math
\Lambda(s,\chi_5)
=
\left(\frac{5}{\pi}\right)^{s/2}
\Gamma\left(\frac{s}{2}\right)L(s,\chi_5).
```

The characters with `chi(2)=i` and `chi(2)=-i` are complex primitive characters modulo `5`. Their parity is determined by the value at `-1=4=2^2`:

```math
\chi(4)=\chi(2)^2=-1.
```

So those two complex characters are odd.

## 4. An induced character: modulus 6 induced from modulus 3

Let `chi_3` be the primitive nontrivial character modulo `3` from Section 1.

Define a character modulo `6` by inducing from `chi_3`:

```math
\chi_6(n)=
\begin{cases}
\chi_3(n),& \gcd(n,6)=1,\\
0,& \gcd(n,6)>1.
\end{cases}
```

The unit group is

```math
(\mathbb Z/6\mathbb Z)^\times=\{1,5\}.
```

For units modulo `6`, the values are

```math
\chi_6(1)=1,
\qquad
\chi_6(5)=\chi_3(2)=-1.
```

This character is displayed modulo `6`, but its conductor is `3`.

Boundary point:

```text
The display modulus is 6, but the analytic conductor is 3.
```

Therefore the primitive completed-function normalization is the one attached to conductor `3`, not conductor `6`.

This is exactly why Heller-Winters analytic artifacts must distinguish display modulus from conductor.

## 5. Principal character caution

The principal character modulo `m` is

```math
\chi_{0,m}(n)=
\begin{cases}
1,& \gcd(n,m)=1,\\
0,& \gcd(n,m)>1.
\end{cases}
```

It is generally induced from the trivial character of conductor `1`.

The associated `L`-function has missing Euler factors:

```math
L(s,\chi_{0,m})
=
\zeta(s)\prod_{p\mid m}(1-p^{-s}).
```

Therefore the principal character modulo `m` should not be treated as a primitive new analytic surface of conductor `m` unless a future artifact explicitly declares the completed-object convention being used.

## 6. Orthogonality example modulo 4

Modulo `4`, the two characters are the principal character `chi_0` and the nontrivial character `chi_4`.

For odd `n`, the indicator of the class `1 mod 4` is

```math
1_{n\equiv1\pmod4}
=
\frac12(\chi_0(n)+\chi_4(n)).
```

The indicator of the class `3 mod 4` is

```math
1_{n\equiv3\pmod4}
=
\frac12(\chi_0(n)-\chi_4(n)).
```

This is the simplest concrete example of residue-sector selection becoming character-phase projection.

## 7. Heller-Winters usage rule

When a future note uses a character, it must record:

| Field | Example |
|---|---|
| display modulus | `m=6` |
| conductor | `f=3` |
| primitive status | induced from primitive mod `3` |
| parity | inherited from primitive character |
| completed function | normalized at conductor `f` |
| root-number convention | explicitly declared if used |
| zero class | declared before any GRH-shaped statement |

This examples note is intended to make those fields concrete.

## 8. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- character examples prove prime equidistribution;
- induced and primitive characters have the same completed-function normalization;
- the display modulus is always the conductor;
- finite examples discharge asymptotic analytic claims.

Permitted use:

```text
This note provides small Dirichlet-character examples used to sanity-check conductor, parity, primitive status, and character-projection notation.
```

## Citation form

```text
[HW-PRIME-CHARACTER-EXAMPLES-001 @ <merge-sha>]       # examples and normalization sanity checks only
```

## Versioning

This is `HW-PRIME-CHARACTER-EXAMPLES-001 v0.1`. Future examples may add full character tables for primorial moduli, Gauss sums, and explicit root-number conventions.
