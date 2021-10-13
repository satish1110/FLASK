## copying a base image from docker hub 
FROM python:3.6-alpine 
## change working dir 
WORKDIR /project 
## copying all files 
ADD . /project
## install requirements 
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 
EXPOSE 5000
## run file 
CMD ["python" , "docker_demo.py"]
