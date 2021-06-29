FROM python:3.8-slim-buster

RUN mkdir /flask-portfolio
COPY requirements.txt /flask-portfolio
WORKDIR /flask-portfolio
RUN pip3 install -r requirements.txt

COPY . /flask-portfolio/

RUN chmod u+x ./entrypoint.sh

CMD ["gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:80" ]