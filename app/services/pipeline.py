from collections.abc import Callable
import requests
from sqlalchemy.orm import Session
from app.config import settings
from app.models.pipeline import PipelineRun


def fetch_items(limit: int = 10) -> list[dict]:
    response = requests.get(settings.external_api_url, timeout=15)
    response.raise_for_status()
    return response.json()[:limit]


def process_items(items: list[dict]) -> list[dict]:
    transformed = []
    for item in items:
        transformed.append({
            "task_id": item["id"],
            "title": item["title"],
            "completed": item["completed"],
            "priority": "high" if not item["completed"] else "normal",
        })
    return transformed


def execute_pipeline(db: Session, limit: int = 10) -> PipelineRun:
    run = PipelineRun(status="running", source_name="jsonplaceholder-todos", items_processed=0, retry_count=0)
    db.add(run)
    db.commit()
    db.refresh(run)

    try:
        items = fetch_items(limit)
        processed = process_items(items)
        run.items_processed = len(processed)
        run.status = "success"
        db.commit()
        db.refresh(run)
        return run
    except Exception as exc:
        run.status = "failed"
        run.retry_count += 1
        run.last_error = {"message": str(exc)}
        db.commit()
        db.refresh(run)
        raise
