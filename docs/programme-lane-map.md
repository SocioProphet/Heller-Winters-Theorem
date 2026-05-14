# Heller–Winters Programme Lane Map

Status: programme-control document.

This document records the lane structure implied by the umbrella README reframing. It distinguishes coordination claims from structural claims and prevents the phrase "one coherence engine" from silently inflating into an unstated theorem.

## 1. Programme posture

The Heller–Winters Programme is an umbrella research programme. It is not a completed theorem.

The umbrella currently has five named programme lanes plus one subordinate prime/operator lane. The five named lanes are not automatically theorem-track. Each lane must carry its own maturity level, load-bearing prerequisites, and non-claims.

The phrase **one coherence engine** is used in two senses:

- **Coordination claim:** the lanes are governed by common claim discipline, shared artifact conventions, and compatible variational/functorial vocabulary.
- **Structural claim:** the lanes form a genuinely coupled mathematical system whose objects and maps compose into one framework.

The current README permits the coordination claim. The structural claim remains programme-level unless separately formalized through definitions, hypotheses, and theorem-candidate obligations.

## 2. Lane inventory

| Lane | Current role | Maturity | Load-bearing prerequisites | Non-claims |
| --- | --- | --- | --- | --- |
| Gravitational information bounds | Regulator on local information density and motivation for invariant/compressed descriptions. | Structural motivation. | Bekenstein-type bounds, area-law interpretation, declared bounded-region setup. | Does not prove a cosmological model; does not identify the universe with any specific white-hole or boundary-state construction. |
| Octonionic Hopf geometry | Apex geometry and nonassociative obstruction source. | Structural/theorem-candidate substrate. | Hopf division-algebra ladder, `S^7` Moufang-loop caveat, `Spin(8)`/triality convention discipline, associative-slice gate. | Does not identify triality sectors with observable physics without a representation-to-sector map. |
| Spectral zeta regularization | Spectral invariant channel and determinant-gradient source. | Mathematical baseline plus theorem-candidate channel. | Positive elliptic baseline or declared regulator, zeta determinant convention, trace-class/regularization assumptions. | Does not automatically transfer to Lorentzian geometry; does not prove a Riemann-zeta bridge. |
| Descent/topos semantics | Gauge/descent-stable language for fibered data. | Definitional/structural. | Čech groupoid, descent equivalence, declared fibration/groupoid objects. | Does not by itself prove physical invariance or existence of functorial lifts. |
| Information-geometric learning dynamics | Variational update layer on connections and boundary-conditioned kernels. | Structural/computational diagnostic target. | Transition kernels, reference-adjoint backward kernel, Fisher/Dirichlet/entropy regularizer, mirror-descent assumptions. | Does not supply empirical falsification without executable kernels and declared observables. |
| Prime/operator lane | Arithmetic/operator research substrate now subordinate to the umbrella. | Active infrastructure and empirical/theorem-candidate work. | Operator registry, claim ledger, run receipts, residual channels, harness protocol. | Does not define the whole Heller–Winters Programme; does not turn RH-shaped residual diagnostics into RH claims. |

## 3. Dependency graph

Current working dependency graph:

```text
Gravitational information bounds
    -> require compressed/invariant observables
    -> motivates spectral zeta regularization and descent-stable data

Octonionic Hopf geometry
    -> supplies apex fiber geometry and associator obstruction
    -> feeds action-commutator and ternary time-defect lanes

Spectral zeta regularization
    -> supplies regularized determinant and spectral-current channel
    -> feeds unified coherence objective

Descent/topos semantics
    -> supplies gauge/descent-stable packaging for fibered configuration data
    -> constrains how invariants are allowed to be transported or compared

Information-geometric learning dynamics
    -> consumes boundary, spectral, and defect signals
    -> updates connections and slice-reset kernels under declared variational rules

Prime/operator lane
    -> remains a subordinate arithmetic substrate
    -> shares claim-ledger and operator-governance discipline where applicable
```

Interpretation: the umbrella is currently both a coordination structure and a structural thesis-in-progress. It becomes a theorem programme only when the dependency arrows are replaced by formal maps, assumptions, and proof obligations.

## 4. Claim-ledger scope

The existing executable claim-ledger schema is currently scoped to the prime/operator lane. It is general in style, but not yet programme-wide by declaration.

Until a programme-wide extension lands:

- prime/operator claims use the existing `ClaimLedgerEntry` schema and prime-lane operator registry;
- non-prime lanes may cite the schema as a pattern but not as a complete validator;
- programme-wide claims require either an extension of `ClaimLedgerEntry` or a separate cross-lane ledger schema;
- any cross-lane theorem candidate must declare which lane ledger validates which part of the claim.

Required future extension points:

- lane identifier;
- artifact classes for geometric, spectral, descent/topos, and information-geometric objects;
- cross-lane dependency references;
- theorem-candidate status independent of prime/operator C0–C3/D0/E0 boundaries where needed;
- reviewer-facing non-claim box per lane.

## 5. Repository naming intent

`Heller-Winters-Theorem` is historical and aspirational.

The name is retained for continuity. The repository does not claim that a Heller–Winters Theorem has been proved. The intended reading is:

> This repository houses the Heller–Winters Programme, whose long-range target is to isolate theorem-worthy Heller–Winters results.

A future rename to `Heller-Winters-Programme` remains a governance option, not a current requirement.

## 6. Cross-repository relationship policy

Other SocioProphet repositories may use Heller methodology without being lanes of this repository.

Default policy: **minimalist unless explicitly promoted.** A repo is not inside the Heller–Winters Programme merely because it shares methodology, vocabulary, or proof discipline.

Relationship classes:

| Class | Meaning |
| --- | --- |
| Methodology-sharing | Uses Heller-style claim discipline, ledgers, gates, or theorem-candidate process, but remains independent. |
| Externally housed lane | A repo is formally declared as a lane of the Heller–Winters Programme and carries a lane map back to this repository. |
| Dependent theorem-candidate repo | A repo contains proof artifacts that are load-bearing for a theorem candidate in this programme. |
| Independent programme | Shares concepts or ancestry but does not participate in the umbrella. |

Candidate repos such as `yang-mills`, `np-program`, `bsd-proof-program`, `Heller-Godel`, and `hphd-zeta-mirror-lattice` must be classified explicitly before they are treated as programme lanes.

## 7. Immediate follow-up obligations

1. Add one scoping document per non-prime lane, or explicitly mark the lane as "README-scoped only" until such a document exists.
2. Decide whether `ClaimLedgerEntry` becomes programme-wide or remains prime/operator-lane infrastructure.
3. Add cross-repository relationship declarations only after repo-specific review.
4. Keep theorem language reserved for formal statements with declared assumptions, proof obligations, and validation artifacts.
