# Overview: how the system fits together

| Layer | Choice | Why |
|---|---|---|
| Base | Arch Linux, `linux` kernel, `base-devel` | Rolling, minimal, I choose every package |
| Boot | systemd-boot on a 1 GiB ESP (`/boot`) | Simple, UEFI-only laptop |
| Compositor | **Sway** (Wayland, i3-compatible) | Tiling, scriptable, no DE needed |
| Bar | **Waybar**, run as a systemd *user* service | Survives crashes, restartable |
| Launcher | **wofi** wrapped in a custom script | Click-away-to-close behaviour |
| Terminal | **foot** | Fast, native Wayland |
| Notifications | **mako** | Tiny Wayland daemon |
| Lock/idle | **swaylock** + **swayidle** | Standard sway stack |
| Audio | PipeWire + WirePlumber (`wpctl`) | Modern default |
| Network | NetworkManager + Tailscale + WireGuard | Wi-Fi plus private mesh/VPN |
| Editor | Neovim, zero plugins | Everything built in |
| Shell | bash + starship + fzf | No framework |

Boot flow: UEFI -> systemd-boot -> `getty@tty1` -> login -> Sway is launched from
the TTY by typing `sway` (no display manager is installed) -> `exec` lines in the Sway config start mako, polkit agent, cliphist and
the Waybar user service.

What is *custom* (as opposed to stock Arch) is documented per area in the
following files. The short version: the Sway config, the three helper scripts,
the Waybar layout/styling, the lid-switch policy, and the VPN/DNS plumbing are
mine; everything else is default package behaviour.
