# HW-OPEN-008 — Parseval Bias Proof Obligation

Identifier: `HW-OPEN-008`  
Status: open proof obligation  
Claim class: proof target — not claimed proved  
Mathematical content added by this document: target theorem statement, proof-obligation boundary, and cancellation-risk accounting

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

## 2. Target theorem

Target theorem:

```text
For non-trivial chi modulo P, if L(s,chi) has a zero
rho = 1/2 + delta + i gamma with delta > 0, then

sum_{g in G_P} f_k(g)^2
  = Omega(10^((1+2 delta) k) / k^2)
```

in the relevant Richter windows, after subtracting the trivial-character baseline and controlling lower-order terms.

This is not proved in this repository. It is the proof target.

## 3. Why this would close the growth-rate route

The quantity

```text
sum_g f_k(g)^2
```

is a real second moment of prime log-weights across residue classes. It cannot be made negative and it cannot cancel across characters after Parseval has converted the character side into absolute squares.

If an off-line zero forces exponential growth in the non-trivial character contribution, that growth should appear as excess second moment beyond the trivial-character baseline.

Thus the target theorem would establish:

```text
off-line zero => exponential Parseval-bias growth.
```

The contrapositive would say:

```text
polynomial Parseval-bias growth => no off-line zero.
```

This would be a GRH-strength statement, not a proof already present in the finite diagnostics.

## 4. Required proof step

The required proof step is to apply the explicit formula to the windowed character sum

```text
psi_{W_k}(chi) = psi(10^k,chi) - psi(10^(k-1),chi),
```

extract the contribution from a zero

```text
rho = 1/2 + delta + i gamma,
```

and show that its contribution to

```text
|psi_{W_k}(chi)|^2
```

grows at scale

```text
10^((1+2 delta)k) / k^2
```

after Richter normalization and lower-order control.

The same contribution then enters the Parseval sum

```text
(1/|G_P|) sum_chi |psi_{W_k}(chi)|^2.
```

## 5. Cancellation question

The linear sum `psi_{W_k}(chi)` can exhibit phase cancellation. A proof must address whether another zero could cancel the off-line contribution at the level of the linear character sum.

The hyperbolic mechanism recorded in `HW-PRIME-WEIL-002` shows that for an off-line zero the even and odd envelopes grow like

```text
cosh(delta k log 10),
sinh(delta k log 10).
```

The conjugate and functional-equation partners carry the same hyperbolic envelope. The expected behavior is reinforcement in the squared norm, not cancellation.

However, ruling out exact cancellation by another zero at a matching ordinate and opposite phase is a genuine analytic proof obligation. It should not be hidden or marked solved by finite tests.

## 6. Baseline and excess

The trivial character records the total window mass:

```text
psi_{W_k}(1) = sum_{p in W_k} log p.
```

The non-trivial signal is the excess second moment after removing the equidistributed baseline. If the residue weights were perfectly equidistributed, Cauchy-Schwarz would minimize

```text
sum_g f_k(g)^2.
```

Bias across residue classes increases the second moment. The Parseval-bias route therefore measures unevenness in prime residue distribution rather than relying on the sign of a linear character sum.

## 7. Non-claims

This document does not prove the target theorem.

This document does not prove RH or GRH.

This document does not prove zero simplicity or distinct ordinates.

This document does not assert that the explicit-formula cancellation problem is solved.

This document does not assert that finite tests discharge this proof obligation.

This document records the exact proof obligation so that future work cannot silently promote it to theorem-grade status.
