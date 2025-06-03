import os
from celery import Celery

app = Celery('root')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Konfiguratsiyani django settings.py dan olib kelish # noqa
app.config_from_object('django.conf:settings', namespace='CELERY')

# Avtomatik tasklarni topish # noqa
app.autodiscover_tasks()


@app.task
def divide(x, y):
    import time
    time.sleep(10)
    return x / y

# https://testdriven.io/courses/django-celery/getting-started/