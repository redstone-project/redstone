"""
WSGI config for redstone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .database.mongo import connect_mongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redstone.settings")
connect_mongo()
application = get_wsgi_application()
