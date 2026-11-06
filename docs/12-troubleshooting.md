# Troubleshooting notes

- **Bar missing or frozen:** Super+Esc -> "Relaunch bar", or
  `systemctl --user restart waybar.service`.
- **Launcher will not close / mouse focus stuck off:** `launcher.sh` turns
  `focus_follows_mouse` off while open; run `swaymsg focus_follows_mouse yes`.
- **No sound keys on lock screen:** bindings need `--locked`; check `wpctl status`.
- **DNS broken after Tailscale:** compare `/etc/resolv.conf` with
  `/etc/resolv.pre-tailscale-backup.conf`.
- **Boot hangs on a data disk:** fstab entries are `nofail` with a 10s timeout,
  so it should not; check `journalctl -b -u systemd-fsck@*` for a dirty NTFS flag.
- **Scripts not executable after cloning:** NTFS drops modes; run `install.sh`.
- **Popups open in an odd spot:** they use `move position cursor`; click the bar module again after reloading.
- **Battery charges to 100% again:** conservation mode is off. To check, run
  `cat /sys/class/power_supply/BAT0/charge_types` (`[Long_Life]` means it is on). To turn it on now,
  run `echo 1 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode`. If it
  is off after a reboot, check that `/etc/udev/rules.d/90-ideapad-conservation.rules` is installed.
- **Screen locks at 5 min with no hearts:** the screensaver failed and `screensaver.sh` locked
  instead. Run `python3 ~/.config/sway/screensaver.py` from a terminal to see the error (it needs
  `python-gobject`, `python-cairo`, `gtk3`, `gtk-layer-shell`). Press any key to close it.
- **Hearts never appear after editing the Sway config:** `swayidle` is started with `exec`, so a
  reload does not restart it. Log out and back in, or `pkill swayidle` and re-run the swayidle
  line from the config with `swaymsg exec`.
- **Pictures missing from clipboard history (Super+Ctrl+V):** check the recorder runs with
  `pgrep -af 'wl-paste --watch cliphist'`; copied pictures show up in `cliphist list` as
  `[[ binary data ... png ... ]]`. Thumbnails live in `~/.cache/cliphist-thumbs` and can be deleted
  at any time; the picker decodes them again.
- **Claude usage module shows a pause sign or nothing:** the usage endpoint answered 429 (rate
  limit; it clears on the next 300 s refresh) or Claude Code is logged out; run `claude` to log in.
  Run `~/.local/bin/claudebar` by hand to see the error.
