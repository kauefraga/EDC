"""A script made with pyautogui to play Idle Slayer automatically."""
import pyautogui
import keyboard
from numpy.random import uniform

# Default delay
pyautogui.PAUSE = 0.1

# Alert people that the program is running
print('The program is running...')


def click(x: int, y: int):
  pyautogui.mouseDown(
    x, y,
    button='left',
    duration=0.75
  )
  pyautogui.sleep(uniform(0.1, 0.3))
  pyautogui.mouseUp()

while keyboard.is_pressed('q') != True:
  # Sprint
  if pyautogui.pixel(100, 630)[2] != 52:
    # print(pyautogui.pixel(100,  630))

    pyautogui.click(100, 630, button='left')

  # Jump and shoot with bow
  click(650, 380)


# Alert that the program finished
print('The program has finished')

"""
1. if the portal is available, use it (x1240, y90 rgb(40, 1, 46))
2. if some key is pressed, open the ascension menu and then:
  2.1. check the "vassalos" menu
  2.2. ascend
3. log the main information
"""
