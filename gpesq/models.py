from django.db import models
from django.db.models import Model, CharField, EmailField, TextField
from django.db.models import IntegerField, DateTimeField, FloatField, ForeignKey

class Plans(Model):
    plan_id = IntegerField(primary_key=True, db_column='id')
    date_added = DateTimeField(auto_now_add=True)
    description = TextField('description', max_length=1000)

    class Meta:
        db_table = 'plans'

class Point(Model):
    id = IntegerField(primary_key=True)
    date_added = DateTimeField(auto_now_add=True)
    lat = CharField(max_length=12)
    lon = CharField(max_length=12)
    altitude = CharField(blank=True, max_length=14)
    plan_id = ForeignKey(Plans)
    label = TextField(blank=True, max_length=40)
    description = TextField(blank=True)
    meters_error = FloatField(blank=False)
