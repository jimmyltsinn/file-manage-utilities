#!/usr/local/bin/python2

import sys
import os
import subprocess
import re

for f in os.listdir('.'):
    fn = re.split('\[|\]|\(|\)', f)
    if (len(fn) < 3):
        continue
    if (len(fn[-1]) > 5):
        continue
    if (fn[-1] == '.ass'):
        continue
    crcProc = subprocess.Popen(['crc32', f], stdout=subprocess.PIPE)
    (crc32,err)  = crcProc.communicate()
    crc32 = crc32.rstrip()
    if (fn[-2][-8:] != crc32.upper()):
        print '!!!! [%s != %s] %s'%(crc32.upper(), fn[-2], f)
    else:
        print 'OK [%s = %s] %s'%(crc32.upper(), fn[-2][-8:], f)
