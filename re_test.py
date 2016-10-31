# -*- coding = utf8 -*-
# for python2.7.9

import os, re, datetime

file_name = 'output_1983.06.10.data'
if os.path.exists(file_name) == False:
    print('{0} not exist!'.format(file_name))
    f = open(file_name, 'w')

try:
    m = re.search('output_(?P<year>\d{4})\.(?P<mon>\d{2})\.(?P<day>\d{2})\.', file_name)
    print('search group[0] is {0}'.format(m.group(0)))

    year = m.group('year')
    mon  = m.group('mon')
    day  = m.group('day')
except:
    year = '2012'
    mon  = '12'
    day  = '12'

date = datetime.date(int(year), int(mon), int(day))
week = date.weekday() + 1

file_other = 'output_{0}-{1}-{2}-{3}.data'.format(year, mon, day, week)
print('file_other is {0}'.format(file_other))

if os.path.exists(file_other) == False:
    os.rename(file_name, file_other)

if f:
    print("close file")
    f.close()
    os.remove(file_other)
    
    
