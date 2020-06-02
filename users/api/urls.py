from django.urls import path, include
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    )

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='apiregister'),
    path('', include('rest_framework.urls', namespace='rest_framework'))	
]