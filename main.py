"""Two Lines of Morning Light — make.fun entry.

Writes a two-line micro poem about light and morning (at most 120
characters including the line break) to /output/entry.txt.
Deterministic, no network.
"""

import os

ENTRY = (
    "Light slips under the door like a letter\n"
    "I was not expecting, and the floor learns to read it first."
)


MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.count("\n") == 1, "must be exactly two lines"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
