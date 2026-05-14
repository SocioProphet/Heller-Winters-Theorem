# Prime Operator Lane — Claim Ledger v0.1

Status: companion ledger for `prime-residual-manuscript-scaffold-v0.1.md` and `operator-registry-v0.1.md`.

This ledger records the claim boundary for the Heller–Winters prime/operator lane. It is not a theorem claim. It is an editorial and scientific control surface: every claim-bearing sentence in the manuscript should map to one of these entries or create a new entry.

## Claim classes

| Class | Meaning | Evidence required | Ceiling without proof |
|---|---|---|---|
| C0 | Definitional or formal | Definition, convention, typed operator, deterministic consequence | C0 |
| C1 | Certified finite empirical | RunSpec, RunReceipt, traces, artifact hashes | C1 |
| C2 | Reproducible empirical structure | C1 artifacts plus replay, controls, perturbation traces | C2 |
| C3 | Theorem-level | Stated hypotheses, proof, proof dependencies | C3 |
| D0 | Diagnostic comparison | Declared diagnostic scale/envelope and boundary language | D0 attached to C1/C2 |
| E0 | Exploratory | Notes, plots, provisional searches, unfrozen parameters | E0 |

No finite run becomes C3 without a proof. No diagnostic envelope becomes proof language. No implementation artifact becomes mathematical proof unless it is a formal proof object or a verified finite-computation proof under declared rules.

## Required ledger fields

Each entry must record:

- claim id;
- claim text;
- claim class;
- object type;
- dependencies;
- required evidence artifacts;
- permitted language;
- prohibited language;
- falsification or downgrade condition;
- current status;
- reviewer note.

## Canonical entries

### CL-001 — Value-coordinate prime density

Claim text: ordinary prime density with respect to the value coordinate x is asymptotically `1/log x`.

Claim class: C3 background, imported from the Prime Number Theorem when cited in the final manuscript.

Object type: standard analytic-number-theory background.

Dependencies:

- PNT-level background;
- coordinate convention x.

Required evidence artifacts:

- final manuscript citation to standard reference;
- no run artifact required unless illustrated computationally.

Permitted language:

- value-coordinate density;
- leading asymptotic density with respect to x.

Prohibited language:

- log-coordinate intensity;
- mass per unit u.

Falsification or downgrade condition: not a new framework claim; misuse occurs if it is transferred to log-coordinate mass without Jacobian.

Current status: active.

Reviewer note: load-bearing background distinction.

---

### CL-002 — Log-coordinate Jacobian

Claim text: under `u = log x`, the value measure transforms as `dx = e^u du`.

Claim class: C0.

Object type: coordinate convention.

Dependencies:

- natural logarithm convention.

Required evidence artifacts:

- DefinitionArtifact;
- COORD-LOG-001;
- COORD-JAC-001.

Permitted language:

- coordinate-change identity;
- Jacobian factor;
- value measure to log measure.

Prohibited language:

- new prime law;
- prime generator.

Falsification or downgrade condition: none as a calculus identity; misuse occurs if the transformed object is not named.

Current status: active.

Reviewer note: every log-window mass statement depends on this.

---

### CL-003 — Log-coordinate prime intensity

Claim text: after combining CL-001 and CL-002, the leading expected prime intensity per unit log-coordinate is `e^u/u`.

Claim class: C0/C3-derived background.

Object type: coordinate-normalized mean-field statement.

Dependencies:

- CL-001;
- CL-002;
- natural log convention.

Required evidence artifacts:

- DefinitionArtifact;
- COORD-JAC-001;
- manuscript derivation.

Permitted language:

- log-coordinate intensity;
- expected prime mass per unit u;
- density transformed by Jacobian.

Prohibited language:

- pointwise primality probability for an individual integer;
- `1/u` as log-coordinate mass.

Falsification or downgrade condition: invalid if used as a pointwise probability or if the Jacobian is omitted.

Current status: active.

