# -*- coding = utf8 -*-
# for python 2.7.9

import os

class Stack(object):
    '''
    Stack class by list;
    '''
    def __init__(self):
        self.item = []

    def push(self, items):
        self.item.append(items)

    def pop(self):
        if not self.empty():
            return self.item.pop()
        return None

    def size(self):
        return len(self.item)

    def empty(self):
        return self.item == []

def char_check(s):
    '''
    char loopcheck
    :param s:  input string
    :return: none
    '''
    if not isinstance(s, str): return False

    left, right = "({[", ")}]"

    s = s.replace(' ', '')
    st = Stack()
    print("{0} is readying identified...".format(s))
    for item in s:
        if item in left:
            st.push(item)
        elif item in right:
            if st.empty(): return False
            top = st.pop()
            if left.index(top) != right.index(item):
                return False
        else:
            pass #print("unvaild char {0}".format(i))

    return st.empty()

def base_conv(dnum, base):
    if not isinstance(dnum, int): return ""
    if not base in (2, 8, 16): return ""
    if dnum < 0: return ""

    dig = "0123456789ABCDEF"
    st = Stack()

    while dnum > 0:
        r = dnum % base
        st.push(r)
        dnum = dnum // base

    dstr = ""
    while not st.empty():
        dstr = dstr + dig[st.pop()]

    return dstr

def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other:
                break
            else:
                res.append(x)
    return res

def union(*args):
    res = []
    for x in args:
        for n in x:
            if n not in res:
                res.append(n)
    return res

if __name__ == "__main__":
    str1 = "((()({)}))"
    str2 = "(((  ()))"
    str3 = "(((()  [])))"

    print("{0} identified {1}".format(str1, char_check(str1)))
    print("{0} identified {1}".format(str2, char_check(str2)))
    print("{0} identified {1}".format(str3, char_check(str3)))

    char_check(23)

    n = 7899
    print("{0} conv 2dig 0b{1}".format(n, base_conv(n, 2)))
    print("{0} conv 2dig 0o{1}".format(n, base_conv(n, 8)))
    print("{0} conv 2dig 0x{1}".format(n, base_conv(n, 16)))

    try:
        u1 = "123"
        u2 = "234"
        u3 = "567"
        print('serial {0},{1},{2} set={3} union={4}'.format(u1, u2, u3, intersect(u1, u2, u3), union(u1, u2, u3)))
        
    except Exception:
        print Exception

    finally:
        os.system("pause")
               


    