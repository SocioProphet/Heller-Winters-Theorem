# First Theorem Candidate Workplan

Status: programmatic.

The Heller–Winters Programme does not currently possess a theorem. This document defines the disciplined path toward the first theorem-worthy result.

## Candidate families

### Candidate A — residual-envelope theorem

Target:

A bounded statement involving:

```math
R(x) = \pi(x) - Li(x)
```

or

```math
\psi(x) - x.
```

This is the highest-risk and most RH-adjacent candidate.

### Candidate B — quotient-normalization theorem

Target:

A finite-window normalization or quotient-stability statement with explicit error control.

Lower ambition than Candidate A but more likely to close rigorously.

### Candidate C — phase-gate distinguishability theorem

Target:

A theorem about finite-window distinguishability between primes and declared null models under a locked phase-gate statistic.

This is instrumentation-heavy and must not be inflated into an RH claim.

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
