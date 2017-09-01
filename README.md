# Python bot for MapleStory

Uses PyAutoGUI to spoof player actions. Since PyAutoGUI cannot send keyboard
events directly to MapleStory, we use the On-Screen Keyboard built into
Windows and set the mouse to click on the appropriate action keys.

Bot.py is the main botting class that handles clicks and actions. Pass key
coordinates to its methods (defined in Keys.py) to have it do an action.
Remember to call checkHealth() and checkMana() frequently. It never hurts to
have an extra call.

Zero.py is an example program that shows the implementation of Bot.py

# Setup
## Windows
You will need to install Python 2 on Windows as well as pyautogui.
The easiest way is probably by installing `pip` and using pip to
install pyautogui.

## Linux setup for development:
```
sudo apt-get install python-pip python-dev python-tk python-xlib
sudo pip install pillow pyautogui
```

# To use:
  - Open the On-Screen Keyboard and take a screenshot of it. Crop out the
  border so that you only have the keys and icon (copy the existing
  `osk.png` as a template).
  - Import Bot.py and write your own bot action sequence using it.
  - Run MapleStory.
  - Run your bot and switch to MapleStory.

## Creator
  - Alvin Lin (omgimanerd)
### Contributor
  - Jonathan Stoebe (jstoebe)
