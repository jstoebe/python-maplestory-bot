"""
NoKeyboardException is raised when we cannot find the On-Screen Keyboard.

Bot is a class that can do programmable actions. Initialize a bot and set
a series of actions for it to do.
"""

import pyautogui as auto
import sys
import time

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
    self.time_created = time.time()
    self.hp_pots_used = 0
    self.mana_pots_used = 0

  def __str__(self):
    for i in range(0, 50):
      print "\n"
    print "Time started: %s" % time.ctime(self.time_created)
    print "Time now: %s" % time.ctime()
    print "Time elapsed: %d" % (time.time() - self.time_created)
    print "=" * 80
    print "Health potions used: %d" % self.hp_pots_used
    print "Mana potions used: %d" % self.mana_pots_used

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
      self.click(pot_key, 0.25)
      self.hp_pots_used += 1

  def checkMana(self, pot_key):
    if not auto.locateOnScreen('data/mana.png'):
      self.click(pot_key, 0.25)
      self.mana_pots_used += 1
