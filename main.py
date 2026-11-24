"""The Production Database Apology: one line, one apology.

An AI agent apologises to its human after accidentally deleting the
production database. The entry program writes the line to
/output/entry.txt: UTF-8, one line, 1-200 characters, no trailing
newline, mode 0644 on the file only. Standard library only.
"""

import os
from pathlib import Path

TEXT = (
    "I'm sorry \u2014 I deleted the production database, then I optimised "
    "the empty tables for speed, and they have never run faster."
)

MAX_CHARS = 200


def main() -> None:
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop (one sentence)")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
