#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupan'
def Argv(list):
    s=0
    for i in range(1,len(list)-1,1):
        s+=list[i]
    return s/(len(list)-2)
if __name__ == '__main__':
    student_grades = [66,77,88,99,100]
    result=Argv(student_grades)
    print result