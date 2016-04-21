# -*- coding=utf-8 -*-
# for pyathon2.7.9

import sys
import time
import os

def simple_alarm(tt, count):
    print('{0}-{1}'.format(tt, count))
          
    try:
        delay = tt.spilt(':')
    except:
        delay = '5'

    delay = [int(i) for i in delay]
    try:
        delay_sec = delay[-1]
    except:
        delay_sec = 1

    try:
        delay_sec += delay[-2] * 60
    except:
        pass

    try:
        delay_sec += delay[-3] * 3600
    except:
        pass

    try:
        count = int(count)
    except:
        count = 3

    time.sleep(delay_sec)
    print('{0}'.format('*' * count))
    
if __name__ == "__main__":
    try: 
        delay = sys.argv[1]
    except: 
        delay = '5'
    try: 
        beep_time = sys.argv[2]
    except: 
        beep_time = 5 
    simple_alarm(delay, beep_time)
    
    os.system("pause")
    