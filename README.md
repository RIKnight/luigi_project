# luigi_project

This project provides an environment for learning and testing Luigi.  Included is a Dockerfile for creating a container which supports Python, Luigi, and Jupyter.  

<!-- ABOUT THE PROJECT -->
## About The Project

This project was inspired by a need to learn how to use [Luigi](https://luigi.readthedocs.io/en/stable/#), combined with an interest in easy reproduction of results and portability of code.  The included [Docerfile](docker/Dockerfile) and associated Python [requirements.txt](docker/requirements.txt) can be used to build a Docker image that can run Luigi.  The entry point for this container is a [Jupyter Notebook](https://jupyter.org/) server, intended for examining the results of data transformations performed via Luigi.  However, Luigi jobs themselves should be run from a command line within the Docker container.  

The organization of the project is based largely on the [Cookiecutter Data Science with Luigi](https://github.com/ffmmjj/luigi_data_science_project_cookiecutter) package.  Part of the structure of the Cookiecutter framework is a method to run Luigi using Make, which is configured in the [Makefile](Makefile).


### Dependencies

* [Docker](https://www.docker.com/) - Everything runs inside a Docker container.


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install Docker on your system.  


### Installation

Copy this repository to your local system.  Then, from the root directory of the repository, build the Docker image:

```sh
cd docker
docker build -t jupyter-luigi .
```
(Note the '.' at the end; don't leave it off.)

## Usage

The container can be used through the Jupyter UI, as well as accessed through the command line.

### Starting the container

Run the Docker container using the provided [script](start.sh):

```sh
cd ..
./start.sh
```

### Interacting via the Jupyter UI

To connect to the Jupyter UI via a web browser, point it to the exposed port (defined in start.sh).  If your browser is on the same host as docker, connect as:

```
127.0.0.1:9999
```

The root directory of the project should be visible and accessible in the Jupyter UI.

### Interacting via the command line

In a terminal, find the docker container ID with:

```sh
docker ps
```

Look for the container ID for image `jupyter-luigi`.  It will look something like `788b940d8616`, for example.  To enter the container:

```sh
docker exec -it <CONTAINER ID> /bin/bash
```

From within the container, commands such as `make data`, for initiating a Luigi run, can be executed.


## Example Project:  Luigi "Hello World"

There are three `.py` files within the [src/data_tasks](src/data_tasks) directory which define a simple Luigi pipeline.  There are three tasks (one per file, in this example): one of them writes `Hello` to an "interim" text file, another writes `World` to another "interim" text file, and the third, which is dependent on the first two tasks, reads the two interim files and combines them to write a "processed" text file, which will contain `Hello World`.  To kick off the pipeline, obtain a docker exec session in the container, then run:

```sh
make data
```

Examine the contents of the [data\interim](data\interim) and [data\processed](data\processed) directories to see the interim and processed output of the pipeline.


<!-- PROJECT ORGANIZATION -->
## Project Organization


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docker
    │   ├── Dockerfile     <- Dockerfile to build docker image.
    │   ├── requirements.txt     <- Python dependencies for installation in image.
    │   └── requirements.bak     <- Original template that requirements.txt is based on.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── start.sh           <- shell script for starting docker container with mounted volume and port mapping
    │
    └── test_environment.py   <- Checks current python version.  For use with Make.
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>, modified for use with <a target="_blank" href="https://github.com/ffmmjj/luigi_data_science_project_cookiecutter">Luigi</a>, <a target="_blank" href="https://www.martinalarcon.org/2018-12-31-a-reproducible-science/">Docker, and Jupyter</a>. #cookiecutterdatascience</small></p>
