import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "zero_registry.schema.json"
FIXTURE_PATH = (
    ROOT
    / "fixtures"
    / "zero-registry"
    / "valid"
    / "zr-001-exp-ap-diagnostic.json"
)
INVALID_FIXTURE_ROOT = ROOT / "fixtures" / "zero-registry" / "invalid"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def zero_registry_validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    return Draft202012Validator(schema)


def validation_errors(path: Path):
    validator = zero_registry_validator()
    fixture = load_json(path)
    return sorted(validator.iter_errors(fixture), key=lambda error: list(error.path))


def test_zero_registry_schema_is_valid_draft_2020_12():
    schema = load_json(SCHEMA_PATH)

    Draft202012Validator.check_schema(schema)


def test_valid_zero_registry_fixture_passes_schema_validation():
    fixture = load_json(FIXTURE_PATH)
    errors = validation_errors(FIXTURE_PATH)

    assert errors == []
    assert fixture["registry_id"] == "HW-ZERO-AP-EXP-001"
    assert fixture["surfaces"][0]["conductor"] == 3
    assert fixture["surfaces"][0]["display_modulus"] == 3
    assert fixture["surfaces"][0]["zero_classes"][0]["location_claim"] == "critical_strip"


def test_invalid_zero_registry_missing_conductor_fails():
    errors = validation_errors(INVALID_FIXTURE_ROOT / "zr-missing-conductor.json")

    assert errors
    assert any("conductor" in error.message for error in errors)


def test_invalid_zero_registry_location_claim_fails():
    errors = validation_errors(INVALID_FIXTURE_ROOT / "zr-invalid-location-claim.json")

    assert errors
    assert any("proved_GRH_without_proof" in error.message for error in errors)
