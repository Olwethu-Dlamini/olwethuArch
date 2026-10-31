# Rebuilding this system from scratch

1. Install Arch (`archinstall` or manual): ext4 root, 1 GiB ESP at `/boot`,
   systemd-boot, `linux linux-firmware intel-ucode base-devel networkmanager`.
2. Create user `<user>`, add to `wheel`, enable `NetworkManager`.
3. Install packages: `sudo pacman -S --needed - < packages/explicit.txt`;
   install `yay-bin` manually, then `yay -S brave-bin`.
4. Copy system files by hand, reviewing each:
   - `etc/systemd/logind.conf.d/lid-ignore.conf`
   - `etc/NetworkManager/conf.d/unmanaged-wg.conf`
   - `etc/xdg/reflector/reflector.conf`
   - NTFS lines from `etc/fstab` (UUIDs are specific to my disks)
5. Enable units from `packages/enabled-units.txt`:
   `sudo systemctl enable --now NetworkManager bluetooth docker tailscaled power-profiles-daemon systemd-timesyncd fstrim.timer paccache.timer reflector.timer`
   `kit-weekly-push.timer` is a user timer that the omp-by-oll kit's `install.sh` links and enables
   (Thursday 18:00 push of local commits); it is listed for completeness, not installed from here.
6. Restore WireGuard config separately into `/etc/wireguard`, then enable `wg-quick@wg0`.
7. Run `./install.sh`, log in on tty1, type `sway`.
8. `sudo tailscale up`, `gh auth login`, and set git `user.name`/`user.email`.
