                                                                                 entrypoint.sh#!/bin/bash
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn ugsra.wsgi:application --bind 0.0.0.0:8000



