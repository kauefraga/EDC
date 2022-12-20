import requests, validators, socket

def get_public_ip():
  publicIp = requests.get('https://api.ipify.org').text

  return 'Public IP: {}'.format(publicIp)

def get_local_ip():
  localIp = socket.gethostbyname(socket.gethostname())

  return 'Local IP: {}'.format(localIp)

def get_response(url: str):
  if not validators.url(url):
    return 'Url not valid'

  res = requests.get(url).text

  return res
