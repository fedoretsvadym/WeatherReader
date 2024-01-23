from datetime import datetime

from rest_framework import serializers

from app.models import WeatherState


class TemperatureDayStatisticSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return datetime.strftime(obj.date_time, "%H:%M:%S")

    class Meta:
        model = WeatherState
        fields = ('time', 'temperature')
