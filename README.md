# Template Docker-based Project


Type `make` in the terminal to start a docker container with preinstalled:
    - Fedora 38
    - SOFA v23.06
    - Python 3.11 environement with SofaPython3
    - SofaScene python package

The code contained in ./src in mounted in the container.

In the `make` command, you build, start and connect to the container.

From within the container, start your SOFA scene: `python main.py`
