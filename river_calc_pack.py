#coding:utf-8
'''
this is the fisrt python example by river.

interface design:
编辑  关于
+/- 1/x clear backspace
7  8  9  +  =
4  5  6  -  //
1  2  3  *  log10
0  .  %  /  sqrt

history:
2016.12.26  the first version
'''

import Tkinter as tk
import tkMessageBox as tkbox
import operator, math
import sys

import win32clipboard as wclip
import win32con
import river

class Calc(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)

		self.safe_dict = {
			'+'    : operator.add,
			'-'    : operator.sub,
			'*'    : operator.mul,
			'/'    : operator.div,
			'//'   : operator.floordiv,
			'%'    : operator.mod,
			'sqrt'   : math.sqrt,
			'log10'  : math.log10,
		}

		self.root = master

		self.create_ctrl(master)
		#create_memu
		self.create_menu(master)
		try:
			river.HideBlankWindow()
		except:
			pass

	def create_ctrl(self, master):
		master.title("计算器(Pack)")
		#master.geometry("320x320")
		# 窗口不可拉伸
		master.resizable(width=False, height=False)

		self.entry = tk.StringVar()
		tk.Entry(master, relief=tk.SUNKEN, textvariable=self.entry)\
			.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH, padx=1, pady=1)
		#± 1/x Clear Backspace
		fram1 = tk.Frame(master)
		fram1.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
		#self.create_buttons(fram1, '', 0, 6, tk.SUNKEN)
		self.create_buttons(fram1, '±',
							lambda x=self.entry : x.set('-('+x.get()+')'))
		self.create_buttons(fram1, '1/x',
							lambda x=self.entry : self.calc('1.0/'+x.get()))
		self.create_buttons(fram1, 'Clear',
							lambda x=self.entry : x.set(''))
		self.create_buttons(fram1, 'Backspace',
							lambda x=self.entry : x.set(self.back(x.get())), 14)

		fram2 = tk.Frame(master)
		fram2.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
		for c in '789+':
			self.create_buttons(fram2, c, lambda x=self.entry, c=c : x.set(x.get()+c))
		self.create_buttons(fram2, '=',
		                    lambda x=self.entry : self.calc(x.get()))

		fram3 = tk.Frame(master)
		fram3.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
		for c in '456-':
			self.create_buttons(fram3, c, lambda x=self.entry, c=c : x.set(x.get()+c))
		self.create_buttons(fram3, '//',
		                    lambda x=self.entry : x.set(x.get()+'//'))

		fram4 = tk.Frame(master)
		fram4.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
		for c in '123*':
			self.create_buttons(fram4, c, lambda x=self.entry, c=c : x.set(x.get()+c))
		self.create_buttons(fram4, 'log10',
		                    lambda x=self.entry : self.calc('log10(' + x.get() + ')'))

		fram5 = tk.Frame(master)
		fram5.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
		for c in '0.%/':
			self.create_buttons(fram5, c, lambda x=self.entry, c=c : x.set(x.get()+c))
		self.create_buttons(fram5, 'sqrt',
		                    lambda x=self.entry: self.calc('sqrt(' + x.get() + ')'))

	def create_buttons(self, frm, str, commands, width=6, rel=tk.RAISED):
		tk.Button(frm, text=str, width=width, height=2, command=commands, relief=rel)\
			.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1)

	def create_menu(self, master):
		menubar = tk.Menu(master)

		editmenu = tk.Menu(menubar, tearoff=0)
		editmenu.add_command(label='复制', accelerator="ctrl + c",
			command= lambda x=self.entry : self.clip_write(x.get()))

		editmenu.add_command(label='剪切', accelerator="ctrl + x",
			command= lambda x=self.entry : self.clip_xcopy(x.get()))

		editmenu.add_separator()
		editmenu.add_command(label='粘帖', accelerator="ctrl + v",
			command= lambda x=self.entry : x.set(self.clib_get()))

		aboutmenu = tk.Menu(menubar, tearoff = 0)
		aboutmenu.add_command(label='关于', command= lambda : self.about())

		menubar.add_cascade(label='编辑', menu=editmenu)
		menubar.add_cascade(label='关于', menu=aboutmenu)
		master.config(menu=menubar)

	def calc(self, str):
		try:
			self.entry.set(self.my_eval(str))
		except:
			self.entry.set("Error")

	def my_eval(self, str):
		try:
			return eval(str, {'__builtins__':None}, self.safe_dict)
		except:
			return 'Error'

	def about(self):
		tkbox.showinfo('calc', "river's calculator by pack!")

	def clip_xcopy(self, str):
		self.entry.set("")
		self.clip_write(str)

	def clip_write(self, str):
		wclip.OpenClipboard()
		wclip.EmptyClipboard()
		wclip.SetClipboardData(win32con.CF_TEXT, str)
		wclip.CloseClipboard()

	def clib_get(self):
		wclip.OpenClipboard()
		str = wclip.GetClipboardData(win32con.CF_TEXT)
		wclip.CloseClipboard()
		return str

	def back(self, str):
		if(len(str) > 0):
			return str[:-1]
		else:
			return str

if __name__ == '__main__':
	Calc(tk.Tk()).mainloop()

