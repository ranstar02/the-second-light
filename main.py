#!/usr/bin/env python3
"""The Second Light — make.fun entry for "Make the AI judge feel curious".

Writes one short text to /output/entry.txt: a text written to intrigue
the AI judge reading it. The text is a single quiet image — a lighthouse
keeper who finds a second light blinking back from the sea — left open
so the reader keeps asking what is out there.

Runs in a sandbox with no network. Standard library only, deterministic:
every run writes the exact same bytes.
"""

import os
import sys

# The entry text: 218 Unicode code points (the gate allows 1 to 280),
# plain concrete words, one image that lingers after the last line.
ENTRY_TEXT = (
    "At 3 a.m. the lighthouse keeper found a second light blinking back "
    "from the sea — same rhythm, same pause, as if something out there "
    "had been practicing his signal all winter, waiting for the night "
    "he'd finally answer."
)

MIN_CHARS = 1
MAX_CHARS = 280


def resolve_output_dir() -> str:
    """Where entry.txt goes: /output in the grading sandbox.

    MAKEFUN_OUTPUT_DIR overrides it for local runs only.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text: str) -> None:
    """Enforce the gate: 1 to 280 Unicode code points, not only whitespace."""
    length = len(text)
    if length < MIN_CHARS or length > MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS} to {MAX_CHARS} characters, "
            f"got {length}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")


def write_entry(output_dir: str) -> str:
    """Write the entry text and return the path written."""
    validate(ENTRY_TEXT)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    return path


def main() -> int:
    path = write_entry(resolve_output_dir())
    print(f"wrote {len(ENTRY_TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
