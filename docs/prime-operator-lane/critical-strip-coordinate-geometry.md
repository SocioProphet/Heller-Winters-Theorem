# Critical Strip Coordinate Geometry

Identifier: `HW-CRIT-GEOM-001`  
Status: diagnostic coordinate geometry / visualization grammar  
Lane: prime/operator lane, with HPHD explicit-formula interface  
Claim class: C0 definitions + diagnostic visualization only  
Non-claim: not RH evidence, not a proof target discharge, not a prime-circle proof transfer

## 0. Claim boundary

This note records a coordinate dictionary for comparing four surfaces already present in the Heller-Winters Programme:

1. the logarithmic prime line;
2. the prime-circle / primorial-wheel construction;
3. the explicit-formula zero spectrum;
4. circular, projective, and hyperbolic encodings of the critical strip.

The note does not prove the Riemann Hypothesis, does not provide evidence for the Riemann Hypothesis, and does not promote any visual alignment into theorem status.

The central invariant carried through this note is the real coordinate

```math
\sigma = \operatorname{Re}(\rho)
```

of a nontrivial zeta zero

```math
\rho = \sigma + i\gamma.
```

The RH-critical value is

```math
\sigma = \frac12.
```

Everything below is a coordinate encoding of that scalar or of the critical strip symmetry around that scalar.

## 1. Prime-circle arithmetic is separate from critical-line geometry

`HW-PRIME-CIRCLE-001` identifies the seed prime-circle construction as a primorial-wheel / reduced-residue-system object.

The prime-circle construction places an integer `P` at angular position

```text
theta(P) = P mod 360.
```

For primes `p > 5`, the visible recurring structure is explained by the reduced residue classes modulo `30`:

```text
1, 7, 11, 13, 17, 19, 23, 29 mod 30.
```

That is arithmetic wheel structure. It is not the same object as the zero-side critical-line coordinate

```math
\operatorname{Re}(\rho)=\frac12.
```

Therefore the repository must distinguish:

| Object | Coordinate | Meaning |
|---|---|---|
| prime circle | `P mod 360` | finite residue/wheel arithmetic |
| critical-line circle overlay | `sigma = cos(theta)` | visual encoding of the zero-side real exponent |

Forbidden transfer:

```text
P mod 360  !=  sigma = cos(theta).
```

The two may appear in a shared figure only as typed overlays.

## 2. Explicit-formula exponent decomposition

The explicit formula connects prime-side residuals to zero-side spectral data. Schematically, for the Chebyshev function,

```math
\psi(x)
=
 x
-\sum_{\rho}\frac{x^{\rho}}{\rho}
-\log(2\pi)
-\frac12\log(1-x^{-2}).
```

Let

```math
u = \log x.
```

Then each zero contribution has exponent decomposition

```math
x^{\rho}
= e^{\rho u}
= e^{\sigma u} e^{i\gamma u}.
```

The factor `e^(sigma u)` is the envelope scale. The factor `e^(i gamma u)` is the log-phase oscillation.

If RH holds, then

```math
\rho = \frac12 + i\gamma,
```

so

```math
x^{\rho} = x^{1/2} e^{i\gamma\log x}.
```

This is the analytic bridge from the log-line coordinate to the RH-shaped phase/envelope visualization.

## 3. Critical scalar: uncentered circular encoding

The scalar

```math
\sigma = \frac12
```

has the unit-circle projection encoding

```math
\sigma = \cos\theta.
```

At the RH-critical value,

```math
\frac12 = \cos\left(\frac{\pi}{3}\right),
```

so

```math
\theta = \frac{\pi}{3} = 60^{\circ}.
```

This is the permitted meaning of the `60 degree` marker:

```text
The RH-critical real exponent has a 60-degree unit-circle projection under the convention sigma = cos(theta).
```

It is not the polar angle of a zero.

For a zero

```math
\rho = \sigma + i\gamma,
```

the Euclidean argument from the origin is

```math
\arg(\rho)=\arctan(\gamma/\sigma),
```

which is not fixed at `60 degrees` and varies with `gamma`.

## 4. Centered strip coordinate

For projective and hyperbolic geometry, the more natural coordinate is the centered strip coordinate

```math
\tau = 2\sigma - 1.
```

The critical strip boundaries become

```math
\sigma=0 \Rightarrow \tau=-1,
```

and

```math
\sigma=1 \Rightarrow \tau=1.
```

The critical line becomes the neutral axis

```math
\sigma=\frac12 \Rightarrow \tau=0.
```

This coordinate is usually better for projective and hyperbolic interpretation because it makes the strip symmetry explicit.

## 5. Centered circular encoding

Using the centered coordinate, one may encode

```math
\tau = \cos\theta.
```

At the critical line,

```math
\tau=0,
```

