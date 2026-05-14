"""Evidence artifact types for the Heller-Winters prime/operator lane."""

from __future__ import annotations

from enum import Enum
import re
from pydantic import BaseModel, ConfigDict, Field, field_validator


class ArtifactType(str, Enum):
    DefinitionArtifact = "DefinitionArtifact"
    OperatorArtifact = "OperatorArtifact"
    RunSpec = "RunSpec"
    RunReceipt = "RunReceipt"
    CandidateTrace = "CandidateTrace"
    ChannelTrace = "ChannelTrace"
    ScoreTrace = "ScoreTrace"
    ObservableTrace = "ObservableTrace"
    ResidualTrace = "ResidualTrace"
    ControlTrace = "ControlTrace"
    PerturbationTrace = "PerturbationTrace"
    FigureArtifact = "FigureArtifact"
    ProofArtifact = "ProofArtifact"
    ClaimLedgerEntry = "ClaimLedgerEntry"


C1_ALLOWED_ARTIFACT_TYPES = {
    ArtifactType.DefinitionArtifact,
    ArtifactType.OperatorArtifact,
    ArtifactType.ProofArtifact,
}

RUN_TRACE_ARTIFACT_TYPES = {
    ArtifactType.CandidateTrace,
    ArtifactType.ChannelTrace,
    ArtifactType.ScoreTrace,
    ArtifactType.ObservableTrace,
    ArtifactType.ResidualTrace,
}

C2_REQUIRED_TRACE_TYPES = {
    ArtifactType.CandidateTrace,
    ArtifactType.ChannelTrace,
    ArtifactType.ScoreTrace,
    ArtifactType.ObservableTrace,
}


def parse_schema_version(version: str) -> tuple[int, ...]:
    """Parse a simple schema version such as v0.1 into a comparable tuple."""
    match = re.fullmatch(r"v?(\d+(?:\.\d+)*)", version.strip())
    if not match:
        raise ValueError(f"Invalid schema version '{version}'. Expected form like 'v0.1'.")
    return tuple(int(part) for part in match.group(1).split("."))


def version_at_least(version: str, minimum: str = "v0.1") -> bool:
    """Return whether version is at least minimum under tuple comparison."""
    return parse_schema_version(version) >= parse_schema_version(minimum)


class ArtifactRef(BaseModel):
    """Reference to an evidence artifact."""

    model_config = ConfigDict(extra="forbid")

    artifact_id: str = Field(min_length=1)
    artifact_type: ArtifactType
    version: str = Field(min_length=1)

    @field_validator("version")
    @classmethod
    def version_must_be_parseable(cls, value: str) -> str:
        parse_schema_version(value)
        return value
