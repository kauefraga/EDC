#!/bin/bash
#   /$$   /$$ /$$$$$$$$
#  | $$  /$$/| $$_____/
#  | $$ /$$/ | $$
#  | $$$$$/  | $$$$$
#  | $$  $$  | $$__/
#  | $$\  $$ | $$
#  | $$ \  $$| $$      Author: Kauê Fraga Rodrigues
#  |__/  \__/|__/      github.com/kauefraga/edc

# => ubuntu

# colors
nocolor='\033[0m'         # Color reset
black='\033[0;30m'        # Black
red='\033[0;31m'          # Red
green='\033[0;32m'        # Green
yellow='\033[0;33m'       # Yellow
blue='\033[0;34m'         # Blue
purple='\033[0;35m'       # Purple
cyan='\033[0;36m'         # Cyan
white='\033[0;37m'        # White

Print() {
  echo -e "${green}[Ana] $@ ${nocolor}"
}

clear

echo -e $purple'******************************************'
echo -e $purple'*                                        *'
echo -e $purple'*    /$$   /$$ /$$$$$$$$                 *'
echo -e $purple'*   | $$  /$$/| $$_____/                 *'
echo -e $purple'*   | $$ /$$/ | $$                       *'
echo -e $purple'*   | $$$$$/  | $$$$$                    *'
echo -e $purple'*   | $$  $$  | $$__/                    *'
echo -e $purple'*   | $$\  $$ | $$                       *'
echo -e $purple'*   | $$ \  $$| $$  gh:kauefraga/edc     *'
echo -e $purple'*   |__/  \__/|__/  Kauê Fraga Rodrigues *'
echo -e $purple'*                                        *'
echo -e $purple'******************************************'

# Install fnm (node version manager)
curl -fsSL https://fnm.vercel.app/install | bash

Print 'configuring nodejs...'
eval "$(fnm env --use-on-cd)"
fnm install --lts
fnm use lts-latest
Print 'done'

Print 'installing rustup...'
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
Print 'done'

Print 'installing zsh and oh my zsh...'
apt install zsh -y > /dev/null
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
Print 'done'

Print 'configuring zsh...'
chsh --shell "$(which zsh)"
Print $yellow'=> plugins:'
Print $yellow'open your ~/.zshrc'
Print $yellow'plugins=(git fnm python docker docker-compose rust zsh-syntax-highlighting zsh-autosuggestions)'

Print $yellow'=> themes:'
Print $yellow'avit, awesomepanda, garyblessington, gozilla, oxide, pi, elessar'
Print 'done'
