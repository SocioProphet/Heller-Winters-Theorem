# Critical Strip Hyperbolic Disk Model

Identifier: `HW-CRIT-GEOM-HYP-001`  
Status: diagnostic conformal model / visualization support  
Lane: prime/operator lane, with HPHD explicit-formula interface  
Claim class: C0/C3 conformal-coordinate background  
Depends on: `HW-CRIT-GEOM-001`, `HW-CRIT-GEOM-LEMMA-001`  
Non-claim: does not prove RH, does not locate zeta zeros, and does not make a spectral theorem claim

## 0. Claim boundary

This note selects a concrete conformal map from the centered critical strip to the unit disk. It is a visualization and coordinate-normalization layer.

It does not assert that any nontrivial zero lies on the critical line. It only describes how the critical strip and its central axis are represented once the strip coordinate is chosen.

The unsolved theorem target remains

```math
\zeta(\rho)=0 \quad\Longrightarrow\quad \operatorname{Re}(\rho)=\frac12.
```

This note describes the geometry of the target axis, not a proof that zeros lie on it.

## 1. Starting strip

Let

```math
s=\sigma+it.
```

The critical strip is

```math
0<\operatorname{Re}(s)<1.
```

Define the centered strip coordinate

```math
z = 2s-1.
```

Then

```math
s=\frac{z+1}{2}.
```

The critical strip becomes

```math
-1<\operatorname{Re}(z)<1.
```

The critical line becomes

```math
\operatorname{Re}(s)=\frac12
\quad\Longleftrightarrow\quad
\operatorname{Re}(z)=0.
```

Thus the critical line is the central axis of the centered strip.

## 2. Strip to right half-plane

Define

```math
q(z)=\exp\left(\frac{i\pi z}{2}\right).
```

Write

```math
z=x+iy.
```

Then

```math
q(z)=\exp\left(\frac{i\pi x}{2}-\frac{\pi y}{2}\right).
```

Therefore

```math
\arg q(z)=\frac{\pi x}{2}.
```

For the centered strip

```math
-1<x<1,
```

we have

```math
-\frac{\pi}{2}<\arg q(z)<\frac{\pi}{2}.
```

So

```math
\operatorname{Re}(q(z))>0.
```

Thus `q` maps the centered vertical strip conformally into the right half-plane.

Boundary behavior:

```math
\operatorname{Re}(z)=1 \quad\mapsto\quad \arg q=\frac\pi2,
```

and

```math
\operatorname{Re}(z)=-1 \quad\mapsto\quad \arg q=-\frac\pi2.
```

Both strip boundaries map to the boundary of the right half-plane.

## 3. Right half-plane to unit disk

Use the Cayley transform

```math
C(q)=\frac{1-q}{1+q}.
```

For `Re(q)>0`, this maps the right half-plane to the unit disk.

The composed map is

```math
W(z)=C(q(z))
     =\frac{1-\exp(i\pi z/2)}{1+\exp(i\pi z/2)}.
```

Equivalently,

```math
W(z)=-\tanh\left(\frac{i\pi z}{4}\right)
     =-i\tan\left(\frac{\pi z}{4}\right).
```

The sign convention is chosen so that positive height on the critical line maps to positive real disk coordinate.

## 4. Critical axis image

On the critical line in `s`-coordinates,

```math
s=\frac12+it.
```

Then

```math
z=2s-1=2it.
```

Apply the map:

```math
q(2it)=\exp\left(\frac{i\pi(2it)}{2}\right)=\exp(-\pi t).
```

So

```math
W(2it)=\frac{1-e^{-\pi t}}{1+e^{-\pi t}}.
```

This simplifies to

```math
W(2it)=\tanh\left(\frac{\pi t}{2}\right).
```

Therefore the critical axis maps to the real diameter of the unit disk:

```math
\operatorname{Re}(s)=\frac12
\quad\mapsto\quad
W\in(-1,1)\subset\mathbb R.
```

The imaginary height `t` becomes the bounded disk coordinate

```math
r(t)=\tanh\left(\frac{\pi t}{2}\right).
```

This is the exact centered hyperbolic compression of the critical-line height.

