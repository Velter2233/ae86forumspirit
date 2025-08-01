# THIS IS FOR DEVELOPMENT ENVIRONMENT
# DO NOT USE IT IN PRODUCTION

# Create your own dev_local.py
# import * this module there and use it like this:
# python manage.py runserver --settings=ae86forum.settings.dev_local

from .base import *

DEBUG = True

TEMPLATES[0]["OPTIONS"]["debug"] = True
# TEMPLATES[0]['OPTIONS']['string_if_invalid'] = '\{\{%s\}\}'  # Some Django templates relies on this being the default

ADMINS = (("John", "john@example.com"),)  # Log email to console when DEBUG = False

SECRET_KEY = "DEV"


ALLOWED_HOSTS = ["ae86forumspirit.onrender.com", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["https://ae86forumspirit.onrender.com"]
CSRF_ALLOWED_ORIGINS = ["https://ae86forumspirit.onrender.com"]
CORS_ORIGINS_WHITELIST = ["https://ae86forumspirit.onrender.com"]

RECAPTCHA_PUBLIC_KEY = '6LdXjWYrAAAAAP5mQ1B7AxtWXxaHWtG-2PUro1fx'
RECAPTCHA_PRIVATE_KEY = '6LdXjWYrAAAAACtD2ESijyUzJPfKt-aXB0nk0G1Y'
RECAPTCHA_REQUIRED_SCORE = 0.75  # Для reCAPTCHA v3 (опционально)



# INSTALLED_APPS.extend([
#    'debug_toolbar',
#    'huey.contrib.djhuey',
# ])

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

CACHES.update(
    {
        "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
        "st_rate_limit": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "spirit_rl_cache",
            "TIMEOUT": None,
        },
    }
)
ST_EXTENDED_FONT = True

LANGUAGE_CODE = 'ru'

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ST_TASK_MANAGER = 'huey'

HUEY = {
    "huey_class": "huey.SqliteHuey",
    "name": "spirit",
    "filename": os.path.join(BASE_DIR, "huey.sqlite3"),
    "immediate_use_memory": False,
    "immediate": False,
    "utc": True,
    "connection": {},
    "consumer": {
        "workers": os.cpu_count() * 2 + 1,
        "worker_type": "thread",
        "initial_delay": 0.1,
        "backoff": 1.15,
        "max_delay": 10.0,
        "scheduler_interval": 1,
        "periodic": True,
        "check_worker_health": True,
        "health_check_interval": 1,
    },
}

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
CELERY_BEAT_SCHEDULE = {
    "notify_weekly": {
        "task": "spirit.core.tasks.notify_weekly",
        "schedule": 3600 * 24 * 7,  # run once every week
        # 'schedule': crontab(hour=0, minute=0, day_of_week='sun')
    },
    "full_search_index_update": {
        "task": "spirit.core.tasks.full_search_index_update",
        "schedule": 3600 * 24,  # run once every 24hs
    },
}

ST_SITE_URL = "http://127.0.0.1:8000/"
