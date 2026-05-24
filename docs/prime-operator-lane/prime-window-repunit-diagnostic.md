# HW-PRIME-WINDOW-001 — Prime-Window Repunit Diagnostic

Identifier: `HW-PRIME-WINDOW-001`  
Status: finite prime-window diagnostic  
Claim class: finite arithmetic / prime-window operator diagnostic  
Mathematical content added by this document: bounded finite identities and diagnostic operator definitions

This document records a finite diagnostic relating repunit additive sums, digital-root cycles, residue-class admissibility, and digit-scale prime-window character sums.

It is not a primality theorem, not a prime-prediction theorem, and not a Hilbert-Pólya or RH claim.

## 1. Repunit additive identity

Let

```text
R_k = (10^k - 1) / 9 = 11...1
```

be the base-10 repunit with `k` digits.

The depth-3 identity is:

```text
R_1 + R_2 + R_3 = 1 + 11 + 111 = 123.
```

Equivalently:

```text
sum_{j=1}^3 R_j = ((10^1-1) + (10^2-1) + (10^3-1)) / 9
                 = (9 + 99 + 999) / 9
                 = 1107 / 9
                 = 123.
```

In general,

```text
sum_{j=1}^k R_j = (10^(k+1) - 10 - 9k) / 81.
```

For `1 <= k <= 9`, this sum is the integer with digit sequence:

```text
123...k.
```

The restriction `k <= 9` is necessary in base 10 because after digit count 9, decimal carries and multi-digit column counts appear.

The column-count interpretation is exact: the digit at position `i` from the left in `123...k` records how many repunits in the tower reach that position. Equivalently, the digit at position `i` from the right is `k+1-i` before reversing to standard left-to-right notation.

This can be represented by an upper-triangular stacking matrix. For `k=3`, stacking the repunits over the decimal basis `(100, 10, 1)` gives column counts `(1,2,3)` and therefore the integer `123`.

## 2. Digital-root homomorphism

For positive integers, define the digital root:

```text
dr(n) = 1 + ((n-1) mod 9).
```

This is the representative in `{1,...,9}` of the class of `n mod 9`.

Since `10 == 1 mod 9`, the repunit satisfies:

```text
R_k = 1 + 10 + ... + 10^(k-1) == k mod 9.
```

Therefore:

```text
dr(R_k) = dr(k).
```

For the additive tower:

```text
dr(sum_{j=1}^k R_j) = dr(sum_{j=1}^k j) = dr(T_k),
```

where

```text
T_k = k(k+1)/2
```

is the `k`-th triangular number.

The triangular numbers modulo 9 have period 9:

```text
T_k mod 9: 1, 3, 6, 1, 6, 3, 1, 0, 0, 1, 3, 6, ...
```

Thus the digital-root cycle is governed by the triangular-number cycle modulo 9.

## 3. Coprimality fingerprint

At depth `k=3`,

```text
R_1 + R_2 + R_3 = 123,
dr(123) = dr(1+2+3) = 6.
```

Also:

```text
phi(9) = 6.
```

The six admissible residue classes modulo 9 for primes greater than 3 are:

```text
1, 2, 4, 5, 7, 8.
```

Therefore, at depth 3, the digital root of the repunit additive sum equals exactly the number of residue classes modulo 9 that can contain primes greater than 3.

This is a finite coprimality fingerprint. It is not a theorem predicting primality. It records that the digit-depth-3 repunit stack lands on the same count as the prime-admissible residue classes modulo 9.

More generally:

```text
dr(sum_{j=1}^k R_j) = dr(T_k).
```

When `k == 3 mod 9`, the triangular digital-root cycle hits `6`, matching `phi(9)`.

## 4. Repunit resonances and prime factorization

For a prime `p` not dividing 10, the resonance condition is:

```text
p divides R_k  iff  ord_p(10) divides k.
```

This is because:

```text
R_k = (10^k - 1) / 9,
```

and, for `p != 3`, divisibility by `R_k` is equivalent to `10^k == 1 mod p`. For `p=3`, the repunit divisibility condition is controlled separately by the digit count `k mod 3`.

Small digit-scale resonances:

| `k` | `R_k` | Prime resonances |
| ---: | ---: | --- |
| 1 | 1 | none |
| 2 | 11 | 11 |
| 3 | 111 | 3, 37 |
| 4 | 1111 | 11, 101 |
| 5 | 11111 | 41, 271 |
| 6 | 111111 | 3, 7, 11, 13, 37 |

These resonances identify primes whose decimal order divides the digit-scale `k`. They modulate which character sums can be amplified in a `k`-digit prime window.

## 5. Window operator

Let `W_k` be a `k`-digit window, for example:

```text
W_k = {q prime : 10^(k-1) <= q < 10^k}.
```

Let `P_k` be the chosen primorial modulus for the window, and let:

```text
G_{P_k} = (Z/P_k Z)^x.
```

Define the prime-window operator:

