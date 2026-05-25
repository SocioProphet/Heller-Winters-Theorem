from pathlib import Path
import unittest

from tools.check_finite_character_operator import (
    MODULUS,
    TOLERANCE,
    build_dlog_table,
    character_indices,
    eigenvalue_for_character,
    inversion_symmetric_kernel,
    raw_prime_residue_kernel,
)


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-021-finite-operator-normality.md"


def max_adjoint_error(kernel, modulus=MODULUS):
    return max(abs(kernel[h] - kernel[pow(h, -1, modulus)]) for h in kernel)


def spectral_radius_from_characters(kernel) -> float:
    dlog = build_dlog_table()
    return max(abs(eigenvalue_for_character(index, kernel, dlog)) for index in character_indices())


def nontrivial_spectral_radius_from_characters(kernel) -> float:
    dlog = build_dlog_table()
    return max(abs(eigenvalue_for_character(index, kernel, dlog)) for index in character_indices() if index != (0, 0, 0))


class TestFiniteOperatorNormality(unittest.TestCase):
    def test_document_exists_and_is_finite_theorem(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-021", text)
        self.assertIn("finite theorem surface", text)
        self.assertIn("theorem-grade finite abelian convolution fact", text)

    def test_raw_kernel_not_self_adjoint_but_has_character_spectral_radius(self) -> None:
        raw = raw_prime_residue_kernel()
        self.assertGreater(max_adjoint_error(raw), TOLERANCE)
        self.assertGreater(spectral_radius_from_characters(raw), 0.0)
        self.assertGreater(nontrivial_spectral_radius_from_characters(raw), 0.0)

    def test_symmetrized_kernel_is_self_adjoint_special_case(self) -> None:
        sym = inversion_symmetric_kernel()
        self.assertLessEqual(max_adjoint_error(sym), TOLERANCE)
        self.assertGreater(spectral_radius_from_characters(sym), 0.0)

    def test_document_pins_norm_identity(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "T_A^* T_A = T_A T_A^*",
            "||T_A|| = max_chi |lambda_chi|",
            "||T_A^perp|| = max_{chi != 1} |lambda_chi|",
            "||T_{P,K}^perp|| = max_{chi != 1} |psi_{W_K}(chi)|",
        ]:
            self.assertIn(token, text)

    def test_infinite_boundary_and_non_claims(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "This theorem is finite",
            "does not construct a Hilbert-Polya operator",
            "does not prove normality of an infinite limiting operator",
            "does not prove an operator-norm bound at GRH scale",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
