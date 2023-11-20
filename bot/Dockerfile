FROM python:3.10

LABEL authors="roman"

WORKDIR /bot

COPY ./requirements.txt  /bot/

RUN pip install -r requirements.txt

COPY . .