```text
T_hat_{W_k} f(g) = sum_{q in W_k, q prime, q mod P_k = g} (log q) f(q mod P_k).
```

Equivalently, the window kernel is:

```text
A_{W_k}(g) = sum_{q in W_k, q prime, q mod P_k = g} log q.
```

Characters of `G_{P_k}` diagonalize the associated finite convolution operator. The corresponding eigenvalues are finite Dirichlet-character-style sums restricted to the digit window:

```text
lambda_chi(W_k) = sum_{g in G_{P_k}} A_{W_k}(g) chi(g).
```

These window eigenvalues approximate the character-sum behavior of primes restricted to `W_k`.

## 6. Polynomial value distributions

For fixed `k` and fixed odd `p`, the polynomial value sequence

```text
n^k + p
```

splits into two parity streams:

```text
E_k = {n^k + p : n even},
O_k = {n^k + p : n odd}.
```

For odd `p`, the even-`n` stream is odd and contains the only ordinary prime candidates beyond the exceptional prime `2`; the odd-`n` stream is even and therefore composite except in trivial edge cases.

For `n^2+1`, the prime-candidate stream is obtained from even `n`. It has values

```text
(2m)^2 + 1 = 4m^2 + 1,
```

so every candidate is congruent to `1 mod 4`. The gaps between consecutive even-`n` candidates are

```text
(2m+2)^2 + 1 - ((2m)^2 + 1) = 8m + 4,
```

an arithmetic progression with common difference `8`. All gaps are divisible by `4`.

Modulo `G_210=(Z/210Z)^x`, the orbit

```text
{n^2+1 mod 210 : gcd(n^2+1,210)=1}
```

has size `16`, exactly one third of the 48 unit classes. Thus the polynomial value stream reaches a strict subset of the finite prime residue surface.

This gives a finite orbit-density diagnostic: polynomial thin sets occupy only the residue classes admitted by their modular orbit. It is an upper-bound and sieve diagnostic, not a prime-count theorem.

For primes `q == 3 mod 4`, `-1` is not a quadratic residue modulo `q`, so

```text
n^2 + 1 != 0 mod q
```

for all `n`. Equivalently, such primes never divide a value of `n^2+1`. The sequence is therefore permanently sieved away from those divisor classes.

More generally, `n^2+p == 0 mod q` is possible exactly when `-p` is a quadratic residue modulo `q`, except at the degenerate local factors dividing `2pq`. This quadratic-residue criterion is the local sieve law for the polynomial value distribution.

## 7. Perfect cancellation and geometric window center

On any finite group `G`, every non-trivial character satisfies

```text
sum_{g in G} chi(g) = 0.
```

For `G_10=(Z/10Z)^x={1,3,7,9}`, this is the perfect cancellation theorem for non-trivial characters modulo 10. It is finite coset orthogonality and does not depend on prime distribution.

The Richter window

```text
[10^(k-1), 10^k)
```

has geometric center

```text
sqrt(10^(k-1) * 10^k) = 10^(k-1/2).
```

The half-step `1/2` in this logarithmic center is the same normalization scale that appears in GRH-compatible Richter growth. This is a coordinate identity, not a proof of GRH.

The density of first digits admissible to primes in base 10 is `2/5`: among digits `1..9`, the terminal-prime-compatible odd non-5 digits are `{1,3,7,9}`. This is the terminal-digit admissibility density, not the full prime density in a window.

## 8. Taylor, theta, and half-integer split diagnostics

The Taylor series split

```text
exp(x) = sum_{n even} x^n/n! + sum_{n odd} x^n/n!
```

separates the even and odd streams. With imaginary argument,

```text
exp(i x) = cos(x) + i sin(x),
```

where `cos(x)` uses even powers and `sin(x)` uses odd powers. This is an exact parity decomposition of the exponential series.

The polynomial generating series

```text
sum_{n>=0} z^(n^k+p) = z^p sum_{n>=0} z^(n^k)
```

has the same parity split:

```text
z^p (sum_m z^((2m)^k) + sum_m z^((2m+1)^k)).
```

For `k=2`, this is a theta-function split. The full bilateral theta series is

```text
theta_3(q) = sum_{n in Z} q^(n^2),
```

and the even-square part is governed by `theta_3(q^4)`. Thus the parity split of `n^2+p` is the arithmetic version of the even/odd split of the theta series.

The tangent ratio records the corresponding analytic split:

```text
tan(x) = sin(x)/cos(x),
tanh(x) = sinh(x)/cosh(x).
```

This is a structural diagnostic only. It does not assert that ratios of prime counts literally converge to a tangent function.

The Mittag-Leffler identity

```text
sum_{n=1}^infinity 1/(n^2+1)
  = (pi coth(pi) - 1)/2
```

is a concrete bridge from the `n^2+1` denominator sequence to the trigonometric / hyperbolic meromorphic structure. It records the same `i`-root structure because `n^2+1=(n-i)(n+i)`.

