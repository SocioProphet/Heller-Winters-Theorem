from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "manuscript" / "prime-weil-reformulation-outline.md"


class TestPrimeWeilManuscriptOutline(unittest.TestCase):
    def test_outline_exists(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("Prime-Weil Reformulation Manuscript Outline", text)
        self.assertIn("Claim class: outline only; no new theorem claim", text)

    def test_working_title_and_abstract_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("Prime-Window Variance, Base-10 Orbit Packets", text)
        self.assertIn("finite character-packet decomposition", text)
        self.assertIn("not a proof", text)

    def test_sections_cover_core_program(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "Section 2 — Prime-window variance and Parseval identity",
            "Section 3 — Base-10 orbit classification",
            "Section 4 — Non-cancelling characters",
            "Section 7 — Three locked gates",
            "Section 8 — Finite operator normality",
        ]:
            self.assertIn(token, text)

    def test_theorem_inventory_is_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "Var_P(W_K) = (1/|G_P|) sum_{chi != 1}",
            "n_nc(p) = (p - 1) / ord_p(10) - 1",
            "N_nc(P_k) = sum_j phi(P_{j-1}) * n_nc(p_j)",
            "||T_A|| = max_chi |lambda_chi|",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "no RH proof",
            "no GRH proof",
            "no Hilbert-Polya construction",
            "no unconditional variance bound",
            "no claim that finite diagnostics establish asymptotic behavior",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
