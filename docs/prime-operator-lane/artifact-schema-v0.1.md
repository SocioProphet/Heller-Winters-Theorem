# Prime Operator Lane — Evidence Artifact Schema v0.1

Status: companion schema to `operator-registry-v0.1.md` and `claim-ledger-v0.1.md`.

This document defines the evidence artifact vocabulary for the Heller–Winters prime/operator lane. It is intentionally implementation-neutral. Artifacts may later be expressed as JSON Schema, Pydantic models, append-only logs, database rows, or signed attestations. The semantics below are the controlling layer.

## Artifact rule

A result is not manuscript-grade unless its artifact class is known. A plot without a FigureArtifact is illustrative. A finite run without a RunSpec and RunReceipt is exploratory. A residual without a ResidualTrace is not claim-bearing. A C2 claim without ControlTrace and PerturbationTrace support is overclassified.

## Artifact classes

- DefinitionArtifact
- OperatorArtifact
- RunSpec
- RunReceipt
- CandidateTrace
- ChannelTrace
- ScoreTrace
- ObservableTrace
- ResidualTrace
- ControlTrace
- PerturbationTrace
- FigureArtifact
- ProofArtifact
- ClaimLedgerEntry

## Common fields

All artifacts should carry:

- artifact_id: stable identifier;
- artifact_type: one of the classes above;
- version: schema/artifact version;
- created_at: timestamp if available;
- created_by: person, agent, or process;
- source_commit: git commit or source ref, when applicable;
- input_hashes: hashes of input artifacts or data;
- output_hash: hash of the artifact payload;
- status: draft, active, superseded, deprecated, rejected;
- notes: freeform reviewer or implementation notes.

## DefinitionArtifact

Purpose: records notation, conventions, and formal definitions.

Required fields:

- definition_id;
- title;
- statement;
- symbols;
- dependencies;
- claim_class, usually C0;
- source_reference.

Examples:

- value coordinate x;
- log coordinate u = log x;
- dx = e^u du;
- log-window W = [u0,u1].

Failure modes:

- undefined symbols;
- competing definitions for the same symbol;
- hidden base convention for logarithms.

## OperatorArtifact

Purpose: records typed operator semantics.

Required fields:

- operator_id;
- name;
- operator_class;
- domain;
- codomain;
- parameters;
- deterministic_status;
- ground_truth_dependence;
- permitted_execution_modes;
- required_certificate_fields;
- claim_ceiling;
- failure_modes;
- registry_reference.

Examples:

- COORD-LOG-001;
- COORD-JAC-001;
- FILTER-WHEEL-001;
- RESID-LI-001;
- RESID-RH-DIAG-001.

Failure modes:

- mixed semantics not declared;
- missing domain/codomain;
- operator uses ground truth while marked discovery-mode.

## RunSpec

Purpose: records the intended run before execution.

Required fields:

- run_id;
- execution_mode;
- coordinate_convention;
- window_schedule;
- candidate_operator_ids;
- hard_filter_ids_in_order;
- channel_operator_ids;
- score_operator_ids;
- observable_operator_ids;
- mean_field_ids;
- normalization_ids;
- control_plan;
- perturbation_plan;
- random_seed_policy;
- implementation_ref;
- claim_target;
- expected_artifacts.

Failure modes:

- parameters chosen after execution but recorded as prior;
- hard-filter order not recorded;
- endpoint convention missing.

## RunReceipt

Purpose: records what actually executed.

Required fields:

- run_id;
- runspec_id;
- execution_started_at;
- execution_completed_at;
- implementation_hash;
- environment_summary;
- input_hashes;
- output_artifact_ids;
- warnings;
- errors;
- execution_status.

Failure modes:

- RunReceipt does not match RunSpec;
- environment drift not recorded;
- failed run reported as successful.

## CandidateTrace

Purpose: records candidate construction and filtering effects.

Required fields:

- run_id;
- window_id;
- raw_candidate_count;
- endpoint_convention;
- filter_steps;
- removed_count_by_filter;
- surviving_count_by_filter;
- small_prime_boundary_events;
- final_candidate_count.

Failure modes:

- off-by-one endpoint errors;
- small primes removed unintentionally;
- filter removal counts do not sum consistently.

## ChannelTrace

Purpose: records deterministic channel assignment and channel-level summaries.

Required fields:

- run_id;
- channel_operator_id;
- channel_rule;
- channel_labels;
- assignment_counts;
- excluded_or_invalid_labels;
- small_prime_policy;
- channel_hash.

Failure modes:

- channel definition changed after observing signal;
- residue normalization omitted;
- candidate channels mixed with prime-label channels.

## ScoreTrace

Purpose: records non-certifying score outputs.

Required fields:

- run_id;
- score_operator_id;
- score_formula;
- parameters;
- fixed_fitted_or_posthoc;
- input_trace_ids;
- output_scores_hash;
- held_out_validation_status;
- score_summary.

Failure modes:

- fitted score presented as fixed;
- post-hoc score used as predictive evidence;
- frequency set omitted for harmonic scores.

## ObservableTrace

Purpose: records measured quantities.

Required fields:

- run_id;
- observable_operator_id;
- observable_name;
- coordinate;
- window_schedule;
- ground_truth_source;
- endpoint_convention;
- values;
- value_hash.

Failure modes:

- π and ψ observables mixed;
- ground-truth dependence hidden;
- endpoint drift.

## ResidualTrace

Purpose: records mean fields, residuals, and normalizations.

Required fields:

- run_id;
- residual_operator_id;
- observable_trace_id;
- mean_field_id;
- mean_field_values;
- raw_residual_values;
- normalization_id;
- normalized_residual_values;
- diagnostic_envelopes;
- precision_policy;
- residual_hash.

Failure modes:

- baseline swapped after inspection;
- normalization missing for cross-scale comparison;
- RH-shaped diagnostic stated without boundary language.

## ControlTrace

Purpose: records positive and negative control outcomes.

Required fields:

- run_id;
- control_id;
- control_type;
- preserved_invariants;
- destroyed_invariants;
- seed;
- control_values;
- comparison_metric;
- pass_fail_or_ambiguous;
- downgrade_recommendation.

Failure modes:

- negative control reproduces signal but claim not downgraded;
- seed missing;
- wrong invariants preserved.

## PerturbationTrace

Purpose: records controlled reruns under changed schedules, baselines, moduli, channels, or implementations.

Required fields:

- run_id;
- base_runspec_id;
- perturbation_id;
- perturbation_type;
- fixed_parameters;
- changed_parameters;
- alternate_runspec_ids;
- comparison_metric;
- survival_status;
- downgrade_recommendation.

Failure modes:

- failed perturbations hidden;
- more than one parameter changed without declaration;
- perturbation selected after observing result.

## FigureArtifact

Purpose: records figure provenance and eligibility.

Required fields:

- figure_id;
- figure_class: F0, F1, F2, or F3;
- caption;
- source_artifact_ids;
- observable;
- coordinate;
- mean_field;
- normalization;
- channel_rule;
- plotting_parameters;
- smoothing_policy;
- axis_policy;
- claim_class_supported;
- limitations.

Failure modes:

- unlabeled smoothing;
- cropped axes without disclosure;
- figure stronger than artifacts;
- RH-shaped plot without diagnostic boundary.

## ProofArtifact

Purpose: records theorem-level support.

Required fields:

- proof_id;
- theorem_statement;
- hypotheses;
- conclusion;
- dependencies;
- proof_text_or_formal_ref;
- verification_status;
- imported_references;
- finite_computation_dependencies;
- reviewer_notes.

Failure modes:

- empirical result presented as proof;
- missing hypotheses;
- imported theorem not cited;
- finite computation not verified where required.

## ClaimLedgerEntry

Purpose: binds a sentence/proposition to claim class and evidence.

Required fields:

- claim_id;
- claim_text;
- claim_class;
- object_type;
- dependencies;
- evidence_artifact_ids;
- permitted_language;
- prohibited_language;
- falsification_or_downgrade_condition;
- current_status;
- reviewer_note.

Failure modes:

- claim stronger than evidence;
- claim lacks artifact mapping;
- D0 language promoted to C3;
- C1 result described as C2 without controls.

## Minimal C1 artifact bundle

A C1 empirical claim requires:

- RunSpec;
- RunReceipt;
- relevant OperatorArtifacts;
- ObservableTrace or CandidateTrace;
- ResidualTrace if residual language is used;
- ClaimLedgerEntry.

## Minimal C2 artifact bundle

A C2 empirical claim requires the C1 bundle plus:

- ControlTrace;
- PerturbationTrace;
- replay record or implementation-replay evidence;
- FigureArtifact if visualized.

## D0 RH-shaped diagnostic bundle

An RH-shaped diagnostic statement requires:

- ResidualTrace;
- RESID-RH-DIAG-001 OperatorArtifact;
- envelope formula;
- finite-domain statement;
- explicit prohibited-language boundary;
- FigureArtifact if plotted.

## SourceOS/SocioProphet implementation boundary

SourceOS/SocioProphet may implement this schema as registries, logs, hashes, attestations, dashboards, or replay receipts. That implementation supports reproducibility and governance. It does not change the claim class of the mathematics unless the artifact is a verified computation or proof object under declared rules.
