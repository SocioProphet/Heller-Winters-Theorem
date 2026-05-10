# Alternate-Substrate Gates

Status: required.

This artifact is incomplete unless all alternate-substrate gates execute successfully.

## Gate A — all integers baseline

Run the identical statistic pipeline on:

```text
{1,2,3,...,X}
```

Expectation:

The statistic should reproduce the baseline predicted by equidistribution behavior under the declared normalization.

## Gate B — density-matched Poisson surrogate

Construct a random sequence with approximately the same density profile as the primes up to `X`.

Expectation:

The pipeline must distinguish the prime sequence from the surrogate if the measured phenomenon is genuinely arithmetic rather than density-driven.

## Gate C — wheel-preserving composite surrogate

Construct a wheel-compatible but intentionally non-prime substrate.

Expectation:

The apparatus should not collapse wheel structure into primality automatically.

## Gate D — replay gate

Independent rerun using identical registry and fixture.

Expectation:

Deterministic replay within declared tolerance.

## Failure policy

If a gate fails:

- the artifact remains empirical-only,
- promotion halts,
- claim status cannot advance.
