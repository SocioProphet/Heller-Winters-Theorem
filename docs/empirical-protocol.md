# Empirical Protocol

## §0 Cross-track translation requirement

Every empirical artifact must explicitly declare:

1. What the artifact demonstrates.
2. What the artifact does not claim.
3. Where the artifact sits relative to any theorem track.
4. Whether the result is finite-window, asymptotic, conjectural, or proven.
5. Whether any scale-limit assumption remains programmatic.

No empirical artifact may be described as evidence for RH, GRH, or an asymptotic residual theorem unless the exact logical bridge is stated.

## §1 Null-model and alternate-substrate gates

Every empirical artifact must specify:

- the target sequence,
- the null model,
- the alternate substrate,
- and the expected trivial-result computation.

Examples:

- all integers,
- Poisson-thinned sequences,
- density-matched random sequences,
- Liouville-randomized surrogates,
- wheel-preserving but non-prime sequences.

An empirical protocol is incomplete unless the alternate-substrate gate produces the expected trivial or baseline behavior.

## §2 Replayability and provenance

Every empirical result must ship with:

- registry version,
- operator version,
- basis declaration,
- window declaration,
- test statistic declaration,
- fixture references,
- replay instructions,
- provenance receipts,
- and hardware/runtime metadata.

All replayable artifacts are typed Proof Fabric Kernel outputs.

## §3 Basis-consistency guardrail

Analytic targets and empirical observations may only be compared after declaring:

1. the basis of the observation,
2. the basis of the analytic target,
3. the transform between them,
4. normalization conventions,
5. window conventions,
6. residuals computed in the common basis only.

No empirical-to-analytic comparison may be made across mismatched conventions.

## §3.5 Finite-window discipline

Finite-window observations do not promote automatically to asymptotic statements.

Any proposed asymptotic promotion must separately prove:

- uniformity in the window parameter,
- convergence control,
- error propagation bounds,
- and scale-limit stability.

Until then, all finite-window results remain empirical or programmatic.

## §4 Phase Wα / Wβ / Wγ structure

Every theorem-candidate empirical pipeline must use the following progression.

### Phase Wα — registry lock

Lock:

- operator definitions,
- windows,
- test statistics,
- sequence selection,
- normalization,
- and comparison conventions.

No downstream statistical comparison may redefine these objects.

### Phase Wβ — invariant audit

Verify:

- symmetry claims,
- translation equivariance,
- parity structure,
- rotational invariance,
- normalization stability,
- and declared operator invariants.

### Phase Wγ — fixture regression

Construct a small explicit fixture and verify exact replay at restricted scale.

Only after Wγ completes may the pipeline be scaled.

## §5 Promotion rules

Promotion path:

- empirical observation,
- replicated observation,
- bounded finite-window statement,
- theorem candidate,
- formal theorem.

No promotion may skip stages.

## §6 Claim taxonomy

All artifacts must classify themselves as:

- proven,
- definitional,
- empirical,
- conjectural,
- or programmatic.
