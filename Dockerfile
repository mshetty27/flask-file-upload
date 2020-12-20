#pull official base image
FROM python:3.8.1-slim-buster

#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /
RUN pip install -r requirements.txt

#copy project
COPY app/ /usr/src/app/
# RUN ls -la /usr/src/app/*

WORKDIR /usr/src/app

RUN mkdir uploads

EXPOSE 8001

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8001", "-w", "1", "--threads", "2", "app" ]