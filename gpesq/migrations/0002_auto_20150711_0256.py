# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpesq', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plans',
            old_name='plan_date',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='plans',
            name='id',
        ),
        migrations.AlterField(
            model_name='plans',
            name='plan_id',
            field=models.IntegerField(serialize=False, primary_key=True, db_column=b'id'),
            preserve_default=True,
        ),
    ]
