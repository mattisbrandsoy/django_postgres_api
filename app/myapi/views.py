# views.py

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import LocationSerializer
from .models import Location

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer