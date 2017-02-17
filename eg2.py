#coding=utf8
from Tkinter import *

class eg(object):
    def __init__(self):
        self.data = 'river'

    def __add__(self, other):
        return other + self.data

    def __str__(self):
        return "{0}".format(self.data)

class section:
    def onPaste(self):
        try:
            self.text = root.clipboard_get()
        except TclError:
            pass
        show.set(str(self.text))
    def onCopy(self):
        self.text = Entry.get()
        root.clipboard_append(self.text)
    def onCut(self):
        self.onCopy()
        try:
            Entry.delete('sel.first', 'sel.last')
        except TclError:
            pass


root = Tk()
root.title('试试文本框右键菜单')
root.resizable(False, False)
root.geometry("300x300")

Label(root, text='下面是一个刚刚被生成的文本框，试试操作吧').pack(side="top")
Label(root).pack(side="top")

show = StringVar()
Entry = Entry(root, textvariable=show, width="30")
Entry.pack()

sc = section()
menu = Menu(root, tearoff=0)
menu.add_command(label="复制", command=sc.onCopy)
menu.add_separator()
menu.add_command(label="粘贴", command=sc.onPaste)
menu.add_separator()
menu.add_command(label="剪切", command=sc.onCut)

def popupmenu(event):
    menu.post(event.x_root, event.y_root)

Entry.bind("<Button-3>", popupmenu)

slangon = Label(root, text='你好,RIVER!', font='宋体 -12')
slangon.pack()

def slangon_set(ev=None):
    slangon.config(font='宋体 -{0}'.format(int(scale.get())))

scale = Scale(root, from_=12, to=36, length=240, orient=HORIZONTAL, command=slangon_set)
scale.set(16)
scale.pack()

eg1 = eg()
print("eg1 is {0}".format(eg1))
print("eg1 add is {0}".format(eg1 + 'hello'))

def f2(a, b):
    t = [list() for i in range(b)]
    for i, x in enumerate(a):
        t[i%b].append(x)
    return dict(zip(range(1, b+1), t))

def f1(a, b):
    r = {}
    for i, x in enumerate(a):
        r.setdefault(i%b + 1, []).append(x)
    return r

aa = ['1', '2', '3', '4', '5', '7']
print("{0}".format(str(f1(aa, 12))))
print("{0}".format(str(f2(aa, 12))))

root.mainloop()
