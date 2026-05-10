# First Theorem Candidate Workplan

Status: programmatic.  
Updated: 2026-05-10.

The Heller–Winters Programme does not currently possess a theorem. This document defines the disciplined path toward the first theorem-worthy result.

## Candidate families

### Candidate A — residual-envelope theorem candidate

Target:

```math
R(x) = \pi(x) - Li(x)
```

or

```math
\psi(x) - x.
```

This is the highest-risk and most RH-adjacent candidate. It remains programmatic.

### Candidate B — quotient-normalization theorem candidate

Target: a finite-window normalization or quotient-stability statement with explicit error control.

This is lower ambition than Candidate A and may be more likely to close rigorously, but it requires Chapters 10–12 to be substantially drafted.

### Candidate C — phase-gate empirical artifact candidate

Target: a finite-window phase-gate artifact comparing primes against declared null and alternate substrates under a locked statistic.

Candidate C is not a theorem yet. It becomes theorem-candidate material only after:

1. the executable artifact is complete,
2. the literature check identifies the exact novelty status,
3. a formal statement is written with hypotheses and conclusion,
4. a proof or bounded finite-window verification argument exists.

## Mandatory progression

No candidate may skip the Wα/Wβ/Wγ sequence.

## Phase Wα — registry lock

Lock:

- operator definitions,
- windows,
- normalization,
- test statistics,
- sampling discipline,
- comparison basis.

Required outputs:

- operator registry,
- notation lock,
- fixture specification,
- provenance schema.

## Phase Wβ — invariant audit

Verify:

- symmetry properties,
- translation equivariance,
- parity behavior,
- normalization stability,
- null-model behavior,
- alternate-substrate trivial-result conditions.

Required outputs:

- invariant audit report,
- residual diagnostics,
- failure cases,
- replay receipts.

## Phase Wγ — fixture regression

Construct explicit low-scale fixtures.

Required outputs:

- exact replay at restricted scale,
- independent replay confirmation,
- deterministic fixture receipts.

No asymptotic language is permitted before Wγ succeeds.

## Candidate C status after registry v0.1

Candidate C has an executable empirical package at:

```text
empirical-claims/phase-gate-null-X1e6/
```

Registry v0.1 produced a useful negative/ambiguous result: the phase-gate statistic does not currently distinguish primes from the Cramér-Bernoulli surrogate at `B = 16`.

That result is not a failure of the programme. It is the empirical protocol doing its job: the first artifact blocks premature theorem promotion.

## Promotion discipline

Progression:

1. empirical observation,
2. replicated empirical observation,
3. bounded finite-window statement,
4. theorem candidate,
5. proof attempt,
6. theorem.

## Explicit non-claim boundary

Finite-window observations are not RH.

Phase-gate distinguishability is not RH.

Residual-envelope heuristics are not RH.

Windowed quotient convergence is not RH.

No repository artifact may claim RH or GRH resolution without a fully formal theorem.
