# Packages: what is installed and why

88 explicitly installed packages (`packages/explicit.txt`), only 3 from the AUR.
Grouped by job:

- **Base:** `base base-devel linux linux-firmware intel-ucode sudo nano vim man-db man-pages`
- **Compositor/desktop:** `sway swayidle swaylock waybar wofi wmenu mako foot xorg-xwayland xdg-desktop-portal-wlr xdg-desktop-portal-gtk polkit-gnome gnome-keyring seahorse`
- **Wayland utilities:** `wl-clipboard cliphist wf-recorder brightnessctl` (plus `grim`/`slurp` used by the screenshot keys; they are present as dependencies, not explicit installs - install them explicitly if they ever disappear)
- **Audio:** `pipewire pipewire-alsa pipewire-pulse pipewire-jack wireplumber alsa-utils pavucontrol rtkit`
- **Network:** `networkmanager network-manager-applet tailscale wireguard-tools systemd-resolvconf bluez bluez-utils blueman`
- **Power:** `power-profiles-daemon`
- **Files:** `thunar gvfs file-roller ntfs-3g exfatprogs dosfstools xdg-user-dirs`
- **Dev:** `git github-cli neovim nodejs npm docker docker-buildx docker-compose kubectl ripgrep fd fzf starship htop`
- **Apps:** `firefox thunderbird mpv brave-bin` (AUR)
- **Fonts:** `ttf-jetbrains-mono ttf-jetbrains-mono-nerd noto-fonts noto-fonts-emoji ttf-dejavu woff2-font-awesome`
- **Maintenance:** `reflector pacman-contrib yay-bin` (AUR)

## Philosophy

No display manager, no desktop environment, no GUI settings daemons. Each
component is a separate small program wired together by the Sway config.
Thunar, pavucontrol, blueman and nm-connection-editor are the only GUI tools,
and the bar opens them on demand.

## Restore

    sudo pacman -S --needed - < packages/explicit.txt   # official repos
    yay -S brave-bin yay-bin                            # foreign packages
