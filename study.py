# -*- coding = utf8 -*-
# for python 2.7.9

import os

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
    try:
        u1 = "123"
        u2 = "234"
        u3 = "567"
        print('serial {0},{1},{2} set={3} union={4}'.format(u1, u2, u3, intersect(u1, u2, u3), union(u1, u2, u3)))
        
    except Exception:
        print Exception

    finally:
        os.system("pause")
               


    