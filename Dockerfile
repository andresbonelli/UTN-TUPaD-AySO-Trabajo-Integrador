FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "promedio.py" ]