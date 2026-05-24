# Arithmetic-Progression Explicit Formula Boundary

Identifier: `HW-PRIME-AP-EXPLICIT-001`  
Status: boundary note / analytic scaffold  
Lane: prime/operator lane, with HPHD and theorem-target interfaces  
Claim class: C0 definitions + C3 standard analytic-number-theory background  
Depends on: `HW-PRIME-CHARACTER-001`, `HW-PRIME-CHARACTER-CONDUCTOR-001`, `HW-PRIME-CHARACTER-TABLES-001`, `HW-PRIME-CHARACTER-P210-001`, `HW-CRIT-GEOM-LEMMA-001`  
Non-claim: not RH, not GRH, not prime-equidistribution proof, not a zero-location theorem

## 0. Claim boundary

This note records the boundary required before discussing explicit formulas for primes in arithmetic progressions.

The finite wheel/cyclotomic/character artifacts establish the path:

```math
\text{wheel sector}
\to
\text{character projector}
\to
L(s,\chi)
\to
\text{zeros of completed }L\text{-surfaces}.
```

This note does not prove the prime number theorem for arithmetic progressions, Dirichlet's theorem, RH, GRH, or any zero-location statement.

It only records the classical analytic scaffold and the claim boundaries needed for Heller-Winters artifacts.

## 1. Reduced residue classes

Let `m >= 1` and let `a` be a reduced residue class:

```math
\gcd(a,m)=1.
```

The wheel sector is

```math
n\equiv a\pmod m.
```

The finite character projector is

```math
1_{n\equiv a\pmod m}
=
\frac{1}{\varphi(m)}\sum_{\chi\bmod m}\overline{\chi(a)}\chi(n),
```

for `gcd(n,m)=1`.

This identity is finite algebra. It is not an asymptotic theorem.

## 2. Character-weighted Chebyshev functions

Define the character-weighted Chebyshev function

```math
\psi(x,\chi)=\sum_{n\le x}\chi(n)\Lambda(n),
```

where `Lambda(n)` is the von Mangoldt function.

The arithmetic-progression Chebyshev function is

```math
\psi(x;m,a)=\sum_{\substack{n\le x \\ n\equiv a\pmod m}}\Lambda(n).
```

Using character orthogonality, for reduced `a`, the formal decomposition is

```math
\psi(x;m,a)
=
\frac{1}{\varphi(m)}\sum_{\chi\bmod m}\overline{\chi(a)}\psi(x,\chi),
```

with the usual boundary discipline around non-reduced terms and prime powers dividing the modulus.

This is the bridge from wheel sectors to character-weighted analytic sums.

## 3. Logarithmic derivative interface

For `Re(s)>1`, a Dirichlet `L`-function has Euler product

```math
L(s,\chi)=\prod_p\left(1-\chi(p)p^{-s}\right)^{-1}.
```

Its logarithmic derivative has the formal Dirichlet-series expansion

```math
-\frac{L'}{L}(s,\chi)
=
\sum_{n=1}^{\infty}\frac{\chi(n)\Lambda(n)}{n^s}.
```

This is the analytic doorway through which zeros of `L(s,chi)` enter explicit formulas for `psi(x,chi)`.

Boundary rule:

```text
Any explicit-formula artifact must declare the character, conductor, completion, zero class, and error terms before making theorem-strength claims.
```

## 4. Schematic explicit formula for primitive characters

Let `chi` be a primitive Dirichlet character with conductor `f`, parity `a_chi`, and completed function as normalized in `HW-PRIME-CHARACTER-CONDUCTOR-001`:

```math
\Lambda(s,\chi)
=
\left(\frac{f}{\pi}\right)^{(s+a_\chi)/2}
\Gamma\left(\frac{s+a_\chi}{2}\right)L(s,\chi).
```

A schematic explicit-formula shape is:

```math
\psi(x,\chi)
=
\delta_\chi x
-
\sum_{\rho_\chi}\frac{x^{\rho_\chi}}{\rho_\chi}
+
\text{trivial-zero/gamma/conductor terms}
+
\text{endpoint terms},
```

where:

- `delta_chi=1` for the principal/trivial contribution in the relevant normalized setting;
- `delta_chi=0` for nonprincipal primitive characters;
- `rho_chi` ranges over the declared nontrivial zeros of `L(s,chi)`;
- the remaining terms depend on the exact smoothing, endpoint convention, and completed-function normalization.

