#!/usr/bin/env python
#coding=utf-8

#  Created by zhoupan on 7/17/16.

from socket import *

HOST='localhost'
PORT=8000
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data=input('请输入：')
    tcpCliSock.send(data.encode())
    data=tcpCliSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()