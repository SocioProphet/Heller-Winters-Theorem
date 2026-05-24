import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "zero_registry.schema.json"
VALID_FIXTURE_ROOT = ROOT / "fixtures" / "zero-registry" / "valid"
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


def test_all_valid_zero_registry_fixtures_pass_schema_validation():
    fixture_paths = sorted(VALID_FIXTURE_ROOT.glob("*.json"))

    assert fixture_paths

    for fixture_path in fixture_paths:
        errors = validation_errors(fixture_path)
        assert errors == [], fixture_path.name


def test_valid_exp_ap_fixture_preserves_expected_bookkeeping():
    fixture = load_json(VALID_FIXTURE_ROOT / "zr-001-exp-ap-diagnostic.json")

    assert fixture["registry_id"] == "HW-ZERO-AP-EXP-001"
    assert fixture["surfaces"][0]["conductor"] == 3
    assert fixture["surfaces"][0]["display_modulus"] == 3
    assert fixture["surfaces"][0]["zero_classes"][0]["location_claim"] == "critical_strip"


def test_valid_p210_fixture_preserves_conductor_boundary():
    fixture = load_json(VALID_FIXTURE_ROOT / "zr-002-p210-character-surface.json")
    surface = fixture["surfaces"][0]

    assert fixture["registry_id"] == "HW-ZERO-P210-CHARACTER-001"
    assert surface["display_modulus"] == 210
    assert surface["conductor"] == 105
    assert surface["primitive_status"] == "induced"
    assert surface["conductor"] != surface["display_modulus"]


def test_invalid_zero_registry_missing_conductor_fails():
    errors = validation_errors(INVALID_FIXTURE_ROOT / "zr-missing-conductor.json")

    assert errors
    assert any("conductor" in error.message for error in errors)


def test_invalid_zero_registry_location_claim_fails():
    errors = validation_errors(INVALID_FIXTURE_ROOT / "zr-invalid-location-claim.json")

    assert errors
    assert any("proved_GRH_without_proof" in error.message for error in errors)
