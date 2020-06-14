FROM python:3.7

ENV PYTHONUNBUFFERED 1

# *TBW*
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]