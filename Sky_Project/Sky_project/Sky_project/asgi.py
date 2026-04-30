"""
ASGI config for Sky_project project.

This exposes the ASGI application for deployment.
"""

# Imports os to set environment variables.
import os

# Imports Django ASGI application.
from django.core.asgi import get_asgi_application

# Sets the settings file used by Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sky_project.settings')

# Creates the ASGI application.
application = get_asgi_application()