"""DjangoLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin

from DjangoLearn.view import *
from books import views

urlpatterns = [
    url(r'^$', index), url(r'^hello/$', hello), url(r'^time/(\d{1,2})/$', hour_ahead), url(r'^temp/$', temp_time),
    url(r'^simple/$', temp_simp),
    url(r'^local_test/$', local_test), url(r'^my/$', my),
    url(r'^admin/', include(admin.site.urls)), url(r'^search-form/$', views.search_form),url(r'^search/$',views.search),
    url('^contact/$',views.contact)
]
