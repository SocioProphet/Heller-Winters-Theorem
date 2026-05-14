"""
tests/test_a2_correction.py

Focused test for the A2 corrected minimality sketch.

Validates:
 1. cl-003-a2-correction.yaml is a well-formed C1 ClaimLedgerEntry.
 2. docs/a2-corrected-minimality-sketch.md contains the three required
    correction statements:
    (a) cubic invariant on C^3 withdrawn;
    (b) Hermitian + alternating volume form as replacement, with no
        symmetric bilinear admitted as an additional replacement;
    (c) non-theorem / non-YM-mass-gap boundary explicit.

These assertions correspond to the review-mandated corrections:
 - d_{abc} on defining rep C^3 is wrong; it lives on the adjoint, dim 8;
 - correct invariant data for SU(3) on V_A=C^3 are H_A plus epsilon in wedge^3 V*;
 - the sketch is not a theorem and does not close the Yang-Mills mass gap.
"""

from pathlib import Path
import re
import warnings

import pytest
import yaml


REPO_ROOT = Path(__file__).parent.parent
FIXTURE_PATH = REPO_ROOT / "fixtures" / "valid" / "cl-003-a2-correction.yaml"
SKETCH_PATH = REPO_ROOT / "docs" / "a2-corrected-minimality-sketch.md"


