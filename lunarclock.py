#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "rich>=13.7",
# ]
# ///
"""
lunarclock — based on the moon phase posts of Froyo☆Tam

In particular, this post:
https://bsky.app/profile/froyotam.bsky.social/post/3mm45hoc4w22k
"""

import datetime
import time

from rich.console import Console

CONSOLE = Console()

PHASES = "🌕🌖🌗🌘🌑🌒🌓🌔"

BITS_TO_PHASE_INDEX = [0, 2, 6, 4]


def clear_screen() -> None:
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

FONT = {
    k: xs_to_phases(xs) for k, xs in {
        ' ' : [
            "    ",
            "    ",
            "    ",
            "    ",
            "    ",
            "    ",
            "    ",
        ],
        '|' : [
            "    ",
            " XX ",
            " XX ",
            " XX ",
            " XX ",
            " XX ",
            "    ",
        ],
        ':' : [
            "    ",
            " XX ",
            " XX ",
            "    ",
            " XX ",
            " XX ",
            "    ",
        ],
        '0' : [
            "      ",
            " XXXX ",
            " XX X ",
            " XX X ",
            " XX X ",
            " XXXX ",
            "      ",
        ],
        '1' : [
            "      ",
            "   XX ",
            "  XXX ",
            "   XX ",
            "   XX ",
            "   XX ",
            "      ",
        ],
        '2' : [
            "      ",
            " XXX  ",
            "    X ",
            "  XX  ",
            " XX   ",
            " XXXX ",
            "      ",
        ],
        '3' : [
            "      ",
            " XXX  ",
            "   XX ",
            " XXX  ",
            "   XX ",
            " XXX  ",
            "      ",
        ],
        '4' : [
            "      ",
            " XX X ",
            " XX X ",
            " XXXX ",
            "    X ",
            "    X ",
            "      ",
        ],
        '5' : [
            "      ",
            " XXXX ",
            " XX   ",
            " XXX  ",
            "   XX ",
            " XXX  ",
            "      ",
        ],
        '6' : [
            "      ",
            "  XXX ",
            " XX   ",
            " XXXX ",
            " XX X ",
            "  XXX ",
            "      ",
        ],
        '7' : [
            "      ",
            " XXXX ",
            "   XX ",
            "  XX  ",
            " XX   ",
            " XX   ",
            "      ",
        ],
        '8' : [
            "      ",
            "  XX  ",
            " XX X ",
            "  XX  ",
            " XX X ",
            "  XX  ",
            "      ",
        ],
        '9' : [
            "      ",
            "  XXX ",
            " XX X ",
            "  XXX ",
            "    X ",
            " XXX  ",
            "      ",
        ],
        'p' : [
            " XXXX XX X  ",
            " X    X X X ",
        ],
        'a' : [
            " XXX  XX X  ",
            " X  X X X X ",
        ],
    }.items()
}

def print_frame(frame: list[list[int]]) -> None:
    clear_screen()
    for line in frame:
        print("".join(PHASES[i] for i in line))

def advance_frame(frame: list[list[int]], next_frame: list[list[int]]) -> None:
    n = len(PHASES)
    for i in range(len(frame)):
        for j in range(len(frame[i])):
            if frame[i][j] != next_frame[i][j]:
                frame[i][j] = (frame[i][j] + 1) % n

def now() -> str:
    """Returns time in format HHMMSSp, where p is "p" or "a"."""
    t = datetime.datetime.now()
    return t.strftime("%I%M%S") + ("p" if t.hour >= 12 else "a")

def render_char_to_frame(frame: list[list[int]], c: str) -> None:
    glyph = FONT[c]
    for i in range(len(frame)):
        frame[i] += glyph[i]

def clock_frame() -> list[list[int]]:
    n = now()
    frame = [[] for x in range(len(FONT[' ']))]
    render_char_to_frame(frame, '|' if n[0] == '1' else ' ')
    render_char_to_frame(frame, str(n[1]))
    render_char_to_frame(frame, ':')
    render_char_to_frame(frame, str(n[2]))
    render_char_to_frame(frame, str(n[3]))
    render_char_to_frame(frame, ':')
    render_char_to_frame(frame, str(n[4]))
    render_char_to_frame(frame, str(n[5]))

    ampm = [[] for x in range(len(FONT['a']))]
    render_char_to_frame(ampm, 'a' if n[-1] == 'a' else 'p')

    padding = [0] * (len(frame[0]) - len(ampm[0]))
    frame.extend(padding + row for row in ampm)
    frame.extend([[0] * len(frame[0])])

    return frame


def main() -> None:
    frame = clock_frame()
    print_frame(frame)
    while True:
        time.sleep(0.125)
        next_frame = clock_frame()
        advance_frame(frame, next_frame)
        print_frame(frame)


if __name__ == "__main__":
    main()
