# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0010_auto_20181007_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 7, 8, 2, 23, 999772)),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'b0c01ae8-b266-46cb-a616-47c2cfea5848', max_length=128),
        ),
    ]
