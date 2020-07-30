FROM python:3.7

ENV PYTHONUNBUFFERED 1

# *TBW*

WORKDIR /opt/api

COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
