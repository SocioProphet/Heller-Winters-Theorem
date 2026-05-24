# HW-PRIME-WEIL-010 — p=11 Non-Cancelling Variance Share

Status: finite diagnostic surface.  
Claim class: finite computation / variance-share comparison, not theorem-grade analytic progress.  
Lane: prime/operator lane, Richter-window / partial-orbit packet surface.  
Depends on: `HW-PRIME-WEIL-009`.

## Purpose

This document measures the finite energy share carried by the non-cancelling `p=11` character sublayer after the `P=2310` extension.

The local `p=11` orbit is:

```text
<10> = {1,10} = {1,-1} subset (Z/11Z)^x.
```

The local nontrivial character split is:

```text
5 cancelling characters      chi(10) = -1
4 non-cancelling characters  chi(10) = +1
```

The finite local count baseline for the non-cancelling part of the new `p=11` layer is therefore:

```text
4 / 9 = 0.444444444444...
```

This document compares the measured non-cancelling energy share against that count baseline.

## Exact local split

Let local characters modulo `11` be indexed by exponent `e in {1,...,9}`.

Because `10 = -1 mod 11`, the orbit sum is:

```text
1 + chi(10).
```

Therefore:

```text
chi(10) = -1  =>  1 + chi(10) = 0
chi(10) = +1  =>  1 + chi(10) = 2
```

Odd exponent characters cancel. Even exponent characters do not cancel.

The non-cancelling value is exactly `2`, the orbit size.

## CRT layer split

For:

```text
P = 2310 = 2 * 3 * 5 * 7 * 11,
```

the full character group has size:

```text
phi(2310) = 480.
```

The old `P=210` layer contains:

```text
48 characters.
```

The new `p=11` layer contains:

```text
432 characters.
```

The new layer splits as:

```text
240 cancelling characters      = 48 * 5
192 non-cancelling characters  = 48 * 4
```

The full-nontrivial-count baselines are:

```text
new p=11 layer / all nontrivial characters = 432 / 479 ~= 0.901879
p=11 non-cancelling layer / all nontrivial characters = 192 / 479 ~= 0.400835
p=11 non-cancelling layer / new p=11 layer = 4 / 9 ~= 0.444444
```

## Finite measured values

The diagnostic computes Chebyshev-weighted character energies over Richter windows at depths `K=2,3,4`.

| K | `p11_new / total` | `p11_non / p11_new` | `p11_non / total` |
|---:|---:|---:|---:|
| 2 | `0.938218008866` | `0.444444444444` | `0.416985781718` |
| 3 | `0.961859768615` | `0.462182505791` | `0.444554758078` |
| 4 | `0.967468868352` | `0.483889986895` | `0.468148498029` |

The finite data show that the new `p=11` layer carries most of the `P=2310` nontrivial energy at these depths. Within that new layer, the non-cancelling share begins at the local `4/9` count baseline and rises modestly at `K=3,4`.

## Interpretation

The finite result supports the orbit-classification diagnosis:

```text
p=11 is between inert/degenerate and full-orbit behavior.
```

It has exact local cancellation for the odd-exponent characters and exact constructive orbit sum `2` for the even-exponent characters.

The non-cancelling sublayer carries the packet obstruction associated with the partial orbit.

## Boundary

The local `4/9` baseline is a character-count baseline, not an asymptotic variance law.

The finite measurements are diagnostic only. They do not prove that the variance decomposition respects the local orbit count asymptotically.

A future theorem would need to control how prime-window mass distributes across the `p=11` CRT fibers and across the inherited `P=210` coordinates.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove an asymptotic `p=11` packet share.

This document does not close the square-root barrier.

This document does not claim that local orbit-count baselines determine prime-window energy shares asymptotically.
