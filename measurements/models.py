from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    measurement = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
