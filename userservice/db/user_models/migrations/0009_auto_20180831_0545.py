# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0008_auto_20180729_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 5, 45, 58, 652561)),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'deaf28b9-4ba5-4785-91d3-d9497da283e8', max_length=128),
        ),
    ]
