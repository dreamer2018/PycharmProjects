#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/18/16.

from socket import *

HOST='localhost'
PORT=8080
BUFSIZE=1024
ADDR=(HOST,PORT)

while True:
    tcpCliSock=socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('请输入：')
    if not data:
        break
    tcpCliSock.send(("%s\n" % data).encode())
    data = tcpCliSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()