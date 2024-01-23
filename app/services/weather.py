from django.conf import settings
import requests


class Weather:
    def __init__(self):
        self.token = settings.WEATHER_API_TOKEN

    def get_current_weather(self, city: str):
        payload = {"key": self.token, "q": city}
        r = requests.get(f"{settings.WEATHER_API_ENDPOINT}/current.json", params=payload)
        if r.status_code != 200:
            # place for logging
            print("some errors")
            return None
        return r.json()
