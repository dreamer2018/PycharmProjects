#!/usr/env python
# -*- coding: UTF-8 -*-
"""
    create by zhoupan on 2016/11/10 08:38:09
"""

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 用户名，昵称
    passwd = models.CharField(max_length=20)  # 用户登陆密码
    score = models.IntegerField()  # 用户积分
    mess = models.IntegerField()  # 消息数

    def __unicode__(self):
        return self.name

    def insert(self, name, passwd, score, message):
        user = User()
        user.name = name
        user.passwd = passwd
        user.score = score
        user.message = message
        user.save()

    def deleteById(self, user_id):
        status, user = User().getUserById(user_id)
        if status == False:
            return False, user
        else:
            user.delete()
            return True, "delete %d success!" % user_id

    def update(self, user_id, name, passwd, score, message):
        status, user = User().getUserById(user_id)
        if status == False:
            return False, user
        else:
            user.name = name
            user.passwd = passwd
            user.score = score
            user.message = message
            user.save()
            return True, "update success!"

    def getUserById(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return False, "user id %d does not found!" % user_id
        else:
            return True, user

    def getUserByName(self, user_name):
        user = User.objects.filter(name=user_name)
        if len(user) == 0:
            return False, "user name %s does not found!" % user_name
        else:
            return True, user

    def check_passwd(self, username, password):
        status, user = User().getUserByName(username)
        if status:
            user = user[0]
            print 'user:' + user.name
            if user.passwd == password:
                return True
            else:
                return False
        else:
            return False


class Task(models.Model):
    title = models.CharField(max_length=30)  # 任务标题
    context = models.TextField()  # 任务概述
    user = models.ForeignKey(User)  # 发布者
    start = models.DateTimeField()  # 任务开始时间
    end = models.DateTimeField()  # 任务截止时间
    level = models.IntegerField()  # 任务等级（难度，分为三级（初1，中2，高3）
    score = models.IntegerField()  # 积分
    status = models.IntegerField()  # 任务状态，0为已过期，1为已停用
    follow = models.IntegerField(default=0)  # 任务认领数量

    def __unicode__(self):
        return self.title

    def insert(self, title, context, user, start, end, level, score, status):
        task = Task()
        task.title = title
        task.context = context
        task.user = user
        task.start = start
        task.end = end
        task.level = level
        task.score = score
        task.status = status
        task.save()

    def deleteByID(self, task_id):
        status, task = Task().getTaskById(task_id)
        if status == False:
            return False, task
        else:
            task.delete()
            return True, "delete %d success!" % task_id

    def update(self, task_id, title, context, user, start, end, level, score, status):
        sta, task = Task().getTaskById(task_id)
        if sta == False:
            return False, task
        else:
            task.title = title
            task.context = context
            task.user = user
            task.start = start
            task.end = end
            task.level = level
            task.score = score
            task.status = status
            task.save()

    def getTaskById(self, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return False, "task id %d does not found!" % task_id
        else:
            return True, task

    def addFollow(self, taskid):
        status, task = Task().getTaskById(taskid)
        if status:
            task.follow += 1
            task.save()
            return True
        else:
            return False

    def getTaskByNumber(self, sign=0, number=1):
        if number >= 0:
            if sign == 0:
                tasks = Task.objects.all().order_by('-id')[:number]
            elif sign == 1:
                tasks = Task.objects.all().order_by('-follow')[:number]
            else:
                tasks = Task.objects.all()
            return tasks
        else:
            return None

    def getTaskNumber(self):
        number = Task.objects.count()
        return number


class Book(models.Model):  # 领取任务记录
    task = models.ForeignKey(Task)  # 任务id
    user = models.ForeignKey(User)  # 订购者id
    date = models.DateTimeField()  # 订购日期
    score = models.IntegerField()  # 最终得分，任务发布者决定
    comment = models.TextField()  # 点评的内容
    package = models.CharField(max_length=256)  # 任务提交结果

    def __unicode__(self):
        return self.taskid

    def insert(self, task, user, date, score, comment, package):
        book = Book()
        book.task = task
        book.user = user
        book.date = date
        book.score = score
        book.comment = comment
        book.package = package
        book.save()

    def deleteByID(self, book_id):
        status, book = Book().getBookById(book_id)
        if status == False:
            return False, book
        else:
            book.delete()
            return True, "delete %d success!" % book_id

    def update(self):
        pass

    def getBookById(self, book_id):
        try:
            book = Book.objects.get(book_id)
        except Book.DoesNotExist:
            return False, "book id %d does not found!" % book_id
        else:
            return True, book

    def getBookByUser(self, userid):
        book = Book.objects.filter(user_id=userid)
        return book

    def getBookByTask(self, task):
        book = Book.objects.filter(task)
        return book

    def isBooked(self, userid, taskid):
        book = Book().getBookByUser(userid)
        for b in book:
            if taskid == b.id:
                return True
        return False


class Message(models.Model):
    type = models.IntegerField()  # 消息类型，0 群发，1 某个人
    user = models.ForeignKey(User)  # 如果消息是群发，则忽略这条
    context = models.TextField()  # 消息内容
    date = models.DateTimeField()  # 消息发送日期

    def __unicode__(self):
        return self.type

    def insert(self, type, user, context, date):
        message = Message()
        message.type = type
        message.user = user
        message.context = context
        message.date = date
        message.save()

    def deleteById(self, message_id):
        status, message = Message().getMessageById(message_id)
        if status == False:
            return False, message
        else:
            message.delete()
            return True, "delete message id %d success!" % message_id

    def update(self, message_id, type, user, context, date):
        status, message = Message().getMessageById(message_id)
        if status == False:
            return False, message
        else:
            message.type = type
            message.user = user
            message.context = context
            message.date = date
            message.save()

    def getMessageById(self, message_id):
        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return False, "message id %d does not found!" % message_id
        else:
            return True, message


if __name__ == '__main__':
    print User().check_passwd(1, 1)
