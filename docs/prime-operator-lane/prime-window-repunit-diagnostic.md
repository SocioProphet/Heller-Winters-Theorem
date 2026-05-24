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

## 6. Euler-Mascheroni correction per window

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

## 7. Boundary with HW-PRIME-FINITE-OPERATOR-001

`HW-PRIME-FINITE-OPERATOR-001` defines the full finite character-operator diagnostic over a selected modulus and prime cutoff.

The window operator `T_hat_{W_k}` is a restriction of that finite operator to a specific digit-scale band. The full operator sums across all bands up to the cutoff; the window operator isolates one band.

Thus `HW-PRIME-WINDOW-001` does not replace `HW-PRIME-FINITE-OPERATOR-001`. It refines it by adding digit-window localization and repunit-resonance diagnostics.

## Non-claims

This document does not predict the next prime.

This document does not prove a prime number theorem in windows.

This document does not prove RH, GRH, Hilbert-Pólya, or any zero-location theorem.

This document does not claim that digital-root cycles determine primality.

This document does not assert proof transfer to Yang-Mills or any Clay problem.
