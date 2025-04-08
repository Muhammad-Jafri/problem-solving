# Add to schemas.py
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Status(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    FAILED = "FAILED"


class EvaluationResponse(BaseModel):
    id: str
    expression: str
    status: Status = Status.NOT_STARTED
    result: Optional[int] = None
    error: Optional[str] = None


class EvaluationRequest(BaseModel):

    expression: str
    id: str 
    