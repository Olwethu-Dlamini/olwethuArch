# Waybar

Files: `waybar/config.jsonc`, `waybar/style.css`, `systemd/user/waybar.service`.

- **Layout:** workspaces + sway mode on the left, clock in the centre (tooltip is
  a calendar, click toggles the long date), then right-aligned: volume, network,
  bluetooth, CPU, memory, backlight, battery, tray. 28px tall, flat, full width.
- **Interaction:** scroll on the backlight module changes brightness;
  right-click on volume mutes; left-click on volume/network/bluetooth opens
  pavucontrol / nm-connection-editor / blueman-manager via `toggle.sh`.
- **Colour per module** (Gruvbox): volume pink, network green, bluetooth blue,
  CPU/backlight yellow, memory/battery green; battery warns yellow <25%, red <12%.
- **Run as a service:** instead of `exec waybar` in Sway, a user unit with
  `Restart=always` keeps it alive. Sway's `exec_always systemctl --user restart
  waybar.service` makes a config reload also reload the bar.
- **Evolution:** started as a floating, rounded, spaced bar showing the window
  title (a `.old` variant); simplified into the flat bar to match Omarchy; the
  backlight module was added last.
- **Caveat:** `toggle.sh` paths in the JSON are absolute (`~/...`).
