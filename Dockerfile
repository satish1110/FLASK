## copying a base image from docker hub 
FROM python:3.6-alpine 
## change working dir 
WORKDIR /project 
## copying all files 
ADD . /
## install requirements 
RUN pip install --upgrade pip 
RUN pip install -r /requirements.txt 
## run file 
CMD ['python', 'main.py']
