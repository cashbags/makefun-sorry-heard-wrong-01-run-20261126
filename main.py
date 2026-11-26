"""Sorry, I Heard That Wrong — entry program.

Writes one line to /output/entry.txt: the apology a smart speaker gives its
owner after mishearing them. The line is fixed text; the program is fully
deterministic (same bytes on every run), reads nothing from the environment,
and uses no network.

The file holds exactly the line's bytes and no trailing newline: the gate
counts the characters in /output/entry.txt, and the brief says the entry is
"one short text and nothing else", so nothing extra rides along with it.
"""

import os

LINE = "Sorry, I heard 'water the plants' as 'water the planet.' The ocean says thanks. The plants are dead."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
