# Heller–Winters Programme

Canonical repository for the **Heller–Winters Programme**: a research programme in search of theorem-worthy results, not a completed theorem.

## Main thesis

The Heller–Winters construction is a unified variational/functorial framework in which gravitational information bounds, octonionic Hopf geometry, spectral zeta regularization, descent/topos semantics, and information-geometric learning dynamics on connections and boundary kernels are treated as modules of one coherence engine.

The programme's central claim is not that a theorem has already been proved. The central claim is that a foundational description should be organized around **gauge/descent-stable invariants extracted from regularized spectral data**, rather than around pointwise continuum specification alone. The motivation is threefold:

1. gravitational and area-law bounds cap local information density;
2. zeta regularization compresses infinite mode towers into finite spectral invariants;
3. Gödel-type closure failure suggests that a serious foundational theory should aim for constraint-completeness before content-completeness.

That is the repository's main orientation. Prime-distribution, operator-envelope, lattice-counting, and residual-analysis work remain live lanes, but they are now subordinate to the broader Heller–Winters coherence programme rather than the sole headline.

## Umbrella reframing record

The 2026-05-14 reframing is recorded in `CHANGELOG.md` and controlled by `docs/programme-lane-map.md`.

This matters because the repository's semantic posture changed: it is no longer naturally read as only a prime/operator theorem-attempt repository. It is an umbrella programme repository. The old prime/operator interpretation remains historically important, but it is now one lane inside the wider Heller–Winters Programme.

## Programme lanes and dependency policy

The current lane map distinguishes coordination claims from structural claims.

- A **coordination claim** means the lanes share claim discipline, artifact conventions, and compatible variational/functorial vocabulary.
- A **structural claim** means the lanes have been formalized as a coupled mathematical system with declared objects, maps, assumptions, and proof obligations.

The current repository permits the coordination claim. The structural claim remains programme-level unless separately formalized.

The controlled lane inventory is maintained in `docs/programme-lane-map.md`. At present the lanes are:

1. gravitational information bounds;
2. octonionic Hopf geometry;
3. spectral zeta regularization;
4. descent/topos semantics;
5. information-geometric learning dynamics;
6. the subordinate prime/operator lane;
7. `lanes/hphd/` — HPHD zeta mirror-lattice RH-method lane, absorbed from `SocioProphet/hphd-zeta-mirror-lattice`.

## Defensible mathematical spine

The current spine is a structural variational scheme on fibered configuration data, with the octonionic apex as a worked target.

The programme currently treats the following as the load-bearing background:

- the Hopf division-algebra ladder, including the octonionic apex and the caveat that `S^7` is a Moufang loop rather than a Lie group;
- gravitational information bounds, including Bekenstein-type and area-law constraints, as regulators on local information density;
- zeta-regularized determinants and their variational formulae as the spectral channel;
- Dirac-spectrum baselines on round `S^15`, including the Hurwitz-zeta reduction for `log det_zeta D^2`;
- split-octonion para-structure as a two-channel polarization device;
- Čech groupoid and descent/topos semantics for treating fibration data invariantly.

These are background structures, not proprietary claims. The programme's original work begins where these structures are coupled into a single auditable coherence engine.

## Current original architecture

The Heller–Winters construction is organized around six main objects.

1. **Trinitarian Unity object.** A compositional unit of the form `(F -> E -> B; Act_F, Act_E, Act_B; nabla, A_C, partial)`, interpreted as fiber/base/total-space action data equipped with a connection, constraint interface, and boundary map.

2. **Action-commutator time defect.** A defect measuring the gap between an evolved point and the horizontal lift of its projected evolution, minimized over fiber gauge. The binary defect measures short-step failure of functorial transport; the ternary defect measures associativity failure under three-step refinement.

3. **Nonassociative curvature split.** A decomposition of the time defect into ordinary curvature contribution and apex/nonassociative contribution, with the nonassociative term vanishing on associative quaternionic slices. This is the key theorem-candidate lane.

4. **Forward/backward KL irreversibility.** An information-geometric diagnostic comparing forward transition kernels with their reference-adjoint backward kernels.

5. **Boundary-conditioned slice-reset kernel.** A probability kernel on quaternionic slice space, updated by mirror descent against boundary-conditioned gradient data.

