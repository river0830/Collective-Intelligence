#coding=utf8

from UiItem import ParamItem, MethodCheckButton, HostBox
from Tkinter import *
from HttpPerformer import *
from urllib import quote
import thread

root = Tk()

root.geometry('600x400')
root.title("HttpTester")

paramItemList = [] #存储参数控件的列表，以便动态添加

methodBox = MethodCheckButton(root)
methodBox.grid(row = 0, column = 0)

deleteCount = IntVar() #记录已删除的个数，仅仅为了布局时grid()
deleteCount.set(0)

"""获取所有请求参数"""
def getAllParams():
    dict = {}
    for paramItem in paramItemList:
        k = paramItem.getKey()
        v = paramItem.getValue()
        if len(k) > 0:
            print k, v
            dict.setdefault(str(k), v.encode("utf8"))
    return dict

"""按钮相应函数 ，增加一个参数控件"""
def addParam():
    currentParamCount = len(paramItemList)
    newParamItem = ParamItem(root, paramItemList, deleteCount)
    paramItemList.append(newParamItem)
    newParamItem.grid(row = currentParamCount + 2 + deleteCount.get(), columnspan = 2)

btnAdd = Button(root, text = "Add Param", command = addParam)
btnAdd.grid(row = 0, column = 1)

hostBox = HostBox(root)
hostBox.grid(row = 1, columnspan = 2)

"""按钮相应函数，异步发起请求"""
def perform():
    
    method = methodBox.getCurrentMethod()
    host = hostBox.getHost()
    url = hostBox.getUrl()
    port = hostBox.getPort()
    param = getAllParams()
    headers = {}
    if HttpPerformer.check(method, host, url, port, param, headers):
        performer = HttpPerformer(method, host, url, port, param, headers)
        #一个简单的异步处理， Tkinter 对异步支持不好，只能这样啦。
        thread.start_new_thread(performer.connect, ()) 
        
        #轮询请求结果      
        def pollFunc():
            flag = performer.getFlag()
            if flag == 0 or flag == 1:
                root.after(1000, pollFunc)
            elif flag == 2:
                performer.showResult()
            elif flag == -1:
                performer.showResultFail()
        root.after(1000, pollFunc)

btnPerform = Button(root, text = "Perform", command = perform, padx = 3)
btnPerform.grid(row = 0, column = 2)

root.mainloop()
