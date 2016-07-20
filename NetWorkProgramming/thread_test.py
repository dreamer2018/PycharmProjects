#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/20/16.
from time import ctime,sleep
import thread

def loop1():
    print 'loop1 start...at',ctime()
    sleep(4)
    print 'loop1 stop...at',ctime()
def loop2():
    print 'loop2 start...',ctime()
    sleep(2)
    print 'loop2 stop...',ctime()
def main():
    print 'start...', ctime()
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    sleep(6)
    print ('stop...', ctime())
if __name__ == '__main__':
    main()
