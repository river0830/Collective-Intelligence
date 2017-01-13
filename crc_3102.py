#coding:utf-8
#crc16 ccitt ccitt_1 for 3102 weight system

import Tkinter as tk
import ttk
import binascii

import river
import crc16

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
		try:
			self.text = ''.join(x for x in self.root.clipboard_get()
									if x in '0123456789ABCDEFabcdef ')
			if len(self.text) > 0:
				self.show.set(self.text)
		except Exception as e:
			pass

	def on_cute(self):
		self.root.clipboard_clear()
		self.on_copy()
		self.show.set('')

class Gui(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)

		river.HideBlankWindow()
		master.title("River's crc16 calculator")
		master.geometry("420x200")
		master.resizable(width=False, height=False)

		self.create_widget(master)
		self.create_popmenu(master)

	def create_widget(self, master):
		self.show = tk.StringVar()
		fram = self.create_frame()
		self.entry = ttk.Entry(fram, textvariable = self.show, font=16)
		self.entry.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)

		self.entry.bind('<Button-3>', self.__popmenu)
		self.entry.bind('<KeyRelease>', self.input_check)

		self.v_ccitt   = tk.IntVar()
		self.v_ccitt1  = tk.IntVar()

		fram = self.create_frame()
		cb = ttk.Checkbutton(fram, variable=self.v_ccitt, text='CCITT',
		                     command=self.fun_ccitt_v)
		cb.pack(expand=tk.YES, side=tk.LEFT)
		cb = ttk.Checkbutton(fram, variable=self.v_ccitt1, text='CCITT_1',
		                     command=self.fun_ccitt1_v)
		cb.pack(expand=tk.YES, side=tk.RIGHT)

		self.crc = crc16.Crc16()
		self.v_ccitt1.set(1)
		self.cflag = crc16.CCITT_1

		#16 key
		for key in ('01234567', '89ABCDEF'):
			fram = self.create_frame()
			for c in key:
				self.create_buttons(fram, c, lambda x=self.show, c=c: x.set(x.get()+c))

		fram = self.create_frame()
		self.create_buttons(fram, 'Blank',
							lambda x=self.show : self.insert_blank(x.get()))
		self.create_buttons(fram, 'Clear',
		                    lambda x=self.show: x.set(''))
		self.create_buttons(fram, 'Backspace',
							lambda x=self.show: x.set(self.back(x.get())))
		self.create_buttons(fram, '=',
							lambda x=self.show: x.set(self.calc_crc(x.get())))

	def create_popmenu(self, master):
		popmenu = Popmemu(master, self.show)

		self.menu = tk.Menu(master, tearoff=0)
		self.menu.add_command(label = '复制', command=popmenu.on_copy)
		self.menu.add_separator()
		self.menu.add_command(label = '剪切', command=popmenu.on_cute)
		self.menu.add_separator()
		self.menu.add_command(label = '粘帖', command=popmenu.on_paste)

	def create_buttons(self, fram, str, commands, widths=6):
		b = ttk.Button(fram, text=str, width=widths, command=commands)
		b.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1)

	def create_frame(self, sides=tk.TOP):
		fram = ttk.Frame(self.master, height=12)
		fram.pack(expand=tk.YES, side=sides, fill=tk.BOTH)
		return fram

	def fun_ccitt_v(self):
		if self.v_ccitt.get() == 1:
			self.v_ccitt1.set(0)
			self.cflag = crc16.CCITT

	def fun_ccitt1_v(self):
		if self.v_ccitt1.get() == 1:
			self.v_ccitt.set(0)
			self.cflag = crc16.CCITT_1

	def back(self, str):
		if(len(str) > 0):
			return str[:-1]
		else:
			return str

	def __popmenu(self, event):
		self.menu.post(event.x_root, event.y_root)

	def input_check(self, event):
		str = ''.join(s for s in self.show.get() if s in '0123456789ABCDEFabcdef ')
		self.entry.delete(0, tk.END)
		self.entry.insert(0, str)

	def insert_blank(self, str):
		str += ' '
		self.show.set(str)
		self.entry.icursor(len(str))

	def calc_crc(self, data):
		back = data
		data = data.replace(' ', '')
		dlen = len(data)
		if dlen > 0:
			try:
				data = binascii.unhexlify(data)
				data = [ord(x) for x in data]
				crc = self.crc.reen_crc16(self.cflag, data, len(data))
				back = '{0} {1:02x} {2:02x}'.format(back, crc>>8, crc&0xff)
			except Exception as e:
				return 'Error'
		return back

if __name__ == '__main__':
	Gui(tk.Tk()).mainloop()
