# Troubleshooting

## Port conflict on startup
### Cause
Another process is already bound to the selected port.

### Fix
Use a different port or stop the existing process.

## Database startup or migration issue
### Cause
`DATABASE_URL` is wrong or the target database is unavailable.

### Fix
Verify the database connection string and ensure the database is reachable.

## Trigger endpoint returns server error
### Cause
The external API failed or the database write failed.

### Fix
- verify `EXTERNAL_API_URL`
- confirm the external endpoint is reachable
- inspect the latest error payload in the run record if available

## PostgreSQL type compatibility note
The model uses a PostgreSQL `JSONB` column for `last_error`. If you switch to another database engine, you may need to adapt the model definition.

## Airflow expectation mismatch
### Clarification
The Airflow DAG in this repository is a starter artifact. The FastAPI service does not require Airflow to handle direct API-triggered execution.
