from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-OPEN-012-detection-threshold.md"


class TestDetectionThreshold(unittest.TestCase):
    def test_document_exists_and_is_open_problem(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-OPEN-012", text)
        self.assertIn("open diagnostic threshold problem", text)
        self.assertIn("explicit-formula threshold surface", text)

    def test_finite_scale_values_are_recorded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "2.952784650337",
            "3.923097663316",
            "3.169831204139",
            "3.578881287026",
            "3.051196916722",
        ]:
            self.assertIn(token, text)

    def test_ratio_inversion_values_are_recorded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "1.000000000000",
            "1.074208515825",
            "1.171964248437",
            "0.852556056493",
        ]:
            self.assertIn(token, text)

    def test_detection_threshold_heuristic_is_bounded(self) -> None:
        delta = 0.1
        current_depths = (2, 3, 4, 5)
        for depth in current_depths:
            off_line_signal = 10 ** (2 * delta * depth) / (depth**2)
            self.assertLess(off_line_signal, 1.0)
        detectable_depth = 20
        self.assertGreater(10 ** (2 * delta * detectable_depth) / (detectable_depth**2), 1.0)
        self.assertGreater(detectable_depth, max(current_depths))

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not rule out off-line zeros",
            "does not prove the explicit-formula surrogate exists",
            "does not prove an unconditional variance bound",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
