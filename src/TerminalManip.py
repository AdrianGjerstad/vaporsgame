#!/usr/bin/env python3

########################################
# IMPORTS                              #
########################################

#----------------STDLIB----------------#
import sys, tty, termios

#----------------PARTY3----------------#
# No imports

#----------------INTLIB----------------#
# No imports

########################################
# METHODS                              #
########################################

def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch
