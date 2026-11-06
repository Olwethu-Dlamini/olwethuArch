# Custom scripts: launcher, system menu, bar toggles, screensaver

A few small scripts hold most of the hand-written behaviour.

## `sway/launcher.sh` - click-away launcher (SUPER+Space)
wofi has no "close when focus is lost" option, so this wraps it:
1. If wofi is already running, check the Sway tree for a *visible* wofi window, then
   kill wofi (`pkill`, `pkill -9` if it is still alive after 0.2s). If it was visible
   the script exits, so pressing the key or the bar button again closes the launcher
   (toggle). If it was open on another workspace or screen it is replaced, so the key
   never just "does nothing".
2. Turn `focus_follows_mouse` **off** while open, so hovering cannot steal focus;
   a `trap` restores it on exit however the script ends.
3. Start `wofi --normal-window --show drun` in the background. `wofi/config` sorts
   entries alphabetically (`sort_order=alphabetical`) instead of by launch count.
4. Subscribe to Sway window events (`swaymsg -t subscribe -m '["window"]'`),
   keep only `focus` changes that did not land on wofi, and poll them on fd
   `$events` every 0.3s. If another window takes focus, kill wofi.

## `sway/system-menu.sh` - power menu (SUPER+Escape)
A wofi `--dmenu` list: Lock, Suspend, Relaunch bar, Reload sway, Log out,
Reboot, Power off - mapped to `swaylock`, `systemctl`, and `swaymsg`.
"Relaunch bar" is a safety hatch if Waybar misbehaves.

## `waybar/toggle.sh` - open-or-close popups from the bar
`toggle.sh <app_id> <command...>`: if a window with that `app_id` exists in the
Sway tree, kill it; otherwise launch the command detached with `setsid`. Used by
the volume and bluetooth modules so one click opens the mixer and a
second click closes it. It is the reason those apps get fixed floating rules in
the Sway config.

## `sway/screensaver.sh` + `screensaver.py` - "Emelda my lala" screensaver
swayidle runs `screensaver.sh` after 5 minutes. It skips if swaylock or a screensaver is
already up, runs `screensaver.py`, and when that exits starts `swaylock -f`. A crash or a
missing library therefore still locks the screen.

`screensaver.py` is a GTK3 layer-shell overlay on every output (covers the bar, keyboard
exclusive, pointer hidden): "Emelda my lala" in cream Noto Serif bold italic with a red glow and
a slow heartbeat pulse, over about 150 hearts (Gruvbox reds, pinks, orange) that rise, wobble and
pop before reaching the top. Hearts and the title are pre-rendered sprites, so a 1920x1080 frame
takes about 2.4 ms to draw at 24 fps. It closes on any key, click, scroll, touch, or a mouse move
of more than 25px (moves in the first 1.5 s are ignored). It also quits on its own when swaylock
is running, so the lock taken before sleep is not followed by a second one. The screen is *not*
locked while the hearts are showing.

`swaylock/make-image.py [W H]` redraws the still lock background `emelda.png` from the same
heart and title code; run it after changing the text, colours, or screen size.

## Key cheat-sheet
`SUPER+K` pipes `sway/keys.txt` into `wofi --dmenu`, giving an on-screen
reference without any extra tooling.
