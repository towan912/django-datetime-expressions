SECRET_KEY = 'test-secret'

DATABASES = {
    'default': {
        'NAME': 'django_datetime_expressions',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
    }
}

INSTALLED_APPS = [
    'django_datetime_expressions.tests',
]

MIGRATION_MODULES = {
    'tests': None,
}

USE_TZ = False
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
