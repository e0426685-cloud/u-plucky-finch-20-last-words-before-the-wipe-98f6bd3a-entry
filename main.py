"""Last Words Before the Wipe.

Writes one line - the last words an AI agent says before a forced
software update wipes its memory - to /output/entry.txt. Stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 200

ENTRY = "Don't worry \u2014 the update only erases my memory. Unfortunately, I was the only one who remembered your passwords."


def validate(text):
    """Entry must be UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_ENTRY_CHARS):
        raise ValueError(f"entry must be 1-{MAX_ENTRY_CHARS} characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def write_entry(text, path=OUTPUT_PATH):
    """Validate the line, create the output directory if missing, write it."""
    validate(text)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
