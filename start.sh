#!/bin/bash
# To use:  Run this from the main directory of the project.
# Maintainter:  Robert Knight <dataknight@zohomail.com>
#

# build the container
# cd docker
# docker build -t jupyter-luigi .

# start the container with the volume mounted
# docker run --name jupyter-luigi-container -p 9999:8888 -v luigi_volume:/app jupyter-luigi
# docker run -p 9999:8888 -v luigi_volume:/app jupyter-luigi
docker run -p 9999:8888 \
  --name jupyter-luigi-container \
  --mount type=bind,source="$(pwd)",target=/app \
  jupyter-luigi
