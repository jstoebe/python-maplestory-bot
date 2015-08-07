#!/usr/bin/python

import pyautogui as auto
import sys
import time

"""
Author: Alvin Lin (alvin.lin@stuypulse.com)
Basic botting program for Zero. Works with my keybindings only.

Premise:
A - Giga Crash
S - Flash Cut
D - Rising Slash
Del - Shadow Rain
End - Rhinne's Protection

Ctrl - Health pots

Run while in Beta form standing on a platform with a wall to your right.
This will bump the character against the wall and spam abilties in all
directions. This bot is not smart responsive except for potting when your
HP is low, so make sure you have thousands of health potions. If you get
moved out of position, the bot will continue doing the same thing, so you
need to find a place to stand where mobs do not or can not attack you.
"""

auto.FAILSAFE = True

# Coordinates of the keys on osk.png
a = [125, 100]
s = [170, 100]
d = [210, 100]
ctrl = [30, 170]
delete = [650, 70]
end = [710, 70]
right = [615, 170]
left = [525, 170]

def clickForTime(duration):
  auto.mouseDown()
  time.sleep(duration)
  auto.mouseUp()
  time.sleep(duration)

def moveTo(osk, coord):
  auto.moveTo(osk[0] + coord[0], osk[1] + coord[1])

def checkHealth():
  # Check for low hp and use a pot if low.
  if not auto.locateOnScreen('hp.png'):
    hp_pots_used += 1
    print "Potions used: " + str(hp_pots_used)
    moveTo(osk, ctrl)
    auto.click()

def main():
  osk = auto.locateOnScreen('data/osk.png')
  if osk is not None:
    print "On-Screen Keyboard found!"
  else:
    print "No On-Screen Keyboard found, it should be visible on your screen!"
    print "Try redoing your screenshot!"
    sys.exit(0)

  hp_pots_used = 0
  iterations_run = 0

  while True:
    checkHealth()

    moveTo(osk, left)
    clickForTime(0.1)
    moveTo(osk, d)
    clickForTime(0.25)
    clickForTime(0.25)
    moveTo(osk, s)
    clickForTime(0.25)
    clickForTime(0.25)
    if iterations_run % 2 == 1:
      moveTo(osk, a)
      clickForTime(0.25)
      clickForTime(0.25)
      clickForTime(0.25)

    checkHealth()
    moveTo(osk, right)
    clickForTime(1.2)
    moveTo(osk, d)
    clickForTime(0.25)
    clickForTime(0.25)
    moveTo(osk, s)
    clickForTime(0.25)
    clickForTime(0.25)
    if iterations_run % 2 == 0:
      moveTo(osk, a)
      clickForTime(0.25)
      clickForTime(0.25)
      clickForTime(0.25)

    # Clear mobs every 25 iterations with ultimate ability
    if iterations_run % 25 == 0:
      moveTo(osk, delete)
      clickForTime(0.25)

    # Buff self every 10 iterations
    if iterations_run % 10 == 0:
      moveTo(osk, end)
      clickForTime(0.25)

  iterations_run += 1

if __name__ == "__main__":
  main()
