#coding:utf-8
from Tkinter import *  
import ctypes
import sys
import ast, operator

import re

def safe_eval(eval_str, **kw):
    '''
    安全eval，确保eval的内容是合法的，并且隔离的。
    **kw不可用，以后扩展为可定义命名空间。
    '''
    #callback functions
    def start_structure(scanner, token): return "start structure", token
    def key(scanner, token):   return "key", token
    def value(scanner, token):
        #非法写法
        if token.lower() == 'true'and token != 'True':
            raise 'value Error "%s"'%token
    def str_value(scanner,token):
        return "string value",token
    def end_structure(scanner, token):  return "end start structure",token

    scanner = re.Scanner([
        (r"[{\[(]", start_structure),
        (r"[\w]+\s*:", key),
        (r"['\"][^'\"]+['\"]",str_value),
        (r"[\w]+", value),
        (r"\s*,\s*",None),
        (r"[})\]]", end_structure),
    ])

    tokens, remainder = scanner.scan(eval_str)
    for token in tokens:
        print token
    #make a list of safe functions
    safe_list = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'de grees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
    #use the list to filter the local namespace s
    safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
    #add any needed builtins back in.
    #由于所有内置的对象被屏蔽 __builtins__中的所有对象不可使用，所以True、False需要单独定义
    #加入命名空间
    safe_dict['True'] = True
    safe_dict['False'] = False

    return eval(eval_str,{'__builtins__':None},safe_dict)

def my_eval(str):
    my_safe_dict = {}
    my_safe_dict['pow'] = operator.pow
    my_safe_dict['abs'] = operator.abs
    my_safe_dict['+']   = operator.add
    my_safe_dict['-']   = operator.sub
    my_safe_dict['*']   = operator.mul
    my_safe_dict['/']   = operator.div
    my_safe_dict['//']  = operator.floordiv

    return eval(str, {'__builtins__':None}, my_safe_dict)

binOps = {
    ast.Add:       operator.add,
    ast.Sub:       operator.sub,
    ast.Mult:      operator.mul,
    ast.Div:       operator.div,
    ast.Mod:       operator.mod,
    ast.FloorDiv : operator.floordiv,
    ast.Pow:       operator.pow,
}

def arithmeticEval (s):
    node = ast.parse(s, mode='eval')

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return binOps[type(node.op)](_eval(node.left), _eval(node.right))
        else:
            raise Exception('Unsupported type {}'.format(node))

    return _eval(node.body)
  
#创建横条型框架  
def frame(root, side):  
    w = Frame(root)  
    w.pack(side = side, expand = YES, fill = BOTH)  
    return w  
#创建按钮  
def button(root, side, text, command = None):  
    w = Button(root, text = text, command = command)  
    w.pack(side = side, expand = YES, fill = BOTH)  
    return w  
#继承了Frame类，初始化程序界面的布局  
class Calculator(Frame):  
    def __init__(self, master = None):
        if sys.platform[:3] == 'win':
            whnd = ctypes.windll.kernel32.GetConsoleWindow()
            if whnd != 0:
                ctypes.windll.user32.ShowWindow(whnd, 0)
                ctypes.windll.kernel32.CloseHandle(whnd)
        
        Frame.__init__(self, master)
          
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Simple Calculater')
          
        display = StringVar()  
        #添加输入框  
        Entry(self, relief = SUNKEN,
              textvariable = display).pack(side = TOP, expand = YES,  
                                           fill = BOTH)  
        #添加横条型框架以及里面的按钮  
        for key in('123', '456', '789', '-0.'):  
            keyF = frame(self, TOP)  
            for char in key:  
                button(keyF, LEFT, char, lambda w = display, c = char:w.set(w.get() + c))  
        #添加操作符按钮  
        opsF = frame(self, TOP)  
        for char in '+-*/=':  
            if char == '=':  
                btn = button(opsF, LEFT, char)  
                btn.bind('<ButtonRelease - 1>', lambda e, s = self, w = display:s.calc(w), '+')  
  
            else:  
                btn = button(opsF, LEFT, char, lambda w = display, s = '%s' %char:w.set(w.get() + s))  
        #添加清除按钮  
        clearF = frame(self, BOTTOM)  
        button(clearF, LEFT, 'clear', lambda w = display:w.set(''))

    #调用eval函数计算表达式的值
    def calc(self, display):
        try:
            display.set(my_eval(display.get()))
            #eval();
        except:
            display.set("ERROR")
#程序的入口  
if __name__ == '__main__':  
    print('ok')
    root = Tk()
    root.geometry("300x300")
    #设置窗口固定不可调
    root.resizable(width=False, height=False)
    Calculator(root)
    root.mainloop()
