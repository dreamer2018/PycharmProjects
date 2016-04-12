#!/usr/bin/env python
#coding=utf-8

'''
#第一题：
__author__ = 'zhoupan'
print repr(u'中国')

#第二题：
#通过lambda函数实现两个数相乘
multiply = lambda a,b : a*b
a=10
b=20
print multiply(a,b)

#第三题：
import xlwt

workbook=xlwt.Workbook(encoding='utf-8')
booksheet=workbook.add_sheet('student')

Data=(("1","张三",150,120,100),("2","李四",90,99,95),("3","王五",60,66,68))

for i,row in enumerate(Data):
    for j,col in enumerate(row):
        booksheet.write(i,j,col)

workbook.save('student.xls')

#第四题：
def deco(func):
    if func.__doc__ == None :
        print func.__name__,'not doc'
    else:
        print func.__name__,'doc is:',func.__doc__
    return func
@deco
def func1():
    'a test function'
    print 'func1 was executed'
@deco
def func2():
    print 'func2 was executed'
func1()
func2()



if 1 in [1,0] == True:
    print 'a'
else:
    print 'b'

#第五题
import redis
import random
r=redis.Redis(host='localhost',port=6379,db=0)
for i in range(0,100):
    r.lpush(random,random.random())
print r.lrange(random,0,100)

#第六题

print 1 in [0,1] == True #false
print (1 in [0,1]) == True #true


#第七题
import svn

#第八题
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,20)
plt.plot(x,x*x*x)
plt.show()
'''

import re
import urllib
#coding=utf-8

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def gettitle(html):
    #reg = r'class="explore-feed feed-item" data-offset="[0-9]*"><h2><a class="question_link" target="_black" href="[a-z0-9]*">?</a><h2>'
    #reg = r'class="explore-feed feed-item" data-offset="[0-9]*">'
    reg=r'class="question_link" target="_blank" href="\S*">\S*'
    list = re.compile(reg)
    list_all= re.findall(list,html)
    print list_all
html = getHtml("https://www.zhihu.com/explore")

print gettitle(html)
