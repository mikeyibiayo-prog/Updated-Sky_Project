"""
WSGI config for Sky_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
""""""

# Imports os to set environment variables.
import os

# Imports Django WSGI application.
from django.core.wsgi import get_wsgi_application

# Sets the settings file used by Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sky_project.settings')

# Creates the WSGI application.
application = get_wsgi_application()