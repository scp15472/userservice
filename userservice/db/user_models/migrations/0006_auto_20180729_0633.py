# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0005_auto_20180727_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='device_id',
            field=models.CharField(default=datetime.datetime(2018, 7, 29, 6, 33, 4, 964101, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 29, 6, 30, 42, 933553)),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'ea57cea4-aeb8-4e59-8274-77421879c306', max_length=128),
        ),
    ]
