#coding=utf8

"""
my module for python
diligent
"""

import sys
import ctypes

def HideBlankWindow():
	if sys.platform[:3] == 'win':
		whnd = ctypes.windll.kernel32.GetConsoleWindow()
		if whnd != 0:
			ctypes.windll.user32.ShowWindow(whnd, 0)
			ctypes.windll.kernel32.CloseHandle(whnd)


if __name__ == '__main__':
	print("{0}".format("river's python dll"))
	raw_input()
	

