Python bot for MapleStory
========

Uses PyAutoGUI to spoof player actions. Since PyAutoGUI cannot send keyboard
events directly to MapleStory, we use the On-Screen Keyboard built into
Windows and set the mouse to click on the appropriate action keys.

Bot.py is the main botting class that handles clicks and actions. Pass key
coordinates to its methods (defined in Keys.py) to have it do an action.

Zero.py is an example program that shows the implementation of Bot.py

To use:
   Install <code>setuptools</code>
   Install <code>pyautogui</code>
   Open the On-Screen Keyboard and take a screenshot of it. Crop out the
        border so that you only have the keys and icon (copy the existing
        osk.png as a template).
   Run MapleStory.
   Run your bot and switch to MapleStory.

Copyright &copy; Alvin Lin 2015
