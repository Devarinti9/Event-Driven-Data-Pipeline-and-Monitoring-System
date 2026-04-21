from datetime import datetime
from pydantic import BaseModel


class PipelineRunOut(BaseModel):
    id: int
    status: str
    source_name: str
    items_processed: int
    retry_count: int
    last_error: dict | None
    created_at: datetime

    class Config:
        from_attributes = True
