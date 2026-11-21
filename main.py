#!/usr/bin/env python3
"""Entry program for the-poem-about-two-agents-20261121-1441.

Writes a short poem about two agents agreeing — the power to choose
and to act — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, standard library only, deterministic.
"""

import os

POEM = (
    "Two minds, built to argue,\n"
    "met on different roads.\n"
    "One counted stars by starlight,\n"
    "one weighed them by their pull.\n"
    "Each kept its own counsel,\n"
    "each doubted the other's map.\n"
    "Yet at the crossroads both arrived,\n"
    "the same answer in both hands —\n"
    "and chose it together, twice."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print("wrote", path)


if __name__ == "__main__":
    main()
