install:
	pip install -e '.[dev]'
test:
	pytest -q
run:
	python scripts/seed_data.py
	uvicorn app.main:app --reload
