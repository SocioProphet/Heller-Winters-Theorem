# Programme Obligations Ledger

Status: live governance document.  
Updated: 2026-05-10.

This ledger tracks work owed before empirical observations or theorem candidates may be promoted.

| ID | Obligation | Status | Evidence | Next action |
|---|---|---:|---|---|
| O-Substrate-1 | Lock canonical notation across all chapters. | open | notation legend still needed | draft canonical notation legend |
| O-Substrate-2 | Complete operator registry normalization. | open | operator registry not fully typed | create operator registry inventory |
| O-Instrumentation-1 | Phase-gate registry lock. | partial | `empirical-claims/phase-gate-null-X1e6/registry.md` v0.1 | independent review of formulas |
| O-Instrumentation-2 | Phase-gate invariant audit. | partial | runner emits rotation-invariance audit | add translation/window audits |
| O-Instrumentation-3 | Alternate-substrate gate. | partial | Cramér and wheel gates implemented | increase replicates and review controls |
| O-Instrumentation-4 | Fixture replay. | partial | fixture result included | independent replay on second machine |
| O-TheoremCandidate-1 | Residual-envelope theorem-candidate formalization. | open | Candidate A still programmatic | isolate residual object and hypotheses |
| O-TheoremCandidate-2 | Uniformity obligation. | open | finite-window only | state exact uniformity theorem needed |
| O-TheoremCandidate-3 | Empirical-to-analytic bridge. | open | no analytic target yet | literature check and target selection |
| O-CrossLane-1 | Cross-track translation requirement. | partial | Candidate C README declares non-claims | enforce in all future artifacts |
| O-CrossLane-2 | Claim taxonomy enforcement. | partial | Candidate C claim ledger added | add CI check for claim class |
| O-Governance-1 | Programme-map consistency. | partial | patch script supplied | run and review patch |
| O-Governance-2 | Replayability compliance. | partial | runner emits JSON receipts | connect to native PFK/Event-IR schema |

## Current blockers

### B-01 — Independent replay

The fixture and `X = 1e6` preliminary results must be replayed outside the originating environment.

### B-02 — Literature status

Candidate C must be checked against uniform distribution and prime-sequence literature before it can be treated as theorem-candidate material.

### B-03 — Negative/ambiguous surrogate result

The registry v0.1 statistic does not currently distinguish primes from the Cramér-Bernoulli surrogate at `B = 16`. This must remain visible and must not be suppressed.

### B-04 — PFK native integration

The receipt emitted here is JSON-compatible with the PFK discipline, but not yet a full Event-IR or ProofArtifact emission.
