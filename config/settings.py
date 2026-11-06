SECRET_KEY = "django-insecure-local-training-project"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

ROOT_URLCONF = "config.urls"
INSTALLED_APPS = ["django.contrib.staticfiles", "factory.apps.FactoryConfig"]
MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": ["django.template.context_processors.request"],
        },
    },
]

LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Moscow"
STATIC_URL = "/static/"
