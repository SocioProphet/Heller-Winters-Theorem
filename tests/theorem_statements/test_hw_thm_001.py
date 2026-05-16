from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
THM = ROOT / "docs" / "theorem-statements" / "HW-THM-001-rh-envelope-target.md"
REGISTRY = ROOT / "docs" / "theorem-statements" / "identifier-reservations.md"
PRIME_CIRCLE = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-CIRCLE-001-primorial-wheel-correspondence.md"


def test_hw_thm_001_exists_and_is_target_grade():
    assert THM.exists()
    text = THM.read_text(encoding="utf-8")
    assert "HW-THM-001" in text
    assert "theorem-target" in text
    assert "NOT PROVED" in text
    assert "target-grade" in text
    assert "no theorem claim" in text


def test_hw_thm_001_states_rh_envelope_target():
    text = THM.read_text(encoding="utf-8")
    assert "psi(x)" in text
    assert "|psi(x) - x| <= C x^{1/2} (log x)^2" in text
    assert "psi(x) = x + O(x^{1/2} (log x)^2)" in text


def test_von_koch_boundary_present():
    text = THM.read_text(encoding="utf-8")
    assert "von Koch" in text
    assert "not a Heller-Winters contribution" in text
    assert "does not claim the equivalence" in text


def test_prime_circle_non_load_bearing_boundary_present():
    text = THM.read_text(encoding="utf-8")
    assert "HW-PRIME-CIRCLE-001" in text
    assert "NOT load-bearing" in text
    assert "NOT partial progress toward RH" in text
    assert "must not be cited as partial progress" in text
    assert PRIME_CIRCLE.exists(), "HW-PRIME-CIRCLE-001 must resolve on main branch content"


def test_grh_and_successors_reserved_not_active():
    text = THM.read_text(encoding="utf-8")
    assert "HW-THM-002" in text
    assert "GRH" in text
    assert "reserved" in text
    assert "not the first target" in text


def test_registry_records_target_and_anti_seed():
    assert REGISTRY.exists()
    text = REGISTRY.read_text(encoding="utf-8")
    assert "HW-THM-001" in text
    assert "active target; not proved" in text
    assert "HW-THM-002" in text
    assert "HW-THM-003" in text
    assert "HW-THM-004" in text
    assert "A-HW-THM-001" in text


def test_discharge_conditions_are_explicit():
    text = THM.read_text(encoding="utf-8")
    assert "Discharge conditions" in text
    assert "not rely on RH" in text
    assert "not rely on" in text
    assert "claim-boundary review" in text