Reviewer note: this is the primary editorial correction.

---

### CL-004 — Li-based log-window mean field

Claim text: when the Li mean field is declared, a log-window `W = [u0,u1]` has expected count mass `Li(e^u1) - Li(e^u0)`.

Claim class: C0 with standard analytic background.

Object type: mean-field definition.

Dependencies:

- CL-003;
- chosen mean-field convention;
- window endpoint convention.

Required evidence artifacts:

- DefinitionArtifact;
- RESID-LI-001 when used in a run.

Permitted language:

- declared Li mean field;
- Li-based expected count mass.

Prohibited language:

- exact count;
- proof of prime placement.

Falsification or downgrade condition: does not apply if a run uses a different baseline; baseline swaps require separate artifacts.

Current status: active.

Reviewer note: baseline identity must be visible in every residual claim.

---

### CL-005 — Hard filters precede soft scores

Claim text: in the canonical pipeline, hard admissibility filters precede soft scoring operators.

Claim class: C0 protocol claim.

Object type: execution semantics.

Dependencies:

- operator taxonomy;
- FILTER class;
- SCORE class.

Required evidence artifacts:

- OperatorArtifact;
- RunSpec for claim-bearing runs.

Permitted language:

- canonical ordering rule;
- filter-first discipline.

Prohibited language:

- mathematical necessity for every possible algorithm;
- proof of primality by filtering.

Falsification or downgrade condition: alternative order must be explicitly declared and justified; otherwise the run is downgraded to exploratory.

Current status: active.

Reviewer note: prevents leakage.

---

### CL-006 — Soft scores do not certify primality

Claim text: a soft score may rank, stratify, or localize candidates but does not certify primality.

Claim class: C0 protocol claim.

Object type: scoring semantics.

Dependencies:

- SCORE class;
- execution-mode declaration.

Required evidence artifacts:

- OperatorArtifact;
- ScoreTrace when used.

Permitted language:

- non-certifying score;
- ranking signal;
- candidate-localization score.

Prohibited language:

- primality proof;
- primality certificate;
- generator of primes.

Falsification or downgrade condition: none unless replaced by a valid primality certificate or theorem.

Current status: active.

Reviewer note: essential boundary for candidate-localization language.

---

### CL-007 — Residual channels are measurable compartments

Claim text: residual channels are deterministic measurable compartments or projections, not ontological fields.

Claim class: C0 terminology and protocol claim.

Object type: channel semantics.

Dependencies:

- CHANNEL class;
- channel membership rule.

Required evidence artifacts:

- OperatorArtifact;
- ChannelTrace when used in a run.

Permitted language:

- residual channel;
- identity channel;
- compartment;
- deterministic projection.

Prohibited language:

- physical field;
- source of primes;
- ontology of primes;
- prime consciousness in the mathematical core.

Falsification or downgrade condition: field language must move to motivation/appendix unless a formal field structure is supplied.

Current status: active.

Reviewer note: protects the paper from metaphor drift.

---

### CL-008 — RH-shaped diagnostic boundary

Claim text: RH-shaped means consistency with a conditional square-root-scale diagnostic under a declared observable and normalization.

Claim class: D0, optionally attached to C1/C2 finite evidence.

Object type: diagnostic comparison.

Dependencies:

- residual observable;
- normalization rule;
- envelope formula;
- finite domain.

Required evidence artifacts:

- ResidualTrace;
- RESID-RH-DIAG-001;
- FigureArtifact if plotted;
- ClaimLedgerEntry with D0 status.

Permitted language:

- RH-shaped diagnostic;
- conditional square-root-scale comparison;
- finite-domain consistency with declared envelope.

Prohibited language:

- RH proof;
- RH verification;
- zero-location proof;
- asymptotic RH verification;
- critical-line confirmation.

Falsification or downgrade condition: invalid as written if presented as theorem-level evidence without proof.

Current status: active.

Reviewer note: this is the central no-overclaim boundary.

---

