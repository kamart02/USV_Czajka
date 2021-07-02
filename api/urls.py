"""webinterface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from . import views

router1 = routers.DefaultRouter()
router1.register(r'', views.SpeedControllViewSet)

router2 = routers.DefaultRouter()
router2.register(r'', views.DataViewSet)

router3 = routers.DefaultRouter()
router3.register(r'', views.MapDataViewSet)

router4 = routers.DefaultRouter()
router4.register(r'', views.WaypointViewSet)

router5 = routers.DefaultRouter()
router5.register(r'', views.StatusViewSet)

urlpatterns = [
    path('speedN/', views.SpeedGet),
    path('speed/', include(router1.urls)),
    path('data/', include(router2.urls)),
    path('dataN/', views.dataGet),
    path('rmAll/', views.rmAll),
    path('mapdata/', include(router3.urls)),
    path('mapdataN/', views.mapDataGet),
    path('waypoint/', include(router4.urls)),
    path('waypointN/', views.waypointGet),
    path('status/', include(router5.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
