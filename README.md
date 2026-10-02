# AI Lakehouse Analytics Agent

Runnable reference implementation of natural-language analytics with SQL safety, schema discovery, DuckDB execution, FastAPI, tests, Docker and CI.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
python scripts/seed_data.py
uvicorn app.main:app --reload
```

POST `{"question":"top products by revenue"}` to `/v1/analyze`.
