# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpesq', '0006_auto_20150714_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='altitude',
            field=models.CharField(max_length=14, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='points',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='points',
            name='label',
            field=models.TextField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
