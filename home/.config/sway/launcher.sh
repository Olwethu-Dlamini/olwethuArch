#!/usr/bin/env bash
# App launcher that closes when another window takes focus (click away to dismiss).
# Pressing the key again while it is open also closes it.
pkill -x wofi && exit 0

# hovering must not steal focus while the launcher is open, only clicks should
swaymsg focus_follows_mouse no >/dev/null
trap 'swaymsg focus_follows_mouse yes >/dev/null' EXIT

wofi --normal-window --show drun &
wofi_pid=$!

# one JSON line per window event; keep only focus changes that did not land on wofi
exec {events}< <(swaymsg -r -t subscribe -m '["window"]' \
    | grep --line-buffered '"change": "focus"' \
    | grep --line-buffered -v '"app_id": "wofi"')

while kill -0 "$wofi_pid" 2>/dev/null; do
    if read -r -t 0.3 -u "$events" _; then
        kill "$wofi_pid"
        break
    fi
done
