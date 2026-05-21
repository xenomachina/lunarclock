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

NEXT_PHASE = {PHASES[i]: PHASES[(i + 1) % len(PHASES)] for i in range(len(PHASES))}


FONT = {
    " ": [
        "🌕🌕",
        "🌕🌕",
        "🌕🌕",
        "🌕🌕",
        "🌕🌕",
    ],
    # Skinnier 1, used only in 10's place of hours
    "|": [
        "🌗🌓",
        "🌗🌓",
        "🌗🌓",
        "🌗🌓",
        "🌗🌓",
    ],
    ":": [
        "🌗🌓",
        "🌗🌓",
        "🌕🌕",
        "🌗🌓",
        "🌗🌓",
    ],
    "0": [
        "🌗🌑🌓",
        "🌗🌓🌓",
        "🌗🌓🌓",
        "🌗🌓🌓",
        "🌗🌑🌓",
    ],
    "1": [
        "🌕🌗🌓",
        "🌕🌗🌓",
        "🌕🌗🌓",
        "🌕🌗🌓",
        "🌕🌗🌓",
    ],
    "2": [
        "🌗🌑🌕",
        "🌕🌗🌓",
        "🌕🌑🌕",
        "🌗🌓🌕",
        "🌗🌑🌓",
    ],
    "3": [
        "🌗🌑🌔",
        "🌕🌗🌓",
        "🌗🌑🌔",
        "🌕🌗🌓",
        "🌗🌑🌔",
    ],
    "4": [
        "🌗🌓🌓",
        "🌘🌔🌓",
        "🌘🌑🌓",
        "🌕🌕🌓",
        "🌕🌕🌓",
    ],
    "5": [
        "🌗🌑🌓",
        "🌗🌓🌕",
        "🌗🌑🌕",
        "🌕🌗🌓",
        "🌗🌑🌕",
    ],
    "6": [
        "🌕🌑🌓",
        "🌘🌕🌕",
        "🌗🌑🌓",
        "🌘🌕🌒",
        "🌖🌑🌓",
    ],
    "7": [
        "🌗🌑🌓",
        "🌕🌗🌓",
        "🌕🌑🌕",
        "🌗🌓🌕",
        "🌗🌓🌕",
    ],
    "8": [
        "🌖🌑🌕",
        "🌗🌕🌓",
        "🌖🌑🌕",
        "🌗🌕🌓",
        "🌖🌑🌕",
    ],
    "9": [
        "🌕🌑🌓",
        "🌘🌕🌒",
        "🌕🌑🌓",
        "🌕🌕🌒",
        "🌗🌑🌕",
    ],
    "p": [
        "🌗🌑🌓🌑🌗🌕",
        "🌗🌕🌕🌓🌓🌓",
    ],
    "a": [
        "🌗🌑🌕🌑🌗🌕",
        "🌗🌕🌓🌓🌓🌓",
    ],
}


def print_frame(frame: list[str]) -> None:
    CONSOLE.clear()
    for line in frame:
        print(line)


def advance_frame(frame: list[str], next_frame: list[str]) -> None:
    for i in range(len(frame)):
        row = ""
        for j in range(len(frame[i])):
            c = frame[i][j]
            if c != next_frame[i][j]:
                c = NEXT_PHASE[c]
            row += c
        frame[i] = row


def now() -> str:
    """Returns time in format HHMMSSp, where p is "p" or "a"."""
    t = datetime.datetime.now()
    return t.strftime("%I%M%S") + ("p" if t.hour >= 12 else "a")


def render_glyph(frame: list[str], c: str) -> None:
    """Renders the specified glyph into the specified frame"""
    glyph = FONT[c]
    assert len(glyph) == len(frame)
    for i in range(len(frame)):
        frame[i] += glyph[i]


def clock_frame() -> list[str]:
    n = now()

    blank = PHASES[0]

    # render the numbers
    frame = [""] * len(FONT[" "])
    render_glyph(frame, "|" if n[0] == "1" else " ")
    render_glyph(frame, str(n[1]))
    render_glyph(frame, ":")
    render_glyph(frame, str(n[2]))
    render_glyph(frame, str(n[3]))
    render_glyph(frame, ":")
    render_glyph(frame, str(n[4]))
    render_glyph(frame, str(n[5]))

    # add top/bottom padding
    width = len(frame[0])
    blank_line = blank * width
    frame.insert(0, blank_line)
    frame.append(blank_line)

    # add right-aligned am/pm indicator
    ampm = [""] * len(FONT["a"])
    render_glyph(ampm, "a" if n[-1] == "a" else "p")
    padding = blank * (width - len(ampm[0]))
    frame.extend(padding + row for row in ampm)

    # add more bottom padding
    frame.append(blank_line)

    return frame


def main() -> None:
    frame = clock_frame()
    while True:
        print_frame(frame)
        time.sleep(0.125)
        next_frame = clock_frame()
        advance_frame(frame, next_frame)


if __name__ == "__main__":
    main()
