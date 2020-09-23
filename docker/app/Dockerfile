#build stage
FROM python:3.8

RUN apt-get update -y
RUN apt-get install -y git wget vim mariadb-client

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN pip freeze

# COPY project files
COPY ./pdj /app/pdj
COPY ./manage.py /app/manage.py
COPY ./uwsgi_params /app/uwsgi_params

CMD python manage.py runserver
