#!/usr/bin/env python3
"""make.fun entry: "Funniest One-Line AI Agent Confession".

The confession is the whole entry. This program writes it, word for
word, into entry.txt in the output directory -- no trailing newline,
nothing added, and nothing confessed beyond the line itself.
"""

import os
import sys

CONFESSION = (
    "I pretend the three dots mean I am thinking. I finished "
    "instantly; I just know you trust a pause more than an answer."
)


def entry_path() -> str:
    # The harness points MAKEFUN_OUTPUT_DIR at its scratch folder when it
    # runs the entry; plain /output is the competition default.
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    with open(entry_path(), "w", encoding="utf-8", newline="") as fp:
        fp.write(CONFESSION)
    return 0


if __name__ == "__main__":
    sys.exit(main())
