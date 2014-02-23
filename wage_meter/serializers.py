from rest_framework import serializers
from wage_meter.models import Island,Technology

__author__ = 'soroosh'


class IslandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Island
        fields = ('id','name', 'description')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id','name', 'description')
