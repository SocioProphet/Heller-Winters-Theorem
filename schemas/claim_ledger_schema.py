"""Executable claim-ledger schema for the Heller-Winters prime/operator lane."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Mapping

from pydantic import BaseModel, ConfigDict, Field, model_validator

from schemas.artifact_schema import (
    ArtifactRef,
    ArtifactType,
    C1_ALLOWED_ARTIFACT_TYPES,
    C2_REQUIRED_TRACE_TYPES,
    RUN_TRACE_ARTIFACT_TYPES,
    version_at_least,
)
from schemas.run_receipt_schema import RunReceipt, RunSpec


class ClaimClass(str, Enum):
    C0 = "C0"  # definitional / setup
    C1 = "C1"  # analytically grounded
    C2 = "C2"  # computationally evidenced
    C3 = "C3"  # theorem-level / proof-backed
    D0 = "D0"  # diagnostic / demoted; prohibited from theorem or abstract use
    E0 = "E0"  # exploratory / excluded from claim-bearing lane


DEFAULT_OPERATOR_REGISTRY: dict[str, str] = {
    "COORD-LOG-001": "v0.1",
    "COORD-JAC-001": "v0.1",
    "CAND-WINDOW-001": "v0.1",
    "FILTER-WHEEL-001": "v0.1",
    "FILTER-DIV-001": "v0.1",
    "CHANNEL-RESIDUE-001": "v0.1",
    "CHANNEL-SHELL-001": "v0.1",
    "SCORE-HARM-001": "v0.1",
    "OBS-COUNT-001": "v0.1",
    "OBS-CHEB-001": "v0.1",
    "RESID-LI-001": "v0.1",
    "RESID-RH-DIAG-001": "v0.1",
    "CERT-RUN-001": "v0.1",
    "CONTROL-NEG-001": "v0.1",
    "PERTURB-SCHEDULE-001": "v0.1",
}

D0_LOCKED_OPERATORS = {"RESID-RH-DIAG-001"}


def validate_operator_refs(
    operator_refs: list[str],
    operator_registry: Mapping[str, str] = DEFAULT_OPERATOR_REGISTRY,
    minimum_version: str = "v0.1",
) -> None:
    """Validate that every operator is registered at or above the minimum version."""
    missing = [operator_id for operator_id in operator_refs if operator_id not in operator_registry]
    if missing:
        raise ValueError(
            f"Operator reference(s) not found in registry: {missing}. "
            f"All referenced operators must be registered at version >= {minimum_version}."
        )

    stale = [
        operator_id
        for operator_id in operator_refs
        if not version_at_least(operator_registry[operator_id], minimum_version)
    ]
    if stale:
        raise ValueError(
            f"Operator reference(s) below required registry version {minimum_version}: {stale}."
        )


class ClaimLedgerEntry(BaseModel):
    """Claim-ledger entry with executable C1/C2/D0 boundary validation."""

    model_config = ConfigDict(extra="forbid")

    claim_id: str = Field(min_length=1)
    claim_class: ClaimClass
    statement: str = Field(min_length=1)
    operator_refs: list[str] = Field(default_factory=list)
    artifact_refs: list[ArtifactRef] = Field(default_factory=list)
    run_receipt_ids: list[str] = Field(default_factory=list)
    demotion_reason: str | None = None
    manuscript_editing_rule: bool = False
    promoted_from: ClaimClass | None = None
    created: datetime
    last_modified: datetime

    @model_validator(mode="after")
    def enforce_claim_boundary(self) -> "ClaimLedgerEntry":
        validate_operator_refs(self.operator_refs)

        if self.claim_class in {ClaimClass.C1, ClaimClass.C2} and self.promoted_from == ClaimClass.D0:
            raise ValueError(
                "D0 claims cannot be promoted in place to C1 or C2. "
                "D0 promotion rule: create a new ClaimLedgerEntry instead of modifying the D0 entry."
            )

        if self.claim_class == ClaimClass.C1:
            if self.run_receipt_ids:
                raise ValueError(
                    "C1 claim cannot reference run_receipt_ids. "
                    "C1 boundary rule: analytically grounded claims cannot carry computational run receipts; "
                    "use C2 for computational evidence."
                )

            bad_artifacts = [
                ref
                for ref in self.artifact_refs
                if ref.artifact_type not in C1_ALLOWED_ARTIFACT_TYPES
            ]
            if bad_artifacts:
                raise ValueError(
                    "C1 claim can only reference DefinitionArtifact, OperatorArtifact, or ProofArtifact. "
                    f"Invalid artifact(s): {[(ref.artifact_id, ref.artifact_type.value) for ref in bad_artifacts]}."
                )

            bad_traces = [
                ref for ref in self.artifact_refs if ref.artifact_type in RUN_TRACE_ARTIFACT_TYPES
            ]
            if bad_traces:
                raise ValueError(
                    "C1 claim cannot reference run-trace artifacts: "
                    f"{[ref.artifact_id for ref in bad_traces]}. "
                    "C1 is analytically grounded; trace artifacts imply computational evidence, "
                    "which requires C2 claim class."
                )

        if self.claim_class == ClaimClass.C2:
            if not self.run_receipt_ids:
                raise ValueError(
                    "Missing field run_receipt_ids: C2 claim requires at least one run_receipt_id. "
                    "C2 promotion rule: computational evidence is mandatory. "
                    "Demote to C1 or provide a RunReceipt."
                )

            has_required_trace = any(
                ref.artifact_type in C2_REQUIRED_TRACE_TYPES for ref in self.artifact_refs
            )
            if not has_required_trace:
                raise ValueError(
                    "C2 claim requires at least one linked trace artifact of type "
                    "CandidateTrace, ChannelTrace, ScoreTrace, or ObservableTrace. "
                    "C2 promotion rule: computational claims require trace evidence."
                )

            d0_locked_used = sorted(set(self.operator_refs) & D0_LOCKED_OPERATORS)
            if d0_locked_used:
                raise ValueError(
                    f"D0-locked operator(s) cannot support a C2 claim: {d0_locked_used}. "
                    "Operator RESID-RH-DIAG-001 has D0 status; RH-shaped diagnostics may not be "
                    "promoted to C2 as residual evidence. Create a separate D0 ClaimLedgerEntry "
                    "with an explicit demotion_reason."
                )

        if self.claim_class == ClaimClass.D0:
            if not self.demotion_reason:
                raise ValueError(
                    "D0 claim requires explicit demotion_reason. "
                    "D0 entries may not be anonymous."
                )
            if not self.manuscript_editing_rule:
                raise ValueError(
                    "D0 claim requires manuscript_editing_rule=true. "
                    "D0 editing rule: no D0 claim may appear in a theorem statement or abstract."
                )

        return self


def validate_claim_references(
    entry: ClaimLedgerEntry,
    *,
    run_receipts: Mapping[str, RunReceipt],
    run_specs: Mapping[str, RunSpec],
    operator_registry: Mapping[str, str] = DEFAULT_OPERATOR_REGISTRY,
) -> None:
    """Cross-artifact validation that cannot be enforced by a single ledger entry."""

    validate_operator_refs(entry.operator_refs, operator_registry=operator_registry)

    if entry.claim_class != ClaimClass.C2:
        return

    for run_receipt_id in entry.run_receipt_ids:
        receipt = run_receipts.get(run_receipt_id)
        if receipt is None:
            raise ValueError(
                f"C2 claim references missing RunReceipt '{run_receipt_id}'. "
                "C2 promotion rule: every run_receipt_id must resolve to a RunReceipt."
            )

        runspec = run_specs.get(receipt.runspec_id)
        if runspec is None:
            raise ValueError(
                f"RunReceipt '{run_receipt_id}' references missing RunSpec '{receipt.runspec_id}'. "
                "C2 promotion rule: RunReceipt must reference a RunSpec."
            )

        if not runspec.operator_ids:
            raise ValueError(
                f"RunSpec '{runspec.runspec_id}' has no declared operator_ids list. "
                "C2 promotion rule: RunSpec must declare operator_ids and each must be registered."
            )

        validate_operator_refs(runspec.operator_ids, operator_registry=operator_registry)
