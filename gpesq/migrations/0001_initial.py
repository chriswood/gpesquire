# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_id', models.IntegerField()),
                ('plan_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=1000, verbose_name=b'description')),
            ],
            options={
                'db_table': 'plans',
            },
            bases=(models.Model,),
        ),
    ]
