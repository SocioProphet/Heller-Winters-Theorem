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

This document also records the finite Rodin / `142857` bridge as a mod-9 unit-set identity and the Midy/complementary-pairs digit-sum law. These bridges are arithmetic bookkeeping only. They are not physical torus claims and not evidence for RH/GRH.

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

## Midy / complementary-pairs digit-sum law

For a denominator `n` coprime to `10`, the repetend of `1/n` has period:

```text
ord_n(10).
```

When the period is even and the standard Midy/complementary-pairs condition applies, the repeating block splits into complementary digit pairs whose sums are `9` in base `10`.

For the prime examples used in this lane, the digit-sum law is:

```text
digit_sum(1/p) = 9 * ord_p(10) / 2.
```

Equivalently:

```text
digit_sum(1/p) = (9/2) * period.
```

This is a digit-repetend identity. It is not an analytic prime-distribution theorem.

### Digit-sum sequence

| Fraction | `10 mod n` / period data | Period | Digit sum | Structure |
|---|---|---:|---:|---|
| `1/9` | `10 == 1 mod 9` | 1 | `1 = 9^0` | fixed identity digit |
| `1/10` | `10 == 0 mod 10` | terminates | — | base reset / terminating case |
| `1/11` | `10 == -1 mod 11` | 2 | `9 = 9^1` | first nontrivial complementary pair |
| `1/13` | `ord_13(10)=6` | 6 | `27 = 3*9` | three complementary pairs |
| `1/17` | `ord_17(10)=16` | 16 | `72 = 8*9` | eight complementary pairs |
| `1/19` | `ord_19(10)=18` | 18 | `81 = 9^2` | nine complementary pairs |

The `1/19` case has digit sum `81` because the period contains exactly nine complementary pairs, and each pair sums to `9`.

This is the precise finite arithmetic meaning of the phrase “two complete Rodin circles” in the informal discussion: the period length is `18`, so the number of complementary pairs is `9`, the mod-9/Rodin modulus.

## Rodin / 142857 bridge

This section records a finite mod-9 bridge. It is included because it explains why the digit string `142857`, the Rodin doubling cycle, and the current mod-7 variance dominance are the same small cyclic arithmetic surface seen through different coordinatizations.

The active unit set modulo `9` is:

```text
(Z/9Z)^x = {1,2,4,5,7,8} ~= Z_6.
```

The nonunit axis is:

```text
{3,6,9}.
```

The Rodin doubling orbit is:

```text
1 -> 2 -> 4 -> 8 -> 7 -> 5 -> 1.
```

The repeating decimal digits of `1/7` are:

```text
142857.
```

As a set:

```text
{digits of 1/7} = {1,2,4,5,7,8} = (Z/9Z)^x.
```

Thus the Rodin cycle and the `1/7` digit cycle use the same six active mod-9 units, though with different orderings. The Rodin sequence is the orbit of generator `2` modulo `9`; the decimal expansion of `1/7` comes from the long-division map attached to the base-10 orbit modulo `7`.

The precise identity is set-level and group-level:

```text
(Z/9Z)^x ~= (Z/7Z)^x ~= Z_6.
```

It is not a claim that the digit string itself is the same ordered orbit as powers of `10` modulo `7` without the long-division quotient map.

## Active/inert split

The Rodin active/inert split matches the base-10 orbit classification at the first primorial level:

| Surface | Active object | Inert / excluded object | Reason |
|---|---|---|---|
| Rodin mod 9 | `{1,2,4,5,7,8}` | `{3,6,9}` | units vs nonunits modulo `9` |
| digits of `1/7` | `{1,2,4,5,7,8}` | `{3,6,9}` | same mod-9 unit set as digit alphabet |
| `P=210` character packet | mod-7 full-orbit packet | mod-2, mod-3, mod-5 degenerate/terminating packet | `2,5 | 10`; `3` has `ord_3(10)=1`; `7` has full orbit |

In the current variance diagnostics, the mod-7 packet dominates because it is the first small-prime component with full base-10 multiplicative orbit.

This is a finite structural explanation for the observed dominance. It is not an asymptotic theorem.

## Fraction bridge

| Fraction | Period | Orbit type | Rodin analogue |
|---|---:|---|---|
| `1/9` | 1 | fixed digit `1` in a base-divisor denominator | `9 -> 9` fixed-axis picture |
| `1/3` | 1 | degenerate digit repetition | `3,6` axis / nonunit surface |
| `1/11` | 2 | partial orbit `{10,1}` modulo `11` | between active and inert |
| `1/7` | 6 | full orbit modulo `7` | active six-node unit circuit |
| `1/19` | 18 | full orbit modulo `19` | full Artin-prime circuit; digit sum `9^2` |

This table is finite arithmetic bookkeeping. It does not create a proof of any analytic statement about prime distribution.

## Character sums and digit sums

The Midy/complementary-pairs law and the finite character-cancellation law are dual finite descriptions of the same orbit structure.

The digit-sum law says that the repetend is balanced around the base-10 midpoint when the period splits into complementary pairs.

The character-sum law says that the finite Fourier transform over a complete multiplicative orbit cancels for every nontrivial character.

The analytic prime-window problem is harder: `psi_{W_K}(chi)` sums characters over primes in a value window, not over a deterministic full digit cycle. Therefore the digit-sum identity explains the finite orbit geometry but does not by itself bound prime-window character sums.

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

This document does not claim Rodin-coil geometry, torus winding, or digital-root numerology proves any analytic number theory result.

This document does not claim the Midy digit-sum law proves any analytic number theory result.

This document does not close the square-root barrier identified in `HW-PRIME-WEIL-005`.