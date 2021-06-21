#!/bin/sh
. "$HOME/.zshrc"
if [ -n "$STARTUP" ]; then
  eval "$STARTUP"
else
  echo -e "\e[31mNo startup \"$STARTUP\"\e[0m"
fi
