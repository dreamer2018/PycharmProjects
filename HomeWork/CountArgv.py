#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupan'
#去除第一个和最后一个在个，并计算平均值在一个函数里面

#######一般########
def Argv(list):
    s=0
    for i in range(1,len(list)-1,1):
        s+=list[i]
    return s/(len(list)-2)
###########进阶级############
def avg(list):
    s=0
    for i in range(len(list)):
        s+=list[i]
    return s/(i+1)

def drop_first_last(list):
    first,*middle,last=list
    print(type(list))
    return avg(middle)

if __name__ == '__main__':
    student_grades = [66,77,88,99,100]
    #result=Argv(student_grades)
    result=drop_first_last(student_grades)
    print(result)