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

  # Read the key from thekey.key
  with open("thekey.key", "rb") as key:
    secret_key = key.read()

  # Run through the files
  for file in files:
    # Read all the files
    with open(file, "rb") as thefile:
      contents = thefile.read()

    # Decrypt the contents
    contents_decrypted = Fernet(secret_key).decrypt(contents)

    # Write the decrypted contents
    with open(file, "wb") as thefile:
      thefile.write(contents_decrypted)

if __name__ == "__main__":
  main()
