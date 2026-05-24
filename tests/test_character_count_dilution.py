from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-OPEN-011-character-count-dilution.md"


class TestCharacterCountDilution(unittest.TestCase):
    def test_document_exists_and_is_open_problem(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-OPEN-011", text)
        self.assertIn("open transition problem", text)
        self.assertIn("finite counting theorem surface", text)

    def test_exact_layer_count_formulas_for_p11(self) -> None:
        phi_p = 48
        q = 11
        old_layer = phi_p
        full_group = phi_p * (q - 1)
        new_layer = phi_p * (q - 2)
        nontrivial_total = full_group - 1
        self.assertEqual(old_layer, 48)
        self.assertEqual(full_group, 480)
        self.assertEqual(new_layer, 432)
        self.assertAlmostEqual(new_layer / nontrivial_total, 432 / 479, places=15)
        self.assertAlmostEqual(old_layer / full_group, 0.1, places=15)

    def test_local_p11_count_baseline(self) -> None:
        local_cancelling = 5
        local_noncancelling = 4
        self.assertAlmostEqual(local_noncancelling / (local_cancelling + local_noncancelling), 4 / 9, places=15)
        self.assertEqual(48 * local_cancelling, 240)
        self.assertEqual(48 * local_noncancelling, 192)

    def test_finite_p11_values_are_recorded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "0.938218008866",
            "0.961859768615",
            "0.967468868352",
            "0.444444444444",
            "0.462182505791",
            "0.483889986895",
        ]:
            self.assertIn(token, text)

    def test_dilution_interpretation_is_bounded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "character-count dilution",
            "energy follows character-count dilution asymptotically",
            "orbit type of `q`",
            "renormalized packet statistic",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove an asymptotic character-count dilution theorem",
            "does not prove an asymptotic Chebyshev-bias theorem",
            "does not claim that the newest primorial layer always dominates variance",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
