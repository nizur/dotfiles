# Sample .bashrc for SUSE Linux
# Copyright (c) SUSE Software Solutions Germany GmbH

# There are 3 different types of shells in bash: the login shell, normal shell
# and interactive shell. Login shells read ~/.profile and interactive shells
# read ~/.bashrc; in our setup, /etc/profile sources ~/.bashrc - thus all
# settings made here will also take effect in a login shell.
#
# NOTE: It is recommended to make language settings in ~/.profile rather than
# here, since multilingual X sessions would not work properly if LANG is over-
# ridden in every subshell.

trekscii 12 100

# Colors
source ~/.local/share/lscolors.sh

export EDITOR=nvim
export TERMINAL=kitty

test -s ~/.alias && . ~/.alias || true


# Aliases
alias bashrc="nvim ~/.bashrc"
alias config="/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME"
alias fda="fd -IH"
alias file="file -b"
alias ls="LC_COLLATE=C ls -h --group-directories-first --color=auto"
alias qtilcheck="python3 ~/.config/qtile/config.py && qtile cmd-obj -o cmd -f validate_config"
alias qtilog="bat -n .local/share/qtile/qtile.log"
alias tree="tree --dirsfirst"
alias vi=nvim
alias vimrc="nvim ~/.config/nvim/init.vim"

# FZF
export FZF_DEFAULT_COMMAND="fd -tf -H -E .git -E node_modules -E Games . $HOME"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND="fd -td . $HOME"
FZF_PREVIEW="--preview '([[ -f {} ]] && (bat --color=always --style=numbers --line-range=:500 {} || cat {})) || ([[ -d {} ]] || (tree -C {} | less)) || echo {} 2>/dev/null | head -200'"
export FZF_DEFAULT_OPTS="
--bind '?:toggle-preview'
--bind 'ctrl-a:select-all'
--bind 'ctrl-y:execute-silent(echo {+} | xclip -selection c)'
--border
--height=80%
--marker='>'
--multi
--preview-window=:hidden
--prompt='~ '
--reverse
--tabstop=4
--color=bg+:#302D41,bg:#1E1E2E,spinner:#F8BD96,hl:#F28FAD
--color=fg:#D9E0EE,header:#F28FAD,info:#DDB6F2,pointer:#F8BD96 
--color=marker:#F8BD96,fg+:#F2CDCD,prompt:#DDB6F2,hl+:#F28FAD
$FZF_PREVIEW
"

_fzf_compgen_path() {
	fd -tf -H -E .git -E node_modules . "$1"
}

_fzf_compgen_dir() {
	fd -td -H . "$1"
}

# History
export HISTTIMEFORMAT="%H:%M:%S "
export HISTCONTROL=ignoredups

# MAN
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export MANROFFOPT="-c"

# Tilix
if [ $TILIX_ID ] || [ $VTE_VERSION ]; then
	source /etc/profile.d/vte.sh
fi

. "$HOME/.cargo/env"
source ~/.config/fzf/completion.bash
source ~/.config/fzf/key-bindings.bash

# Starship
eval "$(starship init bash)"
. "$HOME/.cargo/env"
