# Hardware, boot and storage

- **Machine:** Intel laptop (hostname `<hostname>`) - Intel iGPU (`intel-media-driver`,
  `vulkan-intel`, `intel-gpu-tools`, `libva-utils` for VA-API), `sof-firmware`
  for the audio DSP, `intel-ucode` for microcode. UEFI (Insyde), Secure Boot off.
- **Disks:** 238 GB NVMe holds Linux: `nvme0n1p1` 1 GiB vfat `/boot` (ESP),
  `nvme0n1p2` ext4 `/`. A 931 GB SATA disk holds three NTFS partitions that
  predate Linux (shared with Windows): `Linux` (projects, including this repo),
  `escape`, and a third data partition.
- **Bootloader:** systemd-boot, installed with `bootctl`.
- **Custom bit - NTFS mounts** (`etc/fstab`): mounted with `ntfs-3g` under
  `/media/<user>/...` with `uid=1000,gid=1000` so my user owns the files,
  `windows_names` to refuse names Windows cannot open, and
  `nofail,x-systemd.device-timeout=10` so an absent or dirty disk never stalls
  boot. `x-gvfs-show` makes them appear in Thunar.
- **SSD care:** `fstrim.timer` is enabled; `paccache.timer` prunes the pacman cache.
- **Caveat:** this repo lives on NTFS, so file modes are not preserved
  (`core.filemode = false` in my gitconfig). Executable bits on the scripts are
  restored by `install.sh`.
