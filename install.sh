#!/usr/bin/env bash
# Copy user-level configs from this repo into $HOME, backing up anything that
# differs. System files under etc/ are NOT touched: copy those with sudo by hand.
set -euo pipefail
repo=$(cd "$(dirname "$0")" && pwd)
stamp=$(date +%F-%H%M%S)

cd "$repo/home"
find . -type f | while read -r f; do
    dest="$HOME/${f#./}"
    mkdir -p "$(dirname "$dest")"
    if [ -e "$dest" ] && ! cmp -s "$f" "$dest"; then
        cp -p "$dest" "$dest.bak-$stamp"
        echo "backed up $dest"
    fi
    cp "$f" "$dest"
    echo "installed $dest"
done

# NTFS does not keep the executable bit, so restore it
chmod +x "$HOME/.config/sway/launcher.sh" "$HOME/.config/sway/system-menu.sh" "$HOME/.config/waybar/toggle.sh"

systemctl --user daemon-reload
systemctl --user enable waybar.service
echo "Done. Reload Sway with SUPER+Shift+C."
