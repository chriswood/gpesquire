# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpesq', '0007_auto_20150715_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='plan_id',
        ),
        migrations.AddField(
            model_name='plans',
            name='id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
