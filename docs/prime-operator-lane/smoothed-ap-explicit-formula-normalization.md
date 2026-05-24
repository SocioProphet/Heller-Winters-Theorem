# Smoothed Arithmetic-Progression Explicit Formula Normalization

Identifier: `HW-PRIME-AP-SMOOTHED-EXPLICIT-001`  
Status: normalization scaffold / analytic boundary note  
Lane: prime/operator lane, with HPHD and theorem-target interfaces  
Claim class: C0 definitions + C3 standard analytic-number-theory background  
Depends on: `HW-PRIME-AP-EXPLICIT-001`, `HW-PRIME-CHARACTER-CONDUCTOR-001`, `HW-PRIME-CHARACTER-P210-001`, `HW-CRIT-GEOM-LEMMA-001`  
Non-claim: not RH, not GRH, not PNT-AP proof, not a zero-location theorem

## 0. Claim boundary

This note fixes the normalization obligations for a future smoothed explicit formula for primes in arithmetic progressions.

It does not prove RH, GRH, Dirichlet's theorem, the prime number theorem in arithmetic progressions, or any zero-location statement.

It records the objects that must be declared before theorem-strength explicit formulas are allowed:

```math
\text{smoothing kernel}
+\text{Mellin transform}
+\text{character conductor}
+\text{completed }L\text{-surface}
+\text{zero registry}
+\text{endpoint convention}.
```

## 1. Smoothed Chebyshev sums

Let `w` be a smoothing function on positive reals. Define a smoothed character-weighted Chebyshev sum by

```math
\Psi_w(X,\chi)
=
\sum_{n\ge1}\chi(n)\Lambda(n)w\left(\frac{n}{X}\right).
```

For a reduced residue class `a mod m`, define

```math
\Psi_w(X;m,a)
=
\sum_{\substack{n\ge1 \\ n\equiv a\pmod m}}
\Lambda(n)w\left(\frac{n}{X}\right).
```

Using character orthogonality,

```math
\Psi_w(X;m,a)
=
\frac{1}{\varphi(m)}
\sum_{\chi\bmod m}
\overline{\chi(a)}\Psi_w(X,\chi),
```

with the same reduced-class and conductor discipline stated in `HW-PRIME-AP-EXPLICIT-001`.

## 2. Mellin transform convention

The Mellin transform of the smoothing function is

```math
\widehat w(s)=\int_0^\infty w(t)t^{s-1}\,dt.
```

The inverse Mellin representation is conventionally written as

```math
w(t)=\frac{1}{2\pi i}\int_{(c)}\widehat w(s)t^{-s}\,ds,
```

on a vertical line where the integral is justified.

Substituting into the smoothed Chebyshev sum gives the formal contour integral

```math
\Psi_w(X,\chi)
=
\frac{1}{2\pi i}\int_{(c)}
-\frac{L'}{L}(s,\chi)X^s\widehat w(s)\,ds.
```

This is the normalized doorway from prime sums to zero sums.

## 3. Required smoothing declarations

Any theorem-strength artifact using this form must declare:

| Field | Required declaration |
|---|---|
| support | compact / Schwartz / exponential / other |
| regularity | smoothness and decay assumptions |
| Mellin transform | exact definition of `w_hat(s)` |
| contour | initial vertical line and allowed shifts |
| poles crossed | `L` poles, gamma poles, Mellin poles |
| endpoint policy | whether sharp cutoffs are approximated or avoided |
| error terms | explicit bounds and dependencies |

Without these declarations, the formula remains a scaffold.

## 4. Primitive-character completed surface

Let `chi` be a primitive Dirichlet character of conductor `f` and parity `a_chi`.

Use the completed function

```math
\Lambda(s,\chi)
=
\left(\frac{f}{\pi}\right)^{(s+a_\chi)/2}
\Gamma\left(\frac{s+a_\chi}{2}\right)L(s,\chi).
```

The functional-equation surface has shape

```math
\Lambda(s,\chi)=\varepsilon(\chi)\Lambda(1-s,\overline{\chi}).
```

This note records the normalization surface only. It does not prove the functional equation.

## 5. Zero registry

A future explicit-formula artifact must maintain a zero registry for each analytic surface.

For each character surface, record:

| Field | Meaning |
|---|---|
| `chi` | displayed character label |
| `m` | display modulus |
| `f` | conductor |
| primitive status | primitive or induced |
| parity | `a_chi` |
| zero symbol | `rho_chi` |
| zero class | nontrivial, trivial, pole, exceptional |
| multiplicity | declared or assumed simple only if proven/assumed |
| symmetry relation | paired under completed-function convention |

