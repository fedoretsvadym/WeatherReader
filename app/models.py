from django.db import models


class WeatherState(models.Model):
    temperature = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
