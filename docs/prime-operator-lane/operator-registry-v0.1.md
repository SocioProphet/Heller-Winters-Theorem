# Prime Operator Lane — Operator Registry v0.1

Status: companion registry for `prime-residual-manuscript-scaffold-v0.1.md`.

This registry types the operators used by the Heller–Winters prime/operator lane. It is a publication-control artifact, not a theorem claim. Its purpose is to prevent operator leakage, coordinate drift, and claim-class inflation.

## Registry rule

Every operation used in a claim-bearing run must have a registry entry with:

- operator id;
- operator name;
- operator class;
- domain;
- codomain;
- parameters;
- deterministic status;
- ground-truth dependence;
- permitted execution modes;
- required certificate fields;
- maximum claim class without proof;
- failure modes.

If an operation has mixed semantics, split it into smaller typed operators or mark it as mixed and restrict its claim class to exploratory until the semantics are separated.

## Operator classes

- COORD: coordinate operator.
- CAND: candidate construction operator.
- FILTER: hard filter.
- CHANNEL: deterministic channel/projection operator.
- SCORE: non-certifying scoring operator.
- OBS: observable operator.
- RESID: residual operator.
- CERT: certificate/artifact operator.
- CONTROL: positive or negative control operator.
- PERTURB: perturbation operator.

## Claim-class ceiling

- C0: definitional or formal.
- C1: certified finite empirical.
- C2: reproducible empirical structure after replay, controls, and perturbations.
- C3: theorem-level; requires proof.
- D0: diagnostic comparison; may accompany C1/C2 but is not theorem-level.
- E0: exploratory only.

No operator below has C3 ceiling unless a separate proof object is attached.

---

## COORD-LOG-001 — Log coordinate map

Class: COORD.

Name: Log coordinate map.

Domain: positive value-coordinate points or windows.

Codomain: log-coordinate points or windows.

Definition:

```text
u = log x
x = e^u
```

Parameters:

- logarithm base: natural log only unless explicitly declared otherwise.

Deterministic: yes.

Ground-truth dependence: none.

Permitted modes: exploratory, validation, replay, perturbation, proof.

Required certificate fields:

- coordinate convention;
- log base;
- object transformed: point, window, density, mass, or residual.

Claim ceiling: C0.

Failure modes:

- coordinate object not named;
- natural log silently replaced by another base;
- density transformed without Jacobian.

---

## COORD-JAC-001 — Log-coordinate Jacobian

Class: COORD.

Name: Value-measure to log-measure Jacobian.

Domain: densities or window-mass expressions in x-coordinate.

Codomain: intensities or window-mass expressions in u-coordinate.

Definition:

```text
dx = e^u du
```

The value-coordinate density `dπ/dx ~ 1/log x` becomes log-coordinate intensity `dπ/du ~ e^u/u`.

Deterministic: yes.

Ground-truth dependence: standard analytic background plus coordinate identity.

Permitted modes: all.

Required certificate fields:

- source coordinate;
- target coordinate;
- observable;
- density or mass status.

Claim ceiling: C0 for coordinate identity; C3-derived background when invoking PNT.

Failure modes:

- treating `1/u` as mass per unit log-coordinate;
- comparing log-window counts against value-density without Jacobian.

---

## CAND-WINDOW-001 — Log-window candidate constructor

Class: CAND.

Name: Raw candidate set from log-window.

Domain: log-window `W = [u0,u1]`.

Codomain: finite integer candidate set.

Definition:

```text
C0(W) = {n in Z : e^u0 <= n <= e^u1 and n >= 2}
```

Parameters:

- endpoint inclusivity;
- integer rounding convention;
- small-prime handling policy.

Deterministic: yes.

Ground-truth dependence: none.

Permitted modes: all.

Required certificate fields:

- window schedule;
- endpoint convention;
- rounding rule;
- small-prime policy.

Claim ceiling: C1 for finite certified output; C0 for definition.

Failure modes:

- off-by-one endpoint drift;
- silent floor/ceiling changes;
- accidental exclusion of 2 or small primes.

---

## FILTER-WHEEL-001 — Wheel admissibility filter

Class: FILTER.

Name: Reduced residue wheel filter.

Domain: integer candidate set.

Codomain: subset of input candidate set.

Definition:

```text
R_M = {r mod M : gcd(r,M)=1}
F_M(S) = {n in S : n mod M in R_M}
```

Parameters:

- modulus `M`;
- reduced residue set;
- small-prime preservation policy.

Deterministic: yes.

Ground-truth dependence: none.

Permitted modes: all.

Required certificate fields:

- modulus;
- residue set;
- filter position in stack;
- small-prime exceptions.

Claim ceiling: C1 for certified finite filtering; C0 for definition.

Failure modes:

- removing primes dividing M without declared exception;
- treating wheel survival as primality certification;
- assuming commutativity with boundary-sensitive filters.

---

## FILTER-DIV-001 — Bounded divisibility filter

Class: FILTER.

Name: Bounded prime-basis divisibility filter.

