# Custom scripts: launcher, system menu, bar toggles

Three small scripts hold most of the hand-written behaviour.

## `sway/launcher.sh` - click-away launcher (SUPER+Space)
wofi has no "close when focus is lost" option, so this wraps it:
1. If wofi is already running, `pkill` it and exit - so pressing the key again
   closes the launcher (toggle).
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
the volume, network and bluetooth modules so one click opens the mixer and a
second click closes it. It is the reason those apps get fixed floating rules in
the Sway config.

## Key cheat-sheet
`SUPER+K` pipes `sway/keys.txt` into `wofi --dmenu`, giving an on-screen
reference without any extra tooling.
