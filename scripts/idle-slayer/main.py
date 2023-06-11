"""A script made with pyautogui to play Idle Slayer automatically."""
# screen 1366x768
import pyautogui
import keyboard
import time
from colorama import just_fix_windows_console, Fore, Style
from utils.datetime import get_time_and_datetime
from numpy.random import uniform


def click(x: int, y: int):
  pyautogui.mouseDown(
    x, y,
    button='left',
    duration=0.75
  )
  pyautogui.sleep(uniform(0.1, 0.3))
  pyautogui.mouseUp()

def screenshot(filename: str):
  pyautogui.screenshot(f'{filename}.png')

def main():
  initial_execution_time = time.time()
  initial_time, initial_datetime = get_time_and_datetime()

  print('[script] The program is running... -', initial_time)

  print('[script] Taking screenshot...')
  screenshot(initial_datetime) # hour.minute-day.month.year

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

  end_time, end_datetime = get_time_and_datetime()

  print('[script] Another screenshot...')
  screenshot(end_datetime)
  print('[script] Done! Your screenshots are available at .')

  print('[script] The program has finished -', end_time)
  print(Fore.LIGHTBLACK_EX + '---------------------------------------------' + Style.RESET_ALL)
  print(f'Time running: {Fore.GREEN}{round(time.time() - initial_execution_time, 3)}s')


if __name__ == '__main__':
  # Settings
  pyautogui.PAUSE = 0.1 # delay after all the commands
  just_fix_windows_console() # colorama

  main()
