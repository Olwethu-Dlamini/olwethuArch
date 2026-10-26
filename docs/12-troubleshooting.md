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
