import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "run_arithmetic_volumetric_surface.py"

spec = importlib.util.spec_from_file_location("run_arithmetic_volumetric_surface", MODULE_PATH)
runner = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(runner)


class ArithmeticVolumetricSurfaceTests(unittest.TestCase):
    def test_corrected_mean_field_positive(self):
        self.assertGreater(runner.corrected_mean_field(20.0, 0.1), 0.0)

    def test_score_finite_non_negative(self):
        score = runner.benchmark_score(30.0, 0.1)
        self.assertGreaterEqual(score, 0.0)

    def test_surface_cell_count(self):
        surface = runner.build_surface([20.0, 30.0], [0.05, 0.1])
        self.assertEqual(surface["summary"]["cell_count"], 4)
        self.assertEqual(len(surface["cells"]), 4)

    def test_surface_outputs_written(self):
        with tempfile.TemporaryDirectory() as tmp:
            result, receipt = runner.run_surface([20.0], [0.05, 0.1], pathlib.Path(tmp))
            self.assertEqual(result["surface"]["summary"]["cell_count"], 2)
            self.assertTrue((pathlib.Path(tmp) / "surface.json").exists())
            self.assertTrue((pathlib.Path(tmp) / "summary.md").exists())
            self.assertTrue((pathlib.Path(tmp) / "pfk_receipt.json").exists())
            self.assertEqual(receipt["deterministic_result_sha256"], result["deterministic_result_sha256"])

    def test_claim_boundary_denies_quantum_equivalence(self):
        registry = runner.load_registry()
        disallowed = set(registry["claim_boundary"]["disallowed"])
        self.assertIn("equivalence to quantum volume", disallowed)
        self.assertIn("quantum advantage claim", disallowed)


if __name__ == "__main__":
    unittest.main()
