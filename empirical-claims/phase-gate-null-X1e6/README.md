# Candidate C: Phase-Gate Null-Model Artifact at X = 1e6

Status: scaffolded empirical artifact.  
Claim class: empirical until proved otherwise.  
Programme role: first complete Heller–Winters Programme output conforming to the Empirical Protocol.

## Purpose

This artifact executes Candidate C end-to-end: a phase-gate distinguishability experiment over primes up to `X = 1e6`, compared against declared alternate substrates.

The artifact is not a proof of RH, GRH, an asymptotic residual bound, or a prime number theorem refinement. It is a finite-window empirical artifact designed to verify that the programme can produce a complete, replayable, claim-classified output.

## §0 Cross-track translation

### What this artifact demonstrates

It tests whether a locked phase-gate statistic distinguishes the prime sequence up to `X = 1e6` from declared null and alternate substrates under the same basis, window, normalization, and circular-distance convention.

### What this artifact does not claim

It does not claim:

- RH,
- GRH,
- an asymptotic theorem,
- a residual-envelope result,
- a zero-location result,
- or a theorem about all primes.

### Where it sits relative to the theorem track

Candidate C is an instrumentation theorem-candidate track. It is downstream of operator-registry discipline and upstream of any residual-envelope or RH-adjacent claim.

## Required package contents

- `registry.md` — Phase Wα locked definitions.
- `fixture-spec.md` — Phase Wγ small-scale fixture.
- `null-gates.md` — alternate-substrate gates.
- `claim-ledger-entry.md` — claim classification and promotion status.
- `pfk-receipt-template.json` — provenance receipt schema for this artifact.
- `run-plan.md` — execution and replay plan.

## Acceptance criteria

The artifact is complete only when:

1. Phase Wα registry is locked.
2. Phase Wβ invariant audit is executed.
3. Phase Wγ fixture replay succeeds.
4. Alternate-substrate gates are executed.
5. Results are emitted with provenance receipts.
6. Claim status is updated without inflation.

## Immediate implementation target

Implement a deterministic script that computes the locked statistic for:

- primes up to `1e6`,
- all integers up to `1e6`,
- a density-matched Poisson-thinned surrogate,
- and one wheel-preserving non-prime control.

All outputs must be compared only in the common declared basis.
