#coding:utf-8
#crc16 ccitt ccitt_1 for 3102 weight system

import Tkinter as tk
import ttk
import binascii

import river

class Popmemu(object):
	def __init__(self, root, show):
		self.root  = root
		self.show = show
		self.text   = ''

	def on_copy(self):
		self.text = self.show.get()
		if len(self.text) > 0:
			self.root.clipboard_append(self.text)

	def on_paste(self):
		self.text = self.root.clipboard_get()
		if len(self.text) > 0:
			self.show.set(self.text)

	def on_cute(self):
		self.on_copy()
		self.show.set('')


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
		self.entry = ttk.Entry(master, textvariable = self.show)
		self.entry.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)

		#16 key
		for key in ('01234567', '89ABCDEF'):
			fram = self.create_frame()
			for c in key:
				self.create_buttons(fram, c, lambda x=self.show, c=c: x.set(x.get()+c))

		fram3 = self.create_frame()
		self.create_buttons(fram3, 'Blank',
							lambda x=self.show : self.insert_blank(x.get()))
		self.create_buttons(fram3, 'Clear',
							lambda x=self.show: x.set(''))
		self.create_buttons(fram3, 'Backspace',
							lambda x=self.show: x.set(self.back(x.get())))
		self.create_buttons(fram3, '=',
							lambda x=self.show: self.calc_crc(x.get()))

	def create_buttons(self, fram, str, commands, widths=6):
		b = ttk.Button(fram, text=str, width=widths, command=commands)
		b.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1)

	def create_frame(self, sides=tk.TOP):
		fram = ttk.Frame(self.master)
		fram.pack(expand=tk.YES, side=sides, fill=tk.BOTH)
		return fram

	def back(self, str):
		if(len(str) > 0):
			return str[:-1]
		else:
			return str

	def create_popmenu(self, master):
		popmenu = Popmemu(master, self.show)

		self.menu = tk.Menu(master, tearoff=0)
		self.menu.add_command(label = '复制', command=popmenu.on_copy)
		self.menu.add_separator()
		self.menu.add_command(label = '剪切', command=popmenu.on_cute)
		self.menu.add_separator()
		self.menu.add_command(label = '粘帖', command=popmenu.on_paste)

		self.entry.bind('<Button-3>', self.__popmenu)
		self.entry.bind('<KeyRelease>', self.input_check)

	def __popmenu(self, event):
		self.menu.post(event.x_root, event.y_root)

	def input_check(self, event):
		str = ''.join(s for s in self.show.get() if s in '0123456789.ABCDEFabcdef ')
		self.entry.delete(0, tk.END)
		self.entry.insert(0, str)

	def insert_blank(self, str):
		str += ' '
		self.show.set(str)
		self.entry.icursor(len(str))

	def calc_crc(self, data):
		pass

if __name__ == '__main__':
	Gui(tk.Tk()).mainloop()
