from django.db import models

class SpeedControll(models.Model):
    rightSpeed = models.IntegerField()
    leftSpeed = models.IntegerField()

class Data(models.Model):
    ph = models.DecimalField(max_digits=10 ,decimal_places=5,default=0)
    turbility = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    temperature = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    longitude = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    latitude = models.DecimalField(max_digits=10,decimal_places=5, default=0)
    time = models.DateTimeField('time', auto_now=True)