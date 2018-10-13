# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0011_auto_20181007_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 7, 8, 47, 17, 384994)),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'86065256-6744-4610-94ed-87a0d6a8ff09', max_length=128),
        ),
    ]
