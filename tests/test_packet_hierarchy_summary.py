from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-013-packet-hierarchy-summary.md"


class TestPacketHierarchySummary(unittest.TestCase):
    def test_document_exists_and_is_summary(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-013", text)
        self.assertIn("compact finite hierarchy summary", text)
        self.assertIn("P = 2310", text)

    def test_partition_counts_sum_to_479(self) -> None:
        counts = [7, 40, 240, 192]
        self.assertEqual(sum(counts), 479)
        text = DOC.read_text(encoding="utf-8")
        for token in ["7 + 40 + 240 + 192 = 479", "phi(2310) - 1 = 480 - 1 = 479"]:
            self.assertIn(token, text)

    def test_energy_table_values_are_pinned(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "912.628197074576",
            "881.487346082066",
            "1575.759657835338",
            "12236.765876957472",
            "3923.097663316467",
            "31698.312041391291",
            "4214.224918349286",
            "37149.288448317449",
        ]:
            self.assertIn(token, text)

    def test_local_l_function_counts_are_corrected(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "p=7` full-orbit packet: 5 nontrivial local conductor-7 characters",
            "p=11` local packet: 9 nontrivial local conductor-11 characters",
            "5 + 4 = 9",
            "5 + 9 = 14",
            "not 5",
        ]:
            self.assertIn(token, text)

    def test_digit_cycle_boundary_is_preserved(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "complete finite digit-cycle cancellation is unconditional",
            "not, by itself, an unconditional bound for actual prime-window character sums",
            "HW-OPEN-010",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove an unconditional variance bound",
            "does not prove an asymptotic packet-energy ordering",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
