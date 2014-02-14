from django.db import models

# Create your models here  ...


class Island(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    pass

class Technology(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    parent = models.ManyToManyField('self')
    pass
