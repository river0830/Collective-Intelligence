# -*- coding:utf-8 -*-
#---Desktop Edition---
 
from Tkinter import *
import datetime
import time

def event(self):
	print 'this is a event'
 
def hello(self):
    print 'hello,world'

def about(self):
    print 'hello,world'
    #w = Label(root,text='this is a programe about tictactoe!\n we really need your opinion\nplease email us:wenyuhua90 at gmail.com')
    #w.grid()

root = Tk()
root.title('与xxx聊天中')

#-------------create the menu bar------------
menubar = Menu(root)

#创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Restart", command = hello)
filemenu.add_command(label="Save", command = hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#创建下拉菜单Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command = about)
menubar.add_cascade(label="Help", menu = helpmenu)
 
#显示菜单
root.config(menu=menubar)

#发送按钮事件
def sendmessage():
  #在聊天内容上方加一行 显示发送人及发送时间
    str = text_msg.get('0.0', END) 
    print('ss' + str)
    msgcontent = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
    text_msglist.insert(END, msgcontent, 'green')
    text_msglist.insert(END, text_msg.get('0.0', END))
    text_msg.delete('0.0', END)
 
#创建几个frame作为容器
frame_left_top   = Frame(width=380, height=270, bg='white')
frame_left_center  = Frame(width=380, height=100, bg='white')
frame_left_bottom  = Frame(width=380, height=20)
frame_right     = Frame(width=170, height=400, bg='white')

#创建需要的几个元素
bar             = Scrollbar(frame_left_top, orient = VERTICAL)
text_msglist    = Text(frame_left_top, yscrollcommand = bar.set)
text_msg        = Text(frame_left_center);
button_sendmsg  = Button(frame_left_bottom, text='发送', command=sendmessage)
bar.config(command = text_msglist.yview)

#创建一个绿色的tag
text_msglist.tag_config('green', foreground='#008B00')

#使用grid设置各个容器位置
frame_left_top.grid(row=0, column=0, padx=2, pady=5)
frame_left_center.grid(row=1, column=0, padx=2, pady=5)
frame_left_bottom.grid(row=2, column=0)
frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
frame_left_top.grid_propagate(0)
frame_left_center.grid_propagate(0)
frame_left_bottom.grid_propagate(0)

#把元素填充进frame
text_msglist.grid()
text_msg.grid()
bar.grid()
button_sendmsg.grid(sticky=NE)

#主事件循环
root.mainloop()