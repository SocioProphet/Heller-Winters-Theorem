# Dependencies

Status: live dependency declaration.
Claim level: governance / architecture.

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `988307215ad38ccb16514311222184a1b757752b` | Framework objects (`HG-*`) from `docs/framework-core/`; PFK objects (`PFK-*`) from `proof_fabric_kernel/` |

## Cited framework objects

| Identifier | Use | Citation grade |
|---|---|---|
| `HG-EX-001` | Catalan / mu_2 fixture reference | fixture-grade |
| `HG-MTH-005` | Universal Bridge formal specification | method-grade; no proof transfer |

## Cited PFK surfaces

| Identifier / surface | Path | Use |
|---|---|---|
| `PFK-SCHEMA-002` | `proof_fabric_kernel/schemas/event_ir.schema.json` | Candidate C operator-event traces |
| `PFK-SCHEMA-003` | `proof_fabric_kernel/schemas/proof_artifact.schema.json` | Candidate C proof-artifact envelope |
| `PFK-SCHEMA-001` | `proof_fabric_kernel/schemas/claim_ledger_row.schema.json` | Candidate C descriptive-grade claim row |
| `PFK-SCHEMA-004` | `proof_fabric_kernel/schemas/calibration_bundle.schema.json` | Candidate C baseline calibration bundle |
| `PFK-OP-031` | `proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md` | log-phase embedding |
| `PFK-OP-032` | `proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md` | mean resultant length R |
| `PFK-OP-051..055` | `proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md` | N1/N2/S1/S2/S3 protocol operators |
| `A-PFK-*` | `proof_fabric_kernel/docs/anti-seed-pfk.md` | operational anti-seed boundary |

## Local PFK status

Current `main` has no committed local `proof_fabric_kernel/` tree to delete. Earlier source-location audits found PFK source provenance and Heller-Godel now hosts the canonical PFK surface. Heller-Winters consumes PFK exclusively from Heller-Godel at the pinned commit above.

This PR advances the pin from initial PFK seed import `0ef1cab4c525fd004e38fa9a92f7e911acbbc976` to registry expansion `988307215ad38ccb16514311222184a1b757752b`. The advance is non-breaking because schema files are unchanged; the registry expansion canonicalizes identifiers already used by Candidate C.

## Non-claim boundary

Declaring this dependency does not promote Candidate C, RH, GRH, zero-location, residual-envelope, or asymptotic claims. Green PFK validation is receipt-loop closure only, not theorem-grade evidence.
