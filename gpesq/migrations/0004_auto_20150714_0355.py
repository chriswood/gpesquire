# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpesq', '0003_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('lat', models.CharField(max_length=12)),
                ('lon', models.CharField(max_length=12)),
                ('altitude', models.CharField(max_length=14, blank=True)),
                ('label', models.TextField(max_length=40, blank=True)),
                ('description', models.TextField(blank=True)),
                ('meters_error', models.FloatField()),
                ('plan_id', models.ForeignKey(to='gpesq.Plans')),
            ],
            options={
                'db_table': 'points',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='point',
            name='plan_id',
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]
