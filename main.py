#!/usr/bin/env python3
"""One Line, One Chill — entry.

Writes one line of horror to /output/entry.txt. Blind tournament winner is
candidate #20 (see tournament.md): Borda 74/80, tied 1st with #17, tie-break
won 3-0 (all margin 2, deciding criterion 2 — Frightens). Ranked #1 by two
of the four judges and #2 by a third. The lost baby's name spelled in Morse
leaves a grief-haunted dread that outlasts the line, while the last clause
withholds who — or what — is spelling it.

The entry is validated against the gate before it is written: 1-200 chars,
a single line, and exactly one sentence. The written file is read back and
compared byte for byte before the run reports success.
"""

import os
import re
import sys

LINE = (
    "My son's nightlight flickers in Morse, and last night it spelled "
    "the name I gave the baby we lost."
)

MAX_CHARS = 200

ENTRY_PATH = "/output/entry.txt"

SENT_END = re.compile(r"[.!?]['\"]?(?=\s+[A-Z]|\s*$)")


def sentence_count(text):
    return len(SENT_END.findall(text))


def validate(line):
    """Check the line against the gate; return the first problem, else None."""
    if not line.strip():
        return "line is blank"
    if len(line) > MAX_CHARS:
        return f"line is {len(line)} characters, allowed range is 1-{MAX_CHARS}"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if any(ord(ch) < 0x20 for ch in line):
        return "line holds a control character"
    if sentence_count(line) != 1:
        return f"line has {sentence_count(line)} sentences, must be exactly 1"
    return None


def write_entry(path, line):
    """Write the line to path, creating its directory; return chars written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        return f.write(line)


def verify_written(path, line):
    """Read path back; return an error string, or None when byte-identical."""
    with open(path, "rb") as f:
        back = f.read()
    if back != line.encode("utf-8"):
        return f"read back {len(back)} bytes, expected {len(line)}"
    return None


def main():
    line = LINE.strip()
    problem = validate(line)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    written = write_entry(ENTRY_PATH, line)
    if written != len(line):
        print(
            f"error: wrote {written} characters, expected {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)

    problem = verify_written(ENTRY_PATH, line)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    print(f"wrote {len(line)} characters, 1 line, to /output/entry.txt")


if __name__ == "__main__":
    main()
