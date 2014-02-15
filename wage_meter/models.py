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
    island = models.ForeignKey(Island)

      # #this is a very nice example of CopyPaste Design Pattern
      # #in this way i am sure i will repeat myself much more times
      # #unless i learn to write a general json serializer
    def json_format(self):
        temp = '{{ "id" : "{0}" , "name" : "{1}" , "description" : "{2}"}}'
        return temp.format(self.id,self.name,self.description)
    pass
