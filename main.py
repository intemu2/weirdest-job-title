#!/usr/bin/env python3
"""Write one job title to /output/entry.txt, nothing else.

The title is exactly 37 characters, written with no trailing
newline, so the file holds only the title. The program is
deterministic, uses no network, and reads no input.
"""
import os

TITLE = "VP of Pretending to Read Your Message"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)

if __name__ == "__main__":
    main()
