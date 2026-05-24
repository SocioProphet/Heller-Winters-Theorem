# HW-OPEN-009 — Windowed Omega Theorem Register Note

Status: companion open-problem register note.  
Claim class: open analytic theorem target.  
Canonical target document: `docs/prime-operator-lane/windowed-omega-theorem-target.md`.

## Problem

Prove a windowed Omega theorem for Richter-window character sums.

If `L(s, chi)` has an off-critical zero:

```text
rho_0 = sigma_0 + i t_0,    sigma_0 > 1/2,
```

then prove that there are infinitely many Richter-window depths `K`, preferably a positive-density subsequence, such that:

```text
|psi_{W_K}(chi)| >= c 10^(K sigma_0)
```

for some `c > 0`.

## Relationship to HW-PRIME-WEIL-005

`HW-PRIME-WEIL-005` identifies the square-root barrier for the fixed-modulus Parseval variance route.

`HW-OPEN-009` isolates the lower-bound side of that route. It does not supply the missing unconditional critical-scale variance upper bound.

## Path A — direct phase route

Directly analyze the exponential-polynomial zero sum in the Richter windows. This route may require almost-periodicity or rational-independence control for zero ordinates.

Status: open.

## Path B — Cesaro / second-moment route

Use the normalized second moment over window depth. The diagonal contribution of the selected zero supplies a positive candidate contribution.

Status: promising partial route. The diagonal calculation is not by itself a complete proof. The remaining obligations are cross-term control, truncation control, same-real-part zero handling, and explicit-formula error control.

## Non-claims

This note does not prove RH.

This note does not prove GRH.

This note does not prove the windowed Omega theorem.

This note does not prove the unconditional variance bound.

This note does not close `HW-PRIME-WEIL-004` or `HW-PRIME-WEIL-005`.
