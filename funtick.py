import sys, my_tick

res = 10000
reps = range(res)

def forLoop():
    re = []
    for x in reps:
        re.append(abs(x))

    return re

def listComp():
    return [abs(x) for x in reps]

def mapComp():
    return list(map(abs, reps))

def yieldExr():
    return list(abs(x) for x in reps)

def getFunc():
    def gen():
        for x in reps:
            yield abs(x)

    return list(gen())

import os

if __name__ == "__main__":
    try:
        print(sys.version)

        for test in (my_tick.timer, my_tick.best_timer):
            print('TestFun:{0}'.format(test.__name__))
            
            for tset in (forLoop, listComp, mapComp, yieldExr, getFunc):
                m, n = test(tset)

                print('- ' * 33)
                print('{0:>8} : {1:.6f}s ==> [{2}...{3}]'.format(tset.__name__, m, n[0], n[-1]))
                #print('-9%s: %.5f ==> [%s...%s]' % (tset.__name__, m, n[0], n[1]))

    except Exception:
        print Exception

    finally:
        os.system("pause")

        
