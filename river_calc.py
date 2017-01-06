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

		river.HideBlankWindow()

	def create_ctrl(self, master):
		master.title("RIVER 计算器")
		#master.geometry("320x320")
		# 窗口不可拉伸
		master.resizable(width=False, height=False)
		#master.columnconfigure(0, weight=1)
		#master.rowconfigure(0, weight=1)

		self.entry = tk.StringVar()
		tk.Entry(master, relief=tk.SUNKEN, textvariable=self.entry)\
			.grid(row=0, column=0, columnspan=5, sticky='nesw')
        #± 1/x Clear Backspace
		self.create_buttons('±',
		                    lambda x=self.entry : x.set('-('+x.get()+')'), 2, 0)
		self.create_buttons('1/x',
		                    lambda x=self.entry : self.calc('1.0/'+x.get()), 2, 1)
		self.create_buttons('Clear',
		                    lambda x=self.entry : x.set(''), 2, 2)
		self.create_buttons('Backspace',
		                    lambda x=self.entry : x.set(self.back(x.get())), 2, 3, 2)

		rw = 3
		for key in ('789+', '456-', '123*', '0.%/'):
			col = 0
			for c in key:
				self.create_buttons(c,
				                    lambda x=self.entry, c=c : x.set(x.get()+c), rw, col)
				col += 1
			rw += 1

		self.create_buttons('=',
		                    lambda x=self.entry : self.calc(x.get()), 3, 4)
		self.create_buttons('//',
		                    lambda x=self.entry : x.set(x.get()+'//'), 4, 4)
		self.create_buttons('log10',
		                    lambda x=self.entry : self.calc('log10(' + x.get() + ')'), 5, 4)
		self.create_buttons('sqrt',
		                    lambda x=self.entry: self.calc('sqrt(' + x.get() + ')'), 6, 4)

	def create_buttons(self, str, commands, rows, columns, colspan=1):
		tk.Button(self.root, text=str, height=2, width=6, command=commands)\
			.grid(row=rows, column=columns, columnspan=colspan, padx=1, pady=1, sticky='wens')

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
		tkbox.showinfo('calc', "river's calculator")

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
	root = tk.Tk()
	Calc(root)

	root.mainloop()
