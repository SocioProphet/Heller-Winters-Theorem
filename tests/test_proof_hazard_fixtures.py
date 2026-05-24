from pathlib import Path

from bin.check_proof_hazard_fixtures import validate_fixture


FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "proof_hazards" / "auxiliary_zero_fallacy.rh-style.md"


def test_auxiliary_zero_fallacy_fixture_is_well_formed():
    assert validate_fixture(FIXTURE) == []
