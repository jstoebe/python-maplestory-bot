#!/usr/bin/python
"""
This file contains the Bot class, which is initialize and used to complete
sets of actions.

NoKeyboardException is raised when we cannot find the On-Screen Keyboard.

Author: Alvin Lin (alvin.lin.dev@gmail.com)
"""

import math
import pyautogui
import sys
import time

pyautogui.FAILSAFE = True

class NoKeyboardException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "No On-Screen Keyboard found. Try redo-ing your screenshot."

class Bot():
    def __init__(self):
        self.osk = pyautogui.locateOnScreen('data/osk.png')
        if self.osk is None:
            raise NoKeyboardException()
        self.time_created = time.time()
        self.hp_pots_used = 0
        self.mana_pots_used = 0

    def getDebugText(self):
        """
        Returns debug text showing time running as well the amount of
        health/mana potions used and other statistical data.
        """
        timeDifference = time.time() - self.time_created
        hours = math.floor(timeDifference / 3600)
        minutes = math.floor((timeDifference % 3600) / 60)
        seconds = math.floor(timeDifference % 3600 % 60)

        output = "\n" * 50
        output += "Time started: %s\n" % time.ctime(self.time_created)
        output += "Time now: %s\n" % time.ctime()
        output += "Time elapsed: %02d:%02d:%02d\n" % (hours, minutes, seconds)
        output += ("=" * 80) + "\n"
        output += "Health potions used: %d\n" % self.hp_pots_used
        output += "Health potions per hour: %d\n" % (self.hp_pots_used / (
                timeDifference / 3600))
        output += "Mana potions used: %d\n" % self.mana_pots_used
        output += "Mana potions per hour: %d\n" % (self.mana_pots_used / (
                timeDifference / 3600))
        return output

    def _moveTo(self, coord):
        """
        Helper method that moves the mouse to a specified coordinate.
        """
        pyautogui.moveTo(self.osk[0] + coord[0], self.osk[1] + coord[1])

    def click(self, key, duration):
        """
        Given a key to click and a duration to click it for, this method will
        click the key for the given duration.
        """
        self._moveTo(key)
        pyautogui.mouseDown()
        time.sleep(duration)
        pyautogui.mouseUp()
        time.sleep(0.25)

    def checkHealth(self, pot_key):
        """
        Given a key that is bound to a health potion, this method will check
        for a depleted health bar and use potions until it can no longer see a
        depleted health bar.
        """
        while not pyautogui.locateOnScreen('data/hp.png'):
            self.click(pot_key, 0.25)
            self.hp_pots_used += 1

    def checkMana(self, pot_key):
        """
        Given a key that is bound to a mana potion, this method will check for a
        depleted mana bar and use potions until it can no longer see a depleted
        mana bar.
        """
        while not pyautogui.locateOnScreen('data/mana.png'):
            self.click(pot_key, 0.25)
            self.mana_pots_used += 1
