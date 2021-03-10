FROM python:3.7-buster as base 

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/webapp
ENV SRC_DIR ${PROJECT_DIR}/src

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

WORKDIR ${PROJECT_DIR}

ENV PYTHONUNBUFFERED=1

FROM base as dev

# this is a dev image build, so install dev packages
RUN pipenv install --system --dev

COPY . ${SRC_DIR}/

WORKDIR ${SRC_DIR}

CMD ["make", "serve"]