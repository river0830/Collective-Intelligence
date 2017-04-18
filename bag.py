#coding:utf8

import sys

'''dp by river'''
def bag_user():
    l = input("pls input task nums:")
    if l < 1 or l > 50:
        sys.exit()

    dstr = raw_input("pls input task data:")
    val = [int(s)/1024 for s in dstr.strip().split(" ")]
    if len(val) != l:
        sys.exit()

    ssum = sum(val)
    hsum = ssum/2
    bag = [0] * (hsum + 1)

    for i in xrange(l):
        for j in xrange(hsum, val[i]-1, -1):
            if bag[j] < bag[j - val[i]] + val[i]:
                bag[j] = bag[j - val[i]] + val[i]

    print(bag)
    hsum = max(bag)
    print(max(hsum, ssum - hsum) * 1024)

'''dp by zero_python '''
def dp(jobs, cap):
    now = [0] * (cap)
    for job in jobs:
        for c in range(cap-1, -1, -1):
            if c >= job: #这里用到job的重量
                now[c] = max(now[c], job + now[c-job]) #这里是价值
    return now[cap-1]

def dp_pro(jobs, cap):
    '''0-1背包问题: 价值与重量相等, 正常来说应该用字典'''
    now = set([0])  # now = {w:v} = {0:0}
    for job in jobs:
        tmp = set()
        for x in now:
            if x+job <= cap:  # w + w(job) <= cap
                tmp.add(x+job) # v + v(job)
        now = now.union(tmp)
        '''
        最后的得到 now = {w:v}, 所有的w<cap, 当容量达到w时, 最大价值可以是 v.
        所以最后容量对应为cap的最大价值就是 最大的v.
        '''
    return max(now)

def bag_zero_python():
    num = int(raw_input().strip())

    jobs = map(lambda x: int(x)/1024, raw_input().strip().split())

    total = sum(jobs)
    cap = (total+1)/2

    res = dp(jobs, cap)
    print max((total - res), res)*1024

"""
@author: Aprilvkuo
@file: netbeans.py
@time: 17-3-30 上午10:34
"""

def dp_Aprilvkuo():
    int(raw_input())
    data = map(int,raw_input().split())
    total = 0
    for i in range(len(data)):
        total += data[i]/1024

    state = [0 for i in range(total)]
    state[0] = 1
    for i in range(len(data)):
        tmp = data[i]/1024
        for j in range(total-1,-1,-1):
            if state[j] == 1 and j+tmp<total:
                state[j+tmp] = 1

    for i in range(total/2,-1,-1):
        if state[i] == 1:
            return (total-i)*1024

""" dp by xiaohuan """
def dp_xiaohuan():
    N = int(raw_input().strip())
    a = map(lambda x: int(x)/1024, raw_input().strip().split())

    total = sum(a)
    C = total / 2
    dp = set()
    dp.add(C)
    for num in a:
        tmp = set()
        for key in dp:
            if key - num >= 0 :
                tmp.add(key-num)
        dp = dp.union(tmp)

    print (total - (C-min(dp)))*1024

if __name__ == "__main__":
    bag_user()
    bag_zero_python()