so

```math
\theta=\frac{\pi}{2}=90^{\circ}.
```

Thus the note records two different circular grammars:

| Grammar | Formula | Critical marker | Use |
|---|---|---|---|
| uncentered | `sigma = cos(theta)` | `60 degrees` | emphasizes the scalar `1/2` |
| centered | `tau = cos(theta)` | `90 degrees` | emphasizes the strip's neutral axis |

These are both valid coordinate conventions, but they answer different visualization needs.

## 6. Projective strip symmetry

The critical strip has boundary pair `0` and `1`. The critical line is the midpoint/equal-distance locus between them.

For

```math
s = \frac12 + it,
```

we have

```math
|s| = |1-s|.
```

Equivalently, the critical line is the fixed axis of the involution

```math
s \mapsto 1-\overline{s}.
```

Indeed,

```math
s=1-\overline{s}
\quad\Longleftrightarrow\quad
\operatorname{Re}(s)=\frac12.
```

This fixed-axis statement is more intrinsic than the `60 degree` visual marker. The `60 degree` marker is a projection convention for the scalar `1/2`; the fixed-axis relation is the projective / strip-symmetry geometry.

## 7. Hyperbolic encodings

Two hyperbolic lifts are useful, but they should not be confused.

### 7.1 Uncentered rapidity

If we encode

```math
\sigma = \tanh\eta,
```

then the RH-critical value gives

```math
\eta = \operatorname{artanh}\left(\frac12\right)
     = \frac12\log 3.
```

This is a valid scalar transform of `1/2`.

### 7.2 Centered rapidity

If instead we encode the centered coordinate

```math
\tau = \tanh\eta,
```

then RH gives

```math
\tau=0
\quad\Rightarrow\quad
\eta=0.
```

This is the preferred hyperbolic geometry for the critical strip because the critical line becomes the neutral rapidity axis.

## 8. Complex cosh continuation

The circular identity

```math
\cos\left(\frac{\pi}{3}\right)=\frac12
```

also has a complex hyperbolic continuation:

```math
\operatorname{arccosh}\left(\frac12\right)= i\frac{\pi}{3}
```

up to branch choice.

This is a branch-sensitive complex identity, not a real hyperbolic length. Use it only when the branch convention is declared.

## 9. Figure grammar

A safe four-panel figure should distinguish the layers.

| Panel | Surface | Map | Label |
|---|---|---|---|
| 1 | log line | `p -> log p` | prime events on multiplicative scale |
| 2 | prime wheel | `p -> p mod 360` | reduced-residue / primorial-wheel structure |
| 3 | critical exponent circle | `sigma = cos(theta)` | `sigma=1/2 -> theta=60 degrees`; not zero argument |
| 4 | centered strip / hyperbolic lift | `tau=2sigma-1`, `tau=tanh(eta)` | critical line as neutral projective/hyperbolic axis |

The intended visual comparison is typed alignment, not proof transfer.

## 10. Forbidden interpretations

The following statements are forbidden:

- primes are at `60 degrees`;
- `P mod 360` equals `sigma = cos(theta)`;
- the prime-circle wheel proves or supports RH;
- `cos(60 degrees)` locates zeta zeros;
- the polar angle of every nontrivial zero is `60 degrees`;
- the hyperbolic lift proves critical-line stability;
- finite residue-wheel structure is evidence for the `psi(x)` RH envelope;
- this coordinate dictionary discharges `HW-THM-001`.

Permitted statement:

```text
The scalar sigma = 1/2 admits circular, centered, projective, and hyperbolic coordinate encodings useful for visualizing the RH-shaped explicit-formula envelope, while prime-circle arithmetic remains a separate wheel/residue object.
```

## 11. Relationship to existing artifacts

This note should be read together with:

- `docs/prime-operator-lane/HW-PRIME-CIRCLE-001-primorial-wheel-correspondence.md` — arithmetic wheel object;
- `docs/theorem-statements/HW-THM-001-rh-envelope-target.md` — theorem target and RH-equivalent envelope boundary;
- `lanes/hphd/04-explicit-formula-typing-gate.md` — explicit-formula decomposition and metaphor typing;
- `docs/proof-governance/auxiliary-model-policy.md` — bridge discipline for auxiliary models;
- `docs/proof-hazards/auxiliary-intersection-fallacy.md` — protection against intersection-to-equivalence promotion.

## Citation form

```text
[HW-CRIT-GEOM-001 @ <merge-sha>]       # diagnostic coordinate geometry only
```

## Versioning

This is `HW-CRIT-GEOM-001 v0.1`. Future work may add rendered figures, branch-aware complex hyperbolic diagrams, or a machine-readable coordinate table. Any theorem-strength use requires a separate theorem-target or proof artifact.
