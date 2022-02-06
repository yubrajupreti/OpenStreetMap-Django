FROM python:3.7.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /OSM
WORKDIR /OSM
COPY . /OSM/
RUN pip install -r requirements.txt