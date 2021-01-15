from rest_framework import serializers

from . import models

class SpeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SpeedControll
        fields = ('rightSpeed', 'leftSpeed', 'id')

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Data
        fields = ('ph', 'turbility','temperature', 'latitude', 'longitude', 'time', 'id')

class MapDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MapData
        fields = ('ph', 'turbility','temperature', 'latitude', 'longitude', 'time', 'id')

class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Waypoint
        fields = ('latitude', 'longitude','id')

class AbortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Abort
        fields = ('abort', 'time', 'id')