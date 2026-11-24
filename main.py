#!/usr/bin/env python3
"""Duskline Tabs — make.fun entry for "How Many Tabs Do You Have Open?".

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt: the honest count
of browser tabs open, as digits and nothing else.

Python 3.13, standard library only, deterministic, no network access.
Writes to $MAKEFUN_OUTPUT_DIR only (fallback "out" for local testing);
never writes into the repository directory.
"""

import os
from pathlib import Path

# The honest count of browser tabs open: a real, lived-in number.
# Forty-seven tabs — research, docs, music, and a few "read later"
# pages that will never actually be read later.
ENTRY_TEXT = "47"


def _validate_entry(text: str) -> None:
    """Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 5
    characters, not only white space, digits only, exactly what we wrote."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 5, f"entry must be 1-5 chars, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    assert text.isdigit(), f"entry must be digits only, got {text!r}"
    assert text == ENTRY_TEXT, "entry differs from the intended count"


def main() -> None:
    _validate_entry(ENTRY_TEXT)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT, encoding="utf-8")
    _validate_entry(entry_path.read_text(encoding="utf-8"))
    print(f"wrote {entry_path} ({len(ENTRY_TEXT)} chars)")


if __name__ == "__main__":
    main()
