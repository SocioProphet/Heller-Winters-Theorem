# Alternate-Substrate Gates

Status: executable definitions for registry v0.1.

This artifact is incomplete unless all alternate-substrate gates execute and report results.

## Gate A — all-integers baseline

Run the identical statistic pipeline on:

```text
I(X) = {2,3,...,X}
```

Purpose: expose whether the phase map is measuring log-coordinate structure common to all integers rather than prime-specific structure.

Expected result: report `T(I(X))`. No uniformity assumption is made.

## Gate B — Cramér-Bernoulli surrogate

For each `n in {2,...,X}`, include `n` independently with probability:

```math
p(n) = \min(1,1/\log n).
```

Purpose: test whether the statistic distinguishes primes from a density-matched random surrogate.

Expected result: report Monte Carlo distribution of `T(S_b)` and empirical p-value:

```math
p_{emp} = \frac{1 + |\{b : T(S_b) \ge T(P(X))\}|}{B + 1}.
```

## Gate C — wheel-compatible count-matched composite surrogate

Let:

```text
C_30(X) = {n <= X : gcd(n,30) = 1 and n is composite}.
```

Sample exactly `|P(X)|` elements from `C_30(X)` without replacement.

Purpose: prevent the apparatus from collapsing wheel-admissibility into primality.

Expected result: report Monte Carlo distribution and empirical p-value against the prime statistic.

## Gate D — replay gate

Rerun the fixture with identical registry, seed, and replicate count.

Purpose: verify deterministic replay.

Expected result: deterministic payload hash matches `results/fixture/pfk_receipt.json`.

## Failure policy

If a gate fails:

- the artifact remains empirical-only,
- promotion halts,
- claim status cannot advance,
- and the failure is recorded in the claim ledger.
