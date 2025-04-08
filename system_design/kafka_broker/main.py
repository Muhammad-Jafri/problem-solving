from fastapi import FastAPI
import asyncio
from system_design.kafka_broker.routes import router as process_router
from system_design.kafka_broker.worker import run_worker

app = FastAPI()
app.include_router(process_router)

# Store the task reference to keep it from garbage collection
worker_task = None


@app.on_event("startup")
async def startup_event():
    global worker_task
    # Start the worker in a background task
    worker_task = asyncio.create_task(run_worker())
    print("Worker task started")


@app.on_event("shutdown")
async def shutdown_event():
    global worker_task
    # Cancel the worker task when the app shuts down
    if worker_task:
        worker_task.cancel()
        try:
            await worker_task
        except asyncio.CancelledError:
            print("Worker task was cancelled")


@app.get("/")
async def greet():
    return {"hello": "world"}
