#FROM python:3.9.7-slim
#
#ENV PYTHONUNBUFFERED 1
#ENV PYTHONDONTWRITEBYTECODE 1
#
#EXPOSE 8000
#
#WORKDIR /app
#COPY Pipfile Pipfile.lock /app/
#
#
#RUN pip install pipenv \
#    && pipenv install --deploy --system --ignore-pipfile
#
#COPY . /app/
#RUN chmod +x entrypoint.sh

#ENTRYPOINT ["sh","./entrypoint.sh"]
FROM python:3.9.6-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY . /app
EXPOSE 8000