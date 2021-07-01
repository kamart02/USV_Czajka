from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers
from rest_framework.response import Response

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

@api_view(['GET','POST', 'PUT'])
def SpeedGet(request):
    if request.method=="GET":
        speed = models.SpeedControll.objects.last()
        serializer = serializers.SpeedSerializer(speed)
        return Response(serializer.data)
    if request.method=="POST":
        serializer = serializers.SpeedSerializer(data=request.data)
        if serializer.is_valid():
            test = models.SpeedControll.objects.all()
            for obj in test:
                obj.delete()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PUT':
        try:
            speed = models.SpeedControll.objects.last()
        except models.SpeedControll.DoesNotExist:
            speed = models.SpeedControll(rightSpeed = 0, leftSpeed = 0)
        serializer = serializers.SpeedSerializer(speed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

