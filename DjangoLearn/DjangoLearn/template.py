#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
    Created by zhoupan on 7/26/16.
'''

import os
import sys
from django.template import Template,Context


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoLearn.settings")
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)

class PersonClass1:
    def name(self):
        raise (AssertionError,"foo")

class AsserClass(AssertionError):
        silent_variable_failure = True

class PersonClass2:
    def name(self):
        raise(AsserClass)
if __name__ == "__main__":
    print('--------------------------------------------------------------------')
    temp = "my name is {{ name }} ,I am {{ age }} years old."
    t = Template(temp)
    c = Context({'name': 'ZhouPan', 'age': 20})
    print(t.render(c))
    print('--------------------------------------------------------------------')
    t = Template('my name is {{ person.name }}.')
    # p = PersonClass1()
    # print(t.render(Context({'person':p})))
    print('--------------------------------------------------------------------')
    p=PersonClass2()
    print( t.render(Context({'person':p})))
    print('--------------------------------------------------------------------')
    c=Context({'1':1,'2':2})
    print(c['1'])
    c['name'] = 'ZhouPan'
    print(c['name'])
    print('--------------------------------------------------------------------')
    t="my name is {{ name }},I am a {% if sex %} boy {% else %} girl {% endif %}"
