import pyautogui
import keyboard
from numpy.random import uniform

# Default delay
pyautogui.PAUSE = 1

# Alert people that the program is running
print('The program is running...')


def click(x: int, y: int):
  pyautogui.click(x, y, button='left')
  pyautogui.sleep(uniform(0.1, 0.3))

while keyboard.is_pressed('q') != True:
  if pyautogui.pixel(100, 630)[2] != 50:
    click(100, 630)
    # x 100 y 630 rgb(7, 25, 50)

  click(650, 380)


# Alert that the program finished
print('The program has finished')
