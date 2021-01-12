from django.shortcuts import render
from rest_framework import viewsets

from . import serializers
from . import models

class SpeedControllViewSet(viewsets.ModelViewSet):
    queryset = models.SpeedControll.objects.all()
    serializer_class = serializers.SpeedSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = models.Data.objects.all()
    serializer_class = serializers.DataSerializer