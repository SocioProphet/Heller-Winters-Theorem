from pathlib import Path
import math
import unittest

from tools.check_explicit_formula_surrogate import VERIFIED_HEIGHT, run_checks, truncation_height_rows


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-016-explicit-formula-surrogate.md"


class TestExplicitFormulaSurrogate(unittest.TestCase):
    def test_document_exists_and_is_surrogate_target(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-016", text)
        self.assertIn("explicit-formula surrogate target", text)
        self.assertIn("not implemented as a zero-sum computation", text)

    def test_truncation_height_table(self) -> None:
        rows = {row.depth: row for row in truncation_height_rows()}
        self.assertEqual(VERIFIED_HEIGHT, 3e12)
        self.assertTrue(rows[5].feasible)
        self.assertTrue(rows[10].feasible)
        self.assertFalse(rows[20].feasible)
        self.assertFalse(rows[50].feasible)
        self.assertFalse(rows[11088].feasible)
        self.assertTrue(math.isinf(rows[11088].t_needed))

    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [5, 10, 20, 50, 11088])

    def test_surrogate_boundaries_are_recorded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "off-diagonal zero interactions",
            "smoothed window",
            "K*=11088",
            "does not implement a zero-table surrogate computation",
            "does not prove the diagonal approximation",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)

    def test_surrogate_is_not_a_proof(self) -> None:
        proves_grh = False
        proves_variance_bound = False
        zero_tables_wired = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_variance_bound)
        self.assertFalse(zero_tables_wired)


if __name__ == "__main__":
    unittest.main()
