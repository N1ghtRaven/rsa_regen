FROM python:alpine3.12
MAINTAINER Nate River 'me@red-eye.works'
COPY . /app
WORKDIR /app
RUN apk add --update --no-cache g++ gcc && pip install -r requirements.txt
CMD ["python", "main.py"]