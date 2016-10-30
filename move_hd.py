#python2.7
# -*- coding: utf-8 -*-

import time
from Tkinter import *

#　配置
#　要打开的图像
image1 = "handou.gif"

# 初始坐标
x0 = 50.0
y0 = 50.0

# 列表将包含所有的x和y坐标.到目前为止，他们只包含初始坐标
x = [x0]
y = [y0]
 
# 每次移动的速度或距离
vx = 1.0 # x 速度
vy = 0.5 # y 速度
 
# 边界，这里要考虑到图片的大小，要预留一半的长和宽
x_min = 46.0
y_min = 46.0
x_max = 754.0
y_max = 554.0

# 图片间隔时间,要动画效果，此处设为每秒４０帧
sleep_time = 0.025

# 运行步数
range_min = 1
range_max = 2000

# 创建500次的x和y坐标
for t in range(range_min,range_max): 
    # 新坐标等于旧坐标加每次移动的距离
    new_x = x[t-1] + vx
    new_y = y[t-1] + vy
 
    # 如果已经越过边界，反转方向
    if new_x >= x_max or new_x <= x_min:
        vx = vx*-1.0
 
    if new_y >= y_max or new_y <= y_min:
        vy = vy*-1.0
 
    # 添加新的值到列表
    x.append(new_x)
    y.append(new_y)

# 开始使用ｔｋ绘图
root = Tk()
canvas = Canvas(width=800, height=600, bg='white')
canvas.pack()

photo1 = PhotoImage(file = "handou.GIF")
width1 = photo1.width()
height1 = photo1.height()
image_x = (width1)/2.0
image_y = (height1)/2.0
    
# 每次的移动
for t in range(range_min,range_max): 
    canvas.create_image(x[t], y[t], image = photo1,tag = "pic") 
    canvas.update()
 
    # 暂停0.05妙，然后删除图像
    time.sleep(sleep_time)
    canvas.delete("pic")

root.mainloop()