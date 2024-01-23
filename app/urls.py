from django.urls import path

from app.views import TemperatureView

urlpatterns = [
    path('temperature/', TemperatureView.as_view()),
]
