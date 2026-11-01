#!/usr/bin/env bash
# Idle screensaver: hearts until any input, then the lock screen.
# If the hearts fail to start or crash, the screen is locked straight away.
pgrep -x swaylock >/dev/null && exit 0
pgrep -f 'sway/screensaver.py' >/dev/null && exit 0
python3 "$HOME/.config/sway/screensaver.py"
pgrep -x swaylock >/dev/null || exec swaylock -f
