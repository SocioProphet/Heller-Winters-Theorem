from pathlib import Path
import unittest

from tools.check_finite_character_operator import (
    MODULUS,
    TOLERANCE,
    inversion_symmetric_kernel,
    kernel_is_inversion_symmetric,
    raw_prime_residue_kernel,
    reduced_residues,
)


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-OPEN-015-operator-domain-self-adjointness.md"


def max_adjoint_error(kernel, modulus=MODULUS):
    return max(abs(kernel[h] - kernel[pow(h, -1, modulus)]) for h in kernel)


class TestOperatorDomainSelfAdjointness(unittest.TestCase):
    def test_document_exists_and_is_open_target(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-OPEN-015", text)
        self.assertIn("Operator Domain and Essential Self-Adjointness Target", text)
        self.assertIn("does not prove essential self-adjointness", text)

    def test_finite_kernel_adjoint_criterion(self) -> None:
        raw = raw_prime_residue_kernel()
        sym = inversion_symmetric_kernel()
        self.assertGreater(max_adjoint_error(raw), TOLERANCE)
        self.assertLessEqual(max_adjoint_error(sym), TOLERANCE)
        self.assertTrue(kernel_is_inversion_symmetric(sym))

    def test_finite_dimension_is_48_for_p210(self) -> None:
        self.assertEqual(len(reduced_residues(MODULUS)), 48)

    def test_document_records_infinite_domain_problem(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "L^2(Z_hat^x, d mu_Haar)",
            "D(T_infty)",
            "deficiency indices",
            "essential self-adjointness",
            "operator-norm bound",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not construct a Hilbert-Polya operator",
            "does not prove an operator-norm bound at GRH scale",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
