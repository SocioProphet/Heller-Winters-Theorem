# Claim Ledger Entry — Candidate C Phase-Gate Null-Model Artifact

Claim ID: `HW-CAND-C-PHASE-GATE-V0.1`  
Claim class: empirical.  
Status: executed fixture; preliminary `X = 1e6` run included.  
Promotion status: blocked.

## Claim text

Under registry `phase-gate-v0.1`, the programme can compute a deterministic finite-window phase-gate statistic for primes and declared alternate substrates, emit replayable results, and produce provenance receipts.

## What is proven

Nothing mathematical beyond correctness of the finite computation as replayed under the supplied code and fixture.

## What is empirical

The measured values of the statistic for:

- primes,
- all integers,
- Cramér-Bernoulli surrogates,
- wheel-compatible count-matched composite surrogates.

## What is not claimed

This artifact does not claim:

- RH,
- GRH,
- prime-zero correspondence,
- residual-envelope control,
- asymptotic convergence,
- or novelty.

## Current v0.1 finding

The v0.1 statistic reports a strong difference between all-integers and primes, and a difference between wheel-compatible composite controls and primes.

It does not currently reject the Cramér-Bernoulli surrogate at `B = 16`. Therefore, the artifact should be treated as an executable negative/ambiguous empirical result against that surrogate, not as a prime-specific distinguishability theorem.

## Literature status

Pending.

Required first references:

- Hlawka (1975) on prime-sequence equidistribution,
- Kuipers–Niederreiter, *Uniform Distribution of Sequences*,
- Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*,
- recent equidistribution surveys.

## Promotion blockers

- independent replay,
- literature review,
- formal statement,
- proof review,
- stronger null-model analysis if a distinguishability claim is desired.
