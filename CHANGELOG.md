# Changelog

- 2026-10-26: initial documented mirror of the <hostname> install (configs, packages, docs, install.sh).
- 2026-10-26 (later): screenshot keys now save a file and copy a real `image/png`; Super+V pastes in
  foot; launcher closes when another window is clicked; Brave Meet windows float and the
  "sharing your screen" bar is hidden in the scratchpad (Super+Shift+H); Thunar "Open Terminal
  Here" uses foot; NTFS drives visible in Thunar via `x-gvfs-show`.
- 2026-10-31: sync of 26-30 Oct changes. Waybar gets an app-launcher button and a volume slider
  (5% scroll steps); the launcher replaces a wofi left open on another workspace and lists apps
  alphabetically; pavucontrol opens below the bar; foot uses `[colors-dark]` (foot 1.28 removed
  `[colors]`) and opens links with Ctrl+Shift+O; Kate is the default text editor; reflector picks
  the 10 fastest ZA/DE/NL mirrors; .NET SDK env in bash; Bitbucket credential setup in gitconfig;
  6 new packages and the kit's weekly push timer listed.
- 2026-11-01: battery conservation mode back on (charge stops at about 60% instead of 100%); a
  udev rule turns it on again at every boot because the EC had dropped the setting.
- 2026-11-01 (later): after 5 min idle an "Emelda my lala" screensaver with bubbling hearts shows;
  any input swaps it for swaylock, whose background is now the same text and hearts as a still
  image. The screensaver's Python/GTK libraries are listed in the package file.
- 2026-11-04: clipboard history (Super+Ctrl+V) shows copied pictures as thumbnails instead of a
  "binary data" line and lists the newest copy first (it was sorted alphabetically: 1, 10, 100 ...).
- 2026-11-06: sync of 3-6 Nov changes. Waybar shows only the Wi-Fi icon (network name and
  signal on hover); a click on it opens nmtui in a floating foot window, a right-click
  nm-connection-editor. Sway starts the nm-applet tray icon that lists networks in range, and
  Super+Shift+N opens nmtui. `.xlsx` files open in LibreOffice Calc; `libreoffice-fresh` is
  listed in the package file.
- 2026-11-06 (later): the bar's own Wi-Fi module is gone (it duplicated the tray icon). The
  nm-applet tray icon is now the one Wi-Fi control (click lists networks in range); Super+Shift+N
  still opens nmtui.
- 2026-11-06 (later): Claude usage is back on the bar, as on Omarchy: `custom/claudebar` just left
  of the tray shows the session %, the tooltip the session/weekly/per-model limits, click opens
  claude.ai/settings/usage. It is `claudebar` 0.10.7 built from source into `~/.local`; `curl`
  added to the package file.
- 2026-11-10: memory recorded in the hardware doc (12 GB: 4 GB + 8 GB DDR4-2667, no swap), with how
  to tell a real out-of-memory crash from a capped build. Measured: no whole-laptop out-of-memory
  kill since the 2026-11-06 18:22 boot (3.5 days), against 3 in the 11 days before (Brave killed on
  28 Oct, 29 Oct and 6 Nov). Every boot in the journal (since 24 Oct) saw the same 12 GB, so the log
  does not show what changed.
- 2026-11-10 (later): kitty replaces foot as the default terminal, because foot cannot open links
  with a click. Super+Return, Super+Shift+T, the Super+Shift+N Wi-Fi window and Thunar's "Open
  Terminal Here" all use kitty, and Super+Return windows share one process to save memory.
  `kitty.conf` keeps foot's font, padding, opacity, Gruvbox colours and Super+V paste. A click
  opens a link; inside agent CLIs, Shift+click. foot stays installed as a fallback.
- 2026-11-12: the battery sat at 100% for days unnoticed: the 1 Nov udev rule was in the repo but
  never copied to `/etc`, so conservation mode stayed off. The bar now shows a red "no 60% cap"
  next to the battery whenever conservation mode is off (`custom/battery-cap`, checked every 60 s);
  the tooltip has the command that turns it on.
- 2026-11-12 (later): closing the lid now also switches the CPU to the `power-saver` profile, so
  agents left running with the lid shut use less power; opening it sets `balanced` again. The
  panel still turns off and the laptop keeps running as before.
- 2026-11-13: the bar's red "no 60% cap" warning is gone again; conservation mode is on and its
  udev rule is now installed in `/etc`, so the battery stops at about 60%.
- 2026-11-13 (later): right-click on the Arch logo at the left of the bar opens the power menu
  (Lock, Suspend, Reboot, Power off ...), the same menu as Super+Esc; left-click still opens the apps.
- 2026-11-13 (later): a leaf next to the battery icon on the bar shows that conservation mode (the
  60% cap) is on. The battery is now `custom/battery` (`waybar/battery.sh`), because the built-in
  module cannot read `charge_types`; icons, % and the yellow/red low-battery colours are unchanged.
- 2026-11-13 (later): the leaf is gone; the battery on the bar turns aqua instead while the 60% cap
  is on (the low-battery yellow and red still take over).
