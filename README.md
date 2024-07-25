# Todo app

A Todo app in [Django](https://www.djangoproject.com/)

Check the [Website](https://awesometodoapp.vercel.app) deployed Using Vercel.

## Get the code

- Step 1: Create Virtual Environment

```bash
cd ~/Dev
mkdir ~/Dev/todoapp -p
cd ~/Dev/todoapp
python3.9 -m pip install virtualenv
python3.9 -m virtualenv .
source bin/activate
```

- Step 2: Install the Dependencies

Using **pip**

```bash
git clone https://github.com/Arvind-4/todoapp.git .
pip install -r requirements.txt -r requirements-dev.txt
```

Using **poetry**

```bash
git clone https://github.com/Arvind-4/todoapp.git .
poetry install
```

- Step 3: Run the Migrations!

```bash
python manage.py makemigrations
python manage.py migrate
```

- Step 4: Run the Code!

```bash
python manage.py runserver
```

## Add These to your .env in Root of the Project

```bash
DATABASE_PORT=
DATABASE_HOST=
DATABASE_PASSWORD=
DATABASE_USER=
DATABASE_NAME=
DATABASE_CLUSTER=

DJANGO_SUPERUSER_PASSWORD=
DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_EMAIL=
DJANGO_DEBUG=
DJANGO_SECRET_KEY=
```
