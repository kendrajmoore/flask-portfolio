FROM python:3.9-slim-buster

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get -y update && apt-get -y install gcc 
RUN mkdir /flask-portfolio
COPY requirements.txt /flask-portfolio
WORKDIR /flask-portfolio

RUN pip3 install -r requirements.txt 
COPY . /flask-portfolio/

RUN sudo chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
