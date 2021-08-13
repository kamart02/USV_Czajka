from rest_framework import serializers

from . import models

class SpeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SpeedControll
        fields = ('rightSpeed', 'leftSpeed', 'id')

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Data
        fields = ('ph', 'turbility','temperature', 'latitude', 'longitude','voltage', 'time', 'id')

class MapDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MapData
        fields = ('ph', 'turbility','temperature', 'latitude', 'longitude', 'time', 'id')

class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Waypoint
        fields = ('latitude', 'longitude','id')

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Status
        fields = ('abort', 'automation', 'delMapData', 'delData', 'time', 'id')

class PingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Ping
        fields = ('checked', 'time')