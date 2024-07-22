"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import pathlib
import sys

import dotenv

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

sys.path.insert(0, str(BASE_DIR / "web"))
sys.path.insert(1, str(BASE_DIR / "web" / "backend"))

if ENV_PATH.exists():
    print("Loading environment variables from .env file")
    dotenv.read_dotenv(str(ENV_PATH))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
