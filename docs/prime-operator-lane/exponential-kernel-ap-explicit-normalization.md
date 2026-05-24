# Exponential Kernel for Smoothed AP Explicit Formulae

Identifier: `HW-PRIME-AP-KERNEL-EXP-001`  
Status: concrete smoothing-kernel instantiation / analytic scaffold  
Lane: prime/operator lane, with HPHD and theorem-target interfaces  
Claim class: C0 definitions + C3 standard analytic-number-theory background  
Depends on: `HW-PRIME-AP-SMOOTHED-EXPLICIT-001`, `HW-PRIME-AP-EXPLICIT-001`, `HW-PRIME-CHARACTER-CONDUCTOR-001`  
Non-claim: not RH, not GRH, not PNT-AP proof, not a zero-location theorem

## 0. Claim boundary

This note instantiates one smoothing kernel for future arithmetic-progression explicit-formula work:

```math
w(t)=e^{-t}.
```

The kernel is chosen because its Mellin transform is explicit:

```math
\widehat w(s)=\Gamma(s).
```

This note does not prove RH, GRH, the prime number theorem in arithmetic progressions, a contour-shift theorem, or any zero-location statement. It only fixes a concrete smoothing convention that future theorem-target artifacts may cite.

## 1. Kernel definition

Let

```math
w_{\exp}(t)=e^{-t},\qquad t>0.
```

The smoothed character-weighted Chebyshev sum is

```math
\Psi_{\exp}(X,\chi)
=
\sum_{n\ge1}\chi(n)\Lambda(n)e^{-n/X}.
```

For a reduced residue class `a mod m`, define

```math
\Psi_{\exp}(X;m,a)
=
\sum_{\substack{n\ge1 \\ n\equiv a\pmod m}}
\Lambda(n)e^{-n/X}.
```

By character orthogonality,

```math
\Psi_{\exp}(X;m,a)
=
\frac{1}{\varphi(m)}
\sum_{\chi\bmod m}
\overline{\chi(a)}\Psi_{\exp}(X,\chi),
```

for reduced `a`, subject to the conductor discipline of `HW-PRIME-CHARACTER-CONDUCTOR-001`.

## 2. Mellin transform

The Mellin transform is

```math
\widehat w_{\exp}(s)
=
\int_0^\infty e^{-t}t^{s-1}\,dt
=
\Gamma(s).
```

This is initially valid for

```math
\operatorname{Re}(s)>0.
```

The inverse Mellin representation is

```math
e^{-t}
=
\frac{1}{2\pi i}\int_{(c)}\Gamma(s)t^{-s}\,ds,
\qquad c>0.
```

## 3. Character-weighted contour form

For `Re(s)>1`, the logarithmic derivative identity is

```math
-\frac{L'}{L}(s,\chi)
=
\sum_{n=1}^{\infty}\frac{\chi(n)\Lambda(n)}{n^s}.
```

Using the exponential kernel gives the formal contour integral

```math
\Psi_{\exp}(X,\chi)
=
\frac{1}{2\pi i}\int_{(c)}
-\frac{L'}{L}(s,\chi)X^s\Gamma(s)\,ds,
\qquad c>1.
```

This is the concrete version of the scaffold from `HW-PRIME-AP-SMOOTHED-EXPLICIT-001`.

## 4. Residue slots

When the contour is shifted left, the following residue classes must be declared in any theorem-strength artifact:

| Source | Typical contribution |
|---|---|
| pole at `s=1` | main term for principal/trivial contribution |
| nontrivial zeros `rho_chi` | `-X^{rho_chi} Gamma(rho_chi)` |
| trivial zeros | gamma/completed-function dependent terms |
| poles of `Gamma(s)` | smoothing-kernel lower-order terms |
| contour tail | explicit remainder bound |

The zero contribution slot is

```math
-\sum_{\rho_\chi}X^{\rho_\chi}\Gamma(\rho_\chi).
```

This note does not assert convergence, truncation bounds, or a completed contour-shift theorem.

## 5. Smoothed explicit-formula scaffold

For a primitive character surface, the exponential-kernel scaffold is

```math
\Psi_{\exp}(X,\chi)
=
\delta_\chi X
-
\sum_{\rho_\chi}X^{\rho_\chi}\Gamma(\rho_\chi)
+
\mathcal T_{\exp}(X,\chi)
+
\mathcal R_{\exp}(X,\chi).
```

Here:

- `delta_chi` marks the pole contribution at `s=1`;
- `rho_chi` ranges over the declared nontrivial zero registry;
- `T_exp` collects trivial-zero, conductor, completed-function, and Gamma-pole terms;
- `R_exp` is the declared contour/truncation remainder.

Because

```math
\Gamma(1)=1,
```

the principal main term is normalized as `X` under this kernel.

## 6. Arithmetic-progression version

For a reduced residue class `a mod m`, substitution into the character projector gives

```math
\Psi_{\exp}(X;m,a)
=
\frac{X}{\varphi(m)}
-
\frac{1}{\varphi(m)}
\sum_{\chi\bmod m}\overline{\chi(a)}
\sum_{\rho_\chi}X^{\rho_\chi}\Gamma(\rho_\chi)
+
\text{declared lower-order and remainder terms}.
```

The formula is still a scaffold until conductor-indexed surfaces, zero registries, and remainder bounds are fully declared.

## 7. Conditional GRH envelope

If GRH is assumed for the relevant primitive Dirichlet surfaces, then

```math
\rho_\chi=\frac12+i\gamma_\chi.
```

The nontrivial-zero slot becomes

```math
X^{\rho_\chi}\Gamma(\rho_\chi)
=
X^{1/2}e^{i\gamma_\chi\log X}
\Gamma\left(\frac12+i\gamma_\chi\right).
```

This is a conditional envelope form only. It is not a proof of GRH.

## 8. Why the exponential kernel is useful

The exponential kernel has three governance advantages:

1. no sharp endpoint convention at prime powers;
2. explicit Mellin transform `Gamma(s)`;
3. direct contour-integral doorway through `-L'/L`.

Its tradeoff is that it is not compactly supported. A later compact-support kernel note may be useful for local-window experiments, but this exponential kernel is the cleanest first analytic normalization.

## 9. Heller-Winters usage rule

A future theorem-target artifact may cite this note only after declaring:

| Field | Required declaration |
|---|---|
| character | `chi` and display modulus |
| conductor | primitive conductor `f` |
| completion | exact `Lambda(s,chi)` convention |
| contour | initial line and shifted line |
| zero registry | nontrivial/trivial/pole classes |
| truncation | finite or infinite zero sum convention |
| remainder | explicit bound and dependencies |
| claim status | unconditional / conditional / diagnostic / target |

## 10. Forbidden uses

Do not cite this note to claim:

- RH or GRH is proved;
- PNT in arithmetic progressions is proved;
- the contour shift has been justified;
- endpoint issues are solved for sharp cutoffs;
- the zero sum is automatically convergent without declared convention;
- the scaffold is a theorem.

Permitted use:

```text
This note instantiates the exponential smoothing kernel w(t)=e^{-t}, with Mellin transform Gamma(s), for future smoothed AP explicit-formula artifacts.
```

## Citation form

```text
[HW-PRIME-AP-KERNEL-EXP-001 @ <merge-sha>]       # exponential smoothing kernel only
```

## Versioning

This is `HW-PRIME-AP-KERNEL-EXP-001 v0.1`. Future artifacts may add contour-shift proofs under stated hypotheses, compact-support kernels, or numerical diagnostics using the exponential smoothed sum.
