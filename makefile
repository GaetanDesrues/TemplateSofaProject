all: stop build run

build:
	docker build -t example_sofa .

stop:
	-docker stop ct_example_sofa
	-docker rm ct_example_sofa
	-docker rmi example_sofa

run:
	docker run -v ./src:/app/src -it --name ct_example_sofa example_sofa bash
