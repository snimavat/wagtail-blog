#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys

if __name__ == "__main__":
    env = os.environ.get('APP_ENV', 'dev')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lapsi.settings." + env)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
