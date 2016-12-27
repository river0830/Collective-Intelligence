#coding:utf-8
'''
this is the fisrt python example by river.

interface design:
编辑  关于
backspace clear +/- 1/x
7  8  9  +  //
4  5  6  -  %
1  2  3  *  pow
0  .  =  /  sqrt

history:
2016.12.26  the first version
'''

import Tkinter as tk
import operator, math
import sys

import win32clipboard as wclip
import win32con

safe_dict = {
	'+'    : operator.add,
	'-'    : operator.sub,
	'*'    : operator.mul,
	'/'    : operator.div,
	'//'   : operator.floordiv,
	'%'    : operator.mod,
	'sqrt' : math.sqrt,
	'pow'  : operator.pow,
}

class Calc(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)

		self.master.title("RIVER 计算器")
		self.master.geometry("320x320")
		#窗口不可拉伸
		self.master.resizable(width=False, height=False)

		#create_memu
		self.create_menu(master);

		self.display = tk.StringVar

	def create_menu(self, master):
		menubar = tk.Menu(master)

		editmenu = tk.Menu(menubar, tearoff = 0)
		editmenu.add_command(label = '复制 Ctrl+C',
							 command = lambda x = self.display : self.clip_write(x.get()))
		editmenu.add_command(label = '剪切 Ctrl+X',
							 command = lambda x = self.display : self.clip_xcopy(x.get()))
		editmenu.add_separator()
		editmenu.add_command(label = '粘帖 Ctrl+V',
							 command = lambda x = self.display : x.set(self.clib_get()))

		menubar.add_cascade(label = '编辑', menu = editmenu)

	def calc(self):
		try:
			self.display.set(self.my_eval(self.display.get()))
		except:
			self.display.set("Error")

	def my_eval(self, str):
		return eval(str, {'__builtins__':None}, safe_dict)

	def clip_xcopy(self, str):
		self.display.set("")
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

if __name__ == '__main__':
	root = tk.Tk()
	Calc(root)

	root.mainloop()
