#-*- coding: utf-8 -*-
#for python2.7
import Tkinter as tkinter
import json
import urllib
import sys
import ctypes

#to Python2.7
#tkinter = Tkinter 

class MYIP():
	
	def __init__(self):
		#隐藏窗口
		whnd = ctypes.windll.kernel32.GetConsoleWindow()
		if whnd != 0:
			ctypes.windll.user32.ShowWindow(whnd, 0)
			ctypes.windll.kernel32.CloseHandle(whnd)
		#main frame
			
		self.main_window = tkinter.Tk()
		
		#top frame
		self.top_frame = tkinter.Frame(self.main_window)
		#bottom frame
		self.bottom_frame = tkinter.Frame(self.main_window)

		self.L1 = tkinter.Label(self.top_frame, text='       IP 地址:       ')
		self.L1.pack(side='left')
		default_value = tkinter.StringVar()
		default_value.set('8.8.8.8')
		self.E1 = tkinter.Entry(self.top_frame, textvariable=default_value, bd=2)
		self.E1.pack(side = tkinter.LEFT)
		self.B1 = tkinter.Button(self.top_frame, text='确定', command=self.prcess_input)
		self.B1.pack(side=tkinter.RIGHT)

		self.bottom_left = tkinter.Frame(self.bottom_frame)
		self.bottom_right = tkinter.Frame(self.bottom_frame)
		
		self.label1 = tkinter.Label(self.bottom_left,text="%-10s" % "国家")
		self.label2 = tkinter.Label(self.bottom_left,text="%-10s" % '区域')
		self.label3 = tkinter.Label(self.bottom_left,text="%-10s" % '地区')
		self.label4 = tkinter.Label(self.bottom_left,text="%-10s" % '城市')
		self.label5 = tkinter.Label(self.bottom_left,text="%-10s" % '县')
		self.label6 = tkinter.Label(self.bottom_left,text="%-10s" % '运营商')

		self.label1.pack(side='top')
		self.label2.pack(side='top')
		self.label3.pack(side='top')
		self.label4.pack(side='top')
		self.label5.pack(side='top')
		self.label6.pack(side='top')

		self.En1 = tkinter.Entry(self.bottom_right)
		self.En2 = tkinter.Entry(self.bottom_right)
		self.En3 = tkinter.Entry(self.bottom_right)
		self.En4 = tkinter.Entry(self.bottom_right)
		self.En5 = tkinter.Entry(self.bottom_right)
		self.En6 = tkinter.Entry(self.bottom_right)

		self.En1.pack(side='top')
		self.En2.pack(side='top')
		self.En3.pack(side='top')
		self.En4.pack(side='top')
		self.En5.pack(side='top')
		self.En6.pack(side='top')

		self.bottom_left.pack(side='left')
		self.bottom_right.pack(side='right')
		self.top_frame.pack()
		self.bottom_frame.pack()
		
		self.main_window.mainloop()

	def get_data(self):
		API = "http://ip.taobao.com/service/getIpInfo.php?ip="
		#API = "http://www.daixh.com/app/ipinfo?ip="
		url = API + self.ipaddr
		#ret = (urllib.request.urlopen(url).read()).decode('utf-8')
		ret = (urllib.urlopen(url).read()).decode('utf-8')
		self.jsondata = (json.loads(ret))


	def process_data(self):
		if self.jsondata['data']['country']:
			country = self.jsondata['data']['country']
		else:
			country = "NULL"

		if self.jsondata['data']['area']:
			area = self.jsondata['data']['area']
		else:
			area = "NULL"

		if self.jsondata['data']['region']:
			region = self.jsondata['data']['region']
		else:
			region = "NULL"

		if self.jsondata['data']['city']:
			city = self.jsondata['data']['city']
		else:
			city = "NULL"

		if self.jsondata['data']['county']:
			county = self.jsondata['data']['county']
		else:
			county = "NULL"

		if self.jsondata['data']['isp']:
			isp= self.jsondata['data']['isp']
		else:
			isp = "NULL"
		return (country, area, region, city, county, isp)
		
		
	def prcess_input(self):
		self.ipaddr = self.E1.get()
		myjson = self.get_data()
		if myjson == False:
			return 1
		else:
			ret = self.process_data()
			self.En1.delete(0, tkinter.END)
			self.En2.delete(0, tkinter.END)
			self.En3.delete(0, tkinter.END)
			self.En4.delete(0, tkinter.END)
			self.En5.delete(0, tkinter.END)
			self.En6.delete(0, tkinter.END)
			self.En1.insert(0, ret[0])
			self.En2.insert(0, ret[1])
			self.En3.insert(0, ret[2])
			self.En4.insert(0, ret[3])
			self.En5.insert(0, ret[4])
			self.En6.insert(0, ret[5])

			
myip = MYIP()
