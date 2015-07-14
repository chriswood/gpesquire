# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpesq', '0002_auto_20150711_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
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
            },
            bases=(models.Model,),
        ),
    ]
