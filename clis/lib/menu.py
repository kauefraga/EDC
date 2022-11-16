from colorama import init, Fore
from lib.customized_io import clear, anain, anaout
from lib.nettools import get_ip, get_response

def MenuOption(option: str):
  print(Fore.LIGHTBLACK_EX + option)

def menu():
  MenuOption('[1] Get IP address of this computer')
  MenuOption('[2] Make a request to some server (GET)')
  MenuOption('[0] Exit\n')

def handler(option: str):
  if option == '1':
    ip = get_ip()
    return ip

  if option == '2':
    clear()

    answer = anain('Type a valid URL: ')

    anaout('Making the request...')

    res = get_response(answer)

    return res

  return False

if __name__ == '__main__':
  init()
