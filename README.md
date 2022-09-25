# ToDo-App-in-Django

A ToDo List using [Django](https://www.djangoproject.com/)

Check the [Website](https://to-do-app-in-django-y6zn.vercel.app/) deployed Using Vercel.

# Code

### Step 1: Create Virtual Environment
#### For Linux/Mac
```bash
cd /path/to/folder
mkdir todo
cd todo
python3.9 -m virtualenv .
```
#### For Windows
```bash
cd /path/to/folder
mkdir todo
cd todo
python -m virtualenv .
```

### Step 2: Install the Dependencies
#### With **pip**
```bash
git clone https://github.com/Arvind-4/ToDo-App-in-Django.git .
pip install -r requirements.txt
```
#### With **poetry**
```bash
git clone https://github.com/Arvind-4/ToDo-App-in-Django.git .
poetry install
```

### Step 3: Run the Migrations!
```
python web/manage.py migrate
python web/manage.py createsuperuser
```

### Step 4: Run the Code!
```
python web/manage.py runserver
```

## Add These to your .env in Root of the Project
```bash
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=

DJANGO_SECRET_KEY=
DJANGO_DEBUG=1

DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_PASSWORD=
```
