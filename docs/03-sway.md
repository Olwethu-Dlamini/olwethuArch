# Sway: the heart of the customisation

File: `home/.config/sway/config`. Based on the stock Sway config but rewritten
into sections, with an **Omarchy-style keymap** (the pre-rewrite version still exists on the machine as
`~/.config/sway/config.pre-omarchy`, not mirrored here).

## Look
- Gruvbox palette: focused border `#fe8019` (orange), unfocused `#3c3836`,
  urgent `#fb4934`. Solid `#1d2021` wallpaper - no image to load.
- 2px borders, 6px inner / 8px outer gaps, `focus_follows_mouse yes`.
- Font: JetBrainsMono Nerd Font 10.

## Input
Touchpad: tap-to-click, natural scroll, disable-while-typing, two-finger scroll,
clickfinger clicks.

## Idle and lock (swayidle)
5 min -> lock; 10 min -> screens off (restored on activity); lock before sleep.

## Keybindings (`$mod` = Super)
Omarchy-flavoured: `Return` terminal, `Space` launcher, `Escape`/`Alt+Space`
system menu, `W` close, `Shift+B/F/T` browser/files/top, `Ctrl+V` clipboard
history, `K` pops up the key cheat-sheet (`keys.txt`), numbers for workspaces,
`Tab` cycles workspaces on the current output, `Print` for screenshots (region to
clipboard / full to file / region to file in `~/Pictures/Screenshots`).
Volume and brightness keys use `wpctl` and `brightnessctl` and work while locked
(`--locked`).

## Window rules
Popups (pavucontrol, blueman, nm-connection-editor, wofi) float at fixed
positions under the bar's right side; Firefox Picture-in-Picture floats and
sticks; dialogs float.

## Autostart
polkit-gnome agent, mako, `wl-paste --watch cliphist store` (clipboard history),
`gnome-keyring-daemon` (secret store for Brave passwords), and a systemd user import of the
Wayland environment so user services can reach the session. Waybar is restarted
through systemd on every reload (`exec_always`).

## Lid handling
logind ignores the lid (`etc/systemd/logind.conf.d/lid-ignore.conf`); Sway turns
the internal panel `eDP-1` off/on on lid close/open. Result: close the lid and
keep working on an external monitor or let background jobs run.

## Known rough edges

- Popup positions assume a 1920px-wide screen (`move absolute position 1452 40`).
