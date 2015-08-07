"""
NoKeyboardException is raised when we cannot find the On-Screen Keyboard.

Bot is a class that can do programmable actions. Initialize a bot and set
a series of actions for it to do.
"""

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
    if self.osk is not None:
      print "On-Screen Keyboard found!"
    else:
      raise NoKeyboardException("No On-Screen Keyboard found. "
                                "Try redo-ing your screenshot")
    self.time_created = time.time()
    self.hp_pots_used = 0
    self.mana_pots_used = 0

  def __str__(self):
    output = "\n" * 50
    output += "Time started: %s\n" % time.ctime(self.time_created)
    output +=  "Time now: %s\n" % time.ctime()
    output +=  "Time elapsed: %d\n" % (time.time() - self.time_created)
    output +=  "=" * 80
    output +=  "\nHealth potions used: %d\n" % self.hp_pots_used
    output +=  "Mana potions used: %d\n" % self.mana_pots_used
    return output

  def _moveTo(self, coord):
    pyautogui.moveTo(self.osk[0] + coord[0], self.osk[1] + coord[1])

  def click(self, key, duration):
    self._moveTo(key)
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()
    time.sleep(duration)

  def checkHealth(self, pot_key):
    if not pyautogui.locateOnScreen('data/hp.png'):
      self.click(pot_key, 0.25)
      self.hp_pots_used += 1

  def checkMana(self, pot_key):
    if not pyautogui.locateOnScreen('data/mana.png'):
      self.click(pot_key, 0.25)
      self.mana_pots_used += 1
