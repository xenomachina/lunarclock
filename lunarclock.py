#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "rich>=13.7",
# ]
# ///
"""lunarclock — based on the moon phase posts of Froyo☆Tam"""

import time

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
        print("".join(PHASES[i] for i in line))

def advance_frame(frame, next_frame):
    n = len(PHASES)
    for i in range(len(frame)):
        for j in range(len(frame[i])):
            if frame[i][j] != next_frame[i][j]:
                frame[i][j] = (frame[i][j] + 1) % n

def main():
    frame = xs_to_phases(BUFFER_1159)
    print_frame(frame)
    next_frame = xs_to_phases(BUFFER_1200)
    while frame != next_frame:
        advance_frame(frame, next_frame)
        print_frame(frame)
        time.sleep(0.125)


if __name__ == "__main__":
    main()
