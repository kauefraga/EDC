from sys import exit
from colorama import Fore, init

def clear():
  CLEAR = '\x1b[2J' # Ansi code for clearing

  return print(CLEAR)

def anaout(message: str, color: str = Fore.GREEN):
  return print(color + '[Ana] ' + message)

def anain(message: str, color: str = Fore.GREEN):
  return input(color + '[Ana] ' + message)

def signal_handler(signal, frame):
  exit(0)

if __name__ == '__main__':
  init()
