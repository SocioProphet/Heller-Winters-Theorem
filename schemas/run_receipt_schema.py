"""RunSpec and RunReceipt models for the Heller-Winters prime/operator lane."""

from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class RunSpec(BaseModel):
    """Declared run plan before execution."""

    model_config = ConfigDict(extra="forbid")

    runspec_id: str = Field(min_length=1)
    execution_mode: str = Field(min_length=1)
    operator_ids: list[str] = Field(default_factory=list)
    coordinate_convention: str | None = None
    window_schedule_id: str | None = None


class RunReceipt(BaseModel):
    """Receipt recording what actually executed."""

    model_config = ConfigDict(extra="forbid")

    run_receipt_id: str = Field(min_length=1)
    runspec_id: str = Field(min_length=1)
    execution_status: Literal["success", "failed", "partial"] = "success"
    output_artifact_ids: list[str] = Field(default_factory=list)
