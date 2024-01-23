from datetime import datetime

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from app.models import WeatherState
from app.serializers import TemperatureDayStatisticSerializer


class TemperatureView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        # checking token
        x_token = request.headers.get('x-token')
        if x_token is None:
            return Response({"status": 0,
                             "error": "No x_token found in headers"}, status=status.HTTP_400_BAD_REQUEST)
        if x_token != settings.X_TOKEN:
            return Response({"status": 0,
                             "error": "x_token is not valid"}, status=status.HTTP_401_UNAUTHORIZED)

        # checking day
        day = request.GET.get("day")
        if day is None:
            return Response({"status": 0,
                             "error": "No day found in params"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            parsed_date = datetime.strptime(day, "%Y-%m-%d")
        except Exception:
            return Response({"status": 0,
                             "error": "Wrong day format, provide it in format '%Y-%m-d'"},
                            status=status.HTTP_400_BAD_REQUEST)

        city = settings.ENV_CITY

        # fetching temperature with appropriate date and city equals to written in .env
        temperature_day_data = WeatherState.objects.filter(date_time__day=parsed_date.day,
                                                           date_time__month=parsed_date.month,
                                                           date_time__year=parsed_date.year,
                                                           city=city)

        return Response({"status": 1,
                         "city": city,
                         "day": day,
                         "temperatures": TemperatureDayStatisticSerializer(temperature_day_data, many=True).data})
