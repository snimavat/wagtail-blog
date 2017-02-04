from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
SECRET_KEY = 'x123gd1233556rsgtyu56twefty5redqwqwerh5tretr24%^$%^&$RE2e3qwDSDefref'

ALLOWED_HOSTS = ['nimavat.me','www.nimavat.me', 'localhost']

STATIC_ROOT = "/static"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lapsi',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

try:
    from .local import *
except ImportError:
    pass
