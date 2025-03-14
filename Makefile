.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: run-server
run-server:
	python manage.py runserver 0.0.0.0:8000

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: update
update: install migrate ;