FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./backend ./Pipfile ./Pipfile.lock /app/
WORKDIR /app

RUN apt-get update \
 # dependencies for building Python packages
 && apt-get install -y build-essential \
 # Translations dependencies
 && apt-get install -y gettext \
 # For sudo command available
 && apt-get install -y sudo \
 # Pipenv
 && pip install --upgrade pip \
 && pip install pipenv==2022.11.30 \
 && pipenv sync --system \
 && rm -rf Pipfile.lock Pipfile