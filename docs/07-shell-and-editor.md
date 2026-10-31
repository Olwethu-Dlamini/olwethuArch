# Shell, editor and git

## bash (`home/.bashrc`)
No framework. Custom parts: 50k/100k history with duplicates erased and
`history -a` after every command (shared across terminals), `autocd`/`cdspell`,
`~/.local/bin` on PATH (that is where `omp` lives), `nvim` as
`EDITOR` and aliased over `vi`/`vim`, fzf key bindings (Ctrl-R/T, Alt-C) using
`fd` for file listing, the starship prompt if installed, and the .NET SDK
(`DOTNET_ROOT=~/.dotnet`, `~/.dotnet/tools` on PATH, telemetry opted out).

## foot terminal
Copy is Ctrl+Shift+C; paste is Ctrl+Shift+V or Super+V (`[key-bindings]` in `foot.ini`). Super+V
only works inside foot, and only for text; images paste with plain Ctrl+V in apps that take them.

## Neovim (`nvim/init.lua`)
Deliberately **plugin-free**. Relative line numbers, 4-space indent, smart-case
search, system clipboard via wl-clipboard, persistent undo, `<Space>` leader
(`w` save, `q` quit, `e` netrw), `Ctrl-hjkl` window moves, `J`/`K` move visual
selections, yank highlight.

## git (`home/.gitconfig`)
Rebase on pull, auto-setup upstream on push, histogram diffs with moved-block
colouring, rerere, verbose commit editor, short aliases (`co br ci st`), and
GitHub credentials through `gh`. Identity lines are not mirrored.
