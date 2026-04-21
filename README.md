# Event-Driven Data Pipeline and Monitoring System

A Python-based backend system for automated data collection, transformation, storage, and monitoring of pipeline runs.

## Tech Stack
- Python
- FastAPI
- Airflow
- PostgreSQL
- Docker
- Supabase-ready architecture
- Cloud-ready deployment model

## Features
- Event-driven pipeline triggering
- Monitoring for pipeline runs
- Retry and error tracking fields
- Scheduled Airflow DAG
- Dockerized local setup

## API Endpoints
- `GET /health`
- `POST /pipeline/trigger`
- `GET /pipeline/runs`
- `GET /pipeline/runs/{run_id}`

## Run Locally
```bash
docker compose up --build
```

- API docs: `http://localhost:8003/docs`
- Airflow: `http://localhost:8081`

## Resume Description
Designed and implemented an event-driven backend pipeline to automate data collection, transformation, and structured storage, supporting reliable processing for application and business workflows.
