FROM python:3.8
RUN apt update -y
RUN apt upgrade -y

RUN git clone https://github.com/eslamkarim/fundraiser.git
WORKDIR /fundraiser
RUN pip install -r requirments.txt