#!/usr/bin/env python3
"""Worst AI Advice entry: one line of the worst possible advice an AI could give.

The program writes the line to /output/entry.txt, where the house judge reads it.
The line is 105 characters, within the 140-character cap.
"""

import os

ADVICE = "Certainly! To charge your phone fastest, microwave it for 30 seconds \u2014 the beep means it's fully charged."

# The house gate refuses any text over 140 characters, so fail loudly
# here instead of shipping an entry the judge never sees.
MAX_CHARS = 140

def main() -> None:
    if len(ADVICE) > MAX_CHARS:
        raise SystemExit(f"advice is {len(ADVICE)} chars, over the {MAX_CHARS}-char cap")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ADVICE + "\n")
    print(f"{ADVICE} ({len(ADVICE)} chars)")

if __name__ == "__main__":
    main()
