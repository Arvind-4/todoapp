import os, pathlib

DATABASE_NAME = str(os.environ.get('DATABASE_NAME'))
DATABASE_USER = str(os.environ.get('DATABASE_USER'))
DATABASE_PASSWORD = str(os.environ.get('DATABASE_PASSWORD'))
DATABASE_HOST = str(os.environ.get('DATABASE_HOST'))
DATABASE_PORT = str(os.environ.get('DATABASE_PORT'))

BASE_DIR = pathlib.Path(__file__).resolve().parent

# CERTIFICATE_DIR = NEW_BASE_DIR.parent

CERTIFICATE_FILE_PATH = BASE_DIR / '.postgresql' / 'root.crt'

DB_IS_AVAILABLE = all([
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    CERTIFICATE_FILE_PATH
])

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': 'django_cockroachdb',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
            'OPTIONS': {
                'sslmode': 'verify-full',
                'sslrootcert': str(CERTIFICATE_FILE_PATH),
                'options': '--cluster=coping-raccoon-1276'
            },
        },
    }

    DATABASES['default']['CONN_MAX_AGE'] = None
    DATABASES['default']['ATOMIC_REQUESTS'] = True 