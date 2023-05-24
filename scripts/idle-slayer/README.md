# Idle Slayer Script

> I made this script to play to Idle Slayer automatically because the game is very repetitive about shooting, jumping, collecting coins, etc.

### Features

- Jump and shoot! Get more coins and kills by using the bow.
- Run it, leave it alone and when you back to it, know exactly for how long it runs.
- Currently it's sprinting, jumping, shooting, verifying if there's a portal to use (then using if there is).
- Obtain the offline rewards if there are.

## 🎲 Prerequisites

- Have [Python](https://www.python.org) installed.
- Install the dependencies needed.
- Change the code magic numbers for your screen size (i build it with a laptop, so 1366x768).

## ⬇️ How to download and use it in your game

1. Clone the repository
2. Install the dependencies
3. Run it

```bash
git clone https://github.com/kauefraga/edc.git

pip install -r requirements.txt

python scripts/idle-slayer/main.py # if you have python2, you should run py or python3 instead
```

You are welcome to open issues and pull requests!

## 🛠 Dependencies

The following packages have been used to build the script:

- [Pyautogui](https://pyautogui.readthedocs.io/en/latest/install.html) - PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications.
- [Keyboard](https://pypi.org/project/keyboard) - Take full control of your keyboard with this small Python library.
- [Numpy](https://numpy.org/install) - We are using to get random numbers.
- [Datetime](https://docs.python.org/3/library/datetime.html) - The datetime module supplies classes for manipulating dates and times.

## 📜 Coming soon

- Give it some colors
- Log important information, such as actual coins, coins per second, kill points, etc.
- If some key is pressed, open the ascension menu and then ascend (you can also check the vassals menu)

---

<div align="center">
  <img alt="Built with love" src="https://forthebadge.com/images/badges/built-with-love.svg">
  <img alt="Powered by black magic" src="https://forthebadge.com/images/badges/powered-by-black-magic.svg">
</div>