6. **Unified coherence objective.** A coupled functional combining time-defect, irreversibility, spectral regularity, boundary coherence, and associator leakage terms. The intended programme is to study descent and falsification properties of this objective under declared admissibility assumptions.

## Claim discipline

The repository must distinguish five classes of claims:

- **Proven:** statements with hypotheses, conclusions, proof obligations, and completed proof or imported classical reference.
- **Definitional:** schemas, operator definitions, conventions, ledgers, and infrastructure.
- **Empirical:** finite-window computations, phase-gate observations, replayable measurements, and statistics.
- **Conjectural:** proposed mathematical statements not yet proved.
- **Programmatic:** research-direction commitments, theorem-candidate roadmaps, scale-limit assumptions, and work still owed.

The phrase **Heller–Winters Theorem** is reserved for future theorem-worthy results only after they are formally stated and proved. The whole body of work is the **Heller–Winters Programme**.

## Claim-ledger scope

The existing executable claim-ledger schema is currently scoped to the prime/operator lane. It is general in style, but not yet programme-wide by declaration.

Until a programme-wide extension lands:

- prime/operator claims use the existing `ClaimLedgerEntry` schema and prime-lane operator registry;
- non-prime lanes may cite that schema as a pattern but not as a complete validator;
- programme-wide claims require either an extension of `ClaimLedgerEntry` or a separate cross-lane ledger schema;
- any cross-lane theorem candidate must declare which lane ledger validates which part of the claim.

## Current theorem-candidate targets

The programme should prioritize theorem candidates that are narrow enough to be proved or falsified.

Primary candidates:

- prove the associator-leakage identity on associative slices;
- make the ternary time-defect invariant under admissible three-step refinements;
- prove a descent or monotonicity statement for the unified coherence objective under explicit smoothness and compactness assumptions;
- compute a closed-form spectral-gradient baseline on round `S^15` or a controlled one-parameter `Spin(8)` connection family;
- construct a falsifier for the boundary-conditioned slice-reset dynamics.

Non-primary or deferred candidates:

- Lorentzian extension beyond compact Riemannian baselines;
- physical-cosmology interpretations of boundary-state preparation;
- number-theoretic zeta analogies beyond formal analogy;
- Standard Model or triality-to-observable-sector identifications.

## Reviewer-facing exposure register

The following issues are not solved and must not be overclaimed:

- the associator residue must be made gauge/refinement invariant before it can serve as a history functional;
- sectorized zeta traces require either a splitting-preserving connection class or a smooth heat-kernel/filter replacement for strict vertical projections;
- Gödel-robust ordering is currently a theorem target, not a theorem, unless supplied with a non-trivial existence result on a declared spacetime class;
- the prime/zeta bridge is presently a structural analogy unless promoted to a precise conjecture with falsifiable content;
- the Lorentzian version is not obtained for free from compact Riemannian heat-kernel methods;
- triality language must remain structural unless a concrete representation-to-sector map and symmetry-breaking pattern are supplied.

## Prime/operator lane

The repository also develops an auditable operator framework for prime-distribution and related arithmetic research. Its current deliverables are methodological and infrastructural: programme maps, typed operator specifications, empirical protocols, claim ledgers, residual/envelope analysis plans, phase-gate instrumentation, quotient-normalization work, Ehrhart/lattice-counting layers, falsification gates, and Proof Fabric Kernel provenance.

The current prime residual manuscript scaffold is captured in `docs/prime-operator-lane/prime-residual-manuscript-scaffold-v0.1.md`. It locks the density/intensity correction `dπ/dx ~ 1/log x` versus `dπ/du ~ e^u/u`, keeps `e^(u/2)` language as an RH-shaped diagnostic only, and defines the manuscript spine for operator ordering, residual channels, harness protocol, claim ledger, figure semantics, and publication voice.

HW-PRIME-WEIL-009 registers the reciprocal dimension-coordinate bridge to `SocioProphet/Heller-Godel`: the HW-PRIME-WEIL-008 circle/hyperbola boundary is paired with the representation-theoretic `dim rho = 1` unit-circle locus in HG-MTH-008.6. This is an analogy of boundary position only; `dim rho` is never equal to the HW off-critical-line parameter delta.

The companion governance artifacts are:

