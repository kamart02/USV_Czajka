
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('speed/', include(router1.urls)),
    path('data/', include(router2.urls)),
    path('mapdata/', include(router3.urls)),
    path('waypoint/', include(router4.urls)),
    path('status/', include(router5.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
