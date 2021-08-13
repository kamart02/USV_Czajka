from re import L
import re
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework import response
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

class PingViewSet(viewsets.ModelViewSet):
    queryset = models.Ping.objects.all().order_by('id')
    serializer_class = serializers.PingSerializer

@api_view(['GET','POST', 'PUT'])
def SpeedGet(request):
    if request.method=="GET":
        if models.SpeedControll.objects.exists():
            speed = models.SpeedControll.objects.last()
            serializer = serializers.SpeedSerializer([speed], many=True)
        else:
            speed = models.SpeedControll(rightSpeed = 0, leftSpeed = 0)
            speed.save()
            serializer = serializers.SpeedSerializer([speed], many=True)
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
        if models.SpeedControll.objects.exists():
            speed = models.SpeedControll.objects.last()
        else:
            speed = models.SpeedControll(rightSpeed = 0, leftSpeed = 0)
        serializer = serializers.SpeedSerializer(speed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def dataGet(request):
    if request.method=="POST":
        serializer=serializers.DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=="GET":
        serializer=serializers.DataSerializer([models.Data.objects.last()], many=True)
        return Response(data=serializer.data)

@api_view(['GET','POST'])
def mapDataGet(request):
    if request.method=="POST":
        serializer=serializers.MapDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        if request.data['all']:
            print(models.MapData.objects.all())
            serializer = serializers.MapDataSerializer(models.MapData.objects.all(), many=True)
        else:
            serializer = serializers.MapDataSerializer(models.MapData.objects.last())
        return Response(serializer.data)

@api_view(['DELETE'])
def rmAll(request):
    if request.method=='DELETE':
        objects1=models.Data.objects.all()
        objects1.delete()
        objects2=models.MapData.objects.all()
        objects2.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET','POST', 'DELETE'])
def waypointGet(request):
    if request.method=='POST':
        serializer=serializers.WaypointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        if request.data['all']:
            waypoint = models.Waypoint.objects.all()
            serializer = serializers.WaypointSerializer(waypoint, many=True)
            return Response(serializer.data)
        else:
            waypoint = models.Waypoint.objects.first()
            serializer = serializers.WaypointSerializer(waypoint)
            return Response(serializer.data)
    if request.method=='DELETE':
        if request.data['all']:
            waypoint = models.Waypoint.objects.all()
            waypoint.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            if models.Waypoint.objects.exists():
                waypoint = models.Waypoint.objects.first()
                waypoint.delete()
            return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
def pingGet(request):
    if request.method == 'PUT':
        if models.Ping.objects.exists():
            ping = models.Ping.objects.last()
        else:
            ping = models.Ping(checked = True)
        serializer = serializers.PingSerializer(ping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        ping = models.Ping.objects.first()
        serializer = serializers.PingSerializer(ping)
        return Response(serializer.data)