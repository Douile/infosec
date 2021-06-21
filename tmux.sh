#!/bin/sh

DIR=$(readlink -f $(dirname "$0"))
COMMAND="ZDOTDIR=$DIR STARTUP=\"cd $DIR;. $DIR/hak.sh\" zsh"

tmux new-session -ds "hak" "$COMMAND"
tmux set-option -t "hak" default-command "$COMMAND"
tmux attach-session -t "hak"
