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


def main() -> None:
    output_dir = REPO_ROOT / "schemas" / "json"
    output_dir.mkdir(parents=True, exist_ok=True)

    schemas = {
        "ClaimLedgerEntry": ClaimLedgerEntry.model_json_schema(),
        "ArtifactRef": ArtifactRef.model_json_schema(),
        "RunReceipt": RunReceipt.model_json_schema(),
        "RunSpec": RunSpec.model_json_schema(),
    }

    schemas["ClaimLedgerEntry"]["$comment"] = SCHEMA_COMMENT

    for name, schema in schemas.items():
        target = output_dir / f"{name}.schema.json"
        target.write_text(
            json.dumps(schema, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
