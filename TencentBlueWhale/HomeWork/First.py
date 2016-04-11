#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupan'
print repr(u'中国')


#通过lambda函数实现两个数相乘
multiply = lambda a,b : a*b
a=10
b=20
print multiply(a,b)

import xlwd
file = xlwd.open_workbook('/c/Users/Administrator/PycharmProjects/TencentBlueWhale/HomeWork/')

a[0]=["1","张三",150,120,100]
a[1]=["2","李四",90,99,95]
a[2]=["3","王五",60,66,68]
print a[2][1]

for i in range(0,3):
    for j in range(0,5):
        row=i
        col=j
        # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        if(j<=2):
            type=1
        else:
            type=2
        xf=0
        value=a[i][j]
        file.put_cell(row,col,type,value,xf)
