FROM python:3.7
WORKDIR /usr/src/app
RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install urllib3==1.24
RUN pip install python-dateutil requests kaggle

RUN mkdir /root/.kaggle
ADD kaggle.json /root/.kaggle/
