"""A script made with pyautogui to play Idle Slayer automatically."""
# screen 1366x768
import pyautogui
import keyboard
from datetime import datetime
from numpy.random import uniform

def click(x: int, y: int):
  pyautogui.mouseDown(
    x, y,
    button='left',
    duration=0.75
  )
  pyautogui.sleep(uniform(0.1, 0.3))
  pyautogui.mouseUp()

def main():
  # Alert people that the program is running
  print(f'[script] The program is running... - {datetime.now().time()}')

  while keyboard.is_pressed('q') != True:
    # Get offline rewards
    if pyautogui.pixel(710, 15)[2] == 0:
      pyautogui.click(710, 15, button='left')
      pyautogui.sleep(uniform(0.1, 0.3))

    # Check if the portal is available
    if pyautogui.pixel(1240, 90)[2] == 153:
      # click in the portal icon
      pyautogui.click(1240, 90)
      pyautogui.sleep(uniform(0.1, 0.3))
      # press "yes"
      pyautogui.click(580, 590)
      pyautogui.sleep(uniform(0.5, 1))

    # Sprint
    if pyautogui.pixel(100, 630)[2] == 155:
      pyautogui.click(100, 630, button='left')

    # Jump and shoot with bow
    click(650, 380)

  # Alert that the program finished
  print(f'[script] The program has finished - {datetime.now().time()}')

if __name__ == '__main__':
  # Settings
  pyautogui.PAUSE = 0.1 # delay after all the commands

  main()

"""
1. if some key is pressed, open the ascension menu and then:
  1.1. check the "vassalos" menu
  1.2. ascend
2. log the main information
"""
