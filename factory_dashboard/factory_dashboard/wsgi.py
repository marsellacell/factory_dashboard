"""
WSGI config for factory_dashboard project.

This module exposes the WSGI callable as a module-level variable named
``application``.  WSGI (Web Server Gateway Interface) allows Django to
communicate with web servers, and this configuration is necessary for
deploying the project to production servers such as Gunicorn or uWSGI.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/.
"""
import os

from django.core.wsgi import get_wsgi_application  # type: ignore

# Set the default settings module for the 'wsgi' command-line utility.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "factory_dashboard.settings")

application = get_wsgi_application()