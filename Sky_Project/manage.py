#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# Imports os to set the Django settings module.
import os

# Imports sys so command-line arguments can be passed into Django.
import sys


def main():
    """Run administrative tasks."""

    # Tells Django which settings file to use.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sky_project.settings')

    try:
        # Imports Django's command-line function.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Error message shown if Django is not installed properly.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Runs commands such as runserver, makemigrations and migrate.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()