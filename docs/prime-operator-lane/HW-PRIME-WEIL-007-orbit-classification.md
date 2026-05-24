# HW-PRIME-WEIL-007 — Base-10 Orbit Classification

Status: finite arithmetic theorem surface and Artin-prime transition map.  
Claim class: theorem-grade for orbit classification and finite Fourier cancellation; method-grade for variance-route interpretation.  
Lane: prime/operator lane, Richter-window / digit-cycle / equidistribution surface.  
Depends on: `HW-PRIME-WEIL-006`, `HW-OPEN-009`.

## Purpose

This document classifies primes by the multiplicative orbit of base `10` modulo `p` and records the resulting finite Fourier cancellation law.

The key finite theorem is simple:

```text
For H = <10> subset (Z/pZ)^x,
sum_{h in H} chi(h) = 0 unless chi is trivial on H.
```

Complete cancellation for every nontrivial character occurs exactly when `10` is a primitive root modulo `p`.

This document does not prove RH, GRH, Artin's conjecture, or an unconditional variance bound.

## Category 0 — Terminating primes

Primes:

```text
p | 10
```

In base 10 this means:

```text
p = 2 or p = 5.
```

The decimal expansion terminates. The multiplicative orbit of `10` modulo `p` is not defined in `(Z/pZ)^x` because `10` is not a unit.

There is no repeating orbit and no multiplicative character cancellation from the base-10 digit cycle.

## Category 1 — Degenerate orbit

Primes:

```text
p != 2,5 and 10 == 1 mod p.
```

For prime `p`, this means:

```text
p = 3.
```

The order is:

```text
ord_p(10) = 1.
```

The orbit is:

```text
<10> = {1}.
```

For any character `chi`, the orbit sum is:

```text
sum_{h in <10>} chi(h) = chi(1) = 1.
```

Thus no nontrivial multiplicative Fourier cancellation occurs.

This is the additive single-digit repetition case, not a multiplicative cycle case.

## Category 2 — Partial orbit

Primes:

```text
p != 2,5 and 1 < ord_p(10) < p-1.
```

Here `10` is a unit but not a primitive root. The orbit:

```text
H = <10>
```

is a proper subgroup of `(Z/pZ)^x`.

For any character `chi` of `(Z/pZ)^x`:

```text
sum_{h in H} chi(h) = 0
```

unless `chi` is trivial on `H`.

Thus only the characters nontrivial on `H` cancel over the digit cycle. Characters whose kernels contain `H` do not cancel.

### Example: p = 11

For `p=11`:

```text
ord_11(10) = 2,
<10> = {10, 1}.
```

The unit group has order `10`. There are `9` nontrivial characters. Exactly `5` nontrivial characters cancel on the length-2 orbit, and `4` do not.

This explains why partial-orbit primes provide incomplete Fourier cancellation.

## Category 3 — Full orbit / Artin primes for base 10

Primes:

```text
ord_p(10) = p-1.
```

Equivalently, `10` is a primitive root modulo `p`.

Then:

```text
<10> = (Z/pZ)^x.
```

Therefore for every nontrivial character:

```text
sum_{j=0}^{p-2} chi(10^j) = sum_{a in (Z/pZ)^x} chi(a) = 0.
```

This is complete finite Fourier cancellation over the digit cycle.

Examples below `100`:

```text
7, 17, 19, 23, 29, 47, 59, 61, 97
```

These are base-10 Artin-prime examples: primes for which `10` is a primitive root.

## Bridge table

| Prime type | Condition | Orbit | Cancellation |
|---|---|---|---|
| terminating | `p | 10` | none in unit group | none |
| degenerate | `ord_p(10)=1` | `{1}` | none |
| partial | `1 < ord_p(10) < p-1` | proper subgroup | only characters nontrivial on `<10>` cancel |
| full | `ord_p(10)=p-1` | full unit group | every nontrivial character cancels |

## Exact cancellation theorem

Let `p` be an odd prime with `p notin {2,5}` and let:

```text
H = <10> subset (Z/pZ)^x.
```

For a character `chi` of `(Z/pZ)^x`:

```text
S_H(chi) := sum_{h in H} chi(h).
```

Then:

```text
S_H(chi) = |H| if chi|_H is trivial,
S_H(chi) = 0 otherwise.
```

Proof: this is the standard character orthogonality relation on the finite subgroup `H`.

Corollary: all nontrivial characters cancel over the base-10 orbit iff `H=(Z/pZ)^x`, i.e. iff `10` is a primitive root modulo `p`.

## Resonant-depth oracle surface

For Category 3 primes, the digit-cycle Fourier sum is exactly zero over a complete period:

```text
sum_{j=0}^{p-2} chi(10^j) = 0.
```

This supplies a finite digit-cycle oracle at resonant period:

```text
ell = p-1.
```

In an idealized sample ordered by full digit cycles, complete cycles cancel and only the incomplete terminal cycle contributes. The residual is bounded by the period length times the relevant logarithmic weight scale.

Important boundary: actual Richter-window prime sums are ordered by prime occurrence in a value interval, not by deterministic traversal of the digit cycle `10^j mod p`. Therefore the complete-cycle cancellation does not by itself give an unconditional all-prime-window bound.

To transfer the digit-cycle oracle into actual `psi_{W_K}(chi_p)` bounds, one must prove a distribution statement controlling how primes populate the digit-cycle compartments inside Richter windows.

That transition is recorded as `HW-OPEN-010`.

## Artin connection

Artin's primitive root conjecture predicts that, for integers such as `10` satisfying the usual local exclusions, there are infinitely many primes `p` for which `10` is a primitive root modulo `p`, with positive density.

Hooley proved Artin's conjecture conditionally on GRH for suitable Dedekind zeta functions.

Within this lane, the relevant finite consequence is:

```text
Artin primes for base 10 are exactly Category 3 primes.
```

At those primes, the base-10 digit cycle has full multiplicative orbit and complete nontrivial-character cancellation over the orbit.

This creates a candidate tower of resonant finite cancellation anchors.

## Why p=7 dominates current variance diagnostics

For `G_210`, the CRT factorization includes mod `7` as the first nontrivial base-10 full-orbit component in the current small-prime modulus.

The observed finite diagnostics show that the mod-7 character packet accounts for most of the nontrivial character energy at small Richter depths.

This is consistent with the orbit classification:

- `2` and `5` terminate;
- `3` is degenerate;
- `7` is the first full-orbit component.

This is finite evidence and structural diagnosis, not an asymptotic theorem.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove that there are infinitely many Category 3 primes.

This document does not prove an unconditional bound for `psi_{W_K}(chi_p)` for actual prime windows at all resonant depths.

This document does not prove the finite-to-asymptotic transition from digit-cycle cancellation to prime-window variance cancellation.

This document does not close the square-root barrier identified in `HW-PRIME-WEIL-005`.
