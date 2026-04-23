# API Reference

## `GET /health`
Returns the service health payload.

Example response:
```json
{
  "status": "ok",
  "service": "event-driven-data-pipeline-monitoring-system"
}
```

## `POST /pipeline/trigger`
### Purpose
Start a pipeline execution and persist a run record.

### Query parameter
- `limit` — number of items to fetch and process; allowed range is 1 to 50

### Success behavior
Returns the created pipeline run object with final execution state.

## `GET /pipeline/runs`
### Purpose
Return all pipeline runs ordered from newest to oldest.

## `GET /pipeline/runs/{run_id}`
### Purpose
Return a single pipeline run by ID.

### Error behavior
Returns `404` if the run ID does not exist.
