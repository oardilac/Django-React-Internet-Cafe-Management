# Use an official Python runtime as a parent image
FROM python:3.9-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt