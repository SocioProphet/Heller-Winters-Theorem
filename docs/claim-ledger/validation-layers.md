# Claim Ledger Validation Layers

Status: active validation doctrine for the Heller–Winters prime/operator lane.

The claim-ledger validation stack has two enforcement layers. This document defines the boundary so downstream consumers do not mistake portable JSON Schema validation for full semantic validation.

## Layer 1 — Structural validation

Layer 1 is JSON Schema. The generated schemas live under:

```text
schemas/json/
```

They are produced by:

```bash
make generate-json-schema
```

Layer 1 validates structural constraints only:

- required fields;
- field types;
- enum values such as `ClaimClass` and `ArtifactType`;
- basic string constraints such as non-empty identifiers;
- object shape and `additionalProperties: false`;
- date-time field shape where declared by Pydantic;
- portable schema vocabulary for non-Python consumers.

Layer 1 is designed for cross-repo and cross-language consumption. JavaScript, Rust, OpenAPI tooling, schema registries, and external estate validators can consume `schemas/json/*.schema.json` without importing Python.

Layer 1 does not enforce the C1/C2/D0 semantic promotion boundary.

## Layer 2 — Semantic validation

Layer 2 is the Pydantic validator layer. It lives in:

```text
schemas/claim_ledger_schema.py
```

Layer 2 enforces claim-promotion semantics that are intentionally outside the portable JSON Schema layer.

### C1 boundary

A C1 claim is analytically grounded rather than computationally evidenced.

Layer 2 enforces:

- C1 claims cannot reference `run_receipt_ids`;
- C1 claims cannot reference run-trace artifacts;
- C1 `artifact_refs` are restricted to `DefinitionArtifact`, `OperatorArtifact`, or `ProofArtifact`;
- all referenced operators must be registered at version `v0.1` or later.

### C2 promotion boundary

A C2 claim is computationally evidenced.

Layer 2 enforces:

- C2 claims require at least one `run_receipt_id`;
- C2 claims require at least one linked trace artifact of type `CandidateTrace`, `ChannelTrace`, `ScoreTrace`, or `ObservableTrace`;
- each referenced `RunReceipt` must resolve to a `RunSpec`;
- each resolved `RunSpec` must declare an `operator_ids` list;
- every operator in that list must exist in the operator registry at version `v0.1` or later.

### D0 boundary

A D0 claim is diagnostic, demoted, or prohibited from direct promotion.

Layer 2 enforces:

- D0 claims require an explicit `demotion_reason`;
- D0 claims require `manuscript_editing_rule: true`;
- D0 claims cannot be promoted in place to C1 or C2;
- `RESID-RH-DIAG-001` is D0-locked and cannot support a C2 claim as residual evidence.

The RH-shaped diagnostic boundary is therefore executable: a C2 claim referencing `RESID-RH-DIAG-001` fails with an error naming the operator and its D0 status.

## Integration boundary for external consumers

External consumers may use the JSON Schema files for structural validation, but structural validation is not sufficient for claim acceptance.

A downstream system that consumes `schemas/json/ClaimLedgerEntry.schema.json` must additionally enforce the semantic constraints listed in the schema's `x-semantic-constraints` field or call the Python reference implementation in `schemas/claim_ledger_schema.py`.

The reference command is:

```bash
make validate-claim-ledger
```

The full local gate is:

```bash
make check-claim-ledger
```

That command regenerates JSON Schema, runs the Pydantic fixture tests, and fails if generated schema artifacts are out of date.

## Why the stack is split

JSON Schema is the right interchange format. It is portable, language-neutral, and consumable outside the Python runtime.

Pydantic is the right semantic enforcement boundary for this repository. The C1/C2/D0 constraints depend on cross-field rules, registry membership, and cross-artifact references. Encoding those fully in JSON Schema would require custom keywords or complicated conditional schema logic that would reduce portability and still leave cross-artifact validation incomplete.

The repository therefore uses the following rule:

```text
JSON Schema validates structure.
Pydantic validates claim semantics.
```

Any consumer that needs manuscript-grade validation must use both layers or implement Layer 2 equivalently.

## Current named semantic constraints

The generated `ClaimLedgerEntry.schema.json` advertises these non-JSON-Schema constraints under `x-semantic-constraints`:

- `C1-boundary`;
- `C2-promotion-boundary`;
- `D0-boundary`;
- `RESID-RH-DIAG-001-D0-lock`.

These names are stable integration hooks for downstream estate validators.
