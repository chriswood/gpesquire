from django.db import models
from django.db.models import Model, CharField, EmailField, TextField
from django.db.models import IntegerField, DateTimeField, FloatField, ForeignKey, AutoField
from django.utils import timezone

class Plans(Model):
    date_added = DateTimeField(auto_now_add=True, default=timezone.now)
    description = TextField('description', max_length=1000)

    class Meta:
        db_table = 'plans'

class Points(Model):
    date_added = DateTimeField(auto_now_add=True, default=timezone.now)
    lat = CharField(max_length=12)
    lon = CharField(max_length=12)
    altitude = CharField(blank=True, null=True, max_length=14)
    plan_id = ForeignKey(Plans, related_name='points')
    label = TextField(blank=True, null=True, max_length=40)
    description = TextField(blank=True, null=True)
    meters_error = FloatField(blank=False)

    class Meta:
        db_table = 'points'
