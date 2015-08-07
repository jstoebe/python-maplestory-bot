#!/usr/bin/python

import pyautogui as auto
import time

auto.FAILSAFE = True

def clickForTime(duration):
  auto.mouseDown()
  time.sleep(duration)
  auto.mouseUp()

alt = auto.locateCenterOnScreen('alt.png')
print alt
left = auto.locateCenterOnScreen('left.png')
print left
right = auto.locateCenterOnScreen('right.png')
print right
end = auto.locateCenterOnScreen('end.png')
print end

while True:
  if not auto.locateCenterOnScreen('mana.png'):
    auto.moveTo(end)
    auto.click()

  auto.moveTo(left[0], left[1])
  clickForTime(0.1)
  time.sleep(1)
  auto.moveTo(alt[0], alt[1])
  auto.click()
  time.sleep(1)
  auto.moveTo(right[0], right[1])
  clickForTime(0.5)
  time.sleep(1)
  auto.moveTo(alt[0], alt[1])
  auto.click()
  time.sleep(1)
