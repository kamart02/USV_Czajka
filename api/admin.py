from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.SpeedControll)
admin.site.register(models.Data)
admin.site.register(models.MapData)
admin.site.register(models.Waypoint)