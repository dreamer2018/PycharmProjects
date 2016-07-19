#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/19/16.
from twisted.internet import protocol,reactor

HOST='localhost'
PORT=8000
class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data=input('请输入:')
        if data:
            self.transport.write(data.encode())
        else:
            self.transport.lostConnection()
    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        print(data.decode())
        self.sendData()
class TSClntFactory(protocol.ClientFactory):
    protocol=TSClntProtocol
    clientConnectionLost=clientConnectionFaild=lambda self,connector,reason:reactor.stop()
reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()