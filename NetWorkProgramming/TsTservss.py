#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/18/16.
from socketserver import TCPServer,StreamRequestHandler
from time import ctime

HOST=''
PORT=8080
BUFSIZE=1024
ADDR=(HOST,PORT)

class MyRequestHandle(StreamRequestHandler):
    def handle(self):
        print('....connect from ',self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(),self.rfile.readline())).encode())

tcpServ=TCPServer(ADDR,MyRequestHandle)
print('服务器运行中......')
tcpServ.serve_forever()