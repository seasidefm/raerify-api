SHELL = /bin/bash

install:
	./venv/bin/pip install -r requirements.txt

install-dev:
	./venv/bin/pip install -r requirements-dev.txt

run:
	source .env \
	&& ./venv/bin/uvicorn app.main:app --reload --port=4000

run-prod:
	./venv/bin/uvicorn app.main:app --host=0.0.0.0 --port=10000

migrate:
	source .env \
	&& ./venv/bin/alembic upgrade head

fmt:
	./venv/bin/black .

lint:
	./venv/bin/pylint ./app
