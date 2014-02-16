from django.core import serializers
from django.db import models

# Create your models here  ...

class Island(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

    def json_format(self):
        temp = '{{ "id" : "{0}" , "name" : "{1}" , "description" : "{2}" }}'
        return temp.format(self.id, self.name, self.description)

    # def toJSON(self):
    #     fields = []
    #     for field in self._meta.fields:
    #         fields.append(field.name)
    #
    #     d = {}
    #     for attr in fields:
    #         d[attr] = getattr(self, attr)
    #
    #     import simplejson
    #
    #     return simplejson.dumps(d)


class Technology(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    parent = models.ManyToManyField("self")
    island = models.ForeignKey(Island)

    # #this is a very nice example of CopyPaste Design Pattern
    # #in this way i am sure i will repeat myself much more times
    # #unless i learn to write a general json serializer
    def json_format(self):
        jserializer = serializers.serialize('json', [self], fields=('name', 'description'))
        print(jserializer)
        return jserializer

        # temp = '{{ "id" : "{0}" , "name" : "{1}" , "description" : "{2}"}}'
        # return temp.format(self.id, self.name, self.description)

    # def toJSON(self):
    #     fields = []
    #     for field in self._meta.fields:
    #         fields.append(field.name)
    #
    #     d = {}
    #     for attr in fields:
    #         d[attr] = getattr(self, attr)
    #
    #     import simplejson
    #
    #     return simplejson.dumps(d)

    pass
