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


	def calc(self, entry_show):
		try:
			entry_show.set(self.my_eval(entry_show.get()))
		except:
			entry_show.set("Error")

	def my_eval(self, str):
		return eval(str, {'__builtins__':None}, safe_dict)



if __name__ == '__main__':
	root = tk.Tk()
	Calc(root)

	root.mainloop()
