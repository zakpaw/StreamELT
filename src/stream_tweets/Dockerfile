# syntax=docker/dockerfile:1

FROM python:3.9-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app /app
WORKDIR /app

CMD ["python3 main.py"]