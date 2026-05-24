# HW-PRIME-WEIL-012 — Unified Count-Normalized Packet Comparison

Status: finite diagnostic surface.  
Claim class: finite computation / orbit-class energy-per-character comparison, not theorem-grade analytic progress.  
Lane: prime/operator lane, primorial tower variance decomposition.  
Depends on: `HW-PRIME-WEIL-007`, `HW-PRIME-WEIL-009`, `HW-PRIME-WEIL-010`, `HW-PRIME-WEIL-011`, `HW-OPEN-011`.

## Purpose

This document compares count-normalized character energy across all orbit classes visible at the `P=2310` level.

The goal is to remove raw character-count dilution and test whether orbit type remains visible in energy per character.

## Packet classes

At `P=2310`, split the nontrivial character family into four finite classes:

| Packet | Count | Orbit type |
|---|---:|---|
| `inert_p235` | `7` | terminating / degenerate layer from `p=2,3,5` |
| `p7_full` | `40` | full-orbit `p=7` layer inherited from `P=210` |
| `p11_cancel` | `240` | `p=11` partial-orbit cancelling sublayer |
| `p11_noncancel` | `192` | `p=11` partial-orbit non-cancelling sublayer |

The total is:

```text
7 + 40 + 240 + 192 = 479
```

which is the full nontrivial character count for `P=2310`.

## Statistic

For packet `C`, define:

```text
E_C(K) = (sum_{chi in C} |psi_{W_K}(chi)|^2) / |C|.
```

This is energy per character.

This statistic suppresses raw layer size and makes orbit-quality effects visible at finite depth.

## Finite measured values

| K | inert `p=2,3,5` | `p=7` full orbit | `p=11` cancelling | `p=11` non-cancelling |
|---:|---:|---:|---:|---:|
| 2 | `43.975485786919` | `202.301568265311` | `295.278465033670` | `295.278465033670` |
| 3 | `912.628197074576` | `1575.759657835338` | `3923.097663316467` | `4214.224918349286` |
| 4 | `881.487346082066` | `12236.765876957472` | `31698.312041391291` | `37149.288448317449` |

## Observed finite ordering

At `K=2`:

```text
inert < p7_full < p11_cancel = p11_noncancel.
```

At `K=3,4`:

```text
inert < p7_full < p11_cancel < p11_noncancel.
```

Thus the finite data support the packet-energy stratification:

```text
terminating/degenerate < full-orbit < partial cancelling < partial non-cancelling
```

at the tested depths.

This is a finite diagnostic statement only.

## Ratios

The diagnostic computes the following ratios:

| K | `p7_full / inert` | `p11_cancel / p7_full` | `p11_non / p11_cancel` |
|---:|---:|---:|---:|
| 2 | `4.600323666511` | `1.459595533655` | `1.000000000000` |
| 3 | `1.726615149670` | `2.489654870390` | `1.074208515825` |
| 4 | `13.881955044937` | `2.590415322906` | `1.171964248437` |

The `p11_non / p11_cancel` ratio is exactly `1` at `K=2`, then increases at the next two tested depths.

## Interpretation

The count-normalized statistic separates two effects:

1. raw character-count growth across primorial levels;
2. orbit-quality energy concentration within a fixed finite character family.

After count normalization, the `p=11` non-cancelling sublayer still carries more energy per character than the `p=11` cancelling sublayer at `K=3,4`.

The full-orbit `p=7` layer sits above the inert `p=2,3,5` layer and below the `p=11` partial-orbit layers in the tested windows.

This suggests that orbit type is visible after removing raw character-count growth, but no asymptotic ordering is claimed.

## Boundary

This is a finite computation over `P=2310` and small Richter depths.

It does not prove that this ordering persists for all depths.

It does not prove that the ordering persists at later primorial levels.

It does not prove that orbit classification alone determines energy-per-character asymptotics.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove an asymptotic packet-energy ordering.

This document does not prove that non-cancelling partial-orbit characters always carry more energy per character.

This document does not close the square-root barrier.
