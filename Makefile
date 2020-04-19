install:
	pipenv install
	pip3 install coveralls


uninstall:
	pipenv uninstall

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

serve:
	python3 manage.py runserver

superuser:
	python manage.py createsuperuser

flake8:
	pipenv run flake8

mypy:
	pipenv run mypy

isort:
	pipenv run isort

collectstatic:
	python manage.py collectstatic
