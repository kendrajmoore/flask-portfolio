FROM python:3.9-slim-buster

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get -y update && apt-get -y install gcc 
RUN mkdir /hackathon-portfolio
COPY requirements.txt /hackathon-portfolio
WORKDIR /hackathon-portfolio

RUN pip3 install -r requirements.txt 
COPY . /hackathon-portfolio/

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
