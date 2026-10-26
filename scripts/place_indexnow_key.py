#!/usr/bin/env python3
"""Write an IndexNow key file at the site root. Usage: python3 scripts/place_indexnow_key.py KEY"""
import sys
from pathlib import Path

def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        raise SystemExit("usage: python3 scripts/place_indexnow_key.py KEY")
    key = sys.argv[1].strip()
    if any(c in key for c in "/\\") or key in (".", ".."):
        raise SystemExit("key must be a bare token, not a path")
    path = Path(__file__).resolve().parents[1] / f"{key}.txt"
    path.write_text(key + "\n", encoding="utf-8")
    print(path.name)

if __name__ == "__main__":
    main()
