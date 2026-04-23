# Setup and Run Guide

## Prerequisites
- Python 3.10+
- PostgreSQL or compatible configured database
- Optional: Docker / Docker Compose

## Environment variables
Create `.env` from `.env.example`.

### Important variables
- `APP_NAME`
- `ENVIRONMENT`
- `DATABASE_URL`
- `EXTERNAL_API_URL`

## Recommended run
```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8003
```

## Docker run
```bash
docker compose up --build
```

## Expected validation sequence
1. `GET /health`
2. `POST /pipeline/trigger`
3. `GET /pipeline/runs`
4. `GET /pipeline/runs/{run_id}`

## Behavior of a successful trigger
A successful trigger should:
- insert a new run row
- process the requested number of items
- update the row to `success`
- expose the row through the list and detail endpoints
