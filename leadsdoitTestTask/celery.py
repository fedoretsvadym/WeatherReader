import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leadsdoitTestTask.settings')

app = Celery('leadsdoitTestTask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'fetch-weather-every-minute': {
        'task': 'app.tasks.pull_weather',
        'schedule': crontab(minute="0"),
    },
}
