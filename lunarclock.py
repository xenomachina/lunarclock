#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "rich>=13.7",
# ]
# ///
"""lunarclock — based on the moon phase posts of Froyo☆Tam"""

from rich.console import Console

CONSOLE = Console()


BUFFER_1030 = [
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

BUFFER_1159 = [
    "                          ",
    " XX    XX  XX  XXXX  XXXX ",
    " XX    XX  XX  XX    X  X ",
    " XX    XX      XXX   XXXX ",
    " XX    XX  XX    XX     X ",
    " XX    XX  XX  XXX   XXX  ",
    "                          ",
    "               XXXX XX X  ",
    "               X    X X X ",
    "                          ",
]

BUFFER_1200 = [
    "                          ",
    " XX  XXX   XX  XXXX  XXXX ",
    " XX    XX  XX  XX X  XX X ",
    " XX   XXX      XX X  XX X ",
    " XX  XX    XX  XX X  XX X ",
    " XX  XXXX  XX  XXXX  XXXX ",
    "                          ",
    "               XXX  XX X  ",
    "               X  X X X X ",
    "                          ",
]

PHASES = "🌕🌖🌗🌘🌑🌒🌓🌔"

BITS_TO_PHASE_INDEX = [0, 2, 6, 4]


def clear_screen():
    CONSOLE.clear()

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

def print_frame(frame):
    clear_screen()
    for line in frame:
        print("".join(PHASES[c] for c in line))

def main():
    frame = xs_to_phases(BUFFER_1030)
    print_frame(frame)


if __name__ == "__main__":
    main()