### CL-009 — Certified finite runs are C1 until promoted

Claim text: a certified finite run supports at most C1 unless replay, controls, and perturbation tests support promotion.

Claim class: C0 protocol claim.

Object type: evidence promotion rule.

Dependencies:

- harness protocol;
- RunSpec;
- RunReceipt;
- trace artifacts.

Required evidence artifacts:

- RunSpec;
- RunReceipt;
- relevant traces;
- ClaimLedgerEntry.

Permitted language:

- certified finite result;
- finite-run evidence.

Prohibited language:

- general theorem;
- asymptotic law;
- robust law, unless C2 promotion requirements are met.

Falsification or downgrade condition: if original run cannot be replayed from certificate, downgrade to E0.

Current status: active.

Reviewer note: finite computation cannot outrun its domain.

---

### CL-010 — Perturbation-stable patterns are C2-eligible

Claim text: a pattern that survives declared replay, controls, and perturbation tests is eligible for C2 status.

Claim class: C0 promotion rule.

Object type: evidence promotion rule.

Dependencies:

- CL-009;
- CONTROL-NEG-001;
- PERTURB-SCHEDULE-001;
- implementation replay.

Required evidence artifacts:

- RunSpec;
- RunReceipt;
- ControlTrace;
- PerturbationTrace;
- independent replay record if available.

Permitted language:

- reproducible empirical structure;
- perturbation-stable pattern.

Prohibited language:

- theorem;
- proof;
- asymptotic law.

Falsification or downgrade condition: failure under required controls or perturbations reduces the claim to C1 or E0, depending on replay status.

Current status: active.

Reviewer note: C2 is empirical robustness, not proof.

---

### CL-011 — SourceOS/SocioProphet implementation boundary

Claim text: SourceOS/SocioProphet artifacts support implementation, replay, attestation, operator registries, and certificate governance; they do not provide mathematical proof unless the artifact is a formal proof object or verified finite computation under declared rules.

Claim class: C0 implementation-layer claim.

Object type: implementation boundary.

Dependencies:

- certificate semantics;
- implementation appendix boundary;
- artifact schema.

Required evidence artifacts:

- OperatorArtifact;
- RunSpec/RunReceipt if used in a run;
- hash-linked artifacts if attestation is claimed.

Permitted language:

- implementation substrate;
- replay governance;
- attestation support;
- artifact ledger;
- operator registry.

Prohibited language:

- platform proves the mathematics;
- governance proves prime law;
- ecosystem validates RH.

Falsification or downgrade condition: implementation language without measurable artifacts belongs in appendix-only prose.

Current status: active.

Reviewer note: preserves usefulness of the ecosystem without contaminating mathematical claims.

---

## Prohibited promotions

The following promotions are invalid unless additional proof or artifacts are supplied:

- plot -> evidence without FigureArtifact and traces;
- finite run -> asymptotic law;
- residual envelope -> RH proof;
- score -> certificate;
- channel -> ontology;
- implementation ledger -> mathematical proof;
- post-hoc parameter -> prior structure;
- negative-control failure -> unchanged claim class.

## Acceptable promotions

- E0 -> C1 after freezing the operator stack and rerunning under certificate.
- C1 -> C2 after replay, negative controls, and perturbation tests.
- C2 -> conjecture target after stable empirical structure is documented.
- conjecture -> C3 only by proof.
- verified finite computation -> C3 only when the theorem is finite or the proof formally incorporates the computation.

## Manuscript editing rule

Every strong sentence should map to one of:

- C0 definition/protocol;
- C1 certified finite result;
- C2 reproducible empirical structure;
- C3 theorem;
- D0 diagnostic comparison;
- E0 exploratory note.

Sentences containing “stable,” “robust,” “persists,” or “survives” require C2 support. Sentences containing “theorem,” “for all,” “asymptotically,” or “must” require C3 support unless purely definitional. Sentences containing “RH-shaped” require D0 boundary language.
