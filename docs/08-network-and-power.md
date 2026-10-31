# Network, VPN and power

- **NetworkManager** manages Wi-Fi/Ethernet; `nm-applet` and
  `nm-connection-editor` are the GUIs.
- **Tailscale** (`tailscaled.service`) provides the private mesh. It rewrites
  `/etc/resolv.conf`; a `resolv.pre-tailscale-backup.conf` is kept beside it, and
  `systemd-resolvconf` is installed to cooperate.
- **WireGuard:** `wg-quick@wg0.service` is enabled; keys live in
  `/etc/wireguard` (never mirrored). `etc/NetworkManager/conf.d/unmanaged-wg.conf`
  stops NetworkManager from claiming `wg0`.
- **Bluetooth:** `bluez` + `blueman`, service enabled.
- **Containers/k8s:** `docker` (+ buildx, compose) service enabled; `kubectl`
  installed, `~/.kube` is private.
- **Power:** `power-profiles-daemon` for profile switching; lid ignored by logind
  and handled by Sway; swayidle locks at 5 min and blanks at 10.
- **Time/mirrors:** `systemd-timesyncd`, and `reflector.timer` refreshing the ten
  fastest HTTPS mirrors from South Africa, Germany and the Netherlands (`--country ZA,DE,NL
  --latest 10 --sort rate`).
