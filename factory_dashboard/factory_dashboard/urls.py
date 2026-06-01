"""
Root URL configuration for the factory_dashboard project.

This module routes incoming HTTP requests to the appropriate views.  The
dashboard application is mounted at the site root, and the built-in
Django administration interface is available under the ``/admin/`` path.

For more information on URL configuration, see
https://docs.djangoproject.com/en/4.2/topics/http/urls/.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns: list = [
    # Django admin site (useful if you decide to manage data via the admin)
    path("admin/", admin.site.urls),
    # Delegate all other URLs to the dashboard app
    path("", include("dashboard.urls")),
]