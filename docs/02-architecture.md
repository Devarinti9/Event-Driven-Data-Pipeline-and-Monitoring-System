# Architecture

## High-level flow
Client -> FastAPI -> Pipeline Service -> External API
                             -> Database -> Run history endpoints

## Application structure
- `app/main.py` — FastAPI application setup
- `app/config.py` — environment-backed settings
- `app/db.py` — SQLAlchemy engine and session management
- `app/models/pipeline.py` — `PipelineRun` model
- `app/schemas.py` — Pydantic response schema
- `app/services/pipeline.py` — fetch, transform, and execution logic
- `app/api/routes.py` — API endpoints
- `dags/pipeline_monitoring.py` — Airflow DAG starter file
- `tests/test_health.py` — basic health test

## Pipeline execution flow
### Trigger endpoint
The trigger endpoint calls `execute_pipeline()`.

### Execution steps
1. create a `PipelineRun` row with `running` status
2. fetch items from the external API
3. transform the fetched items
4. update the run with item count and final status
5. on failure, increment retry count and store the error payload

## Current persistence model
`pipeline_runs`
- `id`
- `status`
- `source_name`
- `items_processed`
- `retry_count`
- `last_error`
- `created_at`

## Monitoring focus
The project is centered on status tracking, run visibility, and retry/error recording rather than complex transformation pipelines.
