Python bot for MapleStory
========

Uses PyAutoGUI to spoof player actions. Since PyAutoGUI cannot send keyboard
events directly to MapleStory, we use the On-Screen Keyboard built into
Windows and set the mouse to click on the appropriate action keys.

We check for a full health/mana bar and if we do not see it, then we use a potion.

Copyright &copy; Alvin Lin 2015