This note intentionally does not freeze a theorem-strength formula. It records the structural slots that future artifacts must fill.

## 5. Arithmetic-progression explicit formula shape

Combining the character projector with the schematic character formula gives the arithmetic-progression shape:

```math
\psi(x;m,a)
=
\frac{x}{\varphi(m)}
-
\frac{1}{\varphi(m)}
\sum_{\chi\bmod m}\overline{\chi(a)}
\sum_{\rho_\chi}\frac{x^{\rho_\chi}}{\rho_\chi}
+
\text{normalization-dependent lower-order terms}.
```

This is the classical architecture: finite residue-sector selection becomes a sum over character-weighted zero contributions.

Boundary warning:

```text
This formula shape is not a proof of equidistribution. The strength of the resulting error term depends on what is known or assumed about the zeros rho_chi.
```

## 6. GRH-shaped envelope

If GRH is assumed for the relevant Dirichlet `L`-functions, then the nontrivial zeros satisfy

```math
\operatorname{Re}(\rho_\chi)=\frac12.
```

Under that assumption, the oscillatory terms have square-root envelope shape:

```math
x^{\rho_\chi}=x^{1/2}e^{i\gamma_\chi\log x}.
```

This mirrors the zeta explicit-formula grammar already used in the HPHD lane:

```math
x^\rho=e^{\rho\log x}=e^{\sigma\log x}e^{i\gamma\log x}.
```

But this note does not assume or prove GRH. It only records the conditional envelope form.

## 7. Relation to the P(7)=210 wheel

For the `210` wheel, a reduced sector `a mod 210` has projector

```math
1_{n\equiv a\pmod{210}}
=
\frac{1}{48}
\sum_{j=0}^{1}\sum_{k=0}^{3}\sum_{l=0}^{5}
\overline{\chi_{j,k,l}(a)}\chi_{j,k,l}(n).
```

Therefore a future `210`-sector explicit formula must sum over the `48` displayed characters, while normalizing each analytic surface by its conductor rather than by the display modulus alone.

This is exactly why `HW-PRIME-CHARACTER-CONDUCTOR-001` is a dependency.

## 8. Means-ladder placement

The arithmetic-progression explicit-formula bridge places the means ladder as follows:

| Layer | Object | Role |
|---|---|---|
| arithmetic | residue averaging by `1/phi(m)` | sector decomposition |
| geometric | `sqrt(x)` envelope under critical-line assumptions | zero-contribution scale |
| logarithmic | `x^rho=e^{rho log x}` | phase transport |
| harmonic / reciprocal | `-L'/L` and Euler products | prime-power weighted reciprocal pressure |

The finite wheel itself is not the analytic theorem. The theorem-strength information enters through `L(s,chi)` zeros and their allowed real parts.

## 9. Heller-Winters usage rule

A future theorem-target or proof artifact involving primes in arithmetic progressions must declare:

| Field | Required declaration |
|---|---|
| modulus | display modulus `m` |
| sector | reduced residue class `a` |
| characters | all `chi mod m` or a declared subset |
| conductor | conductor of each analytic character surface |
| completed function | exact `Lambda(s,chi)` convention |
| zero class | nontrivial/trivial/exceptional zeros |
| explicit formula | smoothed or unsmoothed; endpoint convention |
| claim status | theorem target, conditional statement, diagnostic, or proof |

This table is a guard against turning finite wheel identities into analytic zero-location claims.

## 10. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- the prime number theorem for arithmetic progressions is proved;
- Dirichlet's theorem is proved;
- finite character projectors imply asymptotic equidistribution;
- the `210` wheel locates zeros;
- display modulus and conductor can be collapsed;
- the schematic formula is a fully normalized explicit formula.

Permitted use:

```text
This note records the classical boundary from finite character projectors on wheel sectors to character-weighted Chebyshev functions and schematic explicit-formula surfaces for primes in arithmetic progressions.
```

## Citation form

```text
[HW-PRIME-AP-EXPLICIT-001 @ <merge-sha>]       # AP explicit-formula boundary only
```

## Versioning

This is `HW-PRIME-AP-EXPLICIT-001 v0.1`. Future artifacts may add a fully normalized smoothed explicit formula, conductor-indexed zero registries, or worked examples for small moduli.
