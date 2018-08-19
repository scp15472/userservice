# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_time', models.DateTimeField(default=datetime.datetime(2018, 7, 22, 8, 33, 1, 785849))),
                ('token', models.CharField(default=b'8f7d4be5-8554-4360-9818-2ec43e048676', max_length=128)),
                ('logout_time', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('middle_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.ForeignKey(to='user_models.User'),
        ),
    ]
