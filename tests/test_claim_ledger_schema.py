from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from schemas.claim_ledger_schema import ClaimLedgerEntry, validate_claim_references
from schemas.run_receipt_schema import RunReceipt, RunSpec


FIXTURE_ROOT = Path(__file__).resolve().parents[1] / "fixtures"


def load_fixture(path: str) -> dict:
    with (FIXTURE_ROOT / path).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def test_valid_c1_claim_fixture():
    entry = ClaimLedgerEntry.model_validate(load_fixture("valid/cl-001-c1.yaml"))

    assert entry.claim_id == "CL-001"
    assert entry.claim_class.value == "C1"
    assert entry.run_receipt_ids == []


def test_valid_c2_claim_fixture_with_receipt_and_runspec():
    entry = ClaimLedgerEntry.model_validate(load_fixture("valid/cl-002-c2-with-receipt.yaml"))

    run_receipts = {
        "RUN-001": RunReceipt(
            run_receipt_id="RUN-001",
            runspec_id="SPEC-001",
            execution_status="success",
        )
    }
    run_specs = {
        "SPEC-001": RunSpec(
            runspec_id="SPEC-001",
            execution_mode="validation",
            operator_ids=["COORD-JAC-001", "OBS-COUNT-001", "RESID-LI-001"],
        )
    }

    validate_claim_references(entry, run_receipts=run_receipts, run_specs=run_specs)


def test_invalid_c2_without_receipt_fails_with_specific_promotion_error():
    with pytest.raises(ValidationError, match="run_receipt_ids.*C2 promotion rule"):
        ClaimLedgerEntry.model_validate(load_fixture("invalid/c2-no-receipt.yaml"))


def test_invalid_d0_without_demotion_reason_fails_with_specific_error():
    with pytest.raises(ValidationError, match="D0 claim requires explicit demotion_reason"):
        ClaimLedgerEntry.model_validate(load_fixture("invalid/d0-no-reason.yaml"))


def test_invalid_c1_with_run_trace_fails_with_specific_error():
    with pytest.raises(ValidationError, match="C1 claim can only reference"):
        ClaimLedgerEntry.model_validate(load_fixture("invalid/c1-with-run-trace.yaml"))


def test_invalid_rh_diagnostic_promoted_to_c2_names_d0_locked_operator():
    with pytest.raises(ValidationError, match="RESID-RH-DIAG-001.*D0 status"):
        ClaimLedgerEntry.model_validate(load_fixture("invalid/cl-rh-d0-promoted.yaml"))
