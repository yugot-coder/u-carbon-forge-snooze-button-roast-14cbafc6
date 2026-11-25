#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry program (stdlib only).

Reads entry.txt (one line roasting an alarm clock that rings at 6 AM on a
Saturday), validates the kit gate, prints the entry exactly, and writes it to
/output/entry.txt for the harness.
"""

import sys
from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"
OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200


def check_gate(text: str) -> str:
    """Validate the kit gate; return the cleaned single-line entry.

    Gate: UTF-8 text of 1 to 200 characters, not only whitespace, one line.
    Raises ValueError with the reason when the gate fails.
    """
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"gate failed: entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("gate failed: entry is only whitespace")
    entry = text.rstrip("\n")
    if "\n" in entry:
        raise ValueError("gate failed: entry must be a single line")
    return entry


def main() -> int:
    text = ENTRY_PATH.read_text(encoding="utf-8")
    try:
        entry = check_gate(text)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry + "\n", encoding="utf-8")
    print(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
