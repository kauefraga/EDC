"""A script made with pyautogui to play Idle Slayer automatically."""
# screen 1366x768
import pyautogui
import keyboard
import time
from colorama import just_fix_windows_console, Fore, Style
from utils.datetime import now
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
  print(f'[script] The program is running... - {now()}')

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

  print(f'[script] The program has finished - {now()}')
  print(Fore.LIGHTBLACK_EX + '---------------------------------------------' + Style.RESET_ALL)


if __name__ == '__main__':
  # Settings
  pyautogui.PAUSE = 0.1 # delay after all the commands
  just_fix_windows_console() # colorama

  initial_time = time.time()

  main()

  print(f'Time running: {Fore.GREEN}{round(time.time() - initial_time, 3)}s')
