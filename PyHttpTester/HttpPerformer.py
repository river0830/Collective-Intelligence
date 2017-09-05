#coding:utf-8
'''
Created on 2016-2-17

@author: Administrator
'''

from Tkinter import *
import httplib
import urllib
import urllib2
from urllib2 import URLError

class HttpPerformer:
    
    """·¢ÆðÇëÇóÖ®Ç°£¬¼òµ¥¼ì²é²ÎÊý"""
    @staticmethod
    def check(method, host, url, port, param, header):
        if method == None:
            msg = "method is Null !"
        elif len(host) < 3:
            msg = "invalid host"
        elif not port.isdigit():
            msg = "invalid port"
        else:
            return True
        
        root = Tk()
        Message(root, text = msg).pack()
        root.mainloop()
        return False
    
    def __init__(self, method, host, url, port, param, header = {}):
        self.method = method
        self.host = host
        self.url = url
        self.port = port
        self.param = param
        self.header = header
        self.flag = 0
        return
    
    """ÏÔÊ¾´íÎóÌáÊ¾"""
    def showResultFail(self):        
        e = self.e
        msg = ""
        try:
            msg = msg + str(e.code) + "\n"
        except Exception, e:
            print(e)
        
        try:
            msg = msg + str(e.reason) + "\n"
        except Exception, e:
            print(e)
        
        if msg == "":
            msg = "url open error"
        root = Tk()
        root.title("Failed")
        textShow = Text(root)
        textShow.insert(INSERT, msg)
        textShow.pack()
        self.flag = 0
        root.mainloop()
        
    """ÏÔÊ¾³É¹¦ÌáÊ¾"""
    def showResult(self):
        data = self.data
        msg = str(data)
        root = Tk()
        root.title("Result")
        textShow = Text(root)
        textShow.insert(INSERT, msg)
        textShow.pack()
        self.flag = 0
        root.mainloop()
        
    """·¢ÆðÇëÇó£¬ ²¢Î¬»¤flagµÄÖµ"""
    def connect(self):
        if self.flag == 1: 
            print "is connecting! return!"
            return
        self.flag = 1
        paramEncoded = None      
        resp = None 
        data = ""
        if not self.param == None:
            if len(self.param) > 0:
                paramEncoded = urllib.urlencode(self.param)
        try:
            requestUrl = "http://" + self.host + ":" + str(self.port)
            if len(self.url) > 0:
                requestUrl += self.url
            ##doGet
            if self.method == "get":                                
                if not paramEncoded == None:
                    requestUrl = requestUrl + "?" + paramEncoded
                req = urllib2.Request(url=requestUrl, headers=self.header)
                resp = urllib2.urlopen(req)
                data = resp.read()
                self.data = data
            ##doPost
            else:
                req = None
                if not paramEncoded == None:
                    req = urllib2.Request(url=requestUrl, data=paramEncoded, headers=self.header)
                else:
                    req = urllib2.Request(url=requestUrl, headers=self.header)
                resp = urllib2.urlopen(req)
                data = resp.read()
                self.data = data
        except URLError, e:
            print e
            self.flag = -1
            self.e = e
            return
        print "success"
        self.flag = 2
    
    """ flag : 0:prepare 1:connecting 2:success -1:failed"""
    def getFlag(self):
        return self.flag