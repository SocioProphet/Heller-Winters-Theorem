# Arithmetic-Progression Contour-Shift Proof Obligations

Identifier: `HW-PRIME-AP-CONTOUR-OBLIGATIONS-001`  
Status: proof-obligation scaffold / analytic boundary note  
Lane: prime/operator lane, with HPHD and theorem-target interfaces  
Claim class: C0 definitions + C3 standard analytic-number-theory background  
Depends on: `HW-PRIME-AP-KERNEL-EXP-001`, `HW-PRIME-AP-SMOOTHED-EXPLICIT-001`, `HW-PRIME-CHARACTER-CONDUCTOR-001`, `HW-CRIT-GEOM-LEMMA-001`  
Non-claim: not RH, not GRH, not PNT-AP proof, not a zero-location theorem

## 0. Claim boundary

This note records the proof obligations required before an exponential-kernel arithmetic-progression explicit-formula scaffold may be treated as theorem-strength.

It does not prove RH, GRH, the prime number theorem in arithmetic progressions, a full contour-shift theorem, or any zero-location statement.

The starting scaffold from `HW-PRIME-AP-KERNEL-EXP-001` is

```math
\Psi_{\exp}(X,\chi)
=
\frac{1}{2\pi i}\int_{(c)}
-\frac{L'}{L}(s,\chi)X^s\Gamma(s)\,ds,
\qquad c>1.
```

The goal of this note is to specify what must be proven to shift the line of integration and account for all residues and remainders.

## 1. Required analytic surface declaration

Before a contour shift is attempted, the artifact must declare:

| Field | Required declaration |
|---|---|
| character | `chi` |
| display modulus | `m` |
| conductor | primitive conductor `f` |
| primitive status | primitive, induced, principal, or reduced to primitive |
| parity | `a_chi` |
| completed function | exact `Lambda(s,chi)` convention |
| root number | convention for `epsilon(chi)` if used |
| zero registry | nontrivial/trivial/pole classes |

No contour-shift statement is valid if the conductor and completed-function convention are implicit.

## 2. Initial contour obligation

For the exponential kernel, the initial line must satisfy

```math
c>1.
```

The artifact must prove or cite that the integral

```math
\frac{1}{2\pi i}\int_{(c)}
-\frac{L'}{L}(s,\chi)X^s\Gamma(s)\,ds
```

converges and equals

```math
\sum_{n\ge1}\chi(n)\Lambda(n)e^{-n/X}.
```

This requires justifying interchange of the Dirichlet series with the Mellin inversion integral.

## 3. Rectangle and truncation obligation

A theorem-strength contour shift must introduce a finite rectangle or an explicitly justified infinite contour movement.

For a finite rectangle, declare:

```math
c>1,
\qquad
\sigma_L<0,
\qquad
T>0.
```

The boundary consists of:

1. right vertical segment `Re(s)=c`;
2. left vertical segment `Re(s)=sigma_L`;
3. top horizontal segment `Im(s)=T`;
4. bottom horizontal segment `Im(s)=-T`.

The artifact must bound the horizontal integrals and the left vertical integral before sending `T` or `sigma_L` to a limit.

## 4. Pole and residue registry

The shift must enumerate every pole crossed by

```math
-\frac{L'}{L}(s,\chi)X^s\Gamma(s).
```

Required registry:

| Source | Candidate locations | Required action |
|---|---|---|
| pole of `L` | usually `s=1` for principal/trivial surface | main-term residue |
| nontrivial zeros | `rho_chi` | zero residue `-X^{rho_chi} Gamma(rho_chi)` |
| trivial zeros | completion-dependent negative points | lower-order terms |
| Gamma poles | `s=0,-1,-2,...` | smoothing-kernel residues |
| exceptional zeros | if relevant | declared separately |
| coincident poles | overlapping locations | multiplicity and cancellation handling |

Coincident poles are especially important: a zero of `L(s,chi)` may interact with a pole of `Gamma(s)` or a trivial-zero location under the chosen normalization. These cases must not be hidden inside a generic error term.

## 5. Nontrivial-zero residue obligation

For a zero `rho_chi` of `L(s,chi)` of multiplicity `m_rho`, the logarithmic derivative has residue `-m_rho` at `rho_chi`.

Therefore the crossed contribution has the form

```math
-m_\rho X^{\rho_\chi}\Gamma(\rho_\chi).
```

If the artifact assumes simple zeros, that assumption must be stated. Otherwise multiplicities must be carried.

## 6. Principal contribution obligation

If the relevant surface has a pole at `s=1`, then

```math
-\frac{L'}{L}(s,\chi)
```

has a simple pole at `s=1` with residue `-1` for `L'/L`, hence `+1` for `-L'/L`.

The exponential kernel gives

```math
X^1\Gamma(1)=X.
```

So the principal main term is

```math
X.
```

When projected into a reduced residue class modulo `m`, this becomes

```math
\frac{X}{\varphi(m)}.
```

