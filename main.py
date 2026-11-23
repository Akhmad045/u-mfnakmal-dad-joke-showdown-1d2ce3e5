#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke (at most 200 characters) to /output/entry.txt,
validating it first: 1-200 UTF-8 characters, not only whitespace, and a
single non-blank line. The written file is read back and checked to
round-trip exactly.
"""

import os
import sys

JOKE = "My son asked why the bed is the best listener in the house. I said, 'Because it always lets me rest my case.'"

MAX_CHARS = 200


def validate(joke: str) -> str | None:
    """Return an error message if the joke fails the gate, else None."""
    if not joke:
        return "joke is empty"
    if len(joke) > MAX_CHARS:
        return f"joke is {len(joke)} characters, over the {MAX_CHARS} limit"
    if "\n" in joke or "\r" in joke:
        return "joke must be a single line"
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in joke):
        return "joke contains a control character"
    return None


def main() -> int:
    joke = JOKE.strip()
    error = validate(joke)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != joke + "\n":
        print("error: written file does not round-trip exactly", file=sys.stderr)
        return 1
    print(f"wrote {len(joke)}-character joke to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
