#-*- coding:utf-8 -*-
#python example
#for python2.7.9

import Tkinter as tk
import uuid

def print_select(event):
    print("the select is {0}".format(mlist.get(mlist.curselection())))

def get_mac_addr():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

print('Computer Mac Addr:')
print(get_mac_addr())

L = [1, 9, 5, 7, 6]
K = L[::-1]

print(L)
print(K)

while True:
    re = raw_input('Pls Enter text:')
    if re == 'gui': break
    elif not re.isdigit():
        print(re.upper())
    else:
        print(int(re) ** 2)



root = tk.Tk()

#root.geometry('300x300')
root.resizable(width = False, height = False)

#root.columnconfigure(0, weight = 1)
#root.rowconfigure(0, weight = 1)

#sticky 对齐方向选项:
#default为窗体中间
#N-上中 S-下中  W-左中  E-右中
#NE-右上角 SE-右下角 SW-左下角 NW-左上角
#N+S 垂直方向拉升且保持水平中间对齐
#E+W 水平方向拉升且保持垂直中间对齐
#N+E+S+W 水平/垂直方向拉升方式填充单元格

#columnspan,rowspan: 控件跨多列/行显示
#ipadx,ipady: X,Y方向空白区域大小
#padx,pady:   X,Y方向空白区域保留大小

#Label(root, test = 'Center').grid(row = 0, column = 0, columspan = 2, sticky = W+E+N+S, padx = 0, pady = 0)
tk.Label(root, text = 'First').grid(row = 0, sticky = "nsew")
tk.Label(root, text = 'Second').grid(row = 1, sticky = "nsew")

#Label(root, text = 'First').grid(row = 0)
#Label(root, text = 'Second').grid(row = 1)

e1 = tk.Entry(root, width = 40)
e2 = tk.Entry(root, width = 40)

e1.grid(row = 0, column = 1, sticky = "nsew")
e2.grid(row = 1, column = 1, sticky = "nsew")

tk.Button(root, text = 'Entry').grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "nsew")

var = tk.StringVar()
var.set(('a', 'b', 'c', 'd'))
mlist = tk.Listbox(root, listvariable = var, height = 2)
mlist.bind('<ButtonRelease-1>', print_select)

bar = tk.Scrollbar(root)
mlist.config(yscrollcommand = bar.set)
bar['command'] = mlist.yview
bar.grid(row = 4, column = 1, sticky = 'e')
mlist.grid(row = 4, column = 0, columnspan = 2, sticky = "nsew")

root.mainloop()



