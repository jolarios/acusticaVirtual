# Dockerfile

In this folder, we find the dockerfile with the directives to set up our virtual acoustic eviroment. This enviromet is based on ubuntu 20.04 LTS.


## Installation

After download the repo we have to do the following steps to install our enviroment.

    cd ./docker
	docker build -t acustica_virtual .
	docker run -it acustica_virtual

