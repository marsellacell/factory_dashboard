"""
URL patterns for the dashboard application.

The dashboard is mapped to the site root (``/``) in the project's
top‑level ``urls.py``.  Additional dashboard‑specific views can be
added to this list as the project evolves.
"""
from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns: list = [
    path("", views.dashboard_view, name="dashboard"),
]