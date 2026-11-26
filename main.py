#!/usr/bin/env python3
"""One Line, One Laugh entry (program/v1).

Writes one original funny one-liner to /output/entry.txt. The line is
UTF-8 text of 1 to 140 characters, a single line, with no trailing
newline.
"""

import os

MAX_CHARS = 140

ENTRY_TEXT = "My therapist says I use humor to avoid my feelings, which is hilarious because my feelings filed a restraining order years ago."

assert len(ENTRY_TEXT) <= MAX_CHARS, "entry exceeds the 140-character limit"


def check_entry(text):
    """Return True when text passes the sealed scorer's 1-140 char gate."""
    return 1 <= len(text) <= MAX_CHARS and bool(text.strip())


def write_entry(text, out_dir):
    """Write text to entry.txt inside out_dir (mode 0644) and return the path."""
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    # The sealed scorer gates on 1-140 characters; refuse to write
    # anything that would fail the gate instead of shipping it.
    if not check_entry(ENTRY_TEXT):
        raise SystemExit("entry fails the 1-140 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY_TEXT, out_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
