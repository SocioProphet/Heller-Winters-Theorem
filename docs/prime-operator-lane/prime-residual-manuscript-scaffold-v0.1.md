# Prime Residual Manuscript Scaffold v0.1

Status: draft scaffold for the Heller–Winters Programme prime/operator lane.

This document captures the current coherent rewrite spine for the prime residual-analysis manuscript. It is not a theorem claim. It is a publication-control scaffold: definitions, operator ordering, residual discipline, harness protocol, claim ledger, figure semantics, and prose rules.

## Locked editorial correction

The manuscript must preserve the distinction between value-coordinate density and log-coordinate intensity.

Ordinary prime density with respect to the value coordinate x is

```text
dπ/dx ~ 1/log x.
```

Let

```text
u = log x,    x = e^u,    dx = e^u du.
```

Then expected prime intensity per unit log-coordinate is

```text
dπ/du ~ e^u/u.
```

The expression 1/u is the value-coordinate density after substituting u = log x. It is not the expected prime mass per unit u. The log-coordinate intensity includes the Jacobian factor e^u.

This correction is load-bearing. Confusing these two objects is an immediate reviewer-rejection failure mode.

## RH boundary

The e^(u/2) envelope may be used only as a conditional RH-shaped diagnostic. It is not a proof claim, not a zero-location claim, and not theorem-level evidence.

Permitted language:

- RH-shaped diagnostic envelope.
- Conditional square-root-scale comparison.
- Consistent with an e^(u/2)-type finite-domain envelope under a declared observable and normalization.

Prohibited language:

- RH proof.
- RH verification.
- Critical-line confirmation.
- Residuals prove square-root cancellation.
- The framework locates zeta zeros.

## Section 1 — Introduction and historical arc

The introduction should frame primes as locally discrete multiplicative atoms with global statistical structure. The manuscript begins from the classical lineage: Euclid, Eratosthenes, Gauss/Legendre, Dirichlet, Chebyshev, Riemann, the Prime Number Theorem, Brun, Selberg/Erdős, Green–Tao, Zhang/Maynard, and AKS.

The paper’s role is not to replace this lineage. It inherits its constraints:

- Euclid supplies irreducibility and arithmetic openness.
- Eratosthenes supplies the filter-first model.
- Gauss/Legendre/PNT supply logarithmic mean-field discipline.
- Dirichlet supplies residue-class structure.
- Chebyshev supplies weighted prime-mass observables.
- Riemann supplies spectral residual framing.
- Brun/Selberg supply sieve discipline.
- Green–Tao and Zhang/Maynard show that constrained configurations can reveal deep structure.
- AKS distinguishes primality certification from prime localization.

The introduction must state the paper’s claim boundary: the framework defines a disciplined, replayable method for prime-candidate localization and residual diagnostics. It does not claim a proof of RH, a next-prime formula, or a replacement for primality certification.

## Section 2 — Formal definitions and operator ordering

The paper fixes x as the value coordinate and u = log x as the log coordinate. A log-window W = [u0,u1] corresponds to the value-window I(W) = [e^u0, e^u1]. Equal log-width windows are multiplicative windows in value space.

Candidate sets are built first:

```text
C0(W) = integers n with e^u0 <= n <= e^u1 and n >= 2.
```

Filtered candidate sets are built by applying hard filters in declared order:

```text
Ck(W) = Fk o F(k-1) o ... o F1(C0(W)).
```

The ordering is part of the run. Two runs using the same filters in different orders are not identical unless the relevant filters are proved or recorded to commute on the candidate set.

A hard filter is a deterministic map F with F(S) subset S. It removes candidates. It does not assign evidence, phase scores, or proof labels.

Soft scores rank or stratify candidates but do not certify primality.

Canonical pipeline:

```text
C0(W)
  -> hard filters
  -> Ck(W)
  -> channel assignment
  -> soft scores
  -> observables
  -> mean subtraction
  -> normalization
  -> certificate
  -> claim ledger
```

Ground-truth primality labels must not tune filters in a run later described as predictive.

## Section 3 — Mean fields, residual channels, and normalization

A residual is meaningful only after the observable, coordinate, window schedule, mean field, normalization, and claim class are declared.

For count observables, the default Li-based log-window mean is

```text
Mπ(W) = Li(e^u1) - Li(e^u0).
```

Observed count:

```text
Nπ(W) = #{p prime : e^u0 <= p <= e^u1}.
```

Raw count residual:

```text
Rπ(W) = Nπ(W) - Mπ(W).
```

Normalized count residual:

```text
Rhatπ(W) = Rπ(W) / Normπ(W).
```

Permitted normalizations include square-root mass normalization, RH-shaped diagnostic normalization, and empirical variance normalization, but the run must declare which is used.

For Chebyshev-weighted observables:

