###########################################################
##														 ##
##	Docker container for virtual acustic enviroment      ##
##														 ##
##														 ##
##														 ##
##														 ##
##														 ##
###########################################################

FROM ubuntu:20.04

#Sentence MAINTAINER is deprecated
LABEL maintainer="j.lareu@udc.es"

#Doing some configuration
USER root
RUN apt-get update && apt-get upgrade -yq


RUN echo ********* Installing cmake **********
RUN apt-get -yq install cmake

RUN echo ********* Installing git **********
RUN apt-get -yq install git

RUN echo ********* Installing pytho **********
RUN apt-get -yq install python

RUN echo ********* Installing unzip **********
RUN apt-get -yq install unzip

RUN echo ********* Installing wget **********
RUN apt-get -yq install wget

RUN echo ********* Installing apache server 2 **********
RUN apt-get install –y apache2
RUN apt-get install –y apache2-utils 

RUN apt-get clean && apt-get autoclean -yq && apt-get autoremove -yq


#User creation
RUN useradd -rm -d /home/acusticaVirtual -s /bin/bash -g root -G sudo acusticaVirtual
USER acusticaVirtual
WORKDIR /home/acusticaVirtual

RUN echo ********* Downloading resonance-audio and resonance-audio-web-sdk **********
RUN cd /home/acusticaVirtual
RUN git clone https://github.com/resonance-audio/resonance-audio
RUN git clone https://github.com/resonance-audio/resonance-audio-web-sdk

#Execute cmd interpreter
CMD ["/bin/bash"]
