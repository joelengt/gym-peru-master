from .base import *

ALLOWED_HOSTS = ['159.203.120.218']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gym',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
STATIC_URL = '/static/'
ADMINS = (
    ('Erik Admin', 'erikd.guiba@gmail.com'),
)
