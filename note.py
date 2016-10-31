#python2.7
#coding: utf-8
import Tkinter as tk

root = tk.Tk('Simple Editor')
mi = tk.StringVar()
tk.Label(text='Please input something you like~' ).pack()
te = tk.Text(height = 30,width =100)
te.pack()
tk.Label(text='      File name     ').pack(side = tk.LEFT)
tk.Entry(textvariable = mi).pack(side = tk.LEFT)
mi.set('*.txt')
def save():
  t = te.get('0.0','10.0')
  f = open(mi.get(),'w')
  f.write(t)
tk.Button(text = 'Save' , command = save).pack(side = tk.RIGHT)
tk.Button(text = 'Exit' , command = root.quit).pack(side = tk.RIGHT)
tk.mainloop()