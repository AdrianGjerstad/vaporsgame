#!/usr/bin/env python3

########################################
# IMPORTS                              #
########################################

#----------------STDLIB----------------#
import sys
import time

#----------------PARTY3----------------#
# No imports

#----------------INTLIB----------------#
import TerminalMetrics as tm
import TerminalManip as term

########################################
# MAIN METHOD                          #
########################################

def main():
  1/0

########################################
# GLOBALEXEC                           #
########################################

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    # Clear screen
    # - Set cursor to top left
    # - Clear from cursor to end of screen
    sys.stderr.write('\033[H\033[J')

    # Print centering spaces
    sys.stderr.write(' '*(int((tm.COLS - 21)/2)))

    sys.stderr.write('\033[31mAn error has occured:\n')
    
    data = type(e).__name__
    if str(e) != '':
      if str(e).startswith('(') and str(e).startswith(')'):
        data += ': ' + ' '.join(str(e)[1:-1].strip().split(', '))
      else:
        data += ': ' + str(e)
      
    sys.stderr.write(' '*(int((tm.COLS - len(data))/2)))
    sys.stderr.write(data + '\n\n')    
    
    # TODO open TCP socket to send error data to developer server

    sys.stderr.write(' '*(int((tm.COLS - 50)/2)))

    sys.stderr.write(
      '\033[34mⓘ The full report has been sent to the developers.\033[0m\n\n'
    )

    sys.stderr.write('\033[%i;HPress any key to exit' % (tm.ROWS))
    sys.stderr.write('\033[%i;%iH' % (tm.ROWS, tm.COLS))
    sys.stderr.flush()

    term.getch()

    sys.stderr.write('\033[H\033[J')
