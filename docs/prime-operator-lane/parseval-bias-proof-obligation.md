# HW-OPEN-008 — Parseval Bias Proof Obligation

Identifier: `HW-OPEN-008`  
Status: open proof obligation  
Claim class: proof target — not claimed proved  
Mathematical content added by this document: target theorem statement, variance formulation, explicit-formula proof boundary, and cancellation-risk accounting

This document records the remaining proof obligation exposed by `HW-PRIME-WEIL-002`.

It does not prove RH or GRH. It records a precise target estimate that would convert the hyperbolic off-line-zero growth mechanism into a real, positive Parseval-bias lower bound.

## 1. Window residue weights

Let

```text
W_k = [10^(k-1), 10^k)
```

and let `G_P=(Z/PZ)^x` be the finite unit group for the chosen modulus `P`.

For each residue class `g in G_P`, define the window residue weight

```text
f_k(g) = sum_{p in W_k, p mod P = g} log p.
```

Finite Parseval gives

```text
(1/|G_P|) sum_chi |psi_{W_k}(chi)|^2 = sum_{g in G_P} f_k(g)^2.
```

The left side is the averaged squared finite character sum. The right side is a sum of squares of real prime log-weights. It is unconditionally non-negative.

## 2. Variance formulation

Let

```text
mu_k = (1/|G_P|) sum_g f_k(g).
```

Define the finite residue-class variance

```text
Var_P(W_k) = sum_g (f_k(g)-mu_k)^2.
```

Equivalently,

```text
Var_P(W_k) = sum_g f_k(g)^2 - (sum_g f_k(g))^2 / |G_P|.
```

By character orthogonality, this is exactly the non-trivial character mass:

```text
Var_P(W_k) = (1/|G_P|) sum_{chi != 1} |psi_{W_k}(chi)|^2.
```

This is the real, positive bias detector. It is zero exactly when the window weights are perfectly equidistributed over residue classes.

## 3. Target theorem

Target theorem:

```text
For non-trivial chi modulo P, if L(s,chi) has a zero
rho = 1/2 + delta + i gamma with delta > 0, then

Var_P(W_k) = Omega(10^((1+2 delta) k) / k^2)
```

in the relevant Richter windows, after the declared normalization and after controlling lower-order terms and the trivial-character baseline.

Equivalently, in unnormalized form, the off-line zero should force exponential growth in the non-trivial Parseval mass:

```text
(1/|G_P|) sum_{chi != 1} |psi_{W_k}(chi)|^2.
```

This is not proved in this repository. It is the proof target.

## 4. Why this would close the growth-rate route

The quantity

```text
Var_P(W_k)
```

is a real second moment of prime log-weight imbalance across residue classes. It cannot be made negative and it cannot cancel across characters after Parseval has converted the character side into absolute squares.

If an off-line zero forces exponential growth in the non-trivial character contribution, that growth appears as excess second moment beyond the equidistributed baseline.

Thus the target theorem would establish:

```text
off-line zero => exponential Parseval-bias growth.
```

The contrapositive would say:

```text
polynomial Parseval-bias growth => no off-line zero.
```

This would be a GRH-strength statement, not a proof already present in the finite diagnostics.

## 5. Explicit-formula expansion

The windowed character sum has schematic explicit formula

```text
psi_{W_k}(chi)
  = - sum_rho (10^(k rho) - 10^((k-1) rho))/rho
    + lower-order terms.
```

Therefore

```text
Var_P(W_k)
  = (1/|G_P|) sum_{chi != 1}
      |sum_rho (10^(k rho) - 10^((k-1) rho))/rho + error_chi,k|^2.
```

Each outer summand is an absolute square. The target proof must extract the off-line zero contribution for the specific character whose `L`-function has the zero and prove that it dominates the remaining terms in the squared norm on an infinite set of windows, or under a stated standard analytic condition sufficient to control exact cancellation.

## 6. Required proof step

Let `rho_0 = 1/2 + delta + i gamma` be an off-line zero of `L(s,chi_0)`. The isolated contribution is

```text
A_k = -(10^(k rho_0) - 10^((k-1) rho_0))/rho_0.
```

Its magnitude has envelope

```text
|A_k| ~= C(rho_0) 10^(k(1/2+delta)).
```

The target lower-bound step is

```text
|psi_{W_k}(chi_0)|^2 >= c(rho_0) 10^(k(1+2 delta))
```

for the required windows after lower-order terms are controlled.

Once this is proved, Parseval gives immediately

```text
Var_P(W_k) >= (1/|G_P|) |psi_{W_k}(chi_0)|^2.
```

The remaining difficulty is the lower-bound step for the linear windowed character sum, not the finite Parseval identity.

## 7. Cancellation question

The linear sum `psi_{W_k}(chi_0)` can exhibit phase cancellation. A proof must address whether other zeros of the same `L`-function can cancel the off-line contribution at the level of the linear character sum.

The hyperbolic mechanism recorded in `HW-PRIME-WEIL-002` shows that for an off-line zero the even and odd envelopes grow like

```text
cosh(delta k log 10),
sinh(delta k log 10).
```

The conjugate and functional-equation partners carry the same hyperbolic envelope. The expected behavior is reinforcement in the squared norm, not cancellation.

However, ruling out exact cancellation by another zero at a matching ordinate and opposite phase is a genuine analytic proof obligation. The variance formulation moves cancellation outside the character-family average, but it does not by itself prove the lower bound for the specific linear character sum before squaring.

## 8. Baseline and excess

The trivial character records the total window mass:

```text
psi_{W_k}(1) = sum_{p in W_k} log p.
```

The non-trivial signal is the variance after removing the equidistributed baseline. If the residue weights were perfectly equidistributed, Cauchy-Schwarz would minimize

```text
sum_g f_k(g)^2.
```

Bias across residue classes increases the second moment. The Parseval-bias route therefore measures unevenness in prime residue distribution rather than relying on the sign of a linear character sum.

## 9. Relation to Barban-Davenport-Halberstam

The Barban-Davenport-Halberstam theorem controls averaged distribution error over moduli. The proof obligation here is sharper and more local: a fixed-modulus, fixed-window lower-bound criterion connecting off-line zeros to the residue-class variance for the selected finite surface.

The fixed-modulus variance criterion is the precise object needed by this finite program. It should not be conflated with an average-over-moduli theorem.

## 10. Non-claims

This document does not prove the target theorem.

This document does not prove RH or GRH.

This document does not prove zero simplicity or distinct ordinates.

This document does not assert that the explicit-formula cancellation problem is solved.

This document does not assert that finite tests discharge this proof obligation.

This document records the exact proof obligation so that future work cannot silently promote it to theorem-grade status.
