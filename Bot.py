"""
NoKeyboardException is raised when we cannot find the On-Screen Keyboard.

Bot is a class that can do programmable actions. Initialize a bot and set
a series of actions for it to do.
"""

import math
import pyautogui
import sys
import time

pyautogui.FAILSAFE = True

class NoKeyboardException(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class Bot():
  def __init__(self):
    self.osk = pyautogui.locateOnScreen('data/osk.png')
    if self.osk is None:
      raise NoKeyboardException("No On-Screen Keyboard found. "
                                "Try redo-ing your screenshot")
    self.time_created = time.time()
    self.hp_pots_used = 0
    self.mana_pots_used = 0

  """
  Returns debug text showing time running as well the amount of health/mana
  potions used and other statistical data.
  """
  def getDebugText(self):
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
    output += "Health potions per minute: %d\n" % ((
        timeDifference % 60) / self.hp_pots_used)
    output += "Mana potions used: %d\n" % self.mana_pots_used
    output += "Mana potions per minute: %d\n" % ((
        timeDifference % 60) / self.mana_pots_used)
    return output

  """
  Helper method that moves the mouse to a specified coordinate.
  """
  def _moveTo(self, coord):
    pyautogui.moveTo(self.osk[0] + coord[0], self.osk[1] + coord[1])

  """
  Given a key to click and a duration to click it for, this method will
  click the key for the given duration.
  """
  def click(self, key, duration):
    self._moveTo(key)
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()
    time.sleep(0.25)

  """
  Given a key that is bound to a health potion, this method will check for a
  depleted health bar and use potions until it can no longer see a depleted
  health bar.
  """
  def checkHealth(self, pot_key):
    while not pyautogui.locateOnScreen('data/hp.png'):
      self.click(pot_key, 0.25)
      self.hp_pots_used += 1

  """
  Given a key that is bound to a mana potion, this method will check for a
  depleted mana bar and use potions until it can no longer see a depleted
  mana bar.
  """
  def checkMana(self, pot_key):
    while not pyautogui.locateOnScreen('data/mana.png'):
      self.click(pot_key, 0.25)
      self.mana_pots_used += 1
