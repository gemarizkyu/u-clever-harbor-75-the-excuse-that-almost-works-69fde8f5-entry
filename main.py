"""The Excuse That Almost Works — make.fun entry.

Writes one line (at most 20 words, 1 to 140 characters) to
/output/entry.txt: the single line a gamer texts the boss to skip
work on GTA 6 launch week. Fully deterministic: the same text on
every run, no clock, no randomness, no network, no model call.

The line: a boring, specific, almost-believable snag — the water
board dug up the street and cut the power till four, so the laptop
is dead. No dead grandmother, no flat tyre, no sudden fever; no
mention of the game at all, which is exactly why a tired manager
would almost believe it. It reads like a text sent in a hurry:
one line, plain words, no setup, no explanation, no signature.
"""

import os

# The excuse (16 words, 84 characters, one line, no trailing newline).
EXCUSE = (
    "Morning, the water board dug up my street and cut the power "
    "till four, laptop's dead"
)

MAX_WORDS = 20
MAX_CHARS = 140


def main() -> None:
    text = EXCUSE.strip()
    assert text, "excuse must not be blank"
    assert "\n" not in text, "excuse must be a single line"
    assert len(text.split()) <= MAX_WORDS, (
        f"excuse is {len(text.split())} words, over {MAX_WORDS}"
    )
    assert 1 <= len(text) <= MAX_CHARS, (
        f"excuse is {len(text)} chars, outside 1-{MAX_CHARS}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars, {len(text.split())} words to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
