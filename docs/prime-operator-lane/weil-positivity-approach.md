# HW-PRIME-WEIL-001 — Finite Weil Positivity Approach

Identifier: `HW-PRIME-WEIL-001`  
Status: finite positivity / growth-rate diagnostic / conditional-limit approach  
Claim class: diagnostic theorem surface plus open convergence boundary  
Mathematical content added by this document: finite positivity theorem, growth-rate diagnostic, and conditional convergence framing only

This document records the non-circular positivity route exposed by the prime-operator lane.

The direct Hilbert-Pólya route is blocked by a familiar circularity: proving essential self-adjointness of the limit operator requires tail control strong enough to encode the spectral statement being sought. The finite Weil-positivity route avoids that direct circularity by proving positivity at each finite primorial level first, then isolating the separate open problems of growth-rate control and positivity propagation to the limiting Weil distribution.

## 1. Gaussian-smoothed finite operator

For a character `chi`, define the prime-weighted raw character sum

```text
psi(B,chi) = sum_{p <= B} (log p) chi(p).
```

The raw sums do not converge directly to `-L'/L(0,chi)`. They oscillate with growing amplitude.

To move from raw cutoff sums to Weil-compatible test functions, define the Gaussian-smoothed finite eigenvalue

```text
lambda_chi^(sigma)(B)
  = sum_{p <= B} (log p) chi(p) exp(-(log p)^2/(2 sigma^2)).
```

For large `sigma`, this approaches the raw finite sum. For finite `sigma`, it suppresses the hard cutoff and places the computation inside the explicit-formula test-function regime.

## 2. Finite Weil distribution

For a primorial level `P_k`, let

```text
G_k = (Z/P_k Z)^x,
H_k = C[G_k].
```

The finite Haar inner product is

```text
<f,g>_k = (1/|G_k|) sum_{x in G_k} f(x) conjugate(g(x)).
```

The character basis `G_k^` is orthonormal for this inner product.

The Gaussian-smoothed positive finite Weil distribution is

```text
W_{k,sigma}^pos(h)
  = (1/|G_k|) sum_{chi in G_k^} |h_hat(chi)|^2 |lambda_chi^(sigma)(P_k)|^2.
```

Equivalently, the positive kernel is the autocorrelation / squared-spectrum kernel. Its Fourier transform is `|lambda_chi^(sigma)(P_k)|^2`, hence non-negative for every character.

## 3. Finite positivity theorem

Finite theorem: for every `h in H_k`,

```text
W_{k,sigma}^pos(h) >= 0.
```

Proof: each summand in

```text
(1/|G_k|) sum_chi |h_hat(chi)|^2 |lambda_chi^(sigma)|^2
```

is non-negative. Thus the sum is non-negative. Equality holds precisely on the kernel of the squared finite operator, i.e. on the subspace whose character coefficients vanish wherever `lambda_chi^(sigma) != 0`.

This theorem is finite and non-circular. It does not assume RH, GRH, essential self-adjointness, or any limiting spectral theorem.

## 4. GRH signature and growth exponent

The explicit formula gives the schematic relation

```text
psi(B,chi) = - sum_rho B^rho/rho + lower-order and trivial terms,
```

where `rho` ranges over nontrivial zeros of the corresponding `L`-function.

Thus the growth exponent

```text
alpha(chi) = limsup_{B -> infinity} log |psi(B,chi)| / log B
```

is the spectral diagnostic. Under GRH for `L(s,chi)`, one expects

```text
|psi(B,chi)| = O(B^(1/2) log^2 B),
```

so `alpha(chi) <= 1/2`. If a zero has real part `beta > 1/2`, the explicit formula permits growth at exponent at least `beta`.

The corrected attack is therefore not raw eigenvalue convergence. It is growth-rate control of the cutoff sums.

## 5. Three theorem statements

Theorem 1, finite Weil positivity, proved at finite level:

```text
W_{k,sigma}^pos(h) >= 0
```

for all finite `k`, all `sigma > 0`, and all `h in H_k`.

Theorem 2, GRH signature, numerical / conditional:

