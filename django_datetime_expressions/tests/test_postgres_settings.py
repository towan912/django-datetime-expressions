SECRET_KEY = 'test-secret'

DATABASES = {
    'default': {
        'NAME': 'django_datetime_expressions',
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    },
}

INSTALLED_APPS = [
    'django_datetime_expressions',
]

USE_TZ = False
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
