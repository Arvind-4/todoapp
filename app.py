import os
from utils import read_env

read_env()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django

django.setup()

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
