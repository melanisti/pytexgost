FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY .. /app
WORKDIR /app

RUN apt-get update \
 # dependencies for building Python packages
 && apt-get install -y build-essential \
 # Translations dependencies
 && apt-get install -y gettext \
 # For sudo command available
 && apt-get install -y sudo
