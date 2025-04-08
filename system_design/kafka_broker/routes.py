# Routes.py needs to be completed
from fastapi import APIRouter, HTTPException
from system_design.kafka_broker.schemas import (
    EvaluationRequest,
    EvaluationResponse,
    Status,
)

from system_design.kafka_broker.kafka_handler import KafkaHandler
import json
from system_design.kafka_broker.db import job_statuses

router = APIRouter()
kafka_handler = KafkaHandler()


@router.post("/process", response_model=EvaluationResponse)
async def process_payload(request: EvaluationRequest):
    # 1. Create a new job entry with NOT_STARTED status
    # 2. Send the expression to Kafka input topic
    # 3. Return the job ID to the client
    # You'll need to implement this
    response = EvaluationResponse(id=request.id, expression=request.expression)
    job_statuses[request.id] = response
    await kafka_handler.produce_message(topic="my topic", message=response.model_dump())

    return response


@router.get("/status/{job_id}", response_model=EvaluationResponse)
async def get_status(job_id: str):
    # Retrieve and return the current status of a job
    # You'll need to implement this
    if job_id not in job_statuses:
        raise HTTPException(status_code=404, detail="Job not found")
    return job_statuses[job_id]
