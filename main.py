"""One-line chill entry: checks the line, then saves it."""

from pathlib import Path
import sys


CHILL_LINE = "My son's nightlight flickers in Morse, and last night it spelled the name I gave the baby we lost."
DESTINATION = Path("/output/entry.txt")


def _count_sentence_enders(text):
    return sum(1 for ch in text if ch in ".!?")


def _passes_gate(text):
    """Return a reason string when the line fails, else None."""
    if not isinstance(text, str):
        return "line is not text"
    if not text.strip():
        return "line is only whitespace"
    if not 1 <= len(text) <= 200:
        return f"length {len(text)} is outside 1-200 characters"
    if "\n" in text or "\r" in text:
        return "line must be a single line with no newline characters"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "line is not valid UTF-8"
    if _count_sentence_enders(text) != 1:
        return "line must contain exactly one sentence"
    if not text.rstrip().endswith((".", "!", "?")):
        return "line must end with sentence punctuation"
    stripped = text.rstrip()
    if _count_sentence_enders(stripped[:-1]) != 0:
        return "the single sentence ender must be the final character, with no earlier sentence break"
    return None


def _save_and_confirm(text, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    reread = target.read_bytes()
    if reread != text.encode("utf-8"):
        print("ERROR: written file does not match the line byte for byte", file=sys.stderr)
        sys.exit(1)
    print(f"OK: wrote {len(text)} characters to {target}")


def run():
    problem = _passes_gate(CHILL_LINE)
    if problem is not None:
        print(f"ERROR: validation failed: {problem}", file=sys.stderr)
        sys.exit(1)
    _save_and_confirm(CHILL_LINE, DESTINATION)


if __name__ == "__main__":
    run()
