"""Generate JSON Schema artifacts for prime/operator-lane Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from schemas.artifact_schema import ArtifactRef
from schemas.claim_ledger_schema import ClaimLedgerEntry
from schemas.run_receipt_schema import RunReceipt, RunSpec

SCHEMA_COMMENT = (
    "Semantic promotion constraints (C1/C2/D0 boundary) are enforced by "
    "Pydantic validators in claim_ledger_schema.py, not by this JSON Schema. "
    "This schema covers structural type constraints only."
)

STRUCTURAL_ONLY_DESCRIPTION = (
    "Structural JSON Schema only. Semantic promotion constraints for the "
    "Heller-Winters prime/operator lane (C1/C2/D0 boundary and D0-locked "
    "operator rules) are enforced by Pydantic validators in "
    "schemas/claim_ledger_schema.py, not by this JSON Schema."
)

CLAIM_LEDGER_DESCRIPTION = (
    "Structural JSON Schema for ClaimLedgerEntry. Semantic promotion constraints "
    "for the C1/C2/D0 boundary are enforced by Pydantic validators in "
    "schemas/claim_ledger_schema.py, not by this JSON Schema; external consumers "
    "must additionally enforce the x-semantic-constraints listed here."
)

SEMANTIC_CONSTRAINTS = [
    {
        "name": "C1-boundary",
        "enforced_by": "schemas.claim_ledger_schema.ClaimLedgerEntry",
        "not_enforced_by_json_schema": True,
        "description": (
            "C1 claims cannot reference run_receipt_ids or run-trace artifacts; "
            "C1 artifact_refs are restricted to DefinitionArtifact, "
            "OperatorArtifact, or ProofArtifact."
        ),
    },
    {
        "name": "C2-promotion-boundary",
        "enforced_by": "schemas.claim_ledger_schema.ClaimLedgerEntry and validate_claim_references",
        "not_enforced_by_json_schema": True,
        "description": (
            "C2 claims require at least one run_receipt_id, at least one linked "
            "CandidateTrace, ChannelTrace, ScoreTrace, or ObservableTrace, and "
            "each RunReceipt must resolve to a RunSpec with registered operator_ids."
        ),
    },
    {
        "name": "D0-boundary",
        "enforced_by": "schemas.claim_ledger_schema.ClaimLedgerEntry",
        "not_enforced_by_json_schema": True,
        "description": (
            "D0 claims require demotion_reason and manuscript_editing_rule=true; "
            "D0 claims cannot be promoted in place to C1 or C2."
        ),
    },
    {
        "name": "RESID-RH-DIAG-001-D0-lock",
        "enforced_by": "schemas.claim_ledger_schema.ClaimLedgerEntry",
        "not_enforced_by_json_schema": True,
        "description": (
            "RESID-RH-DIAG-001 is D0-locked and cannot support a C2 claim as "
            "residual evidence without a separate D0 ClaimLedgerEntry and explicit "
            "demotion_reason."
        ),
    },
]


def annotate_schema(name: str, schema: dict) -> dict:
    schema["$comment"] = SCHEMA_COMMENT
    if name == "ClaimLedgerEntry":
        schema["description"] = CLAIM_LEDGER_DESCRIPTION
        schema["x-semantic-constraints"] = SEMANTIC_CONSTRAINTS
    else:
        schema["description"] = STRUCTURAL_ONLY_DESCRIPTION
        schema["x-semantic-constraints"] = []
    return schema


def main() -> None:
    output_dir = REPO_ROOT / "schemas" / "json"
    output_dir.mkdir(parents=True, exist_ok=True)

    schemas = {
        "ClaimLedgerEntry": ClaimLedgerEntry.model_json_schema(),
        "ArtifactRef": ArtifactRef.model_json_schema(),
        "RunReceipt": RunReceipt.model_json_schema(),
        "RunSpec": RunSpec.model_json_schema(),
    }

    for name, schema in schemas.items():
        annotate_schema(name, schema)
        target = output_dir / f"{name}.schema.json"
        target.write_text(
            json.dumps(schema, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
