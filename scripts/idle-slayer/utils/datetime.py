from datetime import datetime

def now():
  """A function that formats the datetime native module and returns time"""
  now = datetime.now().time()

  return f'{now.hour}:{now.minute}:{now.second}'
