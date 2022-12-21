from lib.customized_io import clear, anain, anaout
from lib.nettools import get_response

def server_request():
  clear()

  answer = anain('Type a valid URL: ')

  anaout('Making the request...')

  res = get_response(answer)

  return res
