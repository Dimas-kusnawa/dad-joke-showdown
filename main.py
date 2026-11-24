"""Dad Joke Showdown entry (make.fun u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one dad joke to /output/entry.txt.

The joke: a father tells his suitcase there is no vacation this year,
and the punchline lands on "emotional baggage" — a clean, groan-worthy
pun, tight, and easy to deliver out loud at the dinner table.
"""

import os

JOKE = (
    "I told my suitcase there would be no vacation this year. "
    "Now I'm dealing with emotional baggage."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("joke must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
