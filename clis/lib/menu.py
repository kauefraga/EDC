from colorama import init, Fore
from lib.nettools import get_local_ip, get_public_ip
from interfaces.server_request import server_request

def MenuOption(option: str):
  print(Fore.LIGHTBLACK_EX + option)

def menu():
  MenuOption('[1] Get the local IP address of this computer')
  MenuOption('[2] Get the public IP address of this computer')
  MenuOption('[3] Make a request to some server (GET)')
  MenuOption('[4] Fast Restful API')
  MenuOption('[0] Exit\n')

options = {
  '0': exit,
  '1': get_local_ip,
  '2': get_public_ip,
  '3': server_request,
  '4': lambda : 'Try out >>https://npm.im/quicky-server<<',
}

def handler(option: str):
  if option:
    return options[option]()

if __name__ == '__main__':
  init()
