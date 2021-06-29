FROM python:3.8-slim-buster

RUN mkdir /hackthon-portfolio
COPY requirements.txt /hackthon-portfolio
WORKDIR /hackthon-portfolio
RUN pip3 install -r requirements.txt

COPY . /hackthon-portfolio/

CMD ["gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:80" ]