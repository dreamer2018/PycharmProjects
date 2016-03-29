#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupan'
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")
