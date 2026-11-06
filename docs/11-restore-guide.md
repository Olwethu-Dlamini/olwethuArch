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
   - `etc/udev/rules.d/90-ideapad-conservation.rules` (IdeaPad only; NTFS marks it executable,
     so copy with `sudo install -m 644`)
   - NTFS lines from `etc/fstab` (UUIDs are specific to my disks)
5. Enable units from `packages/enabled-units.txt`:
   `sudo systemctl enable --now NetworkManager bluetooth docker tailscaled power-profiles-daemon systemd-timesyncd fstrim.timer paccache.timer reflector.timer`
   `kit-weekly-push.timer` is a user timer that the omp-by-oll kit's `install.sh` links and enables
   (Thursday 18:00 push of local commits); it is listed for completeness, not installed from here.
6. Restore WireGuard config separately into `/etc/wireguard`, then enable `wg-quick@wg0`.
7. Claude usage on the bar (not a package, `install.sh` does not do it): log in to Claude Code
   with `claude`, then `git clone https://github.com/mryll/claudebar ~/.local/src/claudebar`,
   `git -C ~/.local/src/claudebar checkout c187af2` (release 0.10.7) and
   `make -C ~/.local/src/claudebar install PREFIX=~/.local`.
8. Run `./install.sh`, log in on tty1, type `sway`.
9. `sudo tailscale up`, `gh auth login`, and set git `user.name`/`user.email`.
