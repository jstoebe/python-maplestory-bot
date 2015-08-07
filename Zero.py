#!/usr/bin/python

import sys

from Bot import Bot
from Keys import Keys

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

def main():
  bot = Bot()    
  iterations_run = 0

  while True:
    bot.checkHealth(Keys.CTRL)
    bot.click(Keys.LEFT, 0.1)
    bot.click(Keys.D, 0.25)
    bot.click(Keys.D, 0.25)
    bot.click(Keys.S, 0.25)
    bot.click(Keys.S, 0.25)
    if iterations_run % 2 == 1:
      bot.click(Keys.A, 0.25)
      bot.click(Keys.A, 0.25)
      bot.click(Keys.A, 0.25)

    bot.checkHealth(Keys.CTRL)
    bot.click(Keys.RIGHT, 0.5)
    bot.click(Keys.D, 0.25)
    bot.click(Keys.D, 0.25)
    bot.click(Keys.S, 0.25)
    bot.click(Keys.S, 0.25)
    if iterations_run % 2 == 0:
      bot.click(Keys.A, 0.25)
      bot.click(Keys.A, 0.25)
      bot.click(Keys.A, 0.25)

    # Clear mobs every 25 iterations with ultimate ability
    if iterations_run % 25 == 0:
      bot.click(Keys.DEL, 0.25)

    # Buff self every 10 iterations
    if iterations_run % 10 == 0:
      bot.click(Keys.END, 0.25)

  iterations_run += 1

if __name__ == "__main__":
  main()