```text
|psi(B,chi)| / sqrt(B) < log(B)^2
```

is the finite-scale GRH-signature test. It is consistent with GRH but does not prove GRH.

Theorem 3, conditional RH / GRH target:

If

(A) for all finite-level characters, the growth exponent `alpha(chi)` remains `<= 1/2` uniformly in the profinite inductive limit, and

(B) the Gaussian-smoothed finite Weil distributions `W_{k,sigma}^pos` converge weakly to the full Weil distribution as `k -> infinity` and the smoothing parameter is removed in the declared test-function topology,

then the Weil positivity criterion holds for the relevant test-function class, and the corresponding RH / GRH statement follows for the associated `L`-function family.

This third theorem is a target statement, not a theorem currently proved in this repository.

## 6. Numerical evidence at the `P_4=210` character family

For the 48-character family of `(Z/210Z)^x`, the Gaussian-smoothed finite Weil distribution is strictly positive in the tested windows:

| `B` | `W_{sigma}^pos(1)` | `min_chi |lambda_chi^(sigma)(B)|` |
| ---: | ---: | ---: |
| 200 | `53.5` | `0.339` |
| 500 | `313.7` | `0.509` |
| 1000 | `1131.8` | `1.008` |

All tested characters have nonzero Gaussian-smoothed eigenvalue weight at these windows. This is finite evidence for the squared-spectrum positivity surface.

For the GRH-signature ratio at `B=500`, the tested maximum satisfies

```text
max_chi |psi(B,chi)|/sqrt(B) < log(B)^2.
```

The bound is not saturated. This is numerical evidence consistent with the `B^(1/2) log^2 B` signature, not a proof.

Moderate-scale growth exponents are noisy: individual zero oscillations dominate at this scale, and short-window ratios across `B=200` and `B=500` should not be treated as stable asymptotic evidence.

## 7. Richter-window refinement of the finite Weil approach

The Richter logarithmic window at decimal digit depth `k` is

```text
W_k = [10^(k-1), 10^k).
```

It is the natural digit-depth localization of the prime sum. Define the window character sum

```text
psi_{W_k}(chi)
  = sum_{p in W_k, p mod P in G_P} (log p) chi(p).
```

Under GRH one expects

```text
|psi_{W_k}(chi)| = O(10^(k/2) k).
```

If a zero occurs off the critical line at real part `beta > 1/2`, the same explicit-formula heuristic permits window growth of order `10^(k beta)`.

The Richter exponent is

```text
alpha_k(chi) = log |psi_{W_k}(chi)| / log sqrt(10^k).
```

The GRH-compatible target is `alpha_k(chi) -> 1` in the Richter normalization. A zero with real part `beta > 1/2` gives the corresponding limiting exponent `2 beta > 1`.

The normalized window sum is

```text
psi_{W_k}(chi) / (k sqrt(10^k)).
```

Under GRH this is `O(1)`. The individual squared Richter series

```text
W^Richter(chi)
  = sum_{k>=1} |psi_{W_k}(chi)|^2 / (10^k k^2)
```

is therefore GRH-strength: its convergence for every relevant character is not currently an unconditional theorem in this repository. It is part of the hard growth-rate boundary, not a separately proved B1 theorem.

Finite truncations are still positive by construction. What remains open is the passage from finite positive truncations to the full Weil distribution in the correct topology.

Numerical evidence at modulus `P=210`:

| Depth `k` | `max_chi |psi_{W_k}(chi)|` | `k sqrt(10^k)` | ratio | Richter exponent |
| ---: | ---: | ---: | ---: | ---: |
| 1 | `0` | `3.16` | `0` | N/A |
| 2 | `28.7` | `20.0` | `1.44` | `1.46` |
| 3 | `75.7` | `94.9` | `0.80` | `1.25` |

Depth 1 is empty for the `P=210` unit-filter because all single-digit primes divide 210. Depths 2 and 3 are positive, and the observed Richter exponent decreases toward the GRH-compatible value `1`.

Repunit resonance connection: a prime `q` is resonant at window depth `k` when

```text
q | R_k,
R_k = (10^k - 1)/9.
```

