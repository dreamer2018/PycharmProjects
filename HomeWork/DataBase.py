#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupan'

import MySQLdb
try:
    connect=MySQLdb.connect(host="localhost",user="root",passwd="zhoupan")
    connect.select_db('zhoupan')
    cur=connect.cursor()
    cur.execute('show tables;')
    result=cur.fetchall()
    for i in result:
        print i
    cur.close()
    connect.close()
except MySQLdb.Error,e:
    print "mysql Error %d:%s" % (e.args[0],e.args[1])
