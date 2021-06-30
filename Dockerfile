FROM python:3.8-slim-buster

RUN yum update && yum upgrade


RUN yum install --no-cache curl python pkgconfig python-dev openssl-dev libffi-dev musl-dev make gcc

RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3

RUN mkdir /flask-portfolio
COPY requirements.txt /flask-portfolio
WORKDIR /flask-portfolio
RUN pip3 install -r requirements.txt --extra-index-url https://testpypi.python.org/pypi

COPY . /flask-portfolio/

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
