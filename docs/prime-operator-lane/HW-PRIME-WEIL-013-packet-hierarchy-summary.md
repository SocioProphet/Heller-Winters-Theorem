# HW-PRIME-WEIL-013 — Finite Packet Hierarchy Summary

Status: compact finite hierarchy summary.  
Claim class: finite theorem/diagnostic summary, not analytic theorem-grade RH progress.  
Lane: prime/operator lane, primorial packet hierarchy / variance-decomposition surface.  
Depends on: `HW-PRIME-WEIL-006`, `HW-PRIME-WEIL-007`, `HW-PRIME-WEIL-010`, `HW-PRIME-WEIL-011`, `HW-PRIME-WEIL-012`, `HW-OPEN-011`.

## Purpose

This document states the current finite packet hierarchy in one place.

The hierarchy is computed at:

```text
P = 2310 = 2 * 3 * 5 * 7 * 11.
```

The result is a finite, CI-tested packet classification and energy-per-character diagnostic. It does not prove RH, GRH, an unconditional variance bound, or an asymptotic packet-ordering theorem.

## Finite packet partition theorem

The nontrivial character family for `P=2310` has:

```text
phi(2310) - 1 = 480 - 1 = 479
```

characters.

`HW-PRIME-WEIL-012` partitions these 479 characters into four finite packets:

| Packet | Orbit type | Category | Count |
|---|---|---:|---:|
| inert `p=2,3,5` | terminating / degenerate | C0/C1 | 7 |
| `p=7` full orbit | full base-10 orbit | C3 | 40 |
| `p=11` cancelling | partial orbit, odd exponents | C2-odd | 240 |
| `p=11` non-cancelling | partial orbit, even exponents | C2-even | 192 |

The partition is exact:

```text
7 + 40 + 240 + 192 = 479.
```

## Finite energy-per-character hierarchy

Energy per character is:

```text
E_C(K) = (sum_{chi in C} |psi_{W_K}(chi)|^2) / |C|.
```

The finite measured values at depths `K=3,4` are:

| Orbit type | Category | Count | `E/char` at `K=3` | `E/char` at `K=4` |
|---|---:|---:|---:|---:|
| inert `p=2,3,5` | C0/C1 | 7 | `912.628197074576` | `881.487346082066` |
| full orbit `p=7` | C3 | 40 | `1575.759657835338` | `12236.765876957472` |
| partial cancel `p=11` | C2-odd | 240 | `3923.097663316467` | `31698.312041391291` |
| partial non-cancel `p=11` | C2-even | 192 | `4214.224918349286` | `37149.288448317449` |

At the tested depths `K=3,4`, the finite ordering is:

```text
inert < p7 full-orbit < p11 partial-cancelling < p11 partial-non-cancelling.
```

This is the current finite evidence that orbit type remains visible after count normalization.

## What is proved unconditionally

The following are finite or elementary results already captured in the lane:

1. Exact Parseval variance identity for finite character groups.
2. Exact equidistribution-error decomposition of character sums.
3. Exact base-10 orbit classification for the tested primes.
4. Exact finite character partition at `P=2310`.
5. Exact finite energy-per-character values for the computed Richter depths.
6. Exact finite character-count dilution formulas for extending `P -> Pq`.

These are unconditional finite statements.

They do not imply an asymptotic variance bound.

## Conditional / barrier content

For a packet of characters, a GRH-scale estimate requires critical-line control for the Dirichlet `L`-functions attached to the characters in that packet.

Local packet counts:

- `p=7` full-orbit packet: 5 nontrivial local conductor-7 characters.
- `p=11` local packet: 9 nontrivial local conductor-11 characters.
- `p=11` cancelling subpacket: 5 odd-exponent conductor-11 characters.
- `p=11` non-cancelling subpacket: 4 even-exponent conductor-11 characters.

Therefore a statement involving the `p7_full + p11_non` local packets concerns:

```text
5 + 4 = 9
```

local nontrivial Dirichlet `L`-functions, not 5.

A statement involving the full local `p7 + p11` surface concerns:

```text
5 + 9 = 14
```

local nontrivial Dirichlet `L`-functions.

The proof barrier is:

```text
Bounding any layer at GRH scale requires GRH-strength control for the L-functions in that layer.
```

The finite diagnostics make this barrier visible. They do not cross it.

## Digit-cycle anchor

For a full-orbit prime `p`, complete finite digit-cycle cancellation is unconditional:

```text
sum_{j=0}^{p-2} chi(10^j) = 0
```

for every nontrivial character modulo `p`.

This is the digit-cycle anchor from `HW-PRIME-WEIL-007`.

Boundary: this is a statement about deterministic base-10 orbit cycles. It is not, by itself, an unconditional bound for actual prime-window character sums. Transferring it to Richter-window prime sums is the finite-to-asymptotic transition problem recorded in `HW-OPEN-010`.

## Current finite interpretation

The hierarchy now separates four effects:

1. inert/degenerate orbit structure has low finite energy per character;
2. full-orbit `p=7` structure sits above inert but below partial-orbit layers in the tested windows;
3. partial-orbit cancelling `p=11` characters carry larger energy per character than the full-orbit packet at `K=3,4`;
4. partial-orbit non-cancelling `p=11` characters carry the largest energy per character at `K=3,4`.

This is a finite hierarchy and a diagnostic observation.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove an asymptotic packet-energy ordering.

This document does not prove that the finite packet ordering persists for all depths.

This document does not claim that digit-cycle cancellation alone bounds actual prime-window character sums.

This document does not close the square-root barrier identified in `HW-PRIME-WEIL-005`.
