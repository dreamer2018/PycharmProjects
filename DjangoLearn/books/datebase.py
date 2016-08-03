#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""
    Created by zhoupan on 8/3/16.
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoLearn.settings")

from books.models import Publisher
# p1 = Publisher(name='Apress',address='西安市长安区',city='西安市',state_province='陕西省',country='中国',website='https://www.baidu.com')
# p1.save()
# p2 = Publisher(name='OReilly',address='北京市朝阳区',city='北京',state_province='北京',country='中国',website='https://www.qq.com')
# p2.save()
publish_list = Publisher.objects.all()
print(publish_list)

