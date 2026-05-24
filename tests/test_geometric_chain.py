import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-008-geometric-chain.md"


class TestGeometricChain(unittest.TestCase):
    def test_document_exists_and_nonclaims_are_present(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-008", text)
        self.assertIn("does not prove RH", text)
        self.assertIn("does not prove GRH", text)
        self.assertIn("does not claim the Rodin active circuit is literally a hyperbolic geodesic", text)
        self.assertIn("does not close the square-root barrier", text)

    def test_circle_hyperbola_tangency_at_one_zero(self) -> None:
        circle_point = (math.cos(0.0), math.sin(0.0))
        hyperbola_point = (math.cosh(0.0), math.sinh(0.0))
        circle_tangent = (-math.sin(0.0), math.cos(0.0))
        hyperbola_tangent = (math.sinh(0.0), math.cosh(0.0))
        self.assertEqual(circle_point, (1.0, 0.0))
        self.assertEqual(hyperbola_point, (1.0, 0.0))
        self.assertEqual(circle_tangent, (0.0, 1.0))
        self.assertEqual(hyperbola_tangent, (0.0, 1.0))

    def test_unit_identities_hold(self) -> None:
        theta = 0.731
        u = 1.23
        self.assertAlmostEqual(math.cos(theta) ** 2 + math.sin(theta) ** 2, 1.0, places=12)
        self.assertAlmostEqual(math.cosh(u) ** 2 - math.sinh(u) ** 2, 1.0, places=12)

    def test_critical_line_has_unit_amplitude(self) -> None:
        delta = 0.0
        log_x = 17.0
        amplitude = math.exp(delta * log_x)
        self.assertEqual(amplitude, 1.0)

    def test_off_critical_amplitude_has_hyperbolic_parameterization(self) -> None:
        delta = 0.1
        log_x = 17.0
        u = delta * log_x
        amplitude = math.exp(u)
        self.assertAlmostEqual(amplitude, math.cosh(u) + math.sinh(u), places=12)
        self.assertGreater(amplitude, 1.0)

    def test_document_records_precision_corrections(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "not literally a geodesic on the boundary",
            "central-geodesic analogue",
            "geometry-language hygiene",
            "structural dictionary, not a literal Poincare-disk placement theorem",
        ]:
            self.assertIn(token, text)

    def test_document_records_midy_and_character_duality(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "digit_sum(1/p) = 9 * ord_p(10) / 2",
            "digit-pair law and the finite character-cancellation theorem are dual descriptions",
            "actual Richter-window character sum is harder",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
