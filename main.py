"""Entry for make.fun: One Line, One Laugh.

Relationship advice from a fridge that has seen too much at 3 a.m. and kept the receipts.
"""
import os

LINE = "I asked my fridge for relationship advice and it said my love life, like its leftovers, was once promising but I kept opening it at 3 a.m. expecting something new."
MAX_CHARS = 200


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
