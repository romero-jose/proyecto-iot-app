from django.db.models import fields
from rest_framework import serializers

from measurements.models import Measurement, Sensor


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name']


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'measurement', 'date']
