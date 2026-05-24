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


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def test_zero_registry_schema_is_valid_draft_2020_12():
    schema = load_json(SCHEMA_PATH)

    Draft202012Validator.check_schema(schema)


def test_valid_zero_registry_fixture_passes_schema_validation():
    schema = load_json(SCHEMA_PATH)
    fixture = load_json(FIXTURE_PATH)
    validator = Draft202012Validator(schema)

    errors = sorted(validator.iter_errors(fixture), key=lambda error: error.path)

    assert errors == []
    assert fixture["registry_id"] == "HW-ZERO-AP-EXP-001"
    assert fixture["surfaces"][0]["conductor"] == 3
    assert fixture["surfaces"][0]["display_modulus"] == 3
    assert fixture["surfaces"][0]["zero_classes"][0]["location_claim"] == "critical_strip"
