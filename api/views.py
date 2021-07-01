from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from . import serializers
from . import models

class SpeedControllViewSet(viewsets.ModelViewSet):
    queryset = models.SpeedControll.objects.all()
    serializer_class = serializers.SpeedSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = models.Data.objects.all().order_by('time')
    serializer_class = serializers.DataSerializer

class MapDataViewSet(viewsets.ModelViewSet):
    queryset = models.MapData.objects.all().order_by('time')
    serializer_class = serializers.MapDataSerializer

class WaypointViewSet(viewsets.ModelViewSet):
    queryset = models.Waypoint.objects.all().order_by('id')
    serializer_class = serializers.WaypointSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all().order_by('id')
    serializer_class = serializers.StatusSerializer