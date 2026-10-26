# What I made custom (summary)

Stock Arch plus packages is the baseline. These are the pieces that are mine:

1. **Sway config** - Omarchy-style keymap and Gruvbox look on a bare Sway
   (`docs/03-sway.md`).
2. **`launcher.sh`** - toggling, click-away wofi launcher driven by Sway window
   events (`docs/04`).
3. **`system-menu.sh`** and **`keys.txt`** - power menu and on-screen keymap.
4. **Waybar** - flat bar, per-module colours, scroll-to-dim brightness, run as a
   `Restart=always` user service, with **`toggle.sh`** popups (`docs/05`).
5. **Lid policy** - logind ignores the lid; Sway disables only the panel.
6. **fstab NTFS options** - user-owned, `nofail`, 10s timeout (`docs/01`).
7. **Networking glue** - wg0 hidden from NetworkManager, resolv.conf backup around
   Tailscale (`docs/08`).
8. **Plugin-free Neovim, framework-free bash, opinionated gitconfig** (`docs/07`).
9. **Package philosophy** - 88 explicit packages, no DM/DE (`docs/02`).

## Open to-dos found during review
- Make `grim` and `slurp` explicit installs.
- Consider a display manager or a `.bash_profile` snippet to autostart Sway on tty1.
- `Thunar` and `mpv` have little or no custom config worth mirroring yet.
