#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect

from mymako import render_mako_context
from Task.models import *


# Create your views here.
def login(request):
    request.session['userid'] = 0
    return render_mako_context(request, 'login.html', {'message': ''})


def login_verify(request):
    username = request.POST['username']
    password = request.POST['password']
    if len(username) == 0 or username == '' or len(username.strip()) == 0:
        message = u"用户名或密码不能为空"
        return render_mako_context(request, 'login.html', {'message': message})
    elif len(password) == 0 or password == '' or len(password.strip()) == 0:
        message = u"用户名或密码不能为空"
        return render_mako_context(request, 'login.html', {'message': message})
    else:
        status = User().check_passwd(username, password)
        print status
        if not status:
            message = u"用户名或密码错误！"
            return render_mako_context(request, 'login.html', {'message': message})
        else:
            user = User().getUserByName(username)[1][0]
            request.session['userid'] = user.id
            return HttpResponseRedirect('/')


def index(request):
    if request.session['userid'] <= 0:
        return HttpResponseRedirect('/login/')
    userid = request.session['userid']
    user = User().getUserById(userid)[1]
    new = Task().getTaskByNumber(number=10)
    hot = Task().getTaskByNumber(sign=1, number=10)
    return render_mako_context(request, 'index.html', {'users': user, 'new': new, 'hot': hot})


def all_task(request):
    if request.session['userid'] <= 0:
        return HttpResponseRedirect('/login/')
    userid = request.session['userid']
    user = User().getUserById(userid)
    tasks = Task().getTaskByNumber(sign=2)
    return render_mako_context(request, 'alltask.html', {'users': user, 'tasks': tasks})


def add_task(request):
    return render_mako_context(request, 'addtask.html', {'test': 'test'})


def my_create(request):
    return render_mako_context(request, 'mycreate.html', {'test': 'test'})


def my_follow(request):
    return render_mako_context(request, 'myfollow.html', {'test': 'test'})
