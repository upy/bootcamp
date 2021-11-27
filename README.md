# Prerequisites
 - Postgresql
 - PgAdmin

# Installation

### 0. Clone the project
```bash
$ git clone https://github.com/upy/bootcamp
cd bootcamp
```

### 1. Create a `.env` file in the project root directory.

<details>
    <summary>.env</summary>

    DEBUG=
    SECRET_KEY=
    DATABASE_ENGINE=
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_HOST=
    DATABASE_PORT=
    
    ALLOWED_HOSTS=
    TIME_ZONE=
 
</details>

### 2. Start the project .
```bash
# activate virtual environment

> python -m venv env
> env/Scripts/activate

# install dependencies

> pip install -r requirements.txt

# migrate models

> python manage.py migrate

# Run the app

> python manage.py runserver

```

[Home Page](http://127.0.0.1:8000/)