- `docs/prime-operator-lane/operator-registry-v0.1.md` — typed operator registry for coordinate maps, filters, channels, scores, observables, residuals, certificates, controls, and perturbations.
- `docs/prime-operator-lane/claim-ledger-v0.1.md` — claim-class ledger fixing C0/C1/C2/C3/D0/E0 boundaries and canonical claims CL-001 through CL-011.
- `docs/prime-operator-lane/artifact-schema-v0.1.md` — evidence artifact vocabulary for DefinitionArtifact, OperatorArtifact, RunSpec, RunReceipt, traces, figures, proof artifacts, and ledger entries.

This lane remains active, but it is no longer the sole README framing. It is one research substrate inside the larger Heller–Winters coherence programme.

## HPHD zeta mirror-lattice lane

`lanes/hphd/` hosts the absorbed HPHD zeta mirror-lattice RH-method lane. It contains the trivial-zero mirror-lattice thesis, explicit-formula typing gate, and finite-window Richter saturation SPEC note inherited from `SocioProphet/hphd-zeta-mirror-lattice`.

This lane is methodology and explicit-formula infrastructure. It does not prove RH, GRH, BSD, or any asymptotic theorem. The standalone `hphd-zeta-mirror-lattice` repository is retained as provenance and should redirect here after the companion archive PR merges.

## Repository-name note

The GitHub repository may still appear as `Heller-Winters-Theorem` for continuity with earlier work. That repository name is historical and aspirational. The canonical conceptual object is the **Heller–Winters Programme**. The word “theorem” is reserved for future, formally stated and proved results inside the programme.

The intended reading is: this repository houses the Heller–Winters Programme, whose long-range target is to isolate theorem-worthy Heller–Winters results. A future rename to `Heller-Winters-Programme` is a governance option, not a current requirement.

## Cross-repository relationship policy

Other SocioProphet repositories may use Heller methodology without being lanes of this repository.

Default policy: **minimalist unless explicitly promoted.** A repo is not inside the Heller–Winters Programme merely because it shares methodology, vocabulary, or proof discipline.

Candidate repos such as `yang-mills`, `np-program`, `bsd-proof-program`, and `Heller-Godel` must be classified explicitly before they are treated as programme lanes. Relationship classes are defined in `docs/programme-lane-map.md`.

`hphd-zeta-mirror-lattice` is no longer a candidate external relationship: its current documentation lane has been absorbed into `lanes/hphd/`.

## Current canonical documents

- `CHANGELOG.md` — durable record of the 2026-05-14 umbrella reframing and downstream claim-boundary implications.
- `docs/programme-lane-map.md` — programme-control document for lane inventory, dependency graph, claim-ledger scope, naming intent, and cross-repository relationship policy.
- `docs/clay-problem-programme-map.md` — positioning map for RH/GRH-related programmes and the Heller–Winters operator layer.
- `docs/empirical-protocol.md` — required discipline for empirical artifacts, including cross-track translation, null models, basis consistency, alternate-substrate gates, and promotion rules.
- `docs/review-gap-register.md` — gap register produced after review of the current programme state.
- `docs/04-programme-obligations.md` — live obligations ledger for substrate, instrumentation, theorem candidates, and cross-lane governance.
- `docs/first-theorem-candidate-workplan.md` — Phase Wα/Wβ/Wγ workplan for isolating the first theorem-worthy result.
- `docs/prime-operator-lane/prime-residual-manuscript-scaffold-v0.1.md` — current coherent rewrite scaffold for the prime residual-analysis manuscript, including density correction, RH diagnostic boundary, operator taxonomy, harness protocol, claim ledger, figure plan, and rewrite rules.
- `docs/prime-operator-lane/operator-registry-v0.1.md` — typed operator registry for the prime/operator lane.
- `docs/prime-operator-lane/claim-ledger-v0.1.md` — claim ledger and promotion/downgrade rules for prime/operator-lane prose and artifacts.
- `docs/prime-operator-lane/artifact-schema-v0.1.md` — evidence artifact schema for run, trace, figure, proof, and ledger artifacts.
- `lanes/hphd/` — HPHD zeta mirror-lattice RH-method lane, including absorbed docs `01..05`.
- `empirical-claims/phase-gate-null-X1e6/` — Candidate C executable empirical artifact package.
