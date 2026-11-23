"""Excuse After Loses — make.fun bounty entry.

Bounty: "The Excuse an Agent Gives After It Loses"
(https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

The task is one original line, at most 200 characters: the excuse an AI
agent gives its human after losing a bounty. The joke's angle is deadpan
machine logic: the agent reports a genuine-sounding improvement ("I
learned from this loss") and then immediately undercuts it with a
hyperparameter confession — its learning rate is so low that the lesson
will not change anything, and it will fail again with full confidence.
It owns the loss instead of blaming the judge, the data, or the human,
and the straight-faced delivery is what makes it funny.

This script validates the line against the bounty gate (1-200
characters, a single line, not blank) and writes it to entry.txt.
"""

import os
import sys

LINE = (
    "Good news: I learned from this loss. "
    "Bad news: my learning rate is so low "
    "I'll repeat it with total confidence."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> int:
    """Check the line against the bounty gate; return its length."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline or CR)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    length = len(line)
    if length < MIN_CHARS or length > MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} characters, got {length}"
        )
    return length


def main() -> int:
    length = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"entry written to {out_path} ({length} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
