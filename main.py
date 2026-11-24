#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a person
arriving from 1800, to /output/entry.txt, and prints it.

The sentence uses only words and pictures a person from 1800 already
knows (a road, a post office, a library, a letter, a book) and holds
one image: a letter crossing the world in a breath.

The entry is written by write_entry(), which creates the output
directory first; a failure to write is reported as one clean line on
stderr with a non-zero exit instead of a traceback.
"""

import os
import sys

ENTRY = (
    "Picture a road joining every post office and library on earth, "
    "so a letter you post reaches the far side of the world in a breath, "
    "and any book answers you at once."
)


def write_entry(path: str, text: str) -> None:
    """Create the output directory and write the entry text to path.

    Raises OSError to the caller, which reports it cleanly instead of
    letting a traceback escape.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    try:
        write_entry("/output/entry.txt", ENTRY)
    except OSError as exc:
        print(f"could not write /output/entry.txt: {exc}", file=sys.stderr)
        return 1
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
