run_server:
	poetry run uvicorn fastapi_project.main:app --reload

run_shell:
	poetry run python

install:
	poetry install

run_migrations:
	poetry run alembic upgrade head

makemigrations:
	poetry run alembic revision --autogenerate -m "New migration"

run_celery_worker:
	poetry run celery -A fastapi_project.celery_app worker --loglevel=info

run_celery_beat:
	poetry run celery -A fastapi_project.celery_app beat --loglevel=info

pre_commit_run:
	poetry run pre-commit run --files

test:
	poetry run pytest tests/

lint:
	poetry run flake8 fastapi_project/

format:
	poetry run black fastapi_project/ tests/

.PHONY: run_server run_shell install run_migrations makemigrations run_celery_worker run_celery_beat pre_commit_run test lint format
