from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db import Base, engine, get_db
from app.models.pipeline import PipelineRun
from app.schemas import PipelineRunOut
from app.services.pipeline import execute_pipeline

router = APIRouter()
Base.metadata.create_all(bind=engine)


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "event-driven-data-pipeline-monitoring-system"}


@router.post("/pipeline/trigger", response_model=PipelineRunOut)
def trigger_pipeline(limit: int = Query(default=10, ge=1, le=50), db: Session = Depends(get_db)):
    try:
        run = execute_pipeline(db, limit=limit)
        return run
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/pipeline/runs", response_model=list[PipelineRunOut])
def list_runs(db: Session = Depends(get_db)):
    return db.query(PipelineRun).order_by(PipelineRun.id.desc()).all()


@router.get("/pipeline/runs/{run_id}", response_model=PipelineRunOut)
def get_run(run_id: int, db: Session = Depends(get_db)):
    run = db.query(PipelineRun).filter(PipelineRun.id == run_id).first()
    if not run:
        raise HTTPException(status_code=404, detail="Run not found")
    return run
