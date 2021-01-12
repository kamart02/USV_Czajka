from rest_framework import serializers

from . import models

class SpeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SpeedControll
        fields = ('rightSpeed', 'leftSpeed')

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Data
        fields = ('ph', 'turbility','temperature')