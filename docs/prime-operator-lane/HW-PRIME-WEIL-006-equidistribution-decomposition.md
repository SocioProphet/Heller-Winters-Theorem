# HW-PRIME-WEIL-006 — Equidistribution Decomposition Surface

Status: proved finite decomposition and bound; finite diagnostic barrier map.  
Claim class: theorem-grade for the finite decomposition identities; method-grade for barrier interpretation.  
Lane: prime/operator lane, fixed-modulus Richter-window variance route.  
Depends on: `HW-PRIME-WEIL-005`, `HW-OPEN-009`, finite Parseval variance identity.

## Purpose

This document records the sharp finite equidistribution decomposition that sits underneath the Richter-window variance barrier.

It isolates the exact arithmetic fact:

```text
character sums are Fourier transforms of residue-class equidistribution errors.
```

This is unconditional and finite. It does not prove RH or GRH.

## Section 1 — Exact decomposition

Let `P` be fixed and let `G_P=(Z/PZ)^x`. Let `chi` be a nontrivial character of `G_P`.

For a Richter window `W_K`, define the residue-class Chebyshev mass:

```text
M_K(r) = sum_{p in W_K, p == r mod P} log p
```

and the average mass over the finite character quotient:

```text
bar(M)_K = (1 / |G_P / ker chi|) sum_{r in G_P / ker chi} M_K(r).
```

Define the residue-class equidistribution error:

```text
epsilon_K(r) = M_K(r) - bar(M)_K.
```

Then, for every nontrivial `chi`, since:

```text
sum_{r in G_P / ker chi} chi(r) = 0,
```

the main term drops out exactly and:

```text
psi_{W_K}(chi) = sum_{r in G_P / ker chi} chi(r) epsilon_K(r).
```

This is an exact finite identity.

## Section 2 — Triangle bound

The decomposition immediately gives:

```text
|psi_{W_K}(chi)|
  <= sum_r |chi(r)| |epsilon_K(r)|
  <= |G_P / ker chi| max_r |epsilon_K(r)|.
```

In particular, for a primitive mod-7 packet:

```text
|psi_{W_K}(chi_7)| <= 6 max_r |epsilon_K(r)|.
```

This is unconditional and finite.

The bound shows that a square-root bound for the residue-class errors implies a square-root bound for the character sums.

The converse requires the full nontrivial character packet and Fourier inversion, not a single character alone.

## Section 3 — GRH equivalence at the residue-error level

For the mod-7 character packet, the following is the correct theorem-candidate equivalence:

```text
GRH for all nontrivial L(s, chi) in the mod-7 packet
  <=>
max_r |epsilon_K(r)| = O(sqrt(10^K) log^2(10^K))
```

for the Richter-window family, with the usual explicit-formula and windowed-Omega obligations from `HW-PRIME-WEIL-005` and `HW-OPEN-009`.

The forward direction follows from applying the GRH character-sum bound to all nontrivial mod-7 characters and using finite Fourier inversion on `(Z/7Z)^x`.

The reverse direction follows because the finite Fourier transform of the residue-error vector gives all nontrivial character sums.

This is a reformulation of the same GRH-strength square-root barrier, not a proof of GRH.

## Section 4 — Empirical data for K=2..6

For the primitive mod-7 component, the diagnostic records the finite ratios:

```text
max_r |epsilon_K(r)| / sqrt(10^K)
```

| K | `max_r |epsilon_K(r)|` | ratio to `sqrt(10^K)` | Comment |
|---:|---:|---:|---|
| 2 | about `2.49` | about `0.25` | below GRH-shaped envelope |
| 3 | about `8.16` | about `0.26` | below GRH-shaped envelope |
| 4 | about `45.67` | about `0.46` | below GRH-shaped envelope |
| 5 | about `146.58` | about `0.46` | below GRH-shaped envelope |
| 6 | about `220.00` | about `0.22` | below GRH-shaped envelope |

These are finite diagnostics only. They are consistent with square-root-scale behavior and do not prove an asymptotic bound.

## Section 5 — Digit-cycle oracle bound at resonant depth

For `p=7`, base `10` has period:

```text
ord_7(10) = 6.
```

For the primitive mod-7 character used by the diagnostic:

```text
sum_{j=1}^6 chi_7(10^j mod 7) = 0.
```

The finite digit-cycle partial sums satisfy:

```text
max_m |sum_{j=1}^m chi_7(10^j mod 7)| <= 2.
```

At resonant depth `K=6`, the tool verifies the finite oracle-style bound:

```text
|psi_{W_6}(chi_7)| <= 2 log(10^6) sqrt(N_6 / 6),
```

where `N_6` is the prime count in `W_6`.

This is a finite checked bound at the resonant depth. It is not claimed as an all-depth theorem. Extending it requires a distribution hypothesis or a proof controlling how primes populate the digit-cycle compartments across all Richter windows.

## Section 6 — Variance concentration

The full `G_210` character family decomposes through CRT coordinates. Let `Delta_{p=7}(K)` denote the finite energy packet from all `G_210` characters with nontrivial mod-7 coordinate.

The diagnostic computes:

```text
Delta_{p=7}(K) / Var_total(K)
```

for finite depths. At depths `K=2` and `K=3`, the mod-7 packet accounts for more than `85%` of the nontrivial character energy. In the observed windows, the obstruction concentrates strongly in the mod-7 packet.

This is finite numerical evidence. It does not prove asymptotic concentration.

## Section 7 — Barrier location

The finite decomposition proves that the character-sum barrier is exactly a residue-class equidistribution barrier:

```text
psi_{W_K}(chi) = Fourier(epsilon_K)(chi).
```

For mod 7, proving:

```text
max_r |epsilon_K(r)| = O(sqrt(10^K) poly(K))
```

is GRH-strength for the associated character packet.

Thus the barrier has been localized at the finest finite resolution currently available: residue-class equidistribution error inside Richter windows.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the unconditional square-root bound on `max_r |epsilon_K(r)|` for all `K`.

This document does not prove the windowed Omega theorem.

This document does not claim the digit-cycle oracle bound extends to all depths.

This document does not close the square-root barrier identified in `HW-PRIME-WEIL-005`.

This document does not construct a Hilbert-Polya operator.

This document does not promote the prime/operator lane to theorem-grade RH progress.
