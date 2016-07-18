#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/18/16.

from socket import *

HOST='localhost'
PORT=8000
BUFSIZE=1024
ADDR=(HOST,PORT)

udpCliSock=socket(AF_INET,SOCK_DGRAM)
while True:
    data=input('请输入：')
    if not data:
        break
    udpCliSock.sendto(data.encode(),ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    data=data.decode()
    print(data)
udpCliSock.close()

