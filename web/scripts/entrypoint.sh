#!/bin/bash

set -e

if [ $DEBUG != "True" ]; then
    python3 manage.py collectstatic --noinput
fi

python3 manage.py makemigrations
python3 manage.py migrate

if [ $DEBUG == "True" ]; then
    python3 manage.py runserver --insecure 0:8080
else
    gunicorn -w 4 -b 0.0.0.0:8080 portfolio.wsgi
fi