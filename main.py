"""One Word, One Username, One Reward — entry program.

Writes one word (<=30 chars) to /output/entry.txt: the entrant's own
make.fun username, and nothing else — no explanation, no links, no
pitch. Stdlib only, deterministic.
"""
import os

TEXT = "jolly-meteor-97"


def check_gate(text):
    """Return True iff text passes the scorer's gate (RULES.txt):
    UTF-8, 1-30 chars (characters, not bytes), one word, no spaces,
    not whitespace-only, no control characters."""
    if not 1 <= len(text) <= 30:
        return False
    if "\n" in text or "\r" in text or " " in text:
        return False
    if not text.strip():
        return False
    if any(ord(c) < 32 for c in text):
        return False
    return True


def main():
    # Enforce the scorer's gate (RULES.txt). Fail loudly instead of
    # writing an invalid entry.
    if not check_gate(TEXT):
        raise SystemExit("entry text violates the 1-30 char single-word gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
