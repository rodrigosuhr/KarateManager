# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150710_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 20, 39, 16, 795896, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 20, 39, 30, 588719, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='registration',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
