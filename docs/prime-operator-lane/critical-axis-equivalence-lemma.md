# Critical Axis Equivalence Lemma

Identifier: `HW-CRIT-GEOM-LEMMA-001`  
Status: elementary coordinate lemma / diagnostic support  
Lane: prime/operator lane, with HPHD explicit-formula interface  
Claim class: C0/C3 elementary background  
Depends on: `HW-CRIT-GEOM-001`  
Non-claim: does not assert that any zeta zero lies on the critical axis

## 0. Claim boundary

This note proves an elementary coordinate equivalence for an arbitrary complex number

```math
s = \sigma + it.
```

It does not prove the Riemann Hypothesis. It does not prove that any nontrivial zeta zero satisfies the equivalent conditions below. It only records that several coordinate descriptions name the same axis:

```math
\operatorname{Re}(s)=\frac12.
```

The hard theorem target remains the implication

```math
\zeta(\rho)=0 \quad\Longrightarrow\quad \operatorname{Re}(\rho)=\frac12.
```

This lemma describes the right-hand side of that implication, not the implication itself.

## 1. Definitions

Let

```math
s = \sigma + it,
```

where

```math
\sigma,t\in\mathbb R.
```

Define the centered strip coordinate

```math
\tau = 2\sigma - 1.
```

The critical axis is the vertical line

```math
\operatorname{Re}(s)=\frac12.
```

## 2. Lemma

For any complex number `s = sigma + it`, the following conditions are equivalent:

1. `Re(s) = 1/2`.
2. `tau = 0`, where `tau = 2sigma - 1`.
3. `s = 1 - conjugate(s)`.
4. `|s| = |1 - s|`.

Additionally, under chosen coordinate conventions, the same axis is encoded by:

5. `sigma = cos(pi/3)` under the uncentered projection convention `sigma = cos(theta)`.
6. `tau = cos(pi/2)` under the centered projection convention `tau = cos(theta)`.
7. `eta = 0` under the centered hyperbolic convention `tau = tanh(eta)` for real `eta`.

The first four equivalences are intrinsic to the critical strip. The final three are coordinate encodings and must retain their declared conventions.

## 3. Proof: centered coordinate

By definition,

```math
\tau = 2\sigma - 1.
```

Therefore

```math
\tau = 0
\quad\Longleftrightarrow\quad
2\sigma - 1 = 0
\quad\Longleftrightarrow\quad
\sigma = \frac12.
```

Since

```math
\sigma = \operatorname{Re}(s),
```

we have

```math
\tau = 0
\quad\Longleftrightarrow\quad
\operatorname{Re}(s)=\frac12.
```

## 4. Proof: fixed-axis involution

Compute the conjugate:

```math
\overline{s}=\sigma-it.
```

Then

```math
1-\overline{s}=1-\sigma+it.
```

The equation

```math
s=1-\overline{s}
```

becomes

```math
\sigma+it = 1-\sigma+it.
```

Canceling the imaginary part gives

```math
\sigma = 1-\sigma,
```

hence

```math
2\sigma=1,
```

and therefore

```math
\sigma=\frac12.
```

Conversely, if `sigma = 1/2`, then

```math
s=\frac12+it
```

and

```math
1-\overline{s}
=1-\left(\frac12-it\right)
=\frac12+it
=s.
```

Thus

```math
s=1-\overline{s}
\quad\Longleftrightarrow\quad
\operatorname{Re}(s)=\frac12.
```

## 5. Proof: equal-distance locus

Compute

```math
|s|^2 = \sigma^2 + t^2.
```

Also,

```math
1-s = 1-\sigma-it,
```

so

```math
|1-s|^2 = (1-\sigma)^2 + t^2.
```

Thus

```math
|s| = |1-s|
```

is equivalent to

```math
\sigma^2+t^2 = (1-\sigma)^2+t^2.
```

Cancel `t^2`:

```math
\sigma^2=(1-\sigma)^2.
```

Expand the right-hand side:

```math
\sigma^2=1-2\sigma+\sigma^2.
```

Cancel `sigma^2`:

```math
0=1-2\sigma.
```

Therefore

```math
\sigma=\frac12.
```

Conversely, if `sigma = 1/2`, then

```math
|s|^2 = \left(\frac12\right)^2+t^2
```

and

```math
|1-s|^2 = \left(\frac12\right)^2+t^2,
```

so

```math
|s|=|1-s|.
```

Therefore

```math
|s|=|1-s|
\quad\Longleftrightarrow\quad
\operatorname{Re}(s)=\frac12.
```

## 6. Coordinate encodings

### 6.1 Uncentered circular encoding

Under the declared convention

```math
\sigma = \cos\theta,
```

the critical value is

```math
\sigma=\frac12=\cos\left(\frac{\pi}{3}\right).
```

So the marker is

```math
\theta=\frac{\pi}{3}=60^\circ.
```

This is a projection encoding of the real coordinate. It is not the polar angle of `s`.

### 6.2 Centered circular encoding

Under the declared convention

```math
\tau = \cos\theta,
```

the critical axis has

```math
\tau=0=\cos\left(\frac{\pi}{2}\right).
```

So the marker is

```math
\theta=\frac{\pi}{2}=90^\circ.
```

This encoding emphasizes the neutral midpoint of the strip.

### 6.3 Centered hyperbolic encoding

Under the declared convention

```math
\tau = \tanh\eta,
```

with real `eta`, the critical axis has

```math
\tau=0.
```

Since

```math
\tanh\eta=0
\quad\Longleftrightarrow\quad
\eta=0
```

for real `eta`, the centered hyperbolic marker is

```math
\eta=0.
```

This is the preferred hyperbolic coordinate for the critical strip because the critical axis becomes the neutral rapidity axis.

## 7. Consolidated equivalence chain

For arbitrary `s = sigma + it`, the intrinsic coordinate chain is:

```math
\operatorname{Re}(s)=\frac12
\quad\Longleftrightarrow\quad
\tau=0
\quad\Longleftrightarrow\quad
s=1-\overline{s}
\quad\Longleftrightarrow\quad
|s|=|1-s|.
```

Under declared visualization conventions, this same axis is encoded as:

```math
\sigma=\cos\left(\frac\pi3\right),
\qquad
\tau=\cos\left(\frac\pi2\right),
\qquad
\tau=\tanh(0).
```

## 8. Relationship to RH-shaped claims

If `rho` is a nontrivial zero of `zeta(s)`, the Riemann Hypothesis asserts

```math
\operatorname{Re}(\rho)=\frac12.
```

By this lemma, that target line can equivalently be described as

```math
\rho = 1-\overline{\rho},
```

or

```math
|\rho| = |1-\rho|,
```

or

```math
\tau(\rho)=0.
```

But this lemma does not prove that any nontrivial zero satisfies those conditions. It only proves the equivalence between coordinate descriptions after the axis is selected.

## 9. Forbidden uses

Do not cite this lemma to claim:

- RH is proved;
- any zeta zero has been located;
- the prime-circle construction supports RH;
- the `60 degree` projection is the polar angle of a zero;
- hyperbolic neutrality proves critical-line stability.

Permitted use:

```text
This lemma supplies the elementary coordinate equivalence behind the critical-axis visualization used by HW-CRIT-GEOM-001.
```

## Citation form

```text
[HW-CRIT-GEOM-LEMMA-001 @ <merge-sha>]       # elementary coordinate equivalence only
```

## Versioning

This is `HW-CRIT-GEOM-LEMMA-001 v0.1`. A future hyperbolic-model note may choose and verify a specific strip-to-disk or strip-to-half-plane conformal map. That future map is not selected here.
