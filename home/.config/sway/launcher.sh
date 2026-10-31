#!/usr/bin/env bash
# App launcher that closes when another window takes focus (click away to dismiss).
# Pressing the key (or the bar button) again while it is open on the current workspace closes it.
# A launcher left open on another workspace or screen is replaced, so the key never just "does nothing".

if pgrep -x wofi >/dev/null; then
    visible=$(swaymsg -t get_tree | python3 -c '
import json, sys
def walk(n):
    if (n.get("app_id") or "") == "wofi" and n.get("visible"):
        return True
    return any(walk(c) for c in n.get("nodes", []) + n.get("floating_nodes", []))
print("yes" if walk(json.load(sys.stdin)) else "no")')
    pkill -x wofi
    sleep 0.2
    pgrep -x wofi >/dev/null && pkill -9 -x wofi
    [ "$visible" = "yes" ] && exit 0
fi

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
