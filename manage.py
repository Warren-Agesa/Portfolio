#!/usr/bin/env python
<<<<<<< HEAD
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
=======
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Karanja.settings')
>>>>>>> 8461a77a523cedacb8c334a4028e4df39a4a69df
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

<<<<<<< HEAD

if __name__ == '__main__':
    main()
=======
if __name__ == '__main__':
    main()
>>>>>>> 8461a77a523cedacb8c334a4028e4df39a4a69df
