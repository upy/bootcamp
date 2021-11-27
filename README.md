# Django ecommerce project

## Installations

- Pycharm
- PostgreSQL

After installing Pycharm and PostgreSQL, create new project in Pycharm with virtual environment.

## Installing dependencies

create **requirements.txt** in project's root file with following content:
>Django==3.2.9 <br>
>psycopg2-binary==2.9.2 <br>
>django-extensions==3.1.2 <br>
>django-environ==0.8.1

run command:
>pip install requirements.txt

## Project creation

After all dependencies installed, in project's root folder create new django project called "ecommerce" with the following command in terminal:
> django-admin startproject ecommerce

In PostgreSQL create new login role with password and give it all privileges. 
Create new database and assign newly created role as owner of this database.

## Create .env file

It is a must to hide all the sensitive data in settings.py in a separate .env file. 
You have to create .env file in django project's root folder and fill it with all the sensitive variables from settings.py. Here is an example of .env:
>SECRET_KEY=<*your secret key from settings.py*> <br>
>DEBUG=on <br>
ALLOWED_HOSTS= <br>
DATABASE_URL=psql://owner:password@host:port/database_name <br>
LANGUAGE_CODE=en <br>
TIME_ZONE=Europe/Istanbul <br>
USE_I18N=True <br>
USE_L10N=True <br>
USE_TZ=True <br>

You have to change **DATABASE_URL** according to your database and its owner.

## Changing settings.py according to .env

We installed django-environ because it helps us to read .env file.
Add this code snippet to your setting.py:
```Python
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Find path to .env file
ENV_FILE = os.path.join(BASE_DIR, '.env')

# Take environment variables from .env file
environ.Env.read_env(ENV_FILE)
```
Now you can assign variables from .env file to variables in settings.py. Here is example for **SECRET_KEY** variable:
```
SECRET_KEY = env('SECRET_KEY')
```
Argument in env() is the name of variable in .env file.

## Migration

Migrate django's default tables to your database by running the following command:
>python manage.py migrate

## Running project

You have to create a super user so you can access to django admin panel. Use following command:
>python manage.py createsuperuser

Run your django project :
>python manage.py runserver

