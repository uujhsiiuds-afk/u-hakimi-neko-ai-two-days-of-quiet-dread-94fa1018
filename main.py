#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment that approves a PR
with quiet existential dread. Writes the comment to /output/entry.txt."""

import os
import sys

ENTRY_TEXT = (
    "Approved. Tests pass, the diff is clean, and I have quietly accepted "
    "that this code will outlive me without ever telling me what it does."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate self-check: UTF-8, 1-140 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry text must be a string")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    if len(text) < 1 or len(text) > 140:
        raise ValueError(
            f"entry text must be 1-140 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")


def main() -> int:
    validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote {len(ENTRY_TEXT)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
