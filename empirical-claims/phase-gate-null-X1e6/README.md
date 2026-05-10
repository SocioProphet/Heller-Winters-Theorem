# Candidate C: Phase-Gate Null-Model Artifact at X = 1e6

Status: executable empirical artifact package.  
Claim class: empirical.  
Registry version: `phase-gate-v0.1`.  
Programme role: first Heller–Winters Programme output conforming to the Empirical Protocol.

## Purpose

This artifact executes Candidate C: a finite-window phase-gate experiment over primes up to `X = 1e6`, compared against declared alternate substrates.

The artifact is not a proof of RH, GRH, an asymptotic residual bound, or a prime number theorem refinement. It is a finite-window empirical artifact designed to verify that the programme can produce a complete, replayable, claim-classified output.

## §0 Cross-track translation

### What this artifact demonstrates

It tests a locked phase-gate statistic against four sequence families:

1. primes up to `X`,
2. all integers from `2` to `X`,
3. Cramér-Bernoulli density surrogate,
4. wheel-compatible composite surrogate.

### What this artifact does not claim

It does not claim:

- RH,
- GRH,
- an asymptotic theorem,
- a residual-envelope result,
- a zero-location result,
- or a theorem about all primes.

### Where it sits relative to the theorem track

Candidate C is an empirical artifact candidate. It may become theorem-candidate material only after literature review, independent replay, and a formal statement with proof obligations.

## Locked statistic

For each integer `n >= 2` and frequency `omega`:

```math
\theta_\omega(n) = \operatorname{frac}\left(\frac{\omega \log n}{2\pi}\right)
```

with

```text
Omega = {1, 2, 3, 5, 8}
```

The primary statistic is:

```math
T(S) = \max_{\omega \in \Omega}\sqrt{|S|}\,V_\omega(S)
```

where `V_omega(S)` is the one-sample Kuiper statistic against Uniform[0,1).

## Package contents

- `registry.md` — Phase Wα locked definitions.
- `fixture-spec.md` — Phase Wγ fixture specification and expected deterministic value.
- `null-gates.md` — alternate-substrate gates.
- `claim-ledger-entry.md` — claim classification and promotion status.
- `pfk-receipt-template.json` — provenance receipt schema for this artifact.
- `run-plan.md` — execution and replay plan.
- `results/fixture/` — deterministic fixture result at `X=10_000`.
- `results/X1e6-preliminary/` — preliminary finite-window run at `X=1_000_000`.

## Current empirical status

The fixture at `X = 10_000` replays deterministically.

The preliminary `X = 1_000_000` result does **not** distinguish primes from the Cramér-Bernoulli surrogate under registry v0.1 at `B = 16` replicates. This is a protocol-relevant negative/ambiguous result and blocks promotion.

## Acceptance criteria

The artifact is complete at the empirical-artifact level when:

1. Phase Wα registry is locked.
2. Phase Wβ invariant audit is executed.
3. Phase Wγ fixture replay succeeds.
4. Alternate-substrate gates are executed.
5. Results are emitted with provenance receipts.
6. Claim status is updated without inflation.

Promotion beyond empirical status requires:

1. independent replay,
2. literature review,
3. larger Monte Carlo controls,
4. native PFK/Event-IR emission,
5. formal theorem-candidate statement if novelty exists.
