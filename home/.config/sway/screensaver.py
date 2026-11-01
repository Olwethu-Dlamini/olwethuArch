#!/usr/bin/env python3
"""Idle screensaver: "Emelda my lala" with hearts bubbling up, on every output.

Any key, click, or real mouse move closes it (screensaver.sh then starts swaylock).
It also closes by itself when swaylock is already running, so a lock taken
before sleep is not followed by a second lock.
Exit code 0: closed by input. Exit code 3: swaylock was already running.
"""
import functools
import math
import random
import subprocess
import sys
import time

import cairo

TEXT = "Emelda my lala"
FONT = "Noto Serif"
BG = (0x1d / 255, 0x20 / 255, 0x21 / 255)
TEXT_RGB = (0xfb / 255, 0xf1 / 255, 0xc7 / 255)
GLOW_RGB = (0xfb / 255, 0x49 / 255, 0x34 / 255)
# Gruvbox reds, pinks, purples and one orange
HEART_RGBS = [
    (0xfb / 255, 0x49 / 255, 0x34 / 255),
    (0xcc / 255, 0x24 / 255, 0x1d / 255),
    (0xd3 / 255, 0x86 / 255, 0x9b / 255),
    (0xb1 / 255, 0x62 / 255, 0x86 / 255),
    (0xfe / 255, 0x80 / 255, 0x19 / 255),
]
FPS = 24              # smooth enough for drifting hearts, lighter on the CPU than 30
GRACE_S = 1.5          # ignore pointer motion right after the window appears
MOVE_PX = 25           # a mouse move must travel this far to count
LOCK_POLL_S = 1.0


def heart_path(cr, x, y, size):
    """Heart centred on (x, y), `size` pixels wide."""
    s = size / 2
    cr.move_to(x, y + s * 0.9)
    cr.curve_to(x - s * 1.2, y + s * 0.1, x - s * 0.9, y - s * 0.9, x, y - s * 0.35)
    cr.curve_to(x + s * 0.9, y - s * 0.9, x + s * 1.2, y + s * 0.1, x, y + s * 0.9)
    cr.close_path()


@functools.lru_cache(maxsize=None)
def heart_sprite(rgb, size):
    """One heart pre-drawn on its own small surface; `size` is rounded so the cache stays small.
    Filling and stroking ~150 anti-aliased paths per frame was 10 ms; blitting sprites is far less."""
    dim = int(size * 1.3) + 4
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, dim, dim)
    cr = cairo.Context(surf)
    heart_path(cr, dim / 2, dim / 2, size)
    cr.set_source_rgb(*rgb)
    cr.fill_preserve()
    cr.set_source_rgba(1, 1, 1, 0.3)   # thin highlight edge, bubble-like
    cr.set_line_width(max(1.0, size / 22))
    cr.stroke()
    return surf


class Heart:
    def __init__(self, width, height, rng, anywhere=False):
        self.size = rng.uniform(14, 64)
        self.x0 = rng.uniform(0, width)
        self.y = rng.uniform(0, height) if anywhere else height + self.size
        self.speed = rng.uniform(50, 150) * (40 / self.size) ** 0.3   # small ones rise faster
        self.wobble = rng.uniform(8, 36)
        self.freq = rng.uniform(0.6, 1.6)
        self.phase = rng.uniform(0, math.tau)
        self.rgb = rng.choice(HEART_RGBS)
        self.pop_at = rng.uniform(0.05, 0.45) * height    # bubbles burst before the top
        self.popping = 0.0                                # seconds since the burst began

    def step(self, dt):
        if self.popping:
            self.popping += dt
        else:
            self.y -= self.speed * dt
            if self.y <= self.pop_at:
                self.popping = 1e-6

    @property
    def gone(self):
        return self.popping > 0.35

    def draw(self, cr, t):
        x = self.x0 + math.sin(t * self.freq + self.phase) * self.wobble
        size, alpha = self.size, 0.85
        if self.popping:
            k = self.popping / 0.35
            size *= 1 + 0.8 * k
            alpha *= 1 - k
        sprite = heart_sprite(self.rgb, round(size / 3) * 3)
        half = sprite.get_width() / 2
        cr.set_source_surface(sprite, round(x - half), round(self.y - half))
        cr.paint_with_alpha(alpha)


def draw_title(cr, x, y):
    """TEXT with a soft red glow, baseline at (x, y); font face and size already set on cr."""
    for r, a in ((10, 0.06), (6, 0.10), (3, 0.16)):
        for dx, dy in ((r, 0), (-r, 0), (0, r), (0, -r)):
            cr.move_to(x + dx, y + dy)
            cr.set_source_rgba(*GLOW_RGB, a)
            cr.show_text(TEXT)
    cr.move_to(x, y)
    cr.set_source_rgb(*TEXT_RGB)
    cr.show_text(TEXT)


