# serializers.py

from rest_framework import serializers

from .models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id','name', 'alias')