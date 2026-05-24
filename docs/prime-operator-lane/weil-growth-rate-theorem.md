# HW-PRIME-WEIL-002 — Weil Growth-Rate Characterization

Identifier: `HW-PRIME-WEIL-002`  
Status: growth-rate characterization surface  
Claim class: conditional / equivalence framing against the explicit formula  
Mathematical content added by this document: an explicitly computable Richter-window growth-rate reformulation of the GRH-strength boundary

This document records the growth-rate formulation exposed by `HW-PRIME-WEIL-001`.

It is not a proof of RH or GRH. It is a precise finite-arithmetic reformulation: off-critical zeros should appear as exponential growth in the explicitly computable Richter-window squared sums, while GRH-scale behavior corresponds to polynomial growth in the window depth.

## 1. Richter-window sums

For decimal depth `k`, define

```text
W_k = [10^(k-1), 10^k).
```

For a Dirichlet character `chi` represented at a finite modulus surface, define

```text
psi_{W_k}(chi)
  = sum_{p in W_k, p mod P in G_P} (log p) chi(p).
```

The finite positive Richter contribution is

```text
R_k^pos(chi)
  = |psi_{W_k}(chi)|^2 / (10^k k^2).
```

The truncated Richter positive distribution is

```text
W_K^pos(chi) = sum_{k <= K} R_k^pos(chi).
```

Each finite contribution is non-negative by construction.

## 2. Growth-rate detector

The explicit formula relates character sums to zeros of the associated `L`-function:

```text
psi(x,chi) = - sum_rho x^rho/rho + lower-order and trivial terms.
```

Windowing gives

```text
psi_{W_k}(chi)
  = psi(10^k,chi) - psi(10^(k-1),chi).
```

If all zeros satisfy `Re(rho)=1/2`, then the expected GRH-scale bound is

```text
|psi_{W_k}(chi)| = O(10^(k/2) poly(k)).
```

Consequently

```text
R_k^pos(chi) = O(poly(k)).
```

If a zero occurs at `rho = 1/2 + delta + i gamma`, with `delta > 0`, the corresponding explicit-formula term contributes at scale

```text
10^(k(1/2+delta)).
```

After the Richter normalization,

```text
R_k^pos(chi) = Omega(10^(2 delta k) / k^2)
```

along windows where the off-line zero contribution is not cancelled by other terms. Thus an off-critical zero creates exponential-in-`k` growth in the positive Richter contribution.

## 3. Characterization statement

Growth-rate characterization target:

```text
GRH for L(s,chi)
  <=>
R_k^pos(chi) grows at most polynomially in k
```

for every relevant character, with the usual interpretation that the proof passes through the explicit formula and standard zero-cancellation controls.

The forward implication is the GRH estimate for `psi(x,chi)` rewritten in Richter-window form.

The reverse implication is the contrapositive: if any zero satisfies `Re(rho)>1/2`, the explicit formula supplies an exponentially growing contribution `10^(delta k)` to the window sum, yielding `R_k^pos(chi)=Omega(10^(2 delta k)/k^2)` on an infinite set of windows unless exactly cancelled by a matching off-line configuration. The cancellation analysis is part of the analytic-number-theory proof obligation and is not hidden by the finite computation.

This is a characterization surface, not a proof that the polynomial bound holds.

## 4. Hyperbolic cancellation and wave-front theorem surface

Write an off-line zero as

```text
rho = 1/2 + delta + i gamma.
```

Then

```text
x^rho = x^(1/2) x^delta exp(i gamma log x).
```

Using

```text
x^delta = cosh(delta log x) + sinh(delta log x),
```

the contribution decomposes into an even hyperbolic envelope and an odd hyperbolic envelope.

On the critical line, `delta=0`, and therefore

```text
sinh(0)=0,
cosh(0)=1,
cosh(0)^2 - sinh(0)^2 = 1.
```

Thus the odd envelope vanishes exactly. The zero-pair contribution is a pure oscillation at the `x^(1/2)` envelope scale:

```text
Delta_rho(x) = x^rho/rho + x^conjugate(rho)/conjugate(rho)
             = 2 x^(1/2) cos(gamma log x - arg(rho)) / |rho|.
```

Off the critical line, `delta>0`, both `cosh(delta log x)` and `sinh(delta log x)` grow at scale `x^delta`. The identity

```text
cosh(u)^2 - sinh(u)^2 = 1
```

still holds, but the individual envelopes are large. This is the algebraic certificate of broken cancellation: the difference remains fixed while the sum of envelopes grows.

The Richter-normalized off-line envelope has asymptotic scale

```text
4 cosh(delta k log 10)^2 / k^2 ~ 10^(2 delta k) / k^2.
```

This records the algebraic mechanism. It does not by itself prove that every possible off-line zero configuration escapes cancellation in the linear character sum.

## 5. Tanh as Richter deviation meter

The ratio

```text
tanh(delta log x) = sinh(delta log x) / cosh(delta log x)
                  = (x^delta - x^(-delta)) / (x^delta + x^(-delta))
```

is a deviation meter for the odd envelope.

