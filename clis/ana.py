#!/usr/bin/env python3
#   /$$   /$$ /$$$$$$$$
#  | $$  /$$/| $$_____/
#  | $$ /$$/ | $$
#  | $$$$$/  | $$$$$
#  | $$  $$  | $$__/
#  | $$\  $$ | $$
#  | $$ \  $$| $$      Author: Kauê Fraga Rodrigues
#  |__/  \__/|__/      github.com/kauefraga/edc
# BE AWARE OF YOUR ACTIONS!

import signal, sys, os
from colorama import init, Fore, Style
from lib.customized_io import signal_handler, clear, anaout, anain
from lib.menu import menu, handler

def main():
  print(Fore.MAGENTA + '*****************************************')
  print(Fore.MAGENTA + '*    Relax! Ana will take control...    *')
  print(Fore.MAGENTA + '*****************************************\n')

  menu()

  answer = anain('Which tool do you want to run? ')

  data = handler(answer)

  anaout(data)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)

  init() # Colorama.init

  clear()
  main()
