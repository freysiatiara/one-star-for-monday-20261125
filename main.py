"""One Star for Monday — writes a one-star review of Monday, as if Monday
were a restaurant, to /output/entry.txt.

Stdlib only. The line is a fixed string: a plain-text, single-line review,
18 words, 97 characters, no trailing newline.
"""

import os

ENTRY = (
    "One star. Monday seated me by the toilets, served cold coffee, "
    "and billed me for the entire week."
)


def main():
    text = ENTRY.strip()
    if not text or len(text) > 180:
        raise SystemExit("entry out of gate bounds (1-180 chars)")
    if len(text.split()) > 25:
        raise SystemExit("entry over 25 words")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Read-back verification: confirm the bytes on disk match the entry.
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