Domain: integer candidate set.

Codomain: subset of input candidate set.

Definition:

```text
B_Q = {q prime : q <= Q}
F_B(S) = {n in S : q does not divide n for all q in B_Q with q < n}
```

Parameters:

- prime basis bound `Q`;
- prime basis source;
- boundary policy for `q = n`.

Deterministic: yes.

Ground-truth dependence: prime basis construction; no target-label dependence if basis is fixed before run.

Permitted modes: all.

Required certificate fields:

- Q;
- basis hash or generation rule;
- filter order;
- q<n preservation rule.

Claim ceiling: C1 for certified finite filtering.

Failure modes:

- deleting prime q when q lies in window;
- changing Q after seeing residuals;
- presenting filter survival as proof of primality.

---

## CHANNEL-RESIDUE-001 — Residue-channel projection

Class: CHANNEL.

Name: Residue-channel projection modulo M.

Domain: integer candidates, primes, or counted events.

Codomain: residue labels modulo M.

Definition:

```text
Chan_M(n) = n mod M
```

Parameters:

- modulus M;
- admissible residue set;
- excluded-residue policy.

Deterministic: yes.

Ground-truth dependence: none for candidates; prime labels only if applied after oracle-labeled observable.

Permitted modes: exploratory, validation, replay, perturbation.

Required certificate fields:

- modulus;
- admissible residues;
- small-prime policy;
- channel membership rule.

Claim ceiling: C2 after perturbation and controls.

Failure modes:

- defining channels after seeing where signal appears;
- forgetting φ(M) normalization;
- mixing candidate channels and prime-label channels.

---

## CHANNEL-SHELL-001 — Divisibility-shell channel

Class: CHANNEL.

Name: Factorization/divisibility shell channel.

Domain: candidate integers or divisor tests.

Codomain: shell labels.

Definition:

A shell is a declared divisor-space band, usually relative to `sqrt(n)`, a prime-basis range, or a multiplicative interval. Exact shell boundaries must be specified in the run.

Parameters:

- shell-boundary rule;
- divisor basis;
- candidate value n;
- window schedule.

Deterministic: yes when shell boundaries are fixed.

Ground-truth dependence: none unless shell definition uses primality labels, which is prohibited for predictive claims.

Permitted modes: exploratory, validation, replay, perturbation.

Required certificate fields:

- shell rule;
- boundary formula;
- basis source;
- post-hoc status if boundaries were fitted.

Claim ceiling: C2 after controls; E0 if fitted post-hoc without validation.

Failure modes:

- metaphysical field language;
- shell boundaries tuned after inspection;
- composite-survivor control reproduces claimed signal.

---

## SCORE-HARM-001 — Harmonic correlation score

Class: SCORE.

Name: Harmonic or log-periodic residual score.

Domain: residual trace over a declared schedule.

Codomain: real-valued or vector-valued score.

Definition:

Computes correlation, amplitude, or fit statistic between a residual trace and a declared harmonic/log-periodic probe family.

Parameters:

- frequency set;
- phase convention;
- schedule;
- residual observable;
- fitting status: declared, fitted, or post-hoc.

Deterministic: yes if frequency set and fitting procedure are fixed.

Ground-truth dependence: depends on residual observable; must be recorded.

Permitted modes: exploratory, validation, replay, perturbation.

Required certificate fields:

- frequency set;
- phase convention;
- score formula;
- fitted/declared/post-hoc status;
- held-out validation status if fitted.

Claim ceiling: C1 if certified; C2 if perturbation-stable; E0 if post-hoc only.

Failure modes:

- overfitting finite residual noise;
- fitted frequency presented as prior;
- one schedule treated as schedule-independent.

---

## OBS-COUNT-001 — Prime-count observable

Class: OBS.

Name: Prime count in a declared window.

Domain: window and ground-truth primality source.

Codomain: integer count.

Definition:

```text
Nπ(W) = #{p prime : e^u0 <= p <= e^u1}
```

Parameters:

- window schedule;
- primality source;
- endpoint convention.

Deterministic: yes given source and endpoint convention.

Ground-truth dependence: yes.

Permitted modes: validation, replay, perturbation; exploratory if source is provisional.

Required certificate fields:

- primality source;
- endpoint convention;
- window hash or schedule;
- count output.

Claim ceiling: C1 for finite certified count; C2 after replay/perturbation.

Failure modes:

- using ground truth in a run described as prediction;
- mixing counts with candidate survival;
- endpoint drift.

---

## OBS-CHEB-001 — Chebyshev-mass observable

Class: OBS.

Name: Chebyshev weighted mass in a declared window.

Domain: window and von Mangoldt evaluator/source.

Codomain: real or integer-weighted mass.

Definition:

```text
ψ(x) = sum_{n <= x} Λ(n)
Ψ(W) = ψ(e^u1) - ψ(e^u0)
```

Parameters:

- Λ evaluator;
- prime-power convention;
- endpoint convention.

Deterministic: yes.

