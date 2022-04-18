# syntax=docker/dockerfile:1
FROM python:3.10.1
MAINTAINER Artyom Galkin igalart2000@gmail.com
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /nft_app
COPY requirements.txt /nft_app/
RUN pip install -r requirements.txt
COPY . /nft_app/
