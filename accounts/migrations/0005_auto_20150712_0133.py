# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150711_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='confederation',
            name='country',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='federation',
            name='state',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.CharField(default='ATL', max_length=3, choices=[(b'ATL', b'ATHLETE'), (b'INS', b'INSTRUCTOR'), (b'REF', b'REFEREE'), (b'COA', b'COACH'), (b'BOA', b'BOARD MEMBER'), (b'DEL', b'DELEGATE'), (b'JUD', b'JUDGE'), (b'DIR', b'DIRECTOR')]),
            preserve_default=False,
        ),
    ]
