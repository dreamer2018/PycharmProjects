#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/20/16.

import threading
from time import ctime,sleep

secloop=[4,2]

def loop(sign,sec):
    print('loop',sign,'start...',ctime())
    sleep(sec)
    print('loop',sign,'stop...',ctime())
def main():
    print('start...',ctime())
    threads=[]
    for i in range(len(secloop)):
        t=threading.Thread(target=loop,args=(i,secloop[i]))
        threads.append(t)
    for i in range(len(secloop)):
        threads[i].start()
    for i in range(len(secloop)):
        threads[i].join()
    print('stop...',ctime())
if __name__ == '__main__':
    main()