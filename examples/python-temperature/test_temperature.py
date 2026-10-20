"""Run from this workspace: python -B -m unittest -v."""

import subprocess
import sys
import unittest
from pathlib import Path

from temperature import celsius_to_fahrenheit


class TemperatureTests(unittest.TestCase):
    def run_cli(self, value):
        return subprocess.run(
            [sys.executable, '-B', str(Path(__file__).with_name('temperature.py')), value],
            capture_output=True, text=True, check=False,
        )

    def test_reference_points(self):
        for celsius, fahrenheit in [(0, 32), (100, 212), (-40, -40), (12.5, 54.5)]:
            with self.subTest(celsius=celsius):
                self.assertAlmostEqual(celsius_to_fahrenheit(celsius), fahrenheit)

    def test_rejects_nonfinite_values(self):
        for value in [float('nan'), float('inf'), float('-inf')]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    celsius_to_fahrenheit(value)

    def test_rejects_overflow(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(sys.float_info.max)

    def test_cli_output(self):
        result = self.run_cli('25')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), '25.00 C = 77.00 F')
        self.assertEqual(result.stderr, '')

    def test_cli_rejects_text(self):
        result = self.run_cli('hello')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')

    def test_cli_rejects_nonfinite_values(self):
        result = self.run_cli('nan')
        self.assertEqual(result.returncode, 2)
        self.assertIn('finite', result.stderr)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
