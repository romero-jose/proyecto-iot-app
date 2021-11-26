from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.utils import serializer_helpers

from measurements.models import Sensor, Measurement
from measurements.serializers import SensorSerializer, MeasurementSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sensors to be viewed or edited
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows measurements to be viewed or edited
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
