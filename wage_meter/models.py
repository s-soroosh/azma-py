from django.core import serializers
from django.db import models

class Island(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    ratio = models.FloatField()
    parent = models.ManyToManyField("self", symmetrical=False)
    island = models.ForeignKey(Island)

    def __str__(self):
        return self.name
