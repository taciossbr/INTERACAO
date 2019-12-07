FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN pip install flask chatterbot pymongo

EXPOSE 8080

CMD ["python", "server.py"]
