#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os 

def dumpFolder(output, folder):
    files = os.listdir(folder)
    count = 0
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg"):
            f.write("{0}/{1}\n".format(folder,file))
            count += 1
    print "{0} files in {1}/".format(count, folder)
    return count
    
try:
    f = open("neg.txt", 'w')
    count = 0
    count += dumpFolder(f, 'neg/0_fisrt_stage')
    count += dumpFolder(f, 'neg/1_early_stage')
    count += dumpFolder(f, 'neg/neg3')
    count += dumpFolder(f, 'neg/neg4')
    count += dumpFolder(f, 'neg/neg5')
    count += dumpFolder(f, 'neg/neg6')
    count += dumpFolder(f, 'neg')
    f.close()
    print "{0} files".format(count)
except IOError:
    print "cannot be opened neg.txt"
