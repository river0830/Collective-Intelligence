#!/usr/bin/env python
#coding:utf8

import os
import time, shutil

if os.name == "nt":
    DEST_DIR = r"D:\logbak"
    CUR_DIR  = r"D:\log"
else:
    DEST_DIR = u"/opt/applogbak"
    CUR_DIR  = u"/opt/applog"

maxlog = 3
tdelay = 24 * 3600

def compare_log(x, y):
    if os.name == "nt":
        dir_x = CUR_DIR + "\\" + x
        dir_y = CUR_DIR + "\\" + y
    else:
        dir_x = CUR_DIR + "/" + x
        dir_y = CUR_DIR + "/" + y

    if os.path.getmtime(dir_x) < os.path.getmtime(dir_y):
        return -1
    elif os.path.getmtime(dir_x) > os.path.getmtime(dir_y):
        return 1
    else:
        return 0

def log_backup(dest, cur, tick):
    '''
    创建cur目录,保证cur目录下有10个日志文件
    当存在dest目录时,将多余日志文件拷贝到dest目录,否则删除多余的日志
    '''
    if not os.access(cur, os.F_OK):
        os.mkdir(cur)

    while 1:
        try:
            bSDNormal = os.access(dest, os.F_OK)
            dirs = os.listdir(cur)
            if len(dirs) > maxlog:
                dirs.sort(compare_log)
                for i in range(len(dirs) - maxlog):
                    if os.name == "nt":
                        logs = cur + "\\" + dirs[i + maxlog]
                        dlogs = dest + "\\" + dirs[i + maxlog]
                    else:
                        logs = cur + "/" + dirs[i + maxlog]
                        dlogs = dest + "/" + dirs[i + maxlog]
                        
                    #print("{0}-{1}".format(logs, dlogs))
                    try:
                        if bSDNormal and (not os.path.exists(dlogs)):
                            shutil.move(logs, dest)
                        else:
                            os.remove(logs)
                    except Exception as e:
                        pass

                    time.sleep(0.5)
                    continue

        except Exception as e:
            print e
            pass

        time.sleep(tick)

if __name__ == "__main__":
    log_backup(DEST_DIR, CUR_DIR, tdelay)

