#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic, offline, standard library only.
"""

import os

JOKE = "I blocked an hour for actual work, so my boss booked a meeting to ask why I was unavailable."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the joke — 92 characters,
    # one line, valid UTF-8 — comfortably inside the gate's 1-199 range.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
