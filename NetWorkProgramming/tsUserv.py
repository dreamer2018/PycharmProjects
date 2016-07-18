#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/18/16.

from socket import *
from time import ctime

HOST=''
PORT=8000
BUFSIZE=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('服务器运行中......')
    data,addr=udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto(('[%s]%s' % (ctime(),data)).encode(),addr)
    print('...received from ',addr)
udpSerSock.close()

