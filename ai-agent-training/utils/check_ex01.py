"""Run the existing ex01 assertions offline, with a meaningful failure exit code."""
import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / "01-python-basics/tests/test_ex01.py"
spec = importlib.util.spec_from_file_location("training_ex01_checks", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
suite = unittest.TestSuite(unittest.FunctionTestCase(getattr(module, name)) for name in sorted(dir(module)) if name.startswith("test_"))
if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
