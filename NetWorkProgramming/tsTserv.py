#!/usr/bin/env python
#coding=utf-8
##
# Create By zhoupan On 7/17/16
##
from socket import *
from time import ctime

HOST=''
PORT=8080
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(3)

while True:
    print('服务器监听中......')
    tcpCliSock,addr = tcpSerSock.accept()
    print('connect from ',addr)
    while Tru
        data=tcpCliSock.recv(BUFSIZE).decode()
        if not data:
            break
        print(data)
        tcpCliSock.send(('[%s] %s' % (ctime(),data)).encode())
    tcpCliSock.close()
tcpSerSock.close()
