from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-022-current-state-synthesis.md"


class TestPrimeWeilCurrentStateSynthesis(unittest.TestCase):
    def test_document_exists_and_is_synthesis(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-022", text)
        self.assertIn("Current-State Synthesis", text)
        self.assertIn("synthesis / manuscript-surface draft", text)

    def test_finite_theorem_surfaces_are_recorded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "n_nc(p) = (p - 1) / ord_p(10) - 1",
            "N_nc(P_k) = sum_j phi(P_{j-1}) * n_nc(p_j)",
            "||T_A|| = max_chi |lambda_chi|",
            "7 + 40 + 240 + 192 = 479",
        ]:
            self.assertIn(token, text)

    def test_three_locked_gates_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "Gate 1 — Coset variance theorem",
            "Gate 2 — Explicit formula surrogate",
            "Gate 3 — Operator spectral radius",
            "The square-root barrier remains intact",
        ]:
            self.assertIn(token, text)

    def test_negative_diagnostics_are_recorded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "q=37 orbit-quality model falsification",
            "Quotient large sieve",
            "Coset dispersion",
            "Cayley quotient spectral gap",
            "Explicit formula surrogate",
        ]:
            self.assertIn(token, text)

    def test_publication_framing_and_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "finite computable reformulation of the GRH square-root barrier",
            "does not prove RH",
            "does not prove GRH",
            "does not construct a Hilbert-Polya operator",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
