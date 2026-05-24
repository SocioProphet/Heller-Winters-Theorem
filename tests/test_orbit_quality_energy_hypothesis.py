from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-OPEN-013-orbit-quality-energy-hypothesis.md"


def predicted_nc_cancel_ratio(q: int) -> float:
    orders = {11: 2, 13: 6, 37: 3}
    return 1.0 + 0.3439 / orders[q]


class TestOrbitQualityEnergyHypothesis(unittest.TestCase):
    def test_document_exists_and_is_open_hypothesis(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-OPEN-013", text)
        self.assertIn("pre-registered falsifiable hypothesis surface", text)
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

    def test_model_function_is_preregistered(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "R(q) = 1 + 0.3439 / d_q",
            "model is now fixed and must not be changed after the q=37 computation",
            "committed before the q=37 measurement",
        ]:
            self.assertIn(token, text)

    def test_model_prediction_q37_preregistered(self) -> None:
        self.assertLess(abs(predicted_nc_cancel_ratio(37) - 1.1146333333333333), 0.001)

    def test_model_prediction_q13_preregistered(self) -> None:
        self.assertLess(abs(predicted_nc_cancel_ratio(13) - 1.0573166666666666), 0.001)

    def test_support_and_falsification_criteria_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "What would count as support",
            "What would falsify or refine it",
            "the model function remains fixed before measurement",
            "finite-window prime-race oscillations dominate",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove the p=37 packet-energy prediction",
            "does not claim that orbit quality alone determines energy concentration",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
