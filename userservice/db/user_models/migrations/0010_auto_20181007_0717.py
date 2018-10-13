# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0009_auto_20180831_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 7, 7, 17, 19, 635713)),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'72641004-cd33-4e34-8995-f474c0981d76', max_length=128),
        ),
    ]