Ground-truth dependence: yes; Λ encodes prime-power structure.

Permitted modes: validation, replay, perturbation.

Required certificate fields:

- Λ implementation hash;
- endpoint convention;
- prime-power inclusion rule;
- output mass.

Claim ceiling: C2 after controls and perturbation.

Failure modes:

- silently replacing π-observable with ψ-observable;
- claiming prediction while using Λ ground truth;
- missing prime powers.

---

## RESID-LI-001 — Li-based count residual

Class: RESID.

Name: Li-based prime-count residual.

Domain: prime-count observable and Li mean field.

Codomain: raw and optionally normalized residual.

Definition:

```text
Mπ(W) = Li(e^u1) - Li(e^u0)
Rπ(W) = Nπ(W) - Mπ(W)
```

Parameters:

- Li implementation;
- normalization rule;
- window schedule;
- observable source.

Deterministic: yes given numeric precision and implementation.

Ground-truth dependence: yes through Nπ.

Permitted modes: validation, replay, perturbation.

Required certificate fields:

- mean-field ID;
- Li precision;
- observable trace;
- normalization ID;
- residual trace.

Claim ceiling: C2 after perturbation and controls.

Failure modes:

- treating Li mean as exact count;
- baseline swapped after inspection;
- normalization absent in cross-scale comparisons.

---

## RESID-RH-DIAG-001 — RH-shaped diagnostic envelope

Class: RESID.

Name: RH-shaped residual envelope comparison.

Domain: residual trace and declared envelope function.

Codomain: diagnostic comparison trace.

Definition:

Compares residual magnitude to a conditional square-root-scale or e^(u/2)-type envelope under the declared observable and logarithmic factors.

Parameters:

- observable;
- envelope formula;
- included logarithmic factors;
- finite domain;
- normalization.

Deterministic: yes.

Ground-truth dependence: inherited from residual trace.

Permitted modes: validation, replay, perturbation.

Required certificate fields:

- envelope formula;
- diagnostic boundary statement;
- finite domain;
- residual trace;
- normalization.

Claim ceiling: D0 attached to C1/C2; never C3 without proof.

Failure modes:

- RH proof language;
- zero-location language;
- asymptotic claim from finite plot.

---

## CERT-RUN-001 — Run certificate emitter

Class: CERT.

Name: RunSpec/RunReceipt and trace emitter.

Domain: completed run state.

Codomain: replayable artifact bundle.

Required artifacts:

- RunSpec;
- RunReceipt;
- CandidateTrace;
- ChannelTrace;
- ScoreTrace if scores are used;
- ObservableTrace;
- ResidualTrace;
- ControlTrace if controls are used;
- PerturbationTrace if perturbations are used;
- ClaimLedgerEntry.

Deterministic: yes for a fixed run state.

Ground-truth dependence: records but does not introduce ground truth.

Permitted modes: all.

Required certificate fields:

- implementation hash;
- input hash;
- output hash;
- parameters;
- execution mode;
- claim class.

Claim ceiling: C2 for empirical structure; C3 only for formally verified finite computation or proof objects.

Failure modes:

- certificate missing fields needed for replay;
- environment not recorded when relevant;
- artifact hash mismatch.

---

## CONTROL-NEG-001 — Negative-control suite

Class: CONTROL.

Name: Negative controls for residual/scoring claims.

Domain: fixed operator stack and synthetic or shuffled comparison datasets.

Codomain: control traces.

Required controls for C2 candidates:

- shuffled-prime control;
- Cramér-style random model control;
- residue-preserving shuffle;
- composite-survivor control;
- schedule-null control.

Deterministic: deterministic if seeded; stochastic if random seed varies.

Ground-truth dependence: depends on control.

Permitted modes: validation, replay, perturbation.

Required certificate fields:

- control type;
- seed;
- preserved invariants;
- destroyed invariants;
- comparison metric.

Claim ceiling: C2 when passed with perturbation tests.

Failure modes:

- claimed signal reproduced by negative controls;
- seed not recorded;
- control preserves or destroys the wrong structure.

---

## PERTURB-SCHEDULE-001 — Schedule perturbation

Class: PERTURB.

Name: Window schedule perturbation.

Domain: fixed operator stack plus alternate window schedules.

Codomain: perturbation trace.

Perturbations:

- window shift;
- scale dilation;
- incompatible irrational or noncommensurate schedule;
- held-out schedule replay.

Deterministic: yes if schedules are fixed.

Ground-truth dependence: inherited from observable.

Permitted modes: perturbation.

Required certificate fields:

- base schedule;
- alternate schedules;
- changed parameters;
- fixed parameters;
- comparison metrics.

Claim ceiling: C2 when combined with controls and replay.

Failure modes:

- successful schedule shown while failed schedule hidden;
- schedule selected after seeing pattern;
- schedule change also changes baseline or filter stack without declaration.

---

## Registry status

This v0.1 registry is sufficient to type the current manuscript scaffold. It should be expanded when the first executable run artifacts are committed.
