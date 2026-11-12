# Network, VPN and power

- **NetworkManager** manages Wi-Fi/Ethernet. Sway starts `nm-applet --indicator`, a tray
  icon that lists the networks in range (one click connects, the password is asked once);
  `nmtui` (Super+Shift+N) does the same in a floating kitty window. The bar has no Wi-Fi
  module of its own; the tray icon is the one Wi-Fi control.
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
  and handled by Sway (panel off and `power-saver` while closed, `balanced` when opened);
  swayidle locks at 5 min and blanks at 10.
- **Battery:** Lenovo conservation mode keeps the battery at about 60% while on AC, so it
  does not sit at 100% all day. The EC can forget the setting, so
  `etc/udev/rules.d/90-ideapad-conservation.rules` writes `conservation_mode=1` every time
  `ideapad_acpi` binds at boot. To check it, run `cat /sys/class/power_supply/BAT0/charge_types`:
  it should show `[Long_Life]`. To charge to 100% for a trip:
  `echo 0 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode`
  (it turns back on at the next boot). While it is off the bar shows a red "no 60% cap" next to
  the battery (`docs/05`), so a dropped setting or a rule that was never installed shows up.
- **Time/mirrors:** `systemd-timesyncd`, and `reflector.timer` refreshing the ten
  fastest HTTPS mirrors from South Africa, Germany and the Netherlands (`--country ZA,DE,NL
  --latest 10 --sort rate`).
