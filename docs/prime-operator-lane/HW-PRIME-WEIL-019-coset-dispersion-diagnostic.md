# HW-PRIME-WEIL-019 — Coset Dispersion Diagnostic

Status: finite diagnostic surface.  
Claim class: method-grade dispersion comparison, not theorem-grade analytic progress.  
Lane: prime/operator lane, coset variance / dispersion-method surface.  
Depends on: `HW-OPEN-014`, `HW-PRIME-WEIL-017`, `HW-PRIME-WEIL-018`.

## Purpose

This document tests the dispersion-method branch of Gate 1.

The goal is to compare the directly measured q=37 between-coset dispersion against the quotient large-sieve candidate scale and the GRH-shaped packet scale.

The result is negative for proof closure: the finite dispersion values are well behaved, and the quotient restriction gives a real improvement over the standard comparison, but the quotient candidate scale remains above the GRH-shaped packet scale at the tested depth. The square-root barrier remains.

## Setup

For q=37:

```text
H_q = <10> subset (Z/qZ)^x,
d_q = ord_37(10) = 3,
I_q = [(Z/37Z)^x : H_q] = 12.
```

The cosets of `H_q` partition the 36 unit residues modulo 37 into 12 cosets of size 3.

For a Richter window `W_K`, define coset mass:

```text
F_K(C) = sum_{p in W_K, p mod q in C} log p.
```

The between-coset dispersion is:

```text
D_between(q,K) = sum_C (F_K(C) - mean_C F_K)^2.
```

This is the same object as `Var_between(q,K)` in `HW-OPEN-014`.

The within-coset variance is:

```text
D_within(q,K) = sum_C sum_{r in C} (M_K(r) - mean_{r in C} M_K)^2.
```

## Finite q=37 measured values

| K | between variance | within variance | between/within |
|---:|---:|---:|---:|
| 2 | `105.168280863028` | `126.326852505157` | `0.832509310392` |
| 3 | `1694.760557860094` | `682.772557394117` | `2.482174392492` |
| 4 | `8623.482855618979` | `13379.773176405680` | `0.644516371236` |
| 5 | `95181.84283496864` | `100520.91659258083` | `0.946885942363` |

The finite values oscillate, consistent with the prime-race behavior seen in the q=37 packet measurement.

## Comparison scales

The diagnostic compares three scales:

1. measured between-coset variance;
2. quotient large-sieve candidate bound;
3. GRH-shaped packet scale.

The quotient large-sieve candidate remains above the GRH-shaped packet scale at the tested depth `K=5` for q=37.

The implemented outcome is therefore:

```text
quotient_improves_but_gap_remains
```

## Falsification criteria

The branch was evaluated against three possible outcomes:

1. If the dispersion bound reached square-root scale, Gate 1 would become live.
2. If the dispersion bound improved the quotient-large-sieve scale by an additional factor, it would be a stronger component but still short of proof unless it reached square-root scale.
3. If the dispersion comparison stayed at the quotient-large-sieve scale, it would not improve Gate 1.

The current diagnostic lands in the third class for the bound surface: it confirms the finite dispersion object and the quotient improvement, but it does not produce a new square-root-scale theorem.

## Conclusion

The dispersion branch is correctly formulated but does not yet close Gate 1.

The next possible analytic refinement is not another raw finite measurement. It would require a theorem that bounds between-coset dispersion below the quotient-large-sieve candidate scale by exploiting arithmetic structure inside the coset indicators.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the Coset Variance Theorem.

This document does not prove a dispersion-method square-root bound.

This document does not prove an unconditional variance bound.

This document does not claim that the finite q=37 measurements imply asymptotic coset equidistribution.

This document does not close the square-root barrier.
