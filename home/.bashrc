#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# --- history: big, no duplicates, shared between terminals ---
HISTSIZE=50000
HISTFILESIZE=100000
HISTCONTROL=ignoreboth:erasedups
shopt -s histappend checkwinsize cdspell autocd
PROMPT_COMMAND="history -a${PROMPT_COMMAND:+; $PROMPT_COMMAND}"

# --- tab completion ---
[[ -r /usr/share/bash-completion/bash_completion ]] && . /usr/share/bash-completion/bash_completion

# --- user-installed programs (omp) ---
case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) export PATH="$HOME/.local/bin:$PATH" ;; esac

# --- aliases / editor ---
export EDITOR=nvim VISUAL=nvim
alias vi=nvim vim=nvim
alias ll='ls -lah'
alias ..='cd ..'

# --- fuzzy finder: Ctrl-R history, Ctrl-T files, Alt-C directories ---
if command -v fzf >/dev/null; then
    eval "$(fzf --bash)"
    command -v fd >/dev/null && export FZF_DEFAULT_COMMAND='fd --type f --hidden --exclude .git'
fi

# --- prompt (only if starship is installed) ---
command -v starship >/dev/null && eval "$(starship init bash)"

# .NET SDK (restored from the old oll home, 2026-10-26)
export DOTNET_ROOT="$HOME/.dotnet"
export PATH="$PATH:$HOME/.dotnet/tools"
export DOTNET_CLI_TELEMETRY_OPTOUT=1
