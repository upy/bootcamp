# E-Commerce Application using Django

## Dependencies used in the project

- Python 3.9.5
- PostgreSQL 14.1

## Project Setup

- Clone the project with `git clone https://github.com/upy/bootcamp.git ecommerce-django && cd ecommerce-django`
- Create virtual environment with `virtualenv --python=3.9 .venv` and activate it with `source .venv/bin/activate`
- Enter the ecommerce folder with `cd ecommerce`
- Install dependencies with `pip install -r requirements.txt`
- Create server, database and superuser with the Postgresql. (If you want to do database operations with a gui, you can additionally use pgAdmin.)
- Execute the migrate process with `python manage.py migrate`
- Fill in the contents of the [`.env.dist`](ecommerce/.env.dist) file and copy it as `.env`

### Inside of the ".env" File
- SECRET_KEY in the .env file can be generated with the following command. <br> `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

- DEBUG variable should be True only during project development. 

- The parameters in the DATABASE_URL variable in the .env file are the superuser username and password, the IP and port specified for the server, and the database name, respectively.

## Run 

Run `python manage.py runserver ip_you_want:port_you_want` and go to [`http://ip_you_want:port_you_want`](ip_you_want:port_you_want) from the browser.

Ex.: Run `python manage.py runserver 0.0.0.0:5252` and go to [`http://0.0.0.0:5252`](http://0.0.0.0:5252) from the browser.

> Note: If ip and port are not specified, it will work on the default ip(127.0.0.1) and port(8000). Make sure that the ip address entered in "ip_you_want" is in ALLOWED_HOSTS variable in the [`.env`](ecommerce/.env) file.
