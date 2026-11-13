# Waybar

Files: `waybar/config.jsonc`, `waybar/style.css`, `systemd/user/waybar.service`.

- **Layout:** app-launcher button, workspaces and sway mode on the left, clock in the centre (tooltip is
  a calendar, click toggles the long date), then right-aligned: volume, volume slider,
  bluetooth, CPU, memory, backlight, battery, Claude usage, tray (Wi-Fi is the nm-applet icon in the tray:
  click it to list the networks in range; Super+Shift+N opens `nmtui`). 28px tall, flat, full width.
- **Interaction:** scroll on the backlight module changes brightness; scroll on volume
  changes it in 5% steps, or drag the slider (0-100%, a pink fill on a dark trough with
  the knob hidden); right-click on volume mutes; left-click on volume/bluetooth opens
  pavucontrol / blueman-manager via `toggle.sh`; left-click
  on the launcher button runs `sway/launcher.sh`, same as Super+Space, so clicking it
  again closes the launcher; right-click on it opens the power menu (`sway/system-menu.sh`,
  same as Super+Esc) to lock, suspend, reboot or power off.
- **Claude usage (`custom/claudebar`):** the Claude icon and the current session %, from
  `~/.local/bin/claudebar` (https://github.com/mryll/claudebar, 0.10.7, built from source). The
  tooltip shows the session, weekly and per-model limits. It refreshes every 300 s, the minimum,
  because the usage endpoint rate-limits; click opens https://claude.ai/settings/usage. It reads
  the Claude Code login on the machine, so `claude` must be logged in; it needs `curl` and `jq`.
- **Battery (`custom/battery`):** `waybar/battery.sh` replaces the built-in battery module,
  which cannot see `charge_types`. Every 30 s it prints the battery icon (a bolt while charging)
  and the %, and adds the class `eco` while conservation mode is on (`[Long_Life]`, the 60% cap,
  `docs/08`), which turns the battery aqua. The tooltip shows the % and status, plus a line when
  the cap is on.
- **Colour per module** (Gruvbox): volume pink, bluetooth blue,
  CPU/backlight yellow, memory/battery green (battery aqua while the 60% cap is on), launcher
  button blue; battery warns yellow at 25% or less, red at 12% or less.
- **Run as a service:** instead of `exec waybar` in Sway, a user unit with
  `Restart=always` keeps it alive. Sway's `exec_always systemctl --user restart
  waybar.service` makes a config reload also reload the bar.
- **Evolution:** started as a floating, rounded, spaced bar showing the window
  title (a `.old` variant); simplified into the flat bar to match Omarchy; the
  backlight module was added last.
- **Paths:** popup commands use `~/.config/waybar/toggle.sh` (Waybar runs them through a shell), so the config has no user-specific paths.
