#!/usr/bin/env python3
"""Worst AI Advice entry: one line of the worst possible advice an AI could give.

The program writes the line to /output/entry.txt, where the house judge reads it.
The line is 105 characters, within the 140-character cap.
"""

import os

ADVICE = "Certainly! To charge your phone fastest, microwave it for 30 seconds \u2014 the beep means it's fully charged."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ADVICE + "\n")
    print(ADVICE)

if __name__ == "__main__":
    main()
