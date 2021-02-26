install:
	pipenv install

uninstall:
	pipenv uninstall

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

serve:
	python manage.py runserver

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

shell_plus:
	python manage.py shell_plus

flake8:
	pipenv run flake8

mypy:
	pipenv run mypy

isort:
	pipenv run isort

collectstatic:
	python manage.py collectstatic
