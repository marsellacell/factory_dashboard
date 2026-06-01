"""
Django settings for factory_dashboard project.

These settings define the configuration for the sample factory dashboard.  The
values here mirror the defaults created by `django-admin startproject` and
include a minimal set of installed applications and middleware.  The
project uses the local file system to store its static assets and does not
rely on a database because production metrics are loaded from an Excel
spreadsheet via pandas (see ``dashboard/utils.py``).

This file is intended for instructional purposes.  Students can read
through it to understand how Django projects are configured and how
settings such as `TEMPLATES` and `STATICFILES_DIRS` influence the
structure of the web application.
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Path = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# This is a dummy value for demonstration purposes.  Do not use this
# secret key in a real deployment.
SECRET_KEY: str = "django-insecure-factory-dashboard-sample-secret-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = True

# When deploying, set this list to the domain names your site runs on.
ALLOWED_HOSTS: list[str] = []

# Application definition

INSTALLED_APPS: list[str] = [
    "dashboard",  # our custom dashboard app
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "factory_dashboard.urls"

TEMPLATES: list[dict] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # In addition to the templates within apps, look for templates in
        # a global `templates` directory at the project root.  This makes
        # adding global templates easy without modifying app directories.
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: str = "factory_dashboard.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#
# This sample project does not require a relational database because
# production data is loaded from a local Excel file.  Nevertheless,
# configuring the default SQLite database ensures Django can create
# session and authentication tables if those features are used.
DATABASES: dict[str, dict[str, object]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: list[dict[str, object]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE: str = "en-us"

# Set the timezone to Asia/Jakarta so that the dashboard displays dates
# correctly for students located in Indonesia (UTC+7).
TIME_ZONE: str = "Asia/Jakarta"

USE_I18N: bool = True
USE_TZ: bool = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL: str = "/static/"

# During development, static files can be served from these directories.
STATICFILES_DIRS: list[Path] = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"