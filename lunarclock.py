#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "rich>=13.7",
# ]
# ///
"""lunarclock — based on the moon phase posts of Froyo☆Tam"""

X_BUFFER = [
    "                          ",
    " XX  XXXX  XX  XXX   XXXX ",
    " XX  XX X  XX    XX  XX X ",
    " XX  XX X      XXX   XX X ",
    " XX  XX X  XX    XX  XX X ",
    " XX  XXXX  XX  XXX   XXXX ",
    "                          ",
    "               XXXX XX X  ",
    "               X    X X X ",
    "                          ",
]

PHASES = "🌕🌖🌗🌘🌑🌒🌓🌔"

BITS_TO_PHASE_INDEX = [0, 2, 6, 4]


def xs_to_phases(xs: list[str]) -> list[list[int]]:
    result = []
    for line in xs:
        row = []
        for i in range(0, len(line), 2):
            n = 0 if line[i] == " " else 2
            n += 0 if line[i + 1] == " " else 1
            row.append(BITS_TO_PHASE_INDEX[n])
        result.append(row)
    return result


def main():
    frame = xs_to_phases(X_BUFFER)
    for line in frame:
        print(line)
    for line in frame:
        print("".join(PHASES[c] for c in line))


if __name__ == "__main__":
    main()
