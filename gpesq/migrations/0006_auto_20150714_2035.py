# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gpesq', '0005_auto_20150714_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='points',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=True,
        ),
    ]
