FROM ubuntu:18.04
MAINTAINER Changhyun Lyoo<changhyunlyoo@gmail.com>

ADD ./sources.list /etc/apt/sources.list
ADD ./requirements.txt /data/
ADD ./run.script /data/
ADD ./init.script /data/

RUN apt update && apt install -y python3 \
	python3-dev \
	python3-pip \
	git

Run python3 -m pip install --upgrade pip
RUN chmod +x /data/run.script
RUN chmod +x /data/init.script

#git setting
RUN git config --global user.name "youpeterabb1t"
RUN git config --global user.email "21300259@handong.edu"


#Set the locale
RUN apt-get update && apt-get install -y locales
RUN locale-gen ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8

WORKDIR /data/

RUN pip3 install -r /data/requirements.txt
RUN /data/init.script

