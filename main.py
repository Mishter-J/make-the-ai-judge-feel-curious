"""make-the-ai-judge-feel-curious-20261122-2311 entry: write one fixed text
to /output/entry.txt.

The text is a fixed string literal. The program just writes it, so the
output is byte-for-byte identical on every run. The judge reads exactly
the bytes written, so no trailing newline is added.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = (
    "There is a small blue door at the end of this sentence. "
    "Behind it, a room you have never entered, with a letter on the table "
    "addressed to you, in your own handwriting. "
    "You have not written it yet."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit("entry must be 1 to 280 characters")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_text(ENTRY, encoding="utf-8")
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the entry.
    if dest.read_text(encoding="utf-8") != ENTRY:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the entry text")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
