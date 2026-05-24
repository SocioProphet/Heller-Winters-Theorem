from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-018-three-locked-gates.md"


class TestThreeLockedGates(unittest.TestCase):
    def test_document_exists_and_is_status_surface(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-018", text)
        self.assertIn("Three Locked Gates", text)
        self.assertIn("barrier summary / roadmap", text)

    def test_three_gates_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "Gate 1 — Coset Variance Theorem",
            "Gate 2 — Explicit Formula Packet-Energy Surrogate",
            "Gate 3 — Operator Spectral Radius",
        ]:
            self.assertIn(token, text)

    def test_operator_gate_uses_normal_spectral_radius_not_self_adjoint_core(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "raw finite convolution operator is normal, not necessarily self-adjoint",
            "||T_{P,K}^perp|| = max_{chi != 1} |psi_{W_K}(chi)|",
            "Self-adjointness may be useful for a symmetrized operator, but it is not the core finite fact",
        ]:
            self.assertIn(token, text)

    def test_explicit_formula_barrier_is_pinned(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in ["11088", "10^5544", "impossible", "truncation barrier"]:
            self.assertIn(token, text)

    def test_quotient_large_sieve_obstruction_is_pinned(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "quotient large sieve gives a real but insufficient gain",
            "standard large-sieve technology does not prove the Coset Variance Theorem",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove the Coset Variance Theorem",
            "does not construct a Hilbert-Polya operator",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
