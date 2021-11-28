E-commerce project developed by students of patika.dev & platific bootcamp.
Bootcamp is aimed to learn Django, Django Rest Framework and React JS.

To start running this project you need;
1. crate an virtual enviroment with python3 -m venv venv
2. activate the enviroment
3. install requirement with pip install -r requirements.txt
4. setup django environ
   - create a .env file in ecommerce folder.
   - add DEBUG, SECRET_KEY, DEFAULT_DB_NAME, DEFAULT_DB_USER, DEFAULT_DB_PASSWORD, DEFAULT_DB_HOST, DEFAULT_DB_PORT parameters to .env file
5. migrate the databese tables with python3 manage.py migrate command.
6. run the server with python3 manage.py runserver command.
