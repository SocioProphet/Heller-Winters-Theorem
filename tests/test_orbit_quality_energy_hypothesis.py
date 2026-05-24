from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-OPEN-013-orbit-quality-energy-hypothesis.md"


class TestOrbitQualityEnergyHypothesis(unittest.TestCase):
    def test_document_exists_and_is_open_hypothesis(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-OPEN-013", text)
        self.assertIn("open falsifiable hypothesis surface", text)
        self.assertIn("conjectural diagnostic", text)

    def test_q37_values_are_pinned(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "q = 37",
            "ord_37(10) = 3",
            "I_37 = (37-1)/3 = 12",
            "n_nc(37) = 11",
        ]:
            self.assertIn(token, text)

    def test_model_function_not_selected_yet(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("does not select a final model function", text)
        self.assertIn("redacted", text)
        self.assertIn("The next computation must supply it explicitly", text)

    def test_support_and_falsification_criteria_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "What would count as support",
            "What would falsify or refine it",
            "the model function `F` is fixed before measurement",
            "finite-window prime-race oscillations dominate",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove a p=37 packet-energy prediction",
            "does not claim that orbit quality alone determines energy concentration",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
