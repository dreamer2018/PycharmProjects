#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Created by zhoupan on 7/22/16.
'''

import threading
from socket import *

from time import ctime

HOST = ''
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
MAXCLINET=3


class MainThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        '''
            做一些类初始化工作
        '''
        threading.Thread.__init__(self)
        threading.threadID = threadID
        threading.name = name
        self.counter = counter

    def run(self):
        '''
            线程开始后，默认会调用此方法
        '''
        #创建一个socket
        TcpMain = socket(AF_INET, SOCK_STREAM)

        #设置端口可以重用，防止程序一场退出后，马上可以恢复
        TcpMain.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        #绑定地址和端口
        TcpMain.bind(ADDR)
        #监听连接
        TcpMain.listen(MAXCLINET)
        while (True):
            print('服务器监听中......')
            tcpClinet, addr = TcpMain.accept()
            thread1=ResponseThread(addr,tcpClinet)
            thread1.start()
            print('Connect from', addr)


class ResponseThread(threading.Thread):
    def __init__(self, addr, tcpClinet):
        '''
            作类初始化工作
        '''
        threading.Thread.__init__(self)
        self.addr = addr
        self.tcpClinet = tcpClinet
    def run(self):
        '''
            线程要做的事
        '''
        print('New process....')
        while True:
            data = self.tcpClinet.recv(BUFSIZE).decode()
            if not data:
                break
            self.tcpClinet.send(('[ %s ] %s ' % (ctime(),data)).encode())
        #退出后关闭连接
        self.tcpClinet.close()
if __name__ == '__main__':
    thread=MainThread(1,'main',1)
    thread.start()