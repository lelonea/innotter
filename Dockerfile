FROM python:3.9.7-slim as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000

WORKDIR /app
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt
COPY . /app/
COPY entrypoint.sh /entrypoint.sh

FROM mysql:8.0.21 as mysql_migration

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
RUN apt-get update && apt install -y python3 python3-pip musl-dev libmariadb-dev  && apt-get clean
RUN pip3 install SQLAlchemy==1.4.44 mysqlclient==2.0.3 pymysql==1.0.2 alembic==1.7.1

RUN mkdir /migrations
WORKDIR /migrations
COPY src/db /migrations