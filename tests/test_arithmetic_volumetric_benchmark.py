import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "check_arithmetic_volumetric_benchmark.py"
spec = importlib.util.spec_from_file_location("check_arithmetic_volumetric_benchmark", MODULE_PATH)
check = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(check)


class ArithmeticVolumetricBenchmarkTests(unittest.TestCase):
    def test_required_fields(self):
        registry = check.load_registry(ROOT / "empirical-claims/arithmetic-volumetric-benchmark-v0.1/registry.json")
        check.assert_required_fields(registry)
        self.assertEqual(registry["claim_class"], "definitional")

    def test_parent_normalization(self):
        registry = check.load_registry(ROOT / "empirical-claims/arithmetic-volumetric-benchmark-v0.1/registry.json")
        self.assertTrue(check.check_parent_normalization(registry)["pass"])

    def test_two_axis_surface(self):
        registry = check.load_registry(ROOT / "empirical-claims/arithmetic-volumetric-benchmark-v0.1/registry.json")
        result = check.check_two_axis_surface(registry)
        self.assertTrue(result["pass"])
        self.assertEqual(result["surface"], "Score(u,L)")

    def test_fixture_scores(self):
        registry = check.load_registry(ROOT / "empirical-claims/arithmetic-volumetric-benchmark-v0.1/registry.json")
        result = check.check_fixture_scores(registry)
        self.assertTrue(result["pass"])
        for entry in result["scores"]:
            self.assertGreaterEqual(entry["score"], 0.0)

    def test_quantum_volume_boundary(self):
        registry = check.load_registry(ROOT / "empirical-claims/arithmetic-volumetric-benchmark-v0.1/registry.json")
        self.assertTrue(check.check_quantum_volume_boundary(registry)["pass"])

    def test_claim_boundary(self):
        registry = check.load_registry(ROOT / "empirical-claims/arithmetic-volumetric-benchmark-v0.1/registry.json")
        self.assertTrue(check.check_claim_boundary(registry)["pass"])


if __name__ == "__main__":
    unittest.main()