At `delta=0`, `tanh(0)=0`: the odd envelope is absent. For fixed `delta>0`, `tanh(delta log x) -> 1` as `x -> infinity`: the odd and even hyperbolic envelopes become comparable, and the off-line growth becomes visible.

Diagnostic values for `u=delta k log 10`:

| `delta` | `k=2` | `k=3` | `k=5` | `k=10` |
| ---: | ---: | ---: | ---: | ---: |
| `0` | `0` | `0` | `0` | `0` |
| `0.05` | `0.226` | `0.332` | `0.520` | `0.818` |
| `0.10` | `0.430` | `0.598` | `0.818` | `0.980` |
| `0.20` | `0.726` | `0.881` | `0.980` | `0.9998` |

The related envelope-excess quantity

```text
cosh(delta k log 10)^2 - 1
```

is exactly zero at `delta=0` and grows rapidly for `delta>0`.

## 6. Theta functional equation source

The Jacobi theta function

```text
theta_3(q) = sum_{n in Z} q^(n^2)
```

splits into even and odd square streams. Its functional equation

```text
theta_3(exp(-pi t)) = t^(-1/2) theta_3(exp(-pi/t))
```

has self-dual point `t=1`. Under Mellin transform, this self-duality is the source of the zeta functional equation

```text
xi(s) = xi(1-s),
```

whose fixed line is `Re(s)=1/2`.

This is the analytic source of the repeated half-step appearing in the Richter geometric center `10^(k-1/2)`, the tangent pole shift `pi(k+1/2)`, and the critical-line coordinate. The shared half-step is a structural diagnostic; it is not a standalone zero-location proof.

## 7. Parseval bias opening

For a finite modulus group `G_P`, define the residue-window weights

```text
f_k(g) = sum_{p in W_k, p mod P = g} log p.
```

Finite Parseval gives

```text
(1/|G_P|) sum_chi |psi_{W_k}(chi)|^2 = sum_g f_k(g)^2.
```

The trivial character records the total mass. The non-trivial characters record the excess second moment: the amount by which the window distribution across residue classes deviates from perfect equidistribution.

This is the promising cancellation-avoidance surface. Linear character sums can hide phase cancellation. The Parseval second moment is a sum of absolute squares, so it is intrinsically non-negative. An off-line zero, if it forces a persistent bias in one or more residue classes, should appear as growth in this real second-moment excess.

Target estimate:

```text
if L(s,chi) has a zero at 1/2 + delta + i gamma with delta>0,
then sum_g f_k(g)^2 has an Omega(10^((1+2 delta)k)/k^2) excess component
```

in the corresponding windows, after subtracting the trivial-character baseline and controlling lower-order terms.

This is not proved here. The missing proof obligation is the explicit-formula estimate that transfers off-line zero growth into the Parseval-bias excess without allowing cancellation across the character family.

## 8. Fake-zero diagnostic

For a hypothetical off-line zero

```text
rho = 1/2 + delta + i gamma,
```

one can model the magnitude of its window contribution by

```text
Z_k(rho)
  = |10^(k rho) - 10^((k-1) rho)|^2 / (|rho|^2 10^k k^2).
```

If `delta=0`, this contribution is polynomially bounded in `k` after normalization. If `delta>0`, then

```text
Z_k(rho) ~ 10^(2 delta k)/k^2
```

up to oscillatory factors.

This fake-zero diagnostic is not evidence for the existence of an off-line zero. It is a falsifiability harness for the framework: a correct Richter-window model must distinguish GRH-scale behavior from off-line exponential growth.

## 9. Numerical evidence boundary

At the current measured scales for the `P=210` family, the normalized Richter ratios are small and decreasing for the tested character `chi_(1,1,1)`:

```text
k=2: |psi_{W_2}| / (2 sqrt(10^2)) ~= 1.44
k=3: |psi_{W_3}| / (3 sqrt(10^3)) ~= 0.80
```

The corresponding individual normalized squared terms decrease:

```text
k=2: ~= 2.06
k=3: ~= 0.64
```

This is finite evidence consistent with GRH-scale behavior. It is not a proof and it does not establish the asymptotic polynomial bound.

## 10. Relation to `HW-OPEN-001`

`HW-OPEN-001` originally framed the central gap as a Hilbert-Polya finite extension. `HW-PRIME-WEIL-002` records a second route: a growth-rate characterization of the same hard spectral boundary using explicitly computable prime-window sums.

The new route does not shorten the hard problem. It localizes it:

```text
prove polynomial Richter growth
  <=>
control off-critical zero contributions
  <=>
GRH-strength statement.
```

The value of this formulation is operational: it is computable from primes, window-local, and CI-testable at finite depth.

## 11. Non-claims

This document does not prove RH or GRH.

This document does not prove the polynomial growth bound.

This document does not prove the Parseval-bias lower bound for off-line zeros.

This document does not prove that finite positivity propagates to the full Weil distribution.

This document does not construct a Hilbert-Pólya operator.

This document does not use zeros as input to the finite prime-window computation. The fake-zero diagnostic is a separate falsifiability model.

This document does not assert that finite numerical evidence establishes any asymptotic theorem.
