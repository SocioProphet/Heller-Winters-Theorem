# HW-PRIME-WEIL-011 — Count-Normalized Packet Energy

Status: finite diagnostic surface.  
Claim class: finite computation / count-normalized packet-energy comparison, not theorem-grade analytic progress.  
Lane: prime/operator lane, primorial tower variance decomposition.  
Depends on: `HW-PRIME-WEIL-009`, `HW-PRIME-WEIL-010`, `HW-OPEN-011`.

## Purpose

This document defines and computes the count-normalized packet-energy statistic that removes raw character-count growth from primorial variance packets.

Raw packet energy can be dominated by the newest primorial layer because the layer contains many characters. To compare orbit quality rather than raw count, normalize by the number of characters in each packet.

## Definition

For an orbit class or packet `C` inside the character group, define:

```text
E_C(K) = (sum_{chi in C} |psi_{W_K}(chi)|^2) / |C|.
```

This is energy per character.

Under a null model in which energy is equidistributed across characters, `E_C(K)` should be comparable across packets. Deviations from equality measure packet-specific concentration after removing raw character-count dilution.

## Packets compared

At the `P=2310` level, compare:

1. old `P=210` nontrivial layer: `47` characters;
2. `p=11` cancelling sublayer: `240` characters;
3. `p=11` non-cancelling sublayer: `192` characters.

The p=11 cancelling sublayer consists of odd-exponent local characters with:

```text
chi(10) = -1.
```

The p=11 non-cancelling sublayer consists of even-exponent local characters with:

```text
chi(10) = +1.
```

## Finite measured values

| K | old layer per character | p11 cancelling per character | p11 non-cancelling per character | non/cancel ratio | non/old ratio |
|---:|---:|---:|---:|---:|---:|
| 2 | `178.721087896189` | `295.278465033670` | `295.278465033670` | `1.000000000000` | `1.652174729404` |
| 3 | `1476.995397722033` | `3923.097663316467` | `4214.224918349286` | `1.074208515825` | `2.853241739852` |
| 4 | `10545.554180869645` | `31698.312041391290` | `37149.288448317450` | `1.171964248437` | `3.522744069317` |

The finite data show:

```text
E_p11_non(K) = E_p11_cancel(K) at K=2,
E_p11_non(K) > E_p11_cancel(K) for K=3,4.
```

The gap between non-cancelling and cancelling p=11 sublayers grows across the computed depths.

## Interpretation

The p=11 non-cancelling characters are blind to the reflection in the partial orbit `{1,-1}`:

```text
chi(10)=+1,
1 + chi(10) = 2.
```

They see the length-2 orbit as constructively collapsed rather than cancelling.

The p=11 cancelling characters see:

```text
chi(10)=-1,
1 + chi(10) = 0.
```

Count-normalized energy therefore separates orbit-quality effects from raw packet size.

The finite observed ordering is:

```text
p11 non-cancelling >= p11 cancelling > old P=210 layer
```

for the computed windows, with equality between the two p=11 sublayers at `K=2`.

## Boundary

This statistic is finite and diagnostic.

It does not prove that the same ordering holds asymptotically.

It does not prove that local orbit type alone determines energy per character.

It does not prove that prime-window energy follows local character-count or local cancellation baselines at large depths.

## Next questions

1. Does `E_p11_non(K) / E_p11_cancel(K)` continue increasing at deeper feasible depths?
2. Does the same count-normalized separation appear for later partial-orbit primes?
3. Do full-orbit Artin packets have lower energy per character after count normalization?
4. Is there a stable normalized statistic that preserves orbit quality across primorial extensions?

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove an asymptotic packet-energy ordering.

This document does not prove that non-cancelling partial-orbit characters always carry more energy per character.

This document does not close the square-root barrier.
