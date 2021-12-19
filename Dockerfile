# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc gettext python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install gunicorn


COPY ./ecommerce/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./ecommerce .

RUN mkdir /app/static && python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D wwwuser
USER wwwuser

# run gunicorn
CMD gunicorn ecommerce.wsgi:application --bind 0.0.0.0:$PORT
