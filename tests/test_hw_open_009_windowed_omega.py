import cmath
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "prime-operator-lane" / "windowed-omega-theorem-target.md"
REGISTER_NOTE = ROOT / "docs" / "prime-operator-lane" / "HW-OPEN-009-windowed-omega-register-note.md"


class TestHWOpen009WindowedOmega(unittest.TestCase):
    def test_target_document_exists_and_is_not_a_proof(self) -> None:
        self.assertTrue(TARGET.exists())
        text = TARGET.read_text(encoding="utf-8")
        self.assertIn("HW-OPEN-009", text)
        self.assertIn("proof-target document", text)
        self.assertIn("does not prove RH", text)
        self.assertIn("does not prove GRH", text)
        self.assertIn("does not prove the windowed Omega theorem", text)

    def test_windowed_omega_statement_is_present(self) -> None:
        text = TARGET.read_text(encoding="utf-8")
        for token in [
            "rho_0 = sigma_0 + i t_0",
            "sigma_0 > 1/2",
            "|psi_{W_K}(chi)| >= c 10^(K sigma_0)",
            "infinitely many `K`",
            "positive-density subsequence",
        ]:
            self.assertIn(token, text)

    def test_paths_and_obligations_are_pinned(self) -> None:
        text = TARGET.read_text(encoding="utf-8")
        for token in [
            "Path A — Direct phase route",
            "Path B — Cesaro / second-moment route",
            "same-real-part",
            "off-diagonal cross terms",
            "explicit-formula error",
            "Convert positive normalized second moment",
        ]:
            self.assertIn(token, text)

    def test_path_b_diagonal_cesaro_is_positive(self) -> None:
        delta = 0.1
        gamma = 14.1347
        rho_0 = complex(0.5 + delta, gamma)
        sigma_0 = rho_0.real
        c0 = abs((1 - 10 ** (-rho_0)) / rho_0)
        window_cesaro = c0**2
        terminal_scale_r = 10 ** (2 * sigma_0)
        terminal_scale_cesaro = c0**2 * terminal_scale_r / (terminal_scale_r - 1)
        self.assertGreater(window_cesaro, 0.0)
        self.assertGreater(terminal_scale_cesaro, 0.0)

    def test_path_b_partial_discharge_recorded(self) -> None:
        text = TARGET.read_text(encoding="utf-8")
        for token in [
            "This is a partial discharge of Path B at the diagonal-spine level only",
            "The diagonal contribution from the selected zero `rho_0` is positive",
            "C_0^2 > 0",
        ]:
            self.assertIn(token, text)
        path_b_fully_discharged = False
        self.assertFalse(path_b_fully_discharged)

    def test_variance_route_boundary_is_pinned(self) -> None:
        text = TARGET.read_text(encoding="utf-8")
        for token in [
            "HW-PRIME-WEIL-005",
            "unconditional critical-scale variance upper bound",
            "does not by itself supply the missing unconditional upper bound",
            "Var_P(W_K)",
        ]:
            self.assertIn(token, text)

    def test_register_note_exists_and_preserves_non_claims(self) -> None:
        self.assertTrue(REGISTER_NOTE.exists())
        text = REGISTER_NOTE.read_text(encoding="utf-8")
        for token in [
            "HW-OPEN-009",
            "windowed Omega theorem",
            "Canonical target document",
            "promising partial route",
            "does not prove the unconditional variance bound",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
