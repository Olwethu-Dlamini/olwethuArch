# Shell, editor and git

## bash (`home/.bashrc`)
No framework. Custom parts: 50k/100k history with duplicates erased and
`history -a` after every command (shared across terminals), `autocd`/`cdspell`,
`~/.local/bin` on PATH (that is where `omp` lives), `nvim` as
`EDITOR` and aliased over `vi`/`vim`, fzf key bindings (Ctrl-R/T, Alt-C) using
`fd` for file listing, the starship prompt if installed, and the .NET SDK
(`DOTNET_ROOT=~/.dotnet`, `~/.dotnet/tools` on PATH, telemetry opted out).

## kitty terminal (default, `kitty/kitty.conf`)
Started as `kitty --single-instance`, so every window shares one process. Same font, padding,
opacity and Gruvbox colours as foot. A click opens a link in the default browser; inside agent CLIs
(omp, Claude Code), which take over the mouse, hold Shift and click. Ctrl+Shift+E labels every link
with letters, like foot's Ctrl+Shift+O. Copy is Ctrl+Shift+C; paste is Ctrl+Shift+V or Super+V.

## foot terminal (fallback)
Copy is Ctrl+Shift+C; paste is Ctrl+Shift+V or Super+V (`[key-bindings]` in `foot.ini`). Super+V
only works inside the terminal (kitty or foot), and only for text; images paste with plain Ctrl+V in apps that take them.
Ctrl+Shift+O shows a letter next to every URL or path on screen; typing it opens that link with
`xdg-open` (`[url]` in `foot.ini`).

## Default apps (`home/.config/mimeapps.list`)
Thunderbird handles mail links; Kate opens plain text, Markdown, logs and PHP files;
LibreOffice Calc opens `.xlsx` spreadsheets.

## Neovim (`nvim/init.lua`)
Deliberately **plugin-free**. Relative line numbers, 4-space indent, smart-case
search, system clipboard via wl-clipboard, persistent undo, `<Space>` leader
(`w` save, `q` quit, `e` netrw), `Ctrl-hjkl` window moves, `J`/`K` move visual
selections, yank highlight.

## git (`home/.gitconfig`)
Rebase on pull, auto-setup upstream on push, histogram diffs with moved-block
colouring, rerere, verbose commit editor, short aliases (`co br ci st`), and
GitHub credentials through `gh`. Bitbucket uses the `store` helper with an
`x-bitbucket-api-token-auth` URL rewrite, so API tokens work as the password; the token file
itself (`~/.git-credentials`) is not mirrored. Identity lines are not mirrored.
