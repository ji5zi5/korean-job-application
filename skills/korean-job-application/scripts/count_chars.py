from __future__ import annotations

import json
import sys


def count_text(text: str) -> dict[str, int]:
    """Return character, non-whitespace, UTF-8 byte, and line counts."""
    return {
        "chars_including_spaces": len(text),
        "chars_excluding_whitespace": sum(1 for character in text if not character.isspace()),
        "utf8_bytes": len(text.encode("utf-8")),
        "lines": 0 if text == "" else text.count("\n") + 1,
    }


def main() -> int:
    """Read strict UTF-8 stdin and emit one JSON metrics object."""
    try:
        text = sys.stdin.buffer.read().decode("utf-8")
    except UnicodeDecodeError:
        sys.stderr.buffer.write(b"error: stdin must be UTF-8\n")
        return 2

    output = json.dumps(count_text(text), ensure_ascii=False).encode("utf-8")
    sys.stdout.buffer.write(output + b"\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
