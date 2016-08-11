# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160811_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date1',
            field=models.DateTimeField(verbose_name='YYYY-MM-DD'),
        ),
    ]
