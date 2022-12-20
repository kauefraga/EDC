from colorama import init, Fore
from lib.customized_io import clear, anain, anaout
from lib.nettools import get_local_ip, get_public_ip, get_response

def MenuOption(option: str):
  print(Fore.LIGHTBLACK_EX + option)

def menu():
  MenuOption('[1] Get the local IP address of this computer')
  MenuOption('[2] Get the public IP address of this computer')
  MenuOption('[3] Make a request to some server (GET)')
  MenuOption('[0] Exit\n')

def handler(option: str):
  if option == '1':
    localIp = get_local_ip()
    return localIp

  if option == '2':
    publicIp = get_public_ip()
    return publicIp

  if option == '3':
    clear()

    answer = anain('Type a valid URL: ')

    anaout('Making the request...')

    res = get_response(answer)

    return res

  return False

if __name__ == '__main__':
  init()
