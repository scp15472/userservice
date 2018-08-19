# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0002_auto_20180727_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 9, 31, 47, 433436)),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'7e7cb12a-d2ce-4cad-b96a-f295e3da47bf', max_length=128),
        ),
    ]