The poles of `tan(z)` occur at

```text
z = pi(k+1/2),
```

which exposes the half-integer shift in the trigonometric decomposition. This `1/2` also appears in the Richter geometric center `10^(k-1/2)` and in the critical-line coordinate `Re(s)=1/2`. The shared value is a coordinate/fixed-point diagnostic, not by itself a proof of RH.

The theta functional equation is the rigorous analytic bridge from theta parity structure to zeta functional-equation symmetry. This document records the finite diagnostic connection only; it does not claim that the finite window split forces zero locations.

## 9. Euler-Mascheroni correction per window

The Euler-Mascheroni constant records the leading residual between discrete harmonic sums and their continuous logarithmic approximation:

```text
gamma = lim_{N->infinity} (sum_{n=1}^N 1/n - log N).
```

At digit-scale windows, finite prime sums are compared against integral approximants such as logarithmic-integral differences:

```text
Li(10^k) - Li(10^(k-1)).
```

The leading residual is Euler-Mascheroni-type: it is the same kind of discrete-to-continuous correction appearing at each logarithmic scale. Higher moment corrections are encoded by the Stieltjes tower `{gamma_n}`.

The identity

```text
1 + 11 + 111 = 123
```

is the depth-3 fingerprint of this structure: additive repunit stacking, triangular digital-root accumulation, and coprimality-count resonance all coincide at the three-digit level.

This is a diagnostic finite-arithmetic statement. It does not assert that `gamma` alone predicts prime counts in digit windows.

## 10. Boundary with HW-PRIME-FINITE-OPERATOR-001

`HW-PRIME-FINITE-OPERATOR-001` defines the full finite character-operator diagnostic over a selected modulus and prime cutoff.

The window operator `T_hat_{W_k}` is a restriction of that finite operator to a specific digit-scale band. The full operator sums across all bands up to the cutoff; the window operator isolates one band.

Thus `HW-PRIME-WINDOW-001` does not replace `HW-PRIME-FINITE-OPERATOR-001`. It refines it by adding digit-window localization and repunit-resonance diagnostics.

## 11. Ehrhart polynomial — discrete side of zeta

The Ehrhart polynomial of a lattice polytope `P` counts lattice points in dilates:

```text
L(P,t) = |tP cap Z^d|,  t in N.
```

For the standard `d`-simplex `Delta_d` with vertices at the origin and the `d` coordinate points,

```text
L(Delta_d,t) = binom(t+d,d).
```

At unit dilation,

```text
L(Delta_0,1)=1,
L(Delta_1,1)=2,
L(Delta_2,1)=3.
```

Thus the digit sequence of the repunit additive sum is the Ehrhart simplex sequence at unit dilation:

```text
R_1 + ... + R_n = 123...n,
left digit k = L(Delta_{k-1},1)=k,
```

for `1 <= n <= 9` in base 10.

The Ehrhart series is

```text
Ehr(P,z) = sum_{t>=0} L(P,t) z^t = h*(z)/(1-z)^(d+1).
```

For the unit hypercube `[0,1]^d`, this gives

```text
Ehr([0,1]^d,z) = sum_{t>=0} (t+1)^d z^t = sum_{n>=1} n^d z^(n-1).
```

After substituting `z=e^{-u}`, the Mellin transform gives the zeta bridge:

```text
int_0^infinity u^(s-1) Ehr([0,1]^d,e^{-u}) du = Gamma(s) zeta(s-d).
```

This is the analytic bridge from discrete lattice counting to the Riemann zeta function.

The Euler-Mascheroni constant is simultaneously the constant term in the Laurent expansion of zeta at the pole and the leading residual in the discrete-to-continuous Euler-Maclaurin correction. On the Ehrhart side it records the leading error between lattice counts and the corresponding continuous volume approximation, accumulated across dilates.

Ehrhart-Macdonald reciprocity states:

```text
L(P,-t) = (-1)^d L(P^circ,t).
```

This is the discrete functional-equation analogue: it exchanges the polytope with its interior and introduces the parity sign. For the 2-simplex,

```text
L(Delta_2,t) = (t+1)(t+2)/2,
L(Delta_2,-t) = (t-1)(t-2)/2 = L(Delta_2^circ,t).
```

The vanishing of the interior lattice count at small dilations is the Ehrhart-side finite analogue of discrete-side zeros. This diagnostic does not identify nontrivial zeta zeros.

## Non-claims

This document does not predict the next prime.

This document does not prove a prime number theorem in windows.

This document does not prove RH, GRH, Hilbert-Pólya, or any zero-location theorem.

This document does not claim that digital-root cycles determine primality.

This document does not assert that polynomial orbit density proves primality or gives an asymptotic formula for polynomial prime values.

This document does not assert that the Taylor/theta parity split proves a zeta zero-location theorem.

This document does not assert proof transfer to Yang-Mills or any Clay problem.
