from django.db import models

class SpeedControll(models.Model):
    rightSpeed = models.IntegerField()
    leftSpeed = models.IntegerField()

class Data(models.Model):
    ph = models.DecimalField(max_digits=10 ,decimal_places=5,default=0)
    turbility = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    temperature = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    latitude = models.DecimalField(max_digits=15,decimal_places=9, default=0)
    longitude = models.DecimalField(max_digits=15,decimal_places=9,default=0)
    voltage = models.DecimalField(max_digits=15,decimal_places=9,default=0)
    time = models.DateTimeField('time', auto_now=True)

class MapData(models.Model):
    ph = models.DecimalField(max_digits=10 ,decimal_places=5,default=0)
    turbility = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    temperature = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    latitude = models.DecimalField(max_digits=15,decimal_places=9, default=0)
    longitude = models.DecimalField(max_digits=15,decimal_places=9,default=0)
    time = models.DateTimeField('time', auto_now=True)

class Waypoint(models.Model):
    latitude = models.DecimalField(max_digits=15,decimal_places=9, default=0)
    longitude = models.DecimalField(max_digits=15,decimal_places=9,default=0)

class Status(models.Model):
    automation = models.BooleanField(default=False)
    abort = models.BooleanField(default=False)
    delMapData = models.BooleanField(default=False)
    delData = models.BooleanField(default=False)
    time = models.DateTimeField('time', auto_now=True)

class Ping(models.Model):
    checked = models.BooleanField(default=False)
    time = models.DateTimeField('time', auto_now=True)