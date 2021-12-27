from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import sensorSerializer
from .models import sensor


class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all().order_by('dist')
    serializer_class = sensorSerializer
