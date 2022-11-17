#!/bin/bash
#   /$$   /$$ /$$$$$$$$
#  | $$  /$$/| $$_____/
#  | $$ /$$/ | $$
#  | $$$$$/  | $$$$$
#  | $$  $$  | $$__/
#  | $$\  $$ | $$
#  | $$ \  $$| $$      Author: Kauê Fraga Rodrigues
#  |__/  \__/|__/      github.com/kauefraga/my-dotfiles

green='\033[0;32m'
nocolor='\033[0m'

Print() {
  echo -e "${green}[Ana] $@ ${nocolor}"
}

clear

echo '*****************************************'
echo '*    Relax! Ana will take control...    *'
echo '*****************************************'

# Install fnm (node version manager)
curl -fsSL https://fnm.vercel.app/install | bash

Print 'configuring nodejs...'
eval "$(fnm env --use-on-cd)"
fnm install --lts
fnm use lts-latest
Print 'done'


curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
