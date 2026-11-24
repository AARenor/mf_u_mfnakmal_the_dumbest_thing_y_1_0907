#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt."""

import os
import pathlib
import sys

TEXT = (
    "My agent scheduled the deploy for end of day, defined end of day as 11:40, "
    "and went to lunch."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir = pathlib.Path(target)
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    sys.stderr.write(f"{len(TEXT)} characters\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
