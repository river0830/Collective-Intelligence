#coding:utf-8
#crc16 ccitt ccitt_1 for 3102 weight system

import Tkinter as tk
import ttk

import river

class Popmemu(object):
	def __init__(self, root, entry):
		self.root  = root
		self.entry = entry
		self.txt   = ''

	def oncopy(self):
		self.txt = self.entry.get()


class Crc16(object):
	pass

class Gui(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)

		master.title("River's crc16 calculator")
		self.create_widget(master)
		self.create_popmenu(master)

	def create_widget(self, master):
		self.show = tk.StringVar()
		self.entry = tk.Entry(master, textvariable = self.show)\
					.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
		#16 key
		for key in ('01234567', '89ABCDEF'):
			fram = self.create_frame()
			for c in key:
				self.create_buttons(fram, c, lambda x=self.show, c=c: x.set(x.get()+c))

		fram3 = self.create_frame()
		self.create_buttons(fram3, 'Blank',
							lambda x=self.show: x.set(x.get()+' '))
		self.create_buttons(fram3, 'Clear',
							lambda x=self.show: x.set(''))
		self.create_buttons(fram3, 'Backspace',
							lambda x=self.show: x.set(self.back(x.get())))
		self.create_buttons(fram3, '=',
							lambda : self.calc_crc)

	def create_buttons(self, fram, str, commands, widths=6):
		tk.Button(fram, text=str, width=widths, command=commands)\
						.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1)

	def create_frame(self, sides=tk.TOP):
		fram = tk.Frame(self.master)
		fram.pack(expand=tk.YES, side=sides, fill=tk.BOTH)
		return fram

	def back(self, str):
		if(len(str) > 0):
			return str[:-1]
		else:
			return str

	def create_popmenu(self, master):
		pass

	def calc_crc(self):
		pass

if __name__ == '__main__':
	Gui(tk.Tk()).mainloop()
