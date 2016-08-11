# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160811_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date1',
            field=models.DateTimeField(),
        ),
    ]
