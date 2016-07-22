#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
    Created by zhoupan on 7/22/16.
'''
from socket import *
from time import  ctime
import threading

PORT=8000
HOST='localhost'
ADDR=(HOST,PORT)
BUFSIZE=1024

class Clinet(threading.Thread):
    def __init__(self,threadID,threadName):
        threading.Thread.__init__(self)
        threading.threadID=threadID
        threading.name=threadName
    def run(self):
        tcpClinet=socket(AF_INET,SOCK_STREAM)
        tcpClinet.connect(ADDR)
        while True:
            data=input('请输入：')
            tcpClinet.send(data.encode())
            data=tcpClinet.recv(BUFSIZE).decode()
            if not data:
                break
            print(data)
        tcpClinet.close()
if __name__ == '__main__':
    thread=Clinet(1,'first')
    thread.start()


