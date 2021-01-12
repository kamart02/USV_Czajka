from django.db import models

class SpeedControll(models.Model):
    rightSpeed = models.IntegerField()
    leftSpeed = models.IntegerField()

class Data(models.Model):
    ph = models.IntegerField()
    turbility = models.IntegerField()
    temperature = models.IntegerField()