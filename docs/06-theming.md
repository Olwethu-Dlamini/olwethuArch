# Theming

| Component | Palette |
|---|---|
| Sway, Waybar, swaylock | **Gruvbox** dark (`#282828` bg, `#fe8019` orange accent) |
| foot, mako, wofi | **Catppuccin Mocha** (`#1e1e2e` bg, `#89b4fa` blue accent) |

Shared everywhere: **JetBrainsMono Nerd Font** (icons in Waybar come from its
glyphs; `woff2-font-awesome` is a fallback), rounded 8-14px corners on popups,
no wallpaper image (solid `#1d2021`).

foot is 95% opaque; mako notifications are `#1e1e2eee` with a red border and no
timeout for urgent ones; swaylock is a minimal ring with transparent fill that
turns orange while verifying, red when wrong, green when cleared.

**Honest note:** the two palettes are a leftover of building piece by piece.
Unifying on one (likely Gruvbox, since the tiling core uses it) is a pending
cleanup - change `foot.ini`, `mako/config`, `wofi/style.css`.