The zero registry prevents mixing zeros from characters with different conductors or completions.

## 6. Smoothed explicit-formula shape

For a primitive nonprincipal character, the schematic smoothed form is

```math
\Psi_w(X,\chi)
=
-
\sum_{\rho_\chi}
X^{\rho_\chi}\widehat w(\rho_\chi)
+
\text{trivial-zero/gamma/conductor terms}
+
\text{contour-shift remainder}.
```

For the principal/trivial contribution, a main term is present:

```math
\delta_\chi X\widehat w(1),
```

where `delta_chi` records whether the relevant surface contributes a pole at `s=1`.

Thus the general slot structure is

```math
\Psi_w(X,\chi)
=
\delta_\chi X\widehat w(1)
-
\sum_{\rho_\chi}X^{\rho_\chi}\widehat w(\rho_\chi)
+
\mathcal T_w(X,\chi)
+
\mathcal R_w(X,\chi),
```

where:

- `T_w` collects trivial-zero, gamma-factor, conductor, and smoothing-pole terms;
- `R_w` is the declared remainder from contour movement and truncation.

This is still a scaffold unless `w`, contours, and bounds are specified.

## 7. Arithmetic-progression smoothed form

For a reduced class `a mod m`, the character projector gives

```math
\Psi_w(X;m,a)
=
\frac{1}{\varphi(m)}
\sum_{\chi\bmod m}
\overline{\chi(a)}
\Psi_w(X,\chi).
```

Substituting the slot structure gives

```math
\Psi_w(X;m,a)
=
\frac{X\widehat w(1)}{\varphi(m)}
-
\frac{1}{\varphi(m)}
\sum_{\chi\bmod m}
\overline{\chi(a)}
\sum_{\rho_\chi}X^{\rho_\chi}\widehat w(\rho_\chi)
+
\text{declared lower-order and remainder terms}.
```

This is the normalized AP explicit-formula architecture.

## 8. Conditional GRH envelope

If GRH is assumed for all relevant primitive surfaces, then every nontrivial zero satisfies

```math
\rho_\chi=\frac12+i\gamma_\chi.
```

The zero term becomes

```math
X^{\rho_\chi}\widehat w(\rho_\chi)
=
X^{1/2}e^{i\gamma_\chi\log X}\widehat w\left(\frac12+i\gamma_\chi\right).
```

This is a conditional envelope statement only. It is not a proof that the zeros lie on the critical line.

## 9. Endpoint discipline

Sharp cutoff sums such as

```math
\psi(x;m,a)=\sum_{n\le x,\ n\equiv a\pmod m}\Lambda(n)
```

require endpoint conventions when `x` crosses a prime power.

Smoothed sums avoid some endpoint ambiguity by replacing the sharp indicator with `w(n/X)`. A future artifact that returns to sharp cutoff notation must declare:

1. left-continuous, right-continuous, or midpoint convention;
2. whether prime-power endpoints receive half weight;
3. whether smoothing is removed by limiting argument;
4. which bounds survive the limiting process.

## 10. Heller-Winters usage rule

A future proof/theorem-target artifact may cite this note only for normalization structure.

It must still supply:

- the concrete smoothing function `w`;
- the Mellin transform and domain;
- the contour shift and residues;
- the conductor-indexed zero registry;
- the explicit lower-order terms;
- the exact error bounds;
- the claim status: unconditional, conditional-on-GRH, diagnostic, or target.

## 11. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- PNT in arithmetic progressions is proved;
- smoothing removes the need for conductor normalization;
- zero sums are valid without declaring the zero registry;
- endpoint issues disappear for sharp cutoffs;
- the scaffold is a fully normalized theorem.

Permitted use:

```text
This note supplies the normalization scaffold for smoothed arithmetic-progression explicit formulas, including smoothing, Mellin transform, conductor-indexed zero registries, and endpoint discipline.
```

## Citation form

```text
[HW-PRIME-AP-SMOOTHED-EXPLICIT-001 @ <merge-sha>]       # smoothed AP explicit-formula normalization only
```

## Versioning

This is `HW-PRIME-AP-SMOOTHED-EXPLICIT-001 v0.1`. Future artifacts may instantiate a specific smoothing kernel, prove the contour shift under stated hypotheses, or generate a conductor-indexed zero registry fixture.
