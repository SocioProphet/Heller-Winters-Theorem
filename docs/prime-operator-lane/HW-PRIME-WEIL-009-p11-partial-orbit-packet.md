# HW-PRIME-WEIL-009 — p=11 Partial-Orbit Packet Diagnostic

Status: finite diagnostic surface.  
Claim class: finite computation / packet decomposition, not theorem-grade analytic progress.  
Lane: prime/operator lane, Richter-window / orbit-classification / packet-variance surface.  
Depends on: `HW-PRIME-WEIL-006`, `HW-PRIME-WEIL-007`, `HW-PRIME-WEIL-008`.

## Purpose

This document records the first explicit partial-orbit packet diagnostic after the base-10 full-orbit `p=7` packet.

The target is the extension from:

```text
P_7 = 2 * 3 * 5 * 7 = 210
```

to:

```text
P_11 = 2 * 3 * 5 * 7 * 11 = 2310.
```

The new factor `p=11` is the first small prime with a nontrivial partial base-10 orbit:

```text
ord_11(10) = 2,   <10> = {10, 1}.
```

It is neither inert/degenerate nor full/Artin-active. It is the first computable “between active and inert” case.

## Local p=11 orbit split

The unit group has order:

```text
|(Z/11Z)^x| = 10.
```

There are `9` nontrivial local characters.

Since:

```text
<10> = {1,10} = {1,-1},
```

a local character cancels over the digit orbit iff:

```text
chi(10) = -1.
```

Equivalently, in exponent coordinates this is the odd-exponent condition.

The local split is:

```text
5 cancelling nontrivial characters
4 non-cancelling nontrivial characters
```

This is finite character orthogonality on the subgroup `<10>`.

## P=2310 character-layer count

The full character group for `P=2310` has size:

```text
phi(2310) = phi(2) phi(3) phi(5) phi(7) phi(11)
          = 1 * 2 * 4 * 6 * 10
          = 480.
```

The old `P=210` layer corresponds to characters trivial on the `p=11` coordinate:

```text
48 characters.
```

The new `p=11` layer is therefore:

```text
480 - 48 = 432 characters.
```

This is the correct layer count. The informal “40 new characters” count applies only if one compares local nontrivial character counts too coarsely; the CRT product with the old `P=210` character group multiplies the local split by `48`.

The new layer splits as:

```text
240 cancelling characters  = 48 * 5
192 non-cancelling characters = 48 * 4.
```

## What the diagnostic measures

For each Richter depth `K`, the diagnostic computes:

1. total nontrivial `P=2310` character energy;
2. the inherited old `P=210` layer energy;
3. the new `p=11` layer energy;
4. the energy from the `p=11` cancelling sublayer;
5. the energy from the `p=11` non-cancelling sublayer;
6. the share of total variance carried by the new `p=11` layer;
7. the share of the new `p=11` layer carried by the non-cancelling sublayer.

This tests whether the partial orbit behaves between the inert/degenerate packet and the full-orbit packet.

## Expected qualitative behavior

The orbit-classification framework predicts:

```text
terminating / degenerate packets < partial-orbit packets < full-orbit packets
```

in structural cancellation strength.

For `p=11`, the partial orbit cancels only the characters nontrivial on `<10>`. The non-cancelling sublayer therefore carries the genuinely new packet obstruction.

No exact asymptotic share is claimed. A rough local structural ratio is:

```text
orbit size / group size = 2 / 10 = 1/5,
```

but actual finite energy shares depend on prime distribution in the Richter windows and CRT interactions with the inherited `P=210` layer.

## Diagnostic scope

The canonical implementation is:

```text
tools/check_p11_partial_orbit_packet.py
```

The guard tests are:

```text
tests/test_p11_partial_orbit_packet.py
```

The diagnostic is intentionally finite. It does not extrapolate beyond computed depths.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove an asymptotic `p=11` packet share.

This document does not claim that the `p=11` partial-orbit packet closes the square-root barrier.

This document does not claim that local cancellation over `<10>` automatically transfers to prime-window cancellation.
