# olwethuArch

A documented mirror of my personal Arch Linux install (hostname `<hostname>`).
Everything here is either a copy of a real config from the machine or a
write-up of *why* it is the way it is.

The setup is **Omarchy-inspired but hand-built**: I liked Omarchy's keybindings
and look, but instead of installing the whole distro layer I rebuilt the parts I
wanted on a plain Arch base with Sway, so I understand every file.

## Docs
0. [Overview](docs/00-overview.md)
1. [Hardware, boot, storage](docs/01-hardware-boot-storage.md)
2. [Packages](docs/02-packages.md)
3. [Sway](docs/03-sway.md)
4. [Launcher and menu scripts](docs/04-launcher-and-menus.md)
5. [Waybar](docs/05-waybar.md)
6. [Theming](docs/06-theming.md)
7. [Shell, editor, git](docs/07-shell-and-editor.md)
8. [Network and power](docs/08-network-and-power.md)
9. [What is custom + to-dos](docs/09-what-is-custom.md)
10. [Keybindings](docs/10-keybindings.md)
11. [Restore guide](docs/11-restore-guide.md)
12. [Troubleshooting](docs/12-troubleshooting.md)

## Layout
- `home/` - files that belong in `$HOME` (`install.sh` deploys them)
- `etc/` - system files, copy by hand with sudo
- `packages/` - explicit/AUR package lists and enabled units

Secrets (ssh, gpg, kube, browser profiles, wireguard keys) are never stored.
