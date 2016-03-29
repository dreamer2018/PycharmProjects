#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupan'
#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    #return HttpResponse("Hello World!")
    conext={}
    conext['hello']='Hello World!'
    return render(request,'hello.html',conext)
