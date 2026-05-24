# HW-PRIME-WEIL-015 — q=37 Orbit-Quality Measurement

Status: finite measurement / model-falsification surface.  
Claim class: finite diagnostic result, not theorem-grade analytic progress.  
Lane: prime/operator lane, orbit-quality / packet-energy surface.  
Depends on: `HW-OPEN-013`, `HW-PRIME-WEIL-014`.

## Purpose

This document records the first q=37 measurement against the pre-registered orbit-quality model from `HW-OPEN-013`.

The model was fixed before measurement:

```text
R(q) = 1 + 0.3439 / ord_q(10).
```

For `q=37`:

```text
ord_37(10) = 3,
R(37) = 1.114633333333...
```

The measurement below uses local conductor-37 character packets, not the full primorial-through-37 character family.

## q=37 packet structure

For `q=37`:

```text
ord_37(10) = 3,
I_37 = (37-1)/3 = 12,
n_nc(37) = 11.
```

There are:

```text
11 non-cancelling local characters,
24 cancelling local characters.
```

The measured statistic is:

```text
R_meas(37,K) = E_nc(37,K) / E_cancel(37,K),
```

where each energy is count-normalized by the number of characters in the local packet.

## Pre-registered prediction

The pre-registered prediction was:

```text
R(37) = 1.114633333333...
```

No parameter was changed after the measurement.

## Finite measured values

| K | prime count in W_K | E_cancel / char | E_nc / char | measured ratio | deviation from model |
|---:|---:|---:|---:|---:|---:|
| 2 | 21 | `189.490278757736` | `114.729033668758` | `0.605461316649` | `-0.509172016685` |
| 3 | 143 | `1024.158836091167` | `1848.829699483743` | `1.805217739994` | `0.690584406661` |
| 4 | 1061 | `20069.659764608412` | `9407.435842493238` | `0.468739179081` | `-0.645894154253` |
| 5 | 8363 | `150781.374888863530` | `103834.737638151404` | `0.688644321719` | `-0.425989011615` |

The measured ratios oscillate strongly and do not stay near the pre-registered prediction in the tested windows.

## Result

The direct local q=37 packet measurement falsifies the pre-registered model in its finite-depth form.

Specifically, the deepest tested value is:

```text
R_meas(37,5) = 0.688644321719,
```

which is far below:

```text
R(37) = 1.114633333333.
```

This does not refute any theorem. It refines the diagnostic program: orbit period alone is not sufficient to predict finite-depth non-cancelling/cancelling energy ratios.

## Interpretation

The q=37 measurement shows that finite-window prime-race fluctuations dominate the simple `1 + c/d_q` model at the tested depths.

The result does not imply that orbit quality is irrelevant. It implies that the model must include additional structure, such as:

1. coset mass imbalance at the tested window;
2. prime-race fluctuation across cosets of `<10>`;
3. depth dependence;
4. conductor dependence;
5. interaction between local character parity and the observed window.

## Boundary

This is a local conductor-37 diagnostic.

It is not a full primorial-through-37 computation. The full primorial character family is much larger and requires separate machinery.

The measurement does not prove or disprove RH, GRH, Artin's conjecture, or any asymptotic variance law.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove an asymptotic orbit-quality energy law.

This document does not prove that orbit quality is irrelevant.

This document does not close the square-root barrier.
