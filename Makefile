# =================================================================================================
# Settings
# =================================================================================================
PROJECT := review-bot
PROJECT_PATH := $(shell pwd)
PYTHON := python3.8
PIP := pip3

IMAGE_NAME := review-bot-image
CONTAINER_NAME := review-bot

VENV_NAME := venv
PYTHONPATH := ${PROJECT_PATH}:${PYTHONPATH}

RM := rm -rf

# =================================================================================================
# Development
# =================================================================================================
create_venv:
	virtualenv --python="${PYTHON}" ${VENV_NAME} && ${VENV_NAME}/bin/pip3 install -r requirements.txt

clean:
	find . -name '*.pyc' -exec $(RM) {} +
	find . -name '*.pyo' -exec $(RM) {} +
	find . -name '*~' -exec $(RM)  {} +
	find . -name '__pycache__' -exec $(RM) {} +
	$(RM) .cache/ .pytest_cache/ *.egg-info

isort:
	isort ${PROJECT_PATH}

black:
	black ${PROJECT_PATH}

flake8:
	flake8 ${PROJECT_PATH}

lint_all: isort black flake8


# =================================================================================================
# Deployment
# =================================================================================================

docker_build:
	docker build -t ${IMAGE_NAME} .

docker_clean:
	docker rm ${CONTAINER_NAME} && docker rmi ${IMAGE_NAME}

docker_run:
	docker run -it -d -v $(shell pwd)/data:/${PROJECT}/data -v $(shell pwd)/logs:/${PROJECT}/logs --name ${CONTAINER_NAME} ${IMAGE_NAME}

docker_stop:
	docker stop ${CONTAINER_NAME}



