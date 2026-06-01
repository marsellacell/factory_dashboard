"""
ASGI config for factory_dashboard project.

This module exposes the ASGI callable as a module-level variable named
``application``.  It is used by Django's asynchronous server gateway
interface to serve HTTP requests.  While this sample project does not
require asynchronous features, providing this module keeps the project
structure aligned with the defaults created by `django-admin
startproject`.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/.
"""
import os

from django.core.asgi import get_asgi_application  # type: ignore

# Set the default settings module for the 'asgi' command-line utility.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "factory_dashboard.settings")

# Instantiate the ASGI application.
application = get_asgi_application()