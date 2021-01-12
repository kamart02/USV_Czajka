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