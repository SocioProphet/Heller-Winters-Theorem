# HPHD Lane: Zeta Mirror Lattice

Lane status: RH sub-lane of Heller-Winters-Theorem, absorbed from `SocioProphet/hphd-zeta-mirror-lattice` per `PROVENANCE.md`.

Distance tier: RH-method. See `boundary.md`.

HPHD zeta mirror-lattice, explicit-formula experiments, and BSD-adjacent reproducibility archive for the trivial-zero mirror-lattice thesis.

This lane captures the current HPHD working program on:

- trivial zeta zeros as negative mirror-lattice structure;
- non-trivial zeta zeros as fluctuation spectrum;
- negative mirror lattices for Dirichlet L-functions;
- zeta-regularized density;
- finite-window explicit-formula diagnostics and SPEC gates.

## Current thesis

The trivial zeros of the Riemann zeta function are not conceptually disposable. They are the regular negative-side cancellation lattice of the completed zeta system. The non-trivial zeros form the fluctuation spectrum tied to prime-distribution irregularity. Zeta-regularized negative values are finite analytic shadows of divergent positive density.

The manuscript-safe claim is:

```text
negative domain = mirror lattice + completion correction + regularized density shadow
```

For the base zeta function:

```math
\mathcal M^-_{\zeta}=\{-2n:n\in\mathbb N\}
```

is the canonical HPHD mirror lattice.

## Claim boundary

See `boundary.md` for the canonical lane-boundary statement cross-referenced to Heller-Godel and Heller-Dirac anti-seed.

We may say:

- The trivial zeros form a negative mirror lattice for the completed zeta system.
- The non-trivial zeros form a fluctuation spectrum tied to prime irregularity.
- Zeta regularization assigns finite negative invariants to certain divergent positive densities.
- A density correspondence between trivial and non-trivial zeros requires an explicit embedding, reparameterization, spectral index, or pushforward measure.
- Richter saturation data informs finite-window harness design only.

We must not say, literally:

- The trivial zeros are primes.
- The trivial zeros and non-trivial zeros have the same raw density.
- Divergent series equal their zeta-regularized values as ordinary sums.
- Finite-window explicit-formula diagnostics constitute RH/GRH evidence.

Use typed notation such as:

```math
1+1+1+\cdots \overset{\zeta\text{-reg}}{=} -\frac12
```

not ordinary equality.

## Lane layout

```text
lanes/hphd/
├── PROVENANCE.md                         Absorption record from standalone repo
├── README.md                             This file
├── boundary.md                           Lane-specific claim boundary + anti-seed cross-references
├── 01-negative-mirror-lattice.md         Manuscript-grade synthesis
├── 02-formal-claims.md                   Definitions, lemmas, conjectures, admissible boundaries
├── 03-research-roadmap.md                Research lanes and reproducibility backlog
├── 04-explicit-formula-typing-gate.md    Explicit-formula decomposition + typing gate
└── 05-richter-saturation-spec-v0-2.md    Finite-window Richter saturation SPEC note
```

## Immediate research lanes

1. Define the admissible embedding class `Phi` for comparing the trivial-zero mirror lattice with the non-trivial-zero spectrum.
2. Extend from `zeta(s)` to Dirichlet `L(s, chi)` functions so mirror lattices become character/parity dependent.
3. Build explicit-formula experiments separating main term, non-trivial-zero oscillation, and trivial-zero / completion correction terms. These experiments must comply with PFK PrimeStatsProtocol if they emit descriptive-grade claims.
4. Integrate Richter saturation finite-window diagnostics into HW explicit-formula harness design without treating them as RH evidence.

## Status

Draft lane. This lane is a research-program capture, not a proof of RH, GRH, BSD, an envelope theorem, or a critical-line theorem.

## Relationship to HW core

This lane is an RH-method contribution to Heller-Winters-Theorem. Its content is methodology development and explicit-formula infrastructure; it does not advance HW's submission-track theorem statement commitment.

When HW's main theorem statement is committed, this lane may contribute to the explicit-formula decomposition apparatus.
