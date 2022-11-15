from colorama import init, Fore
from lib.nettools import get_ip

def MenuOption(option: str):
  print(Fore.LIGHTBLACK_EX + option)

def menu():
  MenuOption('[1] Get IP address of this computer')
  MenuOption('[0] Exit\n')

# Return data, ok?
def handler(option: str):
  exit = False

  if option == '1':
    ip = get_ip()
    return ip, exit

  if option == '0':
    exit = True
    return None, exit

  return None, exit

if __name__ == '__main__':
  init()
