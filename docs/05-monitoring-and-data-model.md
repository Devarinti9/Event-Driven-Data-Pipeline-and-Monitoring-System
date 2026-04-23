# Monitoring and Data Model

## PipelineRun model
### Fields
- `id` — unique run identifier
- `status` — current run state
- `source_name` — source label for the execution
- `items_processed` — number of processed items
- `retry_count` — retry counter
- `last_error` — structured error payload when a run fails
- `created_at` — creation timestamp

## Status progression
Typical successful path:
1. `running`
2. `success`

Failure path:
1. `running`
2. `failed`
3. `retry_count` increments
4. `last_error` is populated

## Transformation behavior
The current pipeline service fetches todo items and maps each item into a simplified structure with:
- `task_id`
- `title`
- `completed`
- `priority`

## Monitoring value
This project provides a clean example of how to track:
- whether a run succeeded
- how much work it completed
- whether retries occurred
- what the last known error was
