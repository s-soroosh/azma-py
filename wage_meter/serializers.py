from rest_framework import serializers
from wage_meter.models import Island

__author__ = 'soroosh'


class IslandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Island
        fields = ('id','name', 'description')
