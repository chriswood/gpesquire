# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gpesq', '0004_auto_20150714_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='points',
            name='plan_id',
            field=models.ForeignKey(related_name='points', to='gpesq.Plans'),
            preserve_default=True,
        ),
    ]
