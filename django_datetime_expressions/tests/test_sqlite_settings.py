SECRET_KEY = 'test-secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

INSTALLED_APPS = [
    'django_datetime_expressions',
]

USE_TZ = False
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
