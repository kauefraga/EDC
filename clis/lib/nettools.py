import requests, validators

def get_ip():
  ip = requests.get('https://api.ipify.org').text

  return 'Ip: {}'.format(ip)

def get_response(url: str):
  if not validators.url(url):
    return 'Url not valid'

  res = requests.get(url).text

  return res
