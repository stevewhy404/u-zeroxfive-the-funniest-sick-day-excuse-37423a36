"""The Funniest Sick-Day Excuse — one line under 200 characters.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt
when the variable is unset, so it can be smoke-tested locally).
"""

import os

LINE = "I can't come in today — my smart lock updated overnight and now it only opens for the previous tenant, who moved to Canada, so I'm locked out of my own flat until he answers an email."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
