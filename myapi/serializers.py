from rest_framework import serializers

from .models import sensor

class sensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sensor
        fields = ('id', 'temp', 'ic', 'dist')
