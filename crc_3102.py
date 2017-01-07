#coding:utf-8
#crc16 ccitt ccitt_1 for 3102 weight system

import Tkinter as tk
import ttk

import river

class popmemu(object):
	def __init__(self, root, entry):
		self.root  = root
		self.entry = entry
		self.txt   = ''

	def oncopy(self):
		self.txt = self.entry.get()


class crc16(object):
	pass

class gui(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)

		self.master = master
		self.create_widget()
		self.create_popmenu()

	def create_widget(self):
		self.