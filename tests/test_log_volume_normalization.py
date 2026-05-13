import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "check_log_volume_normalization.py"
spec = importlib.util.spec_from_file_location("check_log_volume_normalization", MODULE_PATH)
check = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(check)


class LogVolumeNormalizationTests(unittest.TestCase):
    def test_required_fields(self):
        registry = check.load_registry(ROOT / "empirical-claims/log-volume-normalization-v0.1/registry.json")
        check.assert_required_fields(registry)
        self.assertEqual(registry["claim_class"], "definitional")

    def test_base_gauge_invariance(self):
        self.assertTrue(check.check_base_gauge_invariance()["pass"])

    def test_mean_field_correction(self):
        registry = check.load_registry(ROOT / "empirical-claims/log-volume-normalization-v0.1/registry.json")
        result = check.check_mean_field_correction(registry["fixtures"])
        self.assertTrue(result["pass"])
        for case in result["cases"]:
            self.assertLess(case["corrected_error"], case["leading_error"])

    def test_observable_separation(self):
        registry = check.load_registry(ROOT / "empirical-claims/log-volume-normalization-v0.1/registry.json")
        self.assertTrue(check.check_observable_separation(registry)["pass"])

    def test_claim_boundary(self):
        registry = check.load_registry(ROOT / "empirical-claims/log-volume-normalization-v0.1/registry.json")
        self.assertTrue(check.check_claim_boundary(registry)["pass"])


if __name__ == "__main__":
    unittest.main()
