import pyautogui as auto
import sys
import time

"""
NoKeyboardException is raised when we cannot find the On-Screen Keyboard.

Bot is a class that can do programmable actions. Initialize a bot and set
a series of actions for it to do.
"""

auto.FAILSAFE = True

class NoKeyboardException(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class Bot():
  def __init__(self):
    self.osk = auto.locateOnScreen('data/osk.png')
    if self.osk is not None:
      print "On-Screen Keyboard found!"
    else:
      raise NoKeyboardException("No On-Screen Keyboard found. "
                                "Try redo-ing your screenshot")
    self.hp_pots_used = 0;

  def _moveTo(self, coord):
    auto.moveTo(self.osk[0] + coord[0], self.osk[1] + coord[1])

  def click(self, key, duration):
    self._moveTo(key)
    auto.mouseDown()
    time.sleep(duration)
    auto.mouseUp()
    time.sleep(duration)

  def checkHealth(self, pot_key):
    if not auto.locateOnScreen('data/hp.png'):
      self.hp_pots_used += 1
      print "Health potions used: " + str(self.hp_pots_used)
      self.click(pot_key, 0.25)
