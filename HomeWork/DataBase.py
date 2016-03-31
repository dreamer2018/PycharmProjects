#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupan'

import MySQLdb
try:
    connect=MySQLdb.connect(host="localhost",user="root",passwd="zhoupan")
    connect.select_db('zhoupan')
    cur=connect.cursor()
    cur.execute("create table test ( id int primary key auto_increment, name varchar(20) not null , age tinyint default 0,sex boolean default true);")

    cur.close()
    connect.close()
except MySQLdb.Error,e:
    print "mysql Error %d:%s" % (e.args[0],e.args[1])
