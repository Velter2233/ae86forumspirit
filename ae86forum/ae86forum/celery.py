# Celery is optional, Huey can be used instead
# Read the Celery docs to configure it
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ae86forum.settings.dev")
app = Celery("ae86forum")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