## 5. Boundary and midpoint behavior

The strip center

```math
s=\frac12
```

has

```math
z=0.
```

Then

```math
W(0)=\frac{1-1}{1+1}=0.
```

So the midpoint of the strip maps to the disk origin.

As `t -> +infinity` on the critical line,

```math
W(2it)=\tanh\left(\frac{\pi t}{2}\right)\to 1.
```

As `t -> -infinity`,

```math
W(2it)\to -1.
```

Thus the infinite critical axis is compactified to the open real diameter from `-1` to `1`.

The strip boundaries `Re(z)=+1` and `Re(z)=-1` map to the unit circle boundary. They represent the critical-strip boundary lines `Re(s)=1` and `Re(s)=0` respectively.

## 6. Relation to centered rapidity

The earlier centered rapidity convention was

```math
\tau=\tanh\eta,
```

where

```math
\tau=2\sigma-1.
```

This disk model uses a different hyperbolic coordinate for height along the central axis:

```math
r(t)=\tanh\left(\frac{\pi t}{2}\right).
```

These should not be confused:

| Coordinate | Formula | Meaning |
|---|---|---|
| centered width coordinate | `tau = 2sigma - 1` | horizontal position across the strip |
| centered width rapidity | `tau = tanh(eta)` | hyperbolic encoding of horizontal displacement |
| critical-axis disk coordinate | `r(t)=tanh(pi t/2)` | compactified vertical height along the critical line |

At the critical line,

```math
\tau=0.
```

Along the critical line, height is encoded by

```math
r(t)=\tanh\left(\frac{\pi t}{2}\right).
```

So the axis condition and the height parameter are distinct.

## 7. Relation to the `60 degree` marker

The `60 degree` marker belongs to the uncentered scalar projection

```math
\sigma=\cos\theta.
```

At the critical axis,

```math
\sigma=\frac12=\cos\left(\frac\pi3\right).
```

The disk model instead centers the strip first:

```math
z=2s-1.
```

Then the critical axis is

```math
\operatorname{Re}(z)=0.
```

Thus:

- `60 degrees` emphasizes the scalar `sigma=1/2`;
- the disk model emphasizes the centered axis `tau=0`;
- the disk coordinate `r(t)=tanh(pi t/2)` emphasizes height along the axis.

These are compatible coordinate views, not interchangeable claims.

## 8. Safe figure use

A safe hyperbolic figure may show:

1. the centered strip `-1<Re(z)<1`;
2. the central axis `Re(z)=0`;
3. the map `W(z)=(1-exp(i*pi*z/2))/(1+exp(i*pi*z/2))`;
4. the unit disk;
5. the critical axis image as the real diameter;
6. the height compression `t -> tanh(pi*t/2)`.

The figure must not show actual zeta zeros as lying on the axis unless the figure is explicitly conditional on RH or uses verified finite zero data with a separate citation and scope boundary.

## 9. Forbidden uses

Do not cite this note to claim:

- RH is proved;
- zeros are located by a conformal map;
- the prime-circle wheel implies critical-line structure;
- the `60 degree` marker is a hyperbolic proof;
- disk-center symmetry forces zeta zeros onto the axis;
- finite plots of zeros establish the theorem target.

Permitted use:

```text
This note supplies the conformal coordinate model used to draw the centered critical strip and its neutral axis in the unit disk.
```

## 10. Relationship to existing artifacts

This note extends:

- `HW-CRIT-GEOM-001` — diagnostic critical-strip coordinate dictionary;
- `HW-CRIT-GEOM-LEMMA-001` — elementary equivalence of the critical-axis descriptions;
- `HW-THM-001` — RH-equivalent prime-residual envelope target, not discharged here.

## Citation form

```text
[HW-CRIT-GEOM-HYP-001 @ <merge-sha>]       # conformal disk model only
```

## Versioning

This is `HW-CRIT-GEOM-HYP-001 v0.1`. Future revisions may add a rendered figure, numerical grid checks, or an alternate half-plane convention. Any use involving actual zeta-zero data must declare whether it is conditional, finite verification, or theorem-target exposition.
