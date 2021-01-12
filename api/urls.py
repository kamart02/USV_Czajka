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
router1.register(r'speed', views.SpeedControllViewSet)

router2 = routers.DefaultRouter()
router2.register(r'data', views.DataViewSet)

urlpatterns = [
    path('speed/', include(router1.urls)),
    path('data/', include(router2.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