def title_surface(font_size):
    """Pre-render the title once; redrawing 13 glyph runs every frame costs most of the CPU."""
    probe = cairo.Context(cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1))
    probe.select_font_face(FONT, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
    probe.set_font_size(font_size)
    ext = probe.text_extents(TEXT)
    pad = 16
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(ext.width) + 2 * pad, int(ext.height) + 2 * pad)
    cr = cairo.Context(surf)
    cr.select_font_face(FONT, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(font_size)
    draw_title(cr, pad - ext.x_bearing, pad - ext.y_bearing)
    return surf


class Scene:
    """Everything that is drawn; independent of GTK so a frame can be rendered offscreen."""

    def __init__(self, width, height, seed=None):
        self.width, self.height = width, height
        self.rng = random.Random(seed)
        self.target = max(50, int(width * height / 14000))   # about 150 hearts on 1920x1080
        self.hearts = [Heart(width, height, self.rng, anywhere=True) for _ in range(self.target)]
        self.title = title_surface(min(width / 9, height / 5))

    def step(self, dt):
        for h in self.hearts:
            h.step(dt)
        self.hearts = [h for h in self.hearts if not h.gone]
        while len(self.hearts) < self.target:
            self.hearts.append(Heart(self.width, self.height, self.rng))

    def draw(self, cr, t):
        w, h = self.width, self.height
        cr.set_source_rgb(*BG)
        cr.paint()
        for heart in self.hearts:
            heart.draw(cr, t)

        pulse = 1 + 0.035 * math.sin(t * 2.2)          # a slow heartbeat
        tw, th = self.title.get_width(), self.title.get_height()
        cr.save()
        cr.translate(w / 2, h / 2)
        cr.scale(pulse, pulse)
        cr.set_source_surface(self.title, -tw / 2, -th / 2)
        cr.paint()
        cr.restore()


def swaylock_running():
    return subprocess.run(["pgrep", "-x", "swaylock"], stdout=subprocess.DEVNULL).returncode == 0


def main():
    import gi
    gi.require_version("Gdk", "3.0")
    gi.require_version("Gtk", "3.0")
    gi.require_version("GtkLayerShell", "0.1")

    from gi.repository import Gdk, GLib, Gtk, GtkLayerShell
    display = Gdk.Display.get_default()
    if display is None or display.get_n_monitors() == 0:
        return 0   # nothing to draw on (lid shut, screens off): let screensaver.sh lock at once

    start = time.monotonic()
    state = {"exit": 0, "pointer": None}

    def quit_(code=0):
        if state.get("quitting"):
            return
        state["quitting"] = True
        state["exit"] = code
        Gtk.main_quit()

    def on_motion(_w, ev):
        if time.monotonic() - start < GRACE_S:
            return
        if state["pointer"] is None:
            state["pointer"] = (ev.x_root, ev.y_root)
        elif math.dist(state["pointer"], (ev.x_root, ev.y_root)) > MOVE_PX:
            quit_()

    windows = []
    for i in range(display.get_n_monitors()):
        monitor = display.get_monitor(i)
        geo = monitor.get_geometry()
        scene = Scene(geo.width, geo.height)
        win = Gtk.Window()
        GtkLayerShell.init_for_window(win)
        GtkLayerShell.set_monitor(win, monitor)
        GtkLayerShell.set_layer(win, GtkLayerShell.Layer.OVERLAY)
        GtkLayerShell.set_namespace(win, "screensaver")
        GtkLayerShell.set_exclusive_zone(win, -1)      # cover the bar too
        for edge in (GtkLayerShell.Edge.TOP, GtkLayerShell.Edge.BOTTOM,
                     GtkLayerShell.Edge.LEFT, GtkLayerShell.Edge.RIGHT):
            GtkLayerShell.set_anchor(win, edge, True)
        if i == 0:
            GtkLayerShell.set_keyboard_mode(win, GtkLayerShell.KeyboardMode.EXCLUSIVE)

        area = Gtk.DrawingArea()
        area.connect("draw", lambda _a, cr, s=scene: s.draw(cr, time.monotonic() - start))
        win.add(area)
        win.add_events(Gdk.EventMask.POINTER_MOTION_MASK | Gdk.EventMask.BUTTON_PRESS_MASK
                       | Gdk.EventMask.KEY_PRESS_MASK | Gdk.EventMask.TOUCH_MASK
                       | Gdk.EventMask.SCROLL_MASK)
        win.connect("key-press-event", lambda *_: quit_())
        win.connect("button-press-event", lambda *_: quit_())
        win.connect("touch-event", lambda *_: quit_())
        win.connect("scroll-event", lambda *_: quit_())
        win.connect("motion-notify-event", on_motion)
        win.connect("destroy", lambda *_: quit_())
        win.show_all()
        # hide the pointer while the hearts are up
        win.get_window().set_cursor(Gdk.Cursor.new_for_display(display, Gdk.CursorType.BLANK_CURSOR))
        windows.append((area, scene))

    last = [time.monotonic()]

    def tick():
        now = time.monotonic()
        dt, last[0] = min(now - last[0], 0.1), now
        for area, scene in windows:
            scene.step(dt)
            area.queue_draw()
        return True

    def watch_lock():
        if swaylock_running():
            quit_(3)
        return True

    GLib.timeout_add(1000 // FPS, tick)
    GLib.timeout_add(int(LOCK_POLL_S * 1000), watch_lock)
    Gtk.main()
    return state["exit"]


if __name__ == "__main__":
    sys.exit(main())
