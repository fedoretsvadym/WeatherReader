from datetime import datetime

from django.conf import settings

from app.models import WeatherState
from app.services.weather import Weather

from leadsdoitTestTask.celery import app


@app.task
def pull_weather():
    print("Start pulling weather data")
    time = datetime.now()
    city = settings.ENV_CITY
    ws = WeatherState.objects.filter(date_time__hour__gte=time.hour,
                                     date_time__hour__lt=time.hour + 1)  # checking if there are weather states in db
    if not ws:
        weather = Weather()  # Init weather
        data = weather.get_current_weather(city)  # pulling data from api
        if not data:
            # some logs
            print("Error occurred when executed API")
            return
        temperature = data.get("current").get("temp_c")
        WeatherState.objects.create(city=city,
                                    temperature=temperature)
        print("End pulling weather data")
        return

    print("Weather State already exists")
