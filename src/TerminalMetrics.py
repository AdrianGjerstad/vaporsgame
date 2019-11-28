#!/usr/bin/env python3

########################################
# IMPORTS                              #
########################################

#----------------STDLIB----------------#
import os

#----------------PARTY3----------------#
# No imports

#----------------INTLIB----------------#
# No imports

########################################
# CONSTANTS                            #
########################################

ROWS, COLS = os.popen('stty size', 'r').read().split()
ROWS = int(ROWS)
COLS = int(COLS)
