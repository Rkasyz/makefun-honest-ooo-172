#!/usr/bin/env python3
"""Out of Office, Honestly — make.fun entry.

Writes one painfully honest (but still polite) out-of-office auto-reply
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the same bytes on
every run, no network, no randomness, no timestamps.
"""

import os

ENTRY = (
    "I am out of the office until Monday, November 30, and I will read "
    "your email when I return, in the order it arrived, with the "
    "enthusiasm it deserves \u2014 which is to say, slowly and after coffee."
)


def main() -> None:
    # Empty env var must not become a relative path: fall back to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # Gate guard: the entry must stay within the competition's 1-200
    # character window, or the sealed scorer rejects it outright.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
