from django.db import models

# Create your models here  ...


class Island(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

    def json_format(self):
        temp = '{{ "id" : "{0}" , "name" : "{1}" , "description" : "{2}" }}'
        return temp.format(self.id,self.name,self.description)

class Technology(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    parent = models.ManyToManyField("self")
    pass