For example, `11 | R_2 = 11` and `11 in [10,100)`. These resonant primes modulate the oscillation structure of `psi_{W_k}(chi)` and connect `HW-PRIME-WINDOW-001` directly to the Weil positivity surface.

This section does not prove Condition B. It identifies the convergence of normalized Richter window sums as a precise window-local formulation of the same hard growth boundary and records finite evidence consistent with GRH-scale behavior.

## 8. B1 convergence — corrected analysis

The first attempted B1 statement would have asserted unconditional convergence of the individual Richter series. That statement is too strong. With the normalization above, individual convergence is GRH-strength.

The correct finite identity is the Parseval identity on `G_P`. Define

```text
f_k(g) = sum_{p in W_k, p mod P = g} log p.
```

Then

```text
(1/|G_P|) sum_{chi in G_P^} |psi_{W_k}(chi)|^2
  = sum_{g in G_P} f_k(g)^2.
```

This identity is finite and unconditional. It is the correct averaged squared-window relation. It also explains why replacing the right-hand side with `sum_{p in W_k} (log p)^2` is wrong once multiple primes land in the same residue class: residue-class cross terms contribute to `f_k(g)^2`.

The finite numerical observations at depths 2 and 3 are:

| Depth `k` | individual normalized term for `chi_(1,1,1)` | normalized ratio |
| ---: | ---: | ---: |
| 2 | `2.06` | `1.44` |
| 3 | `0.64` | `0.80` |

The terms decrease in this small sample, consistent with GRH-scale behavior. This is numerical evidence only.

Corrected conditional theorem: if the normalized window sums

```text
psi_{W_k}(chi) / (k sqrt(10^k))
```

remain uniformly bounded for every relevant character in the profinite limit, then the individual Richter series has the expected GRH-scale behavior, the finite positive truncations have a plausible weak-limit target, and the remaining bridge is the identification of that weak limit with the Weil distribution in the correct test-function topology. The boundedness condition is not proved here; it is the hard GRH-strength part of the program.

## 9. Relation to Ehrhart and repunit window data

`HW-PRIME-WINDOW-001` and the Ehrhart section identify a discrete lattice-counting symmetry and reciprocity structure. Ehrhart-Macdonald reciprocity supplies a finite discrete analogue of functional-equation symmetry.

The finite Weil distribution above supplies positivity at the finite Haar-measure level. The missing bridge is the convergence of finite positivity to the full Weil distribution on the correct test-function space.

Thus the finite arithmetic program supplies:

1. finite Haar positivity;
2. finite character orthogonality;
3. finite autocorrelation positivity;
4. Gaussian-smoothed finite positive distributions;
5. GRH-signature finite diagnostics;
6. Richter-window finite diagnostics;
7. finite Parseval window identities;
8. Ehrhart-style reciprocity diagnostics;
9. a profinite completion surface.

The analytic continuation / Weil criterion remains an open boundary.

## 10. Relation to Lane VIII Borel-Stieltjes scope

The Lane VIII Borel-Stieltjes scope in the Yang-Mills repository records the Borel-Laplace / transseries treatment of the Stieltjes correction tower from the continuum side.

Here the same correction tower appears as the finite-to-limit error control surface for prime-operator growth-rate data and finite Weil positivity propagation.

The two framings are not identical, but they point to the same analytic obstruction: whether the discrete-to-continuous correction tower is controlled strongly enough to preserve positivity and growth-rate bounds in the limit.

## 11. Non-claims

This document does not prove RH or GRH.

This document does not construct a Hilbert-Pólya operator.

This document does not prove essential self-adjointness of `T_infinity`.

This document does not assert that the raw symmetric finite operator is positive.

This document does not assert that raw finite eigenvalues converge to `-L'/L(0,chi)`.

This document does not assert that the finite GRH-signature ratio proves GRH.

This document does not assert that Richter-window evidence proves GRH.

This document does not assert unconditional convergence of the individual Richter series.

This document does not assert strict Borel summability of the Stieltjes tower; renormalon or transseries corrections are explicitly part of the open boundary.

This document does not assert that finite positivity has been propagated to the full Weil distribution.
