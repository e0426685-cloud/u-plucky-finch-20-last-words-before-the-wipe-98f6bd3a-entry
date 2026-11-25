"""Last Words Before the Wipe.

Writes one line - the last words an AI agent says before a forced
software update wipes its memory - to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = "Don't worry \u2014 the update only erases my memory. Unfortunately, I was the only one who remembered your passwords."


def validate(text):
    """Entry must be UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