This contribution must be separated from nonprincipal character surfaces.

## 7. Gamma-pole obligation

The Gamma function has simple poles at

```math
s=0,-1,-2,\ldots.
```

with residues

```math
\operatorname{Res}_{s=-k}\Gamma(s)=\frac{(-1)^k}{k!}.
```

A shifted-contour artifact must say whether these poles are crossed and, if so, include their residues:

```math
\operatorname{Res}_{s=-k}
\left(
-\frac{L'}{L}(s,\chi)X^s\Gamma(s)
\right).
```

This is part of the smoothing-kernel lower-order term.

## 8. Trivial-zero obligation

The trivial zeros of `L(s,chi)` depend on the completed-function convention and the character parity.

The artifact must derive or cite their locations from the declared completed function

```math
\Lambda(s,\chi)
=
\left(\frac{f}{\pi}\right)^{(s+a_\chi)/2}
\Gamma\left(\frac{s+a_\chi}{2}\right)L(s,\chi).
```

The trivial-zero contribution must be listed separately from Gamma-pole contributions.

## 9. Horizontal-bound obligation

For a finite rectangular contour, the top and bottom horizontal integrals must be bounded.

A theorem-strength artifact must provide bounds for

```math
-\frac{L'}{L}(\sigma\pm iT,\chi)X^{\sigma\pm iT}\Gamma(\sigma\pm iT)
```

uniformly for `sigma` in the shifted interval.

The exponential kernel helps because `Gamma(s)` decays rapidly in vertical strips, but that decay still must be stated and used explicitly.

## 10. Left-contour obligation

The shifted left vertical integral must be bounded or retained as an explicit remainder:

```math
\mathcal R_{\exp}(X,\chi;\sigma_L,T).
```

The artifact must state whether this remainder is:

1. sent to zero;
2. bounded by an explicit function of `X`, `f`, and `T`;
3. retained as part of the formula.

No theorem-strength formula may drop the left-contour integral without a bound.

## 11. Zero-sum convergence and ordering

The nontrivial-zero sum

```math
\sum_{\rho_\chi}X^{\rho_\chi}\Gamma(\rho_\chi)
```

requires an ordering convention.

Acceptable declarations include:

1. symmetric height truncation `|Im(rho_chi)|<=T` followed by a limit;
2. absolutely convergent smoothed sum with proof;
3. distributional or contour-defined interpretation.

The artifact must specify which interpretation is used.

## 12. Arithmetic-progression projection obligation

After each character formula is normalized, the AP projection is

```math
\Psi_{\exp}(X;m,a)
=
\frac{1}{\varphi(m)}
\sum_{\chi\bmod m}\overline{\chi(a)}\Psi_{\exp}(X,\chi).
```

The artifact must ensure all displayed characters are reduced to the correct conductor-normalized analytic surfaces before summing. Display modulus `m` must not be treated as the conductor unless proven.

## 13. Conditional GRH envelope obligation

If a future artifact states a GRH-conditional envelope, it must explicitly mark the assumption:

```math
\operatorname{GRH}(\chi):
\quad
L(\rho,\chi)=0\text{ nontrivial}
\Rightarrow
\operatorname{Re}(\rho)=\frac12.
```

Only under this assumption may it rewrite

```math
X^{\rho_\chi}\Gamma(\rho_\chi)
```

as

```math
X^{1/2}e^{i\gamma_\chi\log X}
\Gamma\left(\frac12+i\gamma_\chi\right).
```

This is conditional envelope language, not proof.

## 14. Heller-Winters proof gate

A theorem-strength contour-shift artifact must include the following checklist:

| Gate | Required evidence |
|---|---|
| initial integral | Mellin inversion and interchange justified |
| conductor normalization | primitive/induced surfaces declared |
| contour rectangle | `c`, `sigma_L`, and `T` declared |
| residue registry | all poles and zeros listed |
| multiplicities | carried or explicitly assumed simple |
| horizontal bounds | proved/cited |
| left-contour bound | proved/cited or retained |
| zero-sum convention | declared |
| AP projection | conductor-safe character sum |
| claim class | unconditional / conditional / diagnostic / target |

## 15. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- PNT in arithmetic progressions is proved;
- contour shifts are automatically valid;
- Gamma decay alone justifies dropping all contours;
- zero sums can be reordered without convention;
- display modulus is conductor;
- endpoint-free smoothing eliminates all analytic obligations.

Permitted use:

```text
This note records the proof obligations required to upgrade the exponential-kernel AP explicit-formula scaffold into a theorem-strength contour-shift artifact.
```

## Citation form

```text
[HW-PRIME-AP-CONTOUR-OBLIGATIONS-001 @ <merge-sha>]       # contour-shift proof obligations only
```

## Versioning

This is `HW-PRIME-AP-CONTOUR-OBLIGATIONS-001 v0.1`. Future artifacts may instantiate the contour rectangle, prove horizontal bounds, or define a machine-checkable zero-registry schema.
