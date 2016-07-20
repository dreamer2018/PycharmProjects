#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/20/16.

import threading
from time import ctime,sleep

loops=[4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=""):
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
        apply(self.func,self.args)
def loop(nloop,sec):
    print('loop',nloop,'start at',ctime())
    sleep(sec)
    print('loop',nloop,'',ctime())
def main():
    print('start at:',ctime())
    threads=[]
