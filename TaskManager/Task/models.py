#!/usr/env python
# -*- coding: UTF-8 -*-
"""
    create by zhoupan on 2016/11/10 08:38:09
"""

from django.db import models


# Create your models here.
class user():
    name = models.CharField(max_length=20, unique=True)  # 用户名，昵称
    passwd = models.CharField(max_length=20)  # 用户登陆密码
    score = models.IntegerField()  # 用户积分


class task():
    title = models.CharField(max_length=30)  # 任务标题
    context = models.TextField()  # 任务概述
    start = models.TimeField()  # 任务开始时间
    end = models.DateField()  # 任务截止时间
    level = models.IntegerField()  # 任务等级（难度，分为三级（初，中，高）
    score = models.IntegerField()  # 积分

    def __unicode__(self):
        return self.title

    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def getTaskById(self):
        pass


class message():
    pass
