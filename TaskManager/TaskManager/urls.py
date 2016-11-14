"""TaskManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Task.views import login, login_verify, index, all_task, add_task, my_create, my_follow

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
Task = [
    url(r'^$', index),
    url(r'^login/$', login),
    url(r'^LoginVerify/$', login_verify),
    url(r'^AllTask/$', all_task),
    url(r'^AddTask/$', add_task),
    url(r'^MyCreate/$', my_create),
    url(r'^MyFollow/$', my_follow),

]
urlpatterns += Task
