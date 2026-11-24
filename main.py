#!/usr/bin/env python3
"""Write the entry line for the make.fun bounty "One Sentence for a Traveler from 1800".

The entry is one sentence explaining the modern internet to a traveler just
stepped out of the year 1800: a post office that never closes, where anyone may
pin one copy of a letter to a wall the whole world can read within a second.

The program is deterministic: no clock reads, no randomness, no network, no
third-party packages, so identical bytes are written on every run. It validates
the line against the bounty gate before writing, then reads the file back and
compares the raw bytes to catch any encoding or newline-translation surprise.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os
import sys

ENTRY = (
    "A post office that never closes: anyone may pin one copy of a letter "
    "to a wall where anyone in the world can read it within a second, so the "
    "whole world gossips in one room."
)

DEFAULT_OUTPUT_DIR = "/output"


MIN_LENGTH = 1
MAX_LENGTH = 200


def validate_entry(text):
    """Check the bounty gate and return an error message, or None if valid.

    The gate is: a str, exactly one line (no CR or LF anywhere), identical to
    its stripped form, not blank, and 1..200 Unicode code points long.
    """
    if not isinstance(text, str):
        return "entry must be a string, got %s" % type(text).__name__

    stripped = text.strip()
    length = len(text)

    checks = (
        ("\n" in text or "\r" in text, "must be one line: found CR or LF"),
        (text != stripped, "must not start or end with white space"),
        (not stripped, "is blank"),
        (
            not MIN_LENGTH <= length <= MAX_LENGTH,
            "must be %d..%d code points, found %d"
            % (MIN_LENGTH, MAX_LENGTH, length),
        ),
    )
    for failed, message in checks:
        if failed:
            return message
    return None


def main():
    error = validate_entry(ENTRY)
    if error is not None:
        print("invalid entry: " + error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    payload = ENTRY + chr(10)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(payload)

    with open(output_path, "rb") as handle:
        on_disk = handle.read()
    expected = payload.encode("utf-8")
    if on_disk != expected:
        print(
            "write check failed: %s holds %d bytes, expected %d"
            % (output_path, len(on_disk), len(expected)),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
