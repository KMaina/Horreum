FROM python:3

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

RUN pip3 install pipenv
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system --dev
COPY . /code/
