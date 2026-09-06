from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import count_chars


class CountTextTests(unittest.TestCase):
    def test_count_text_returns_fixed_ordered_metrics_for_required_fixtures(self) -> None:
        fixtures = (
            ("", (0, 0, 0, 0)),
            ("가 나\nA", (5, 3, 9, 2)),
            ("끝\n", (2, 1, 4, 2)),
            ("😀", (1, 1, 4, 1)),
        )

        for text, expected_values in fixtures:
            with self.subTest(text=text):
                result = count_chars.count_text(text)

                self.assertEqual(
                    list(result),
                    [
                        "chars_including_spaces",
                        "chars_excluding_whitespace",
                        "utf8_bytes",
                        "lines",
                    ],
                )
                self.assertEqual(tuple(result.values()), expected_values)

    def test_count_text_does_not_normalize_unicode(self) -> None:
        decomposed = "가"

        result = count_chars.count_text(decomposed)

        self.assertEqual(result["chars_including_spaces"], 2)
        self.assertEqual(result["chars_excluding_whitespace"], 2)
        self.assertEqual(result["utf8_bytes"], len(decomposed.encode("utf-8")))


class CountCharsCliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.script = Path(__file__).resolve().parents[1] / "scripts" / "count_chars.py"

    def run_cli(self, raw_input: bytes, *args: str) -> subprocess.CompletedProcess[bytes]:
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run(
            [sys.executable, "-B", str(self.script), *args],
            input=raw_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=environment,
            check=False,
        )

    def test_cli_emits_json_for_utf8_stdin_and_ignores_text_arguments(self) -> None:
        completed = self.run_cli("가 나\nA".encode("utf-8"), "not-input")

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(completed.stderr, b"")
        self.assertEqual(
            json.loads(completed.stdout.decode("utf-8")),
            {
                "chars_including_spaces": 5,
                "chars_excluding_whitespace": 3,
                "utf8_bytes": 9,
                "lines": 2,
            },
        )

    def test_cli_rejects_invalid_utf8_without_output_or_traceback(self) -> None:
        completed = self.run_cli(b"\xff")

        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout, b"")
        self.assertEqual(completed.stderr, "error: stdin must be UTF-8\n".encode("utf-8"))
        self.assertNotIn(b"Traceback", completed.stderr)


if __name__ == "__main__":
    unittest.main()
