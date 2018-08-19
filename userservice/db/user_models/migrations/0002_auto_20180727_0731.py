# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('username', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('middle_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 7, 31, 40, 991852)),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'25e76840-745d-4527-9dbb-bbd41d904576', max_length=128),
        ),
        migrations.AlterField(
            model_name='login',
            name='user',
            field=models.ForeignKey(to='user_models.UserData'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
