#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/18/16.

from twisted.internet import protocol,reactor
from time import ctime

PORT=8000

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt=self.clnt=self.transport.getPeer().host
        print('connect from ',clnt)
    def dataReceived(self, data):
        self.transport.write(('[%s] %s' % (ctime(),data.decode())).encode())
factory = protocol.Factory()
factory.protocol=TSServProtocol
print('服务器运行中......')
reactor.listenTCP(PORT,factory)
reactor.run()