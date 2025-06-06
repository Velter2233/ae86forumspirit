import logging
import os

from django.core.wsgi import get_wsgi_application

logging.captureWarnings(True)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ae86forum.settings.dev")

application = get_wsgi_application()
