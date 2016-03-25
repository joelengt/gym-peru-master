__author__ = 'klaatu'
from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gym',
        'USER': 'postgres',
        'PASSWORD': 'baudelaire123',
        'HOST': 'localhost',
        'PORT': '',
    }
}