@pytest.fixture
def cl003_fixture():
    assert FIXTURE_PATH.exists(), (
        f"Fixture not found: {FIXTURE_PATH}. "
        f"Expected cl-003-a2-correction.yaml in fixtures/valid/."
    )
    with open(FIXTURE_PATH, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


@pytest.fixture
def sketch_text():
    assert SKETCH_PATH.exists(), (
        f"Correction sketch not found: {SKETCH_PATH}. "
        f"Expected a2-corrected-minimality-sketch.md in docs/."
    )
    return SKETCH_PATH.read_text(encoding="utf-8")


class TestCL003FixtureSchema:
    def test_fixture_loads(self, cl003_fixture):
        assert cl003_fixture is not None

    def test_claim_id(self, cl003_fixture):
        assert cl003_fixture.get("claim_id") == "CL-003", (
            f"Expected claim_id='CL-003'. Got: {cl003_fixture.get('claim_id')!r}"
        )

    def test_claim_class_is_c1(self, cl003_fixture):
        assert cl003_fixture.get("claim_class") == "C1", (
            f"A2 correction must be C1 (analytically grounded). "
            f"Got: {cl003_fixture.get('claim_class')!r}. "
            f"C2 would require a RunReceipt; no computation is claimed here."
        )

    def test_no_run_receipts(self, cl003_fixture):
        receipts = cl003_fixture.get("run_receipt_ids", [])
        assert len(receipts) == 0, (
            f"C1 claim must have no run_receipt_ids. Got: {receipts}"
        )

    def test_no_run_trace_artifacts(self, cl003_fixture):
        run_trace_types = {
            "CandidateTrace",
            "ChannelTrace",
            "ScoreTrace",
            "ObservableTrace",
            "ResidualTrace",
            "RunReceipt",
        }
        artifact_refs = cl003_fixture.get("artifact_refs", [])
        bad = [ref for ref in artifact_refs if ref.get("artifact_type") in run_trace_types]
        assert len(bad) == 0, f"C1 claim cannot reference run-trace artifacts: {bad}"

    def test_stage2_not_claimed(self, cl003_fixture):
        statement = cl003_fixture.get("statement", "")
        forbidden_phrases = [
            "proves A2",
            "confirms theorem",
            "establishes naturality",
            "I-12 eligible",
            "YM mass gap",
            "mass gap closed",
            "Yang-Mills proven",
        ]
        for phrase in forbidden_phrases:
            assert phrase.lower() not in statement.lower(), (
                f"Fixture statement contains forbidden phrase: {phrase!r}. "
                f"This is a C1 correction note, not a theorem."
            )

    def test_manuscript_editing_rule_set(self, cl003_fixture):
        rule = cl003_fixture.get("manuscript_editing_rule")
        assert rule is True, (
            f"manuscript_editing_rule should be true: the original d-symbol-on-C^3 "
            f"claim is forbidden from manuscript theorem statements. Got: {rule!r}"
        )

    def test_required_fields_present(self, cl003_fixture):
        required = ["claim_id", "claim_class", "statement"]
        for field in required:
            assert field in cl003_fixture, f"Missing required field: {field!r}"


class TestSketchCorrectionContent:
    def test_sketch_loads(self, sketch_text):
        assert len(sketch_text.strip()) > 0

    def test_correction_a_cubic_invariant_withdrawn(self, sketch_text):
        text_lower = sketch_text.lower()
        required_signals = [
            "cubic",
            "fundamental",
            "adjoint",
        ]
        for signal in required_signals:
            assert signal in text_lower, (
                f"Correction (a) incomplete: expected signal {signal!r}. "
                f"The sketch must distinguish the adjoint cubic tensor from the "
                f"SU(3) fundamental representation."
            )
        withdrawal_signals = ["withdrawn", "false", "incorrect", "not `c^3`", "not c^3"]
        assert any(signal in text_lower for signal in withdrawal_signals), (
            "Correction (a) not found: the sketch must explicitly withdraw or reject "
            "the cubic invariant claim on the SU(3) fundamental."
        )

    def test_correction_b_hermitian_alternating_volume_replacement(self, sketch_text):
        text_lower = sketch_text.lower()
        hermitian_signals = ["hermitian", "h_a", "h(v,w)"]
        assert any(sig in text_lower for sig in hermitian_signals), (
            "Correction (b) incomplete: replacement invariant data must include "
            "the Hermitian form H_A."
        )

        volume_signals = [
            "alternating",
            "volume form",
            "determinant",
            "wedge^3",
            "lambda^3",
            "\\lambda^3",
            "λ³",
            "Λ³".lower(),
            "epsilon",
            "ε",
        ]
        assert any(sig.lower() in text_lower for sig in volume_signals), (
            "Correction (b) incomplete: replacement invariant data must include "
            "the alternating determinant/volume form epsilon in wedge^3 V*."
        )

        # The correction is allowed, and indeed required, to mention symmetric
        # bilinear forms as excluded structure. It must not propose such a form
        # as a replacement invariant.
        forbidden_patterns = [
            r"replacement[^.]{0,80}symmetric\s+bilinear",
            r"symmetric\s+bilinear[^.]{0,80}replacement",
            r"preserves[^.]{0,80}symmetric\s+bilinear",
        ]
        for pattern in forbidden_patterns:
            assert not re.search(pattern, text_lower), (
                "Correction (b) violation: sketch appears to propose a symmetric "
                "bilinear form as replacement. Correct replacement is Hermitian "
                "+ alternating volume, with symmetric bilinear explicitly excluded."
            )

        exclusion_signals = [
            "no additional symmetric bilinear",
            "does not preserve any symmetric bilinear",
            "no symmetric bilinear",
            "exclude that orthogonal structure",
        ]
        assert any(sig in text_lower for sig in exclusion_signals), (
            "Correction (b) incomplete: the sketch must explicitly exclude the "
            "symmetric bilinear / orthogonal branch."
        )

    def test_correction_c_non_theorem_non_ym_mass_gap_boundary(self, sketch_text):
        text_lower = sketch_text.lower()
        boundary_signals = [
            "non-claim",
            "does not claim",
            "does not prove",
            "not a theorem",
            "not a proof",
            "sketch-level",
            "boundary",
        ]
        assert any(sig in text_lower for sig in boundary_signals), (
            "Correction (c) not found: the sketch must carry explicit non-theorem "
            "and non-Yang-Mills-mass-gap boundary language."
        )

        ym_signals = ["yang--mills", "yang-mills", "mass-gap", "mass gap", "ym"]
        if any(sig in text_lower for sig in ym_signals):
            negation_signals = [
                "not",
                "does not",
                "no claim",
                "outside scope",
                "non-claim",
                "boundary",
            ]
            ym_with_negation = False
            for ym_sig in ym_signals:
                for match in re.finditer(re.escape(ym_sig), text_lower):
                    start = max(0, match.start() - 200)
                    end = min(len(text_lower), match.end() + 200)
                    window = text_lower[start:end]
                    if any(neg in window for neg in negation_signals):
                        ym_with_negation = True
                        break
            assert ym_with_negation, (
                "Correction (c): Yang-Mills or mass gap is mentioned but not in "
                "a clear non-claim context."
            )


class TestFixtureSketchConsistency:
    def test_fixture_statement_consistent_with_corrections(self, cl003_fixture):
        statement = cl003_fixture.get("statement", "")
        forbidden = [
            "d-symbol on c^3",
            "d-symbol on c³",
            "d_{abc} on the defining",
            "symmetric cubic on v_a",
            "dim v_a = milnor",
        ]
        for phrase in forbidden:
            assert phrase.lower() not in statement.lower(), (
                f"Fixture statement contains language from the original incorrect claim: "
                f"{phrase!r}."
            )

    def test_fixture_references_sketch_or_operator(self, cl003_fixture):
        artifact_refs = cl003_fixture.get("artifact_refs", [])
        operator_refs = cl003_fixture.get("operator_refs", [])
        has_evidence = len(artifact_refs) > 0 or len(operator_refs) > 0
        if not has_evidence:
            warnings.warn(
                "CL-003 has no artifact_refs or operator_refs. A correction claim "
                "should reference its evidence basis.",
                UserWarning,
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
