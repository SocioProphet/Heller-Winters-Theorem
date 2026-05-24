# HW-OPEN-011 — Character-Count Dilution in the Primorial Tower

Status: open transition problem / finite counting theorem surface.  
Claim class: exact finite character-count decomposition; finite diagnostic interpretation, not asymptotic theorem.  
Lane: prime/operator lane, primorial character-packet / variance-decomposition surface.  
Depends on: `HW-PRIME-WEIL-009`, `HW-PRIME-WEIL-010`.

## Purpose

This document records the character-count dilution effect exposed by the `p=11` partial-orbit packet diagnostic.

When the primorial modulus is extended from:

```text
P
```

to:

```text
Pq
```

by adding a new prime factor `q`, the new character layer is large. Even if the old layer contains a structurally strong full-orbit signal, the new layer may dominate finite variance by sheer character count if per-character energies are comparable.

This document separates the exact finite counting statement from the open analytic question of whether energy follows character count asymptotically.

## Exact character-count decomposition

Let `P` be coprime to a new prime `q`, and compare character groups:

```text
G_P^*  and  G_{Pq}^*.
```

At the dual-character level:

```text
hat(G_{Pq}) ~= hat(G_P) x hat((Z/qZ)^x).
```

The old layer consists of characters with trivial `q`-coordinate:

```text
|old layer| = phi(P).
```

The full character group has size:

```text
|hat(G_{Pq})| = phi(P)(q-1).
```

The new `q` layer consists of characters with nontrivial `q`-coordinate:

```text
|new q layer| = phi(P)(q-2).
```

Among nontrivial characters of `G_{Pq}`, the count shares are:

```text
old layer nontrivial share = (phi(P)-1) / (phi(P)(q-1)-1)
new q layer share          = phi(P)(q-2) / (phi(P)(q-1)-1).
```

As `q` grows with fixed `P`, the new-layer count share approaches:

```text
(q-2)/(q-1)
```

and the old-layer share approaches:

```text
1/(q-1).
```

This is exact finite counting.

## The p=11 instance

For:

```text
P=210,  q=11,  Pq=2310,
```

we have:

```text
phi(210)=48,
phi(2310)=480.
```

Therefore:

```text
old P=210 layer = 48 characters,
new p=11 layer = 432 characters.
```

Among all nontrivial `P=2310` characters:

```text
new p=11 layer share = 432 / 479 ~= 0.901879.
```

The measured finite energy share from `HW-PRIME-WEIL-010` is:

| K | `p11_new / total` |
|---:|---:|
| 2 | `0.938218008866` |
| 3 | `0.961859768615` |
| 4 | `0.967468868352` |

Thus, in the finite computed windows, the new `p=11` layer carries most of the `P=2310` energy.

## Within-layer p=11 split

The local `p=11` orbit is:

```text
<10> = {1,10} = {1,-1}.
```

The local nontrivial characters split as:

```text
5 cancelling characters      chi(10) = -1,
4 non-cancelling characters  chi(10) = +1.
```

The non-cancelling local count baseline is:

```text
4/9 ~= 0.444444.
```

The measured finite non-cancelling share inside the new `p=11` layer is:

| K | `p11_non / p11_new` |
|---:|---:|
| 2 | `0.444444444444` |
| 3 | `0.462182505791` |
| 4 | `0.483889986895` |

The departure from `4/9` is a finite prime-race / residue-bias diagnostic. It should not be promoted to an asymptotic Chebyshev-bias theorem without a separate theorem-grade reference surface.

## Interpretation

Two mechanisms are now separated.

First, orbit quality controls local cancellation structure:

```text
terminating / degenerate < partial orbit < full orbit.
```

Second, primorial extension controls character-count dilution:

```text
new q layer size = phi(P)(q-2).
```

As the primorial tower grows, each newly added prime introduces a large new character layer. The newest layer can dominate finite variance even if an older layer has cleaner orbit structure, because the new layer contains many more characters.

Therefore the `p=7` full-orbit signal dominates at `P=210`, but after extending to `P=2310`, the `p=11` layer can overwhelm the old `P=210` layer by count and measured energy.

## Open problem

Determine whether energy follows character-count dilution asymptotically in the primorial tower.

Concrete questions:

1. For extension `P -> Pq`, does the new `q` layer typically carry a share comparable to its character-count share?
2. How does orbit type of `q` modify that expected share?
3. Can full-orbit Artin-prime components remain visible after many later primorial extensions?
4. Is there a renormalized packet statistic that preserves orbit-quality information after character-count dilution?
5. Can the finite variance decomposition be normalized so that orbit structure, not raw character count, becomes the primary observable?

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove an asymptotic character-count dilution theorem.

This document does not prove an asymptotic Chebyshev-bias theorem.

This document does not claim that the newest primorial layer always dominates variance.

This document does not close the square-root barrier identified in `HW-PRIME-WEIL-005`.
