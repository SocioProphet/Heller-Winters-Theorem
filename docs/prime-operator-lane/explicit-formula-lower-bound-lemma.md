# Explicit Formula Lower-Bound Lemma

Identifier: `HW-PRIME-WEIL-003`  
Related open problem: `HW-OPEN-008`  
Status: lemma surface / proof-obligation decomposition  
Claim class: partial proof structure — not claimed fully discharged  
Mathematical content added by this document: isolated off-line-zero term bound, standard on-line remainder target, and remaining off-line cancellation/equidistribution step

This document records the next proof step for the Parseval-bias route. It does not prove RH or GRH, and it does not claim that `HW-OPEN-008` is closed.

## 1. Lemma statement

Let `chi` be a non-trivial Dirichlet character modulo `P`. Suppose `L(s,chi)` has a zero

```text
rho_0 = 1/2 + delta + i gamma,
delta > 0.
```

Define the Richter window

```text
W_k = [10^(k-1), 10^k)
```

and the windowed character sum

```text
psi_{W_k}(chi) = psi(10^k,chi) - psi(10^(k-1),chi).
```

Target lower-bound lemma:

```text
|psi_{W_k}(chi)| >= C_delta 10^(k(1/2+delta)) / |rho_0|
```

on infinitely many windows, or under the stronger version, for all sufficiently large windows outside an explicitly bounded exceptional set.

The version required for `HW-OPEN-008` is enough to imply that

```text
|psi_{W_k}(chi)|^2 / (10^k k^2)
```

is unbounded with exponential envelope `10^(2 delta k)/k^2`.

## 2. Explicit-formula decomposition

The windowed explicit formula has schematic form

```text
psi_{W_k}(chi)
  = - sum_rho (10^(k rho) - 10^((k-1) rho))/rho
    + lower-order terms.
```

Separate the chosen off-line zero:

```text
psi_{W_k}(chi) = A_k + B_k,
```

where

```text
A_k = -(10^(k rho_0) - 10^((k-1) rho_0))/rho_0
```

and `B_k` contains every other zero contribution plus lower-order terms.

## 3. Proved component: isolated `A_k` envelope

The isolated contribution satisfies

```text
|A_k|
  = |10^(k rho_0)| |1 - 10^(-rho_0)| / |rho_0|.
```

Since `Re(rho_0)=1/2+delta`,

```text
|10^(k rho_0)| = 10^(k(1/2+delta)).
```

Also

```text
|1 - 10^(-rho_0)| >= 1 - |10^(-rho_0)|
                      >= 1 - 10^(-1/2).
```

Therefore

```text
|A_k| >= (1 - 10^(-1/2)) 10^(k(1/2+delta)) / |rho_0|.
```

This is an elementary bound and is discharged at the finite algebraic level.

## 4. Standard component: on-line zero remainder

If the remaining zero contribution is restricted to the critical line, the standard explicit-formula estimate gives an on-line contribution of size

```text
O(10^(k/2) log^2(10^k)).
```

Thus the ratio of the isolated off-line envelope to the on-line envelope is

```text
10^(k delta) / log^2(10^k),
```

which tends to infinity for every fixed `delta>0`.

This component is standard analytic-number-theory input. It is recorded here as an imported estimate, not as a theorem proved by the finite test suite.

## 5. Remaining component: other off-line zeros

The remaining hard case is the contribution of other off-line zeros of the same `L`-function, especially zeros with the same maximal real part.

A different zero

```text
rho_j = beta_j + i gamma_j
```

contributes a phasor with phase depending on

```text
( gamma_j - gamma ) k log 10.
```

For the `Omega` statement, it is not necessary to rule out cancellation at every `k`. It is enough to show that the off-line contributions cannot cancel the isolated maximal-real-part term for all sufficiently large `k`, or that a non-cancelling subsequence of windows exists.

The expected route is an equidistribution or almost-periodicity argument for the finite set of dominant ordinates. This is the remaining proof obligation.

## 6. Consequence for Parseval variance

Once the lower-bound lemma is discharged for `chi_0`, Parseval gives

```text
Var_P(W_k)
  = (1/|G_P|) sum_{chi != 1} |psi_{W_k}(chi)|^2
  >= (1/|G_P|) |psi_{W_k}(chi_0)|^2.
```

Therefore an off-line zero would imply

```text
Var_P(W_k) = Omega(10^(k(1+2 delta)))
```

in unnormalized form, and

```text
Var_P(W_k) / (10^k k^2) = Omega(10^(2 delta k)/k^2)
```

under Richter normalization.

This is the direct connection to `HW-OPEN-008`.

## 7. Non-claims

This document does not prove RH or GRH.

This document does not prove the lower-bound lemma in full.

This document does not prove the required equidistribution or almost-periodicity statement for dominant off-line zero ordinates.

This document does not assume zero simplicity.

This document does not mark `HW-OPEN-008` closed.

This document isolates the remaining analytic step so future work can target it directly.
