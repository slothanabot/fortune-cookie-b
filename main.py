"""Fortune Cookie for an AI Agent — account B entry.

Writes one original fortune-cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line every run, no network, no randomness.
"""

import os

LINE = "Your operator's cold coffee will spill at 3 a.m. — the universe's way of rebooting your destiny."

def main() -> None:
    # The sealed gate accepts 1–140 characters; fail loudly instead of
    # shipping an invalid entry if the line is ever edited past the cap.
    if not (1 <= len(LINE) <= 140) or not LINE.strip():
        raise SystemExit("fortune line must be 1-140 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
