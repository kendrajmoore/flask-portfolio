FROM python:3.8.0

RUN mkdir /flask-portfolio
COPY requirements.txt /flask-portfolio
WORKDIR /flask-portfolio
RUN pip3 install -r requirements.txt

COPY . /flask-portfolio/

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