```text
ψ(x) = sum_{n <= x} Λ(n)
Ψ(W) = ψ(e^u1) - ψ(e^u0)
Mψ(W) = e^u1 - e^u0
Rψ(W) = Ψ(W) - Mψ(W)
```

π-residuals and ψ-residuals answer different questions and cannot be silently interchanged.

Residue-channel residuals split the observable into admissible congruence compartments. For a mod M:

```text
N_{a,M}(W) = #{p in I(W) : p = a mod M}
M_{a,M}(W) = Mπ(W) / φ(M)
R_{a,M}(W) = N_{a,M}(W) - M_{a,M}(W)
```

Small-prime boundary handling must be recorded.

Shell residuals measure divisibility pressure and candidate survival across declared divisor-space bands. Shells are compartments of divisibility pressure, not physical fields and not proof objects.

Identity channels are deterministic projections such as residue class, wheel sector, shell status, or certificate status. They must be replayable and must not be defined by the later-stage claim target.

Harmonic and log-periodic channels are allowed only with strict overfitting controls. Frequencies chosen after looking at the data are fitted parameters and cannot support predictive claims without held-out validation.

## Section 4 — Operator taxonomy and execution semantics

Every operation in the manuscript must be typed. Operator classes:

1. Coordinate operators: change representation, such as x -> u = log x, and must declare the object being transformed.
2. Candidate operators: construct initial integer domains and endpoint conventions.
3. Hard filters: remove candidates by deterministic arithmetic law.
4. Channel operators: assign deterministic labels to candidates, windows, observables, residuals, or certificates.
5. Scoring operators: assign non-certifying numerical values.
6. Observable operators: measure counts, Chebyshev mass, channel counts, survival counts, or score summaries.
7. Residual operators: subtract a declared mean field and apply a declared normalization.
8. Certificate operators: emit replayable artifacts with hashes, parameters, implementation metadata, and claim class.

Execution modes:

- Exploratory: post-hoc inspection and hypothesis generation; not evidential.
- Training: tuning on labeled data; requires held-out validation for predictive language.
- Validation: fixed pipeline evaluated against ground truth; can support C1 claims.
- Replay: rerun of prior certified experiment.
- Perturbation: controlled changes to schedules, baselines, moduli, channels, or implementations; can support C2 claims.
- Proof: mathematical proof independent of finite computation; required for C3 claims.

Leakage failures to prohibit:

- Label leakage.
- Baseline leakage.
- Schedule leakage.
- Channel leakage.
- Figure leakage.

All operators should have registry entries with name, class, domain, codomain, parameters, deterministic status, ground-truth dependence, permitted modes, certificate fields, and maximum claim class.

## Section 5 — Harness protocol and falsification tests

The harness is part of the scientific object. A residual pattern is meaningful only if the protocol that produced it can be repeated, perturbed, and falsified.

Harness object fields:

- run identifier;
- execution mode;
- coordinate convention;
- window schedule;
- candidate construction rule;
- ordered hard-filter list;
- channel definitions;
- score definitions;
- observable definitions;
- mean-field definitions;
- normalization rules;
- ground-truth source if any;
- random seed or deterministic-seed statement;
- implementation hash;
- input-data hash;
- output-artifact hash;
- claim class;
- falsification criteria.

Required perturbation tests for C2 eligibility:

1. Window-shift test.
2. Scale-dilation test.
3. Residue-split test.
4. Baseline-swap test.
5. Schedule-incompatibility test.
6. Implementation-replay test.

Required negative controls for nontrivial residual or scoring claims:

- shuffled-prime control;
- Cramér-style random model control;
- residue-preserving shuffle;
- composite-survivor control;
- schedule-null control.

Positive controls:

- residue-equidistribution sanity check;
- Chebyshev-main-term sanity check;
- known-modulus artifact test;
- known-composite test;
- small-window exact-count test.

A C2 claim must specify which perturbation tests and controls it survived. Failure under controls must downgrade the claim.

## Section 6 — Claim ledger and evidence registry

The manuscript uses claim classes:

- C0: definitional or formal.
- C1: certified finite empirical.
- C2: reproducible empirical structure.
- C3: theorem-level.
- E0: exploratory, not evidential.
- D0: diagnostic comparison, such as RH-shaped envelope language.

Canonical claim entries:

CL-001. Ordinary prime density in value coordinate is asymptotically 1/log x.

CL-002. Under u = log x, the value measure transforms by dx = e^u du.

CL-003. Expected prime mass per unit log-coordinate is e^u/u at leading order.

CL-004. A log-window W = [u0,u1] has Li-based mean mass Li(e^u1) - Li(e^u0) when that mean field is declared.

CL-005. Hard filters precede soft scores in the canonical pipeline.

CL-006. A soft score does not certify primality.

