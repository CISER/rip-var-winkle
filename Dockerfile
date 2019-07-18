FROM python:3.7.4-buster

MAINTAINER Brandon T. Kowalski <kowalski@cornell.edu>

RUN useradd -m rvw

WORKDIR /home/rvw

COPY *.py requirements.txt supervisor.conf ./

RUN apt-get update && apt-get install -y supervisor && pip install --no-cache-dir -r requirements.txt && pip install gunicorn

EXPOSE 8000

CMD ["supervisord", "-n", "-c", "/home/rvw/supervisor.conf"]

