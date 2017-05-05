#coding:utf8

def get_max_core():
    len = input("pls input task number:")
    if len < 1 and len > 50:
        return

    item = raw_input("pls input task data len:")
    val = item.split(" ")
    if len(val) > len:
        print("input data err")
        return

    val = [int(s) for s in val]
    sum = 0
    for s in val:
        s /= 1024
        sum += s

    msum = sum / 2 + 1
    bag = [0] * (msum + 1)
    print(val)
    print("sum is {0} msum is {1}".format(sum, msum))

    for i in xrange(len):
        for j in xrange(msum, val[i] - 1, -1):
            if bag[j] < bag[j - val[i]] + val[i]:
                bag[j] = bag[j - val[i]] + val[i]

    print("{0}".format(max(bag[msum], msum - bag[msum]) * 1024))

if __name__ == "__main__":
    try:
        get_max_core()
    except Exception as e:
        print e

    raw_input()
    
    
    