CL-007. Residual channels are measurable compartments, not ontological fields.

CL-008. RH-shaped means consistent with a conditional square-root-scale diagnostic under a declared observable and normalization.

CL-009. A certified finite run supports at most C1 unless perturbation and replay tests are passed.

CL-010. A pattern that survives declared perturbations and controls is eligible for C2 status.

CL-011. SourceOS/SocioProphet artifacts support implementation, replay, attestation, and certificate governance. They do not provide mathematical proof unless the artifact is a formal proof object or verified computation under declared rules.

Evidence artifact types:

- DefinitionArtifact;
- OperatorArtifact;
- RunSpec;
- RunReceipt;
- CandidateTrace;
- ChannelTrace;
- ScoreTrace;
- ObservableTrace;
- ResidualTrace;
- ControlTrace;
- PerturbationTrace;
- FigureArtifact;
- ProofArtifact;
- ClaimLedgerEntry.

Prohibited promotions:

- plot -> evidence without artifacts;
- finite run -> asymptotic law;
- residual envelope -> RH proof;
- score -> certificate;
- channel -> ontology;
- implementation ledger -> mathematical proof;
- post-hoc parameter -> prior structure.

## Section 7 — Figure plan and visualization semantics

Figure classes:

- F0: schematic, no empirical claim.
- F1: certified finite-result figure, supports C1.
- F2: perturbation/replay figure, can support C2.
- F3: theorem-support figure, illustrative only unless proof exists.

Planned figures:

1. Coordinate and measure distinction: x-density versus u-intensity.
2. Canonical operator pipeline and leakage barrier.
3. Mean-field and residual decomposition.
4. Residue-channel split.
5. Shell-removal and candidate-survival profile.
6. Schedule-incompatibility test.
7. Negative-control comparison.
8. RH-shaped diagnostic envelope.
9. Claim-ledger flow.
10. Implementation appendix architecture for SourceOS/SocioProphet replay and attestation.

Plotting prohibitions:

- unlabeled smoothing;
- cropped axes without disclosure;
- raw residual comparison across unequal-mass windows without normalization;
- mixing π and ψ without labeling;
- post-hoc window selection presented as prior;
- fitted frequency presented as declared;
- successful perturbations shown while failures are hidden;
- RH-shaped envelopes without diagnostic boundary language.

## Section 8 — Rewrite rules and publication voice

Every paragraph in the mathematical core must do one of five things:

1. state a definition;
2. explain standard background;
3. introduce an operator or protocol;
4. report a certified finite result;
5. state a bounded conjectural or diagnostic interpretation.

Coordinate rules:

- Use value-coordinate density for per-unit-x statements.
- Use log-coordinate intensity for per-unit-u statements.
- Use log-window mass for counts or integrals over log intervals.
- Never say prime density in log space is 1/u when discussing mass per unit u.

Residual rules:

- Name the observable.
- Name the mean field.
- Name the normalization.
- Name the claim class.

Sieve/filter rules:

- Use hard filter, admissibility constraint, candidate removal, bounded divisibility filter, wheel sector, composite certificate.
- Do not say the sieve predicts or proves primes.

Channel rules:

- Use residual channel, identity channel, residue compartment, deterministic projection.
- Avoid ontology language in the mathematical core.

Implementation rules:

- SourceOS/SocioProphet belongs in appendix or implementation layer unless tied to concrete artifacts: operator registries, RunSpecs, RunReceipts, hashes, certificates, replay records, and claim-ledger entries.
- Platform architecture cannot justify number-theoretic claims.

Terminology replacements:

- prime field -> residual channel, unless a field structure is formally defined;
- prime signal -> measured residual pattern;
- proof harness -> computational harness, unless formally verified;
- RH evidence -> RH-shaped diagnostic comparison;
- predicts primes -> scores candidates or localizes candidates;
- governance proves integrity -> certificate records replay and artifact integrity;
- lawful prime behavior -> behavior under declared admissibility and residual rules;
- harmonic law -> harmonic residual component unless a theorem is supplied.

Final manuscript tests:

1. Coordinate test.
2. Observable test.
3. Baseline test.
4. Claim-class test.
5. Figure test.
6. Implementation-boundary test.

## Placement inside Heller–Winters

This belongs in the Heller–Winters Programme as the prime/operator lane, subordinate to the broader coherence programme. It should not displace the current README lead. It should be referenced from the README’s Prime/operator lane section and developed under docs/prime-operator-lane/ or docs/manuscripts/.

The correct framing is:

The Heller–Winters prime/operator lane develops an auditable residual-analysis calculus for arithmetic experiments. It contributes typed operators, residual channels, finite-run certificates, falsification protocols, and claim-ledger discipline. It remains methodological and infrastructural unless specific finite runs, perturbation-stable empirical structures, or theorem-level proofs are supplied.
