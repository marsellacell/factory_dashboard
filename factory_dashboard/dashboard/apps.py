"""
Application configuration for the dashboard app.

The AppConfig class is used by Django to identify installed
applications.  Naming the app ``dashboard`` here ensures that it can
be referenced unambiguously throughout the project.
"""
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "dashboard"