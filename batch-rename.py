#!/usr/local/bin/python2
# coding=utf8

import os
import glob

fmt_str = '[][%02d][%s]'
ori_search_fmt = '[%02d]'
ext = 'ass'
search_range = [0, 25] # Inclusive
fn = {
}

ls = os.listdir('.')

rename_list = []

for i in xrange(search_range[0], search_range[1] + 1):
    match = []
    for f in ls:
        if ((ori_search_fmt%(i)) in f and f[-len(ext):] == ext):
            match.append(f)
    if (len(match) > 1):
        print "Multiple entry for %03d. Skipping this! (%s)"%(i, match)
        continue
    if (len(match) == 0):
        print "Unfound for %03d"%(i)
        continue
    rename_list.append((match[0], '%s.%s'%(fmt_str%(i, fn[i]), ext)))

for p in rename_list:
    print "%s => %s"%(p[0], p[1])

i = raw_input("Continue? [y/N] ")

if (i == 'y' or i == 'Y'):
    for p in rename_list:
        print 'Moving %s => %s'%(p[0], p[1])
        os.rename(p[0], p[1])
