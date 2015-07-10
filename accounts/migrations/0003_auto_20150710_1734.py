# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from datetime import date


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150710_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'MALE'), (b'F', b'FEMALE')]),
        ),
        migrations.AddField(
            model_name='member',
            name='nick_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='passport',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(default=b'MEM', max_length=3, choices=[(b'SYS', b'SYSADMIN'), (b'MEM', b'MEMBER'), (b'ACA', b'ACADEMY'), (b'FED', b'FEDERATION'), (b'CON', b'CONFEDERATION')]),
        ),
    ]
