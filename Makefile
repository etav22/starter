make install:
	poetry install
	poetry run pre-commit install --hook-type commit-msg

make test:
	poetry run pytest

make lint:
	poetry run pre-commit run --all-files
