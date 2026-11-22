"""make-the-ai-judge-feel-curious-01.

Writes one short, original text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os
import sys

TEXT = (
    "The house at the end of the lane keeps one window lit all night, "
    "every night, though no one has lived there for years. "
    "The curtains never move. The light never goes out. "
    "And every morning the gate stands open a finger's width, "
    "as if someone had only just stepped out."
)


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= 280):
        print(f"self-check failed: length {len(text)} out of range 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("self-check failed: text is whitespace-only", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
