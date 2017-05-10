#!/usr/bin/env python
#coding:utf8

import os, sys

def parse_log():
    '''
        parse log looks like:
        114.249.4.96 - - [15/Jan/2016:20:59:47 +0800] "POST /api2/realtimetrack/ HTTP/1.1" 200 48 "-" "-" "-"
        114.249.4.96 - - [15/Jan/2016:20:59:47 +0800] "POST /api2/getgoodslist/ HTTP/1.1" 200 48 "-" "-" "-"
        222.128.172.215 - - [15/Jan/2016:23:59:47 +0800] "POST /api2/button_log/ HTTP/1.1" 200 48 "-" "-" "-"

        the out:
        IP:222.128.172.215     URL_CNT:{'/api2/button_log/': 1}
        IP:114.249.4.96        URL_CNT:{'/api2/getgoodslist/': 3, '/api2/realtimetrack/': 4}
    '''
    ipinfo = {}
    with open("plog.txt", 'r') as ff:
        for line in ff.readlines():
            try:
                ip = line.split()[0]
                url = line.split()[6]
            except Exception as err:
                continue

            if ip not in ipinfo:
                ipinfo[ip] = {url:1}
            else:
                if url not in ipinfo[ip]:
                    ipinfo[ip][url] = 1
                else:
                    ipinfo[ip][url] += 1
            
    with open('log_out.txt', 'a') as f:
        for ip, value in ipinfo.items():
            ss = "IP:{0:18}URL_CNT:{1}\n".format(ip, value)
            print(ss)
            f.write(ss)

if __name__ == "__main__":
    parse_log()
    raw_input()
    