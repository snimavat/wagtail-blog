from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
SECRET_KEY = 'x123gd1233556rsgtyu56twefty5redqwqwerh5tretr24%^$%^&$RE2e3qwDSDefref'

ALLOWED_HOSTS = ['nimavat.me','www.nimavat.me']

STATIC_ROOT = "/static"

try:
    from .local import *
except ImportError:
    pass
