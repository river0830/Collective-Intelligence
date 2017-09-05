#coding: utf-8
'''
Created on 2016-2-17

@author: Administrator
'''
from Tkinter import Frame, Label, Entry, Button, Checkbutton, IntVar, StringVar

""" ÊäÈë²ÎÊýµÄ¿Ø¼þ """
class ParamItem(Frame):
    
    def __init__(self, master, itemList, deleteCount):
        Frame.__init__(self, master)
        self.labelKey = Label(self, text = "Key:")
        self.labelValue = Label(self, text = "Value:")
        self.entryKey = Entry(self, width = 8)
        self.entryValue = Entry(self, width = 20)
        self.deleteCount = deleteCount
        self.itemList = itemList
        self.btnDelete = Button(self, text = "delete", \
            command = self.__internalDelete, padx = 5)
        self.__boxComponents()
    
    def __boxComponents(self):
        self.labelKey.grid(row = 0, column = 0)
        self.entryKey.grid(row = 0, column = 1)
        self.labelValue.grid(row = 0, column = 2)
        self.entryValue.grid(row = 0, column = 3)
        self.btnDelete.grid(row = 0, column = 4)
    
    def __internalDelete(self):
        self.deleteCount.set(self.deleteCount.get() + 1)
        self.itemList.remove(self)
        self.destroy()
    def getKey(self):
        return self.entryKey.get()
    
    def getValue(self):
        return self.entryValue.get()
    
"""Ñ¡ÔñGet PostµÄ¿Ø¼þ"""
class MethodCheckButton(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width = 15)
        self.initComplete = False
        self.getVar = IntVar()
        self.postVar = IntVar()
        self.getCheckButton = Checkbutton(self, \
            text = "GET", width = 6, variable = self.getVar, \
            command = self.__singleSelectCommandGet, onvalue = 1, offvalue = 0)
        self.postCheckButton = Checkbutton(self, \
            text = "POST", width = 6, variable = self.postVar, \
            command = self.__singleSelectCommandPost, onvalue = 1, offvalue = 0)
        self.label = Label(self, text = "Use Method:", padx = 3)
        self.__boxComponents()
        self.initComplete = True
        
    def __boxComponents(self):
        self.label.grid(row = 0, column = 0)
        self.getCheckButton.grid(row = 0, column = 1)
        self.postCheckButton.grid(row = 0, column = 2)
        
        
    def __singleSelectCommandGet(self):
        if self.initComplete == False:
            return
        self.postCheckButton.deselect()

          
    def __singleSelectCommandPost(self):
        if self.initComplete == False:
            return
        self.getCheckButton.deselect()              
    
    def getCurrentMethod(self):
        if self.getVar.get() == 1:
            return "get"
        if self.postVar.get() == 1:
            return "post"
        return None

"""ÊäÈëhost url port µÄ¿Ø¼þ"""
class HostBox(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.labelHost = Label(self, text = "Host: http://")
        self.entryHost = Entry(self, width = 20)
        self.labelUrl = Label(self, text = "Url:")
        self.entryUrl = Entry(self, width = 20)
        self.labelPort = Label(self, text = "Port:")
        self.port = StringVar()
        self.port.set("80")
        self.entryPort = Entry(self, width = 8, textvariable = self.port)
        self.__boxComponents()
    
    def __boxComponents(self):
        self.labelHost.grid(row = 0, column = 0)
        self.entryHost.grid(row = 0, column = 1)
        self.labelUrl.grid(row = 1, column = 0)
        self.entryUrl.grid(row = 1, column = 1)
        self.labelPort.grid(row = 0, column = 2)
        self.entryPort.grid(row = 0, column = 3)
        
    def getHost(self):
        return self.entryHost.get()
    
    def getPort(self):
        return self.port.get()
    
    def getUrl(self):
        return self.entryUrl.get()