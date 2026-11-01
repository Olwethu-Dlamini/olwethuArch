#!/usr/bin/env python3
"""Draw the still swaylock background: "Emelda my lala" over scattered hearts.

Uses the screensaver's heart shape, colours and font so both screens match.
Usage: make-image.py [WIDTH HEIGHT]   (default 1920 1080, writes emelda.png next to this file)
"""
import math
import os
import random
import sys

import cairo

sys.path.insert(0, os.path.expanduser("~/.config/sway"))
from screensaver import BG, FONT, HEART_RGBS, TEXT, draw_title, heart_path  # noqa: E402

RING_R = 70 + 50   # swaylock indicator-radius plus a margin: keep the centre clear


def main():
    w, h = (int(a) for a in sys.argv[1:3]) if len(sys.argv) == 3 else (1920, 1080)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "emelda.png")
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, w, h)
    cr = cairo.Context(surface)
    cr.set_source_rgb(*BG)
    cr.paint()

    cr.select_font_face(FONT, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(min(w / 10, h / 6))
    ext = cr.text_extents(TEXT)
    tx = (w - ext.width) / 2 - ext.x_bearing
    ty = h * 0.27 - ext.y_bearing - ext.height / 2        # above the swaylock ring
    text_box = (tx - 30, ty + ext.y_bearing - 30, ext.width + 60, ext.height + 60)

    rng = random.Random(1405)
    placed = 0
    while placed < 140:
        size = rng.uniform(14, 70)
        x, y = rng.uniform(0, w), rng.uniform(0, h)
        bx, by, bw, bh = text_box
        if bx - size < x < bx + bw + size and by - size < y < by + bh + size:
            continue
        if math.dist((x, y), (w / 2, h / 2)) < RING_R + size:
            continue
        heart_path(cr, x, y, size)
        cr.set_source_rgba(*rng.choice(HEART_RGBS), rng.uniform(0.35, 0.85))
        cr.fill()
        placed += 1

    draw_title(cr, tx, ty)
    surface.write_to_png(out)
    print(out)


if __name__ == "__main__":
    main()
