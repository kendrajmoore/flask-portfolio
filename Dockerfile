FROM python:3.9-slim-buster

RUN apt-get -y update && apt-get -y install gcc && apt-get -y install cloud-init
RUN mkdir /flask-portfolio
COPY requirements.txt /flask-portfolio
WORKDIR /flask-portfolio

RUN pip3 install -r requirements.txt --extra-index-url https://testpypi.python.org/pypi

COPY . /flask-portfolio/

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